"""Write README.md, reports/<repo>.md, csv/release_stats.csv and csv/changes.csv from data/classified.jsonl."""
import json, os, re, csv, collections, datetime
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import commentary
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CATS = ["feature", "fix", "perf", "i18n", "docs", "test", "build-ci", "release", "refactor", "deps", "security", "revert", "other"]
HEAD = {"feature": "Feature", "fix": "Fix", "perf": "Perf", "i18n": "i18n", "docs": "Docs", "test": "Test", "build-ci": "Build/CI",
        "release": "Release", "refactor": "Refactor", "deps": "Deps", "security": "Security", "revert": "Revert", "other": "Other"}
KINDS = ["pr-merge", "squash", "direct", "batch-commit"]
TEAM = {"MEMBER", "OWNER", "COLLABORATOR"}

rows = [json.loads(l) for l in open(f"{ROOT}/data/classified.jsonl")]
rels = [json.loads(l) for l in open(f"{ROOT}/data/releases.jsonl")]
api = {}
for r in {x["repo"] for x in rels}:
    for a in json.load(open(f"{ROOT}/data/releases_api/{r}.json")): api[(r, a["tag"])] = a
by = collections.defaultdict(list)
for r in rows: by[(r["repo"], r["release"])].append(r)
repos = list(dict.fromkeys(x["repo"] for x in rels))
os.makedirs(f"{ROOT}/reports", exist_ok=True); os.makedirs(f"{ROOT}/csv", exist_ok=True)

def people(r): return ([r["human"]] if r["human"] else []) + r["coauthors"]
def agents(r): return r["agents_author"] + r["agents_coauthor"]

# Humans seen in an earlier release of the same repo, to tell new contributors from returning ones
seen_before = {}
_seen = collections.defaultdict(set)
for rel in rels:
    seen_before[(rel["repo"], rel["release"])] = set(_seen[rel["repo"]])
    for r in by[(rel["repo"], rel["release"])]: _seen[rel["repo"]].update(people(r))

def stats(rel):
    ch = by[(rel["repo"], rel["release"])]
    humans = {h for r in ch for h in people(r)}
    families = collections.Counter(f for r in ch for f in agents(r))
    cat = collections.Counter(r["category"] for r in ch); kind = collections.Counter(r["kind"] for r in ch)
    prs = [r for r in ch if r["kind"] in ("pr-merge", "squash")]
    a = next((api[(rel["repo"], t)] for t in rel["tags"] if (rel["repo"], t) in api), None)
    return dict(repo=rel["repo"], release_tag=rel["release"], tags=", ".join(rel["tags"]),
                published=(a["published_at"][:10] if a else rel["date"][:10]), url=(a["url"] if a else ""),
                commits=rel["commits"], changes=len(ch), uncategorised=cat.get("uncategorised", 0),
                **{c: cat.get(c, 0) for c in CATS}, **{k: kind.get(k, 0) for k in KINDS},
                folded_pr_commits=rel["folded_pr_commits"], sync_merges=rel["sync_merges"],
                community_prs=sum(1 for r in prs if r["assoc"] and r["assoc"] not in TEAM),
                team_prs=sum(1 for r in prs if r["assoc"] in TEAM),
                humans=len(humans), new_humans=len(humans - seen_before[(rel["repo"], rel["release"])]),
                agents=len(families), agent_names=", ".join(f for f, _ in families.most_common()),
                bots=len({b for r in ch for b in r["bots"]}),
                changes_agent_disclosed=sum(1 for r in ch if agents(r)),
                changes_agent_authored=sum(1 for r in ch if r["agents_author"]),
                changes_no_human=sum(1 for r in ch if not people(r)))

S = [stats(r) for r in rels]
# Every change is in exactly one category and one landing type, and every commit is accounted for
for s in S:
    where = f"{s['repo']} {s['release_tag']}"
    assert s["changes"] == sum(s[c] for c in CATS) + s["uncategorised"], f"category counts do not add up for {where}"
    assert s["changes"] == sum(s[k] for k in KINDS), f"landing-type counts do not add up for {where}"
    assert s["commits"] == s["changes"] + s["folded_pr_commits"] + s["sync_merges"], f"commit counts do not add up for {where}"
assert sum(s["changes"] for s in S) == len(rows), "release totals do not match the number of changes"

fields = ["repo", "release_tag", "tags", "published", "commits", "changes"] + CATS + ["uncategorised"] + KINDS + ["folded_pr_commits", "sync_merges", "community_prs", "team_prs", "humans", "new_humans", "agents", "agent_names", "bots", "changes_agent_disclosed", "changes_agent_authored", "changes_no_human", "url"]
with open(f"{ROOT}/csv/release_stats.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(S)
with open(f"{ROOT}/csv/changes.csv", "w", newline="") as f:
    cols = ["repo", "release", "date", "category", "basis", "kind", "pr", "human", "coauthors", "agents_author", "agents_coauthor", "agent_models", "bots", "assoc", "branch", "title", "sha"]
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader()
    for r in rows:
        w.writerow({**r, **{k: "; ".join(r[k]) for k in ("coauthors", "agents_author", "agents_coauthor", "agent_models", "bots")}})

# ---- contributors: released, categorised changes only, like the headline numbers
released = [r for r in rows if r["category"] != "uncategorised" and r["release"] != "(unreleased)"]
rel_order = {(x["repo"], x["release"]): i for i, x in enumerate(rels)}

def contributor_rows(changes, scope):
    """One row per human, agent and bot behind `changes`."""
    acc = {}
    def row(name, kind):
        return acc.setdefault((kind, name), dict(repo=scope, contributor=name, kind=kind, changes_authored=0, changes_coauthored=0,
                                                 changes_disclosing_agent=0, _rels=set()))
    for r in changes:
        key = (r["repo"], r["release"])
        if r["human"]:
            d = row(r["human"], "human"); d["changes_authored"] += 1; d["changes_disclosing_agent"] += bool(agents(r)); d["_rels"].add(key)
        for h in r["coauthors"]:
            d = row(h, "human"); d["changes_coauthored"] += 1; d["_rels"].add(key)
        for f in r["agents_author"]:
            d = row(f, "agent"); d["changes_authored"] += 1; d["_rels"].add(key)
        for f in r["agents_coauthor"]:
            d = row(f, "agent"); d["changes_coauthored"] += 1; d["_rels"].add(key)
        for b in r["bots"]:
            d = row(b, "bot"); d["changes_authored"] += 1; d["_rels"].add(key)
    out = []
    for d in acc.values():
        ordered = sorted(d.pop("_rels"), key=rel_order.get)
        d["releases"] = len(ordered)
        d["first_release"], d["last_release"] = (ordered[0][1], ordered[-1][1]) if scope != "(all)" else ("", "")
        if d["kind"] != "human": d["changes_disclosing_agent"] = ""
        out.append(d)
    return sorted(out, key=lambda d: (["human", "agent", "bot"].index(d["kind"]), -(d["changes_authored"] + d["changes_coauthored"]), d["contributor"].lower()))

C_ALL = contributor_rows(released, "(all)")
C_REPO = {repo: contributor_rows([r for r in released if r["repo"] == repo], repo) for repo in repos}
with open(f"{ROOT}/csv/contributors.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["repo", "contributor", "kind", "changes_authored", "changes_coauthored", "changes_disclosing_agent", "releases", "first_release", "last_release"])
    w.writeheader(); w.writerows(C_ALL)
    for repo in repos: w.writerows(C_REPO[repo])

def n(v): return str(v) if v else "·"
def table(header, lines): return "\n".join(["| " + " | ".join(header) + " |", "|" + "|".join(["---"] + ["--:"] * (len(header) - 1)) + "|"] + ["| " + " | ".join(l) + " |" for l in lines])
def total(ss, keys): return {k: sum(s[k] for s in ss) for k in keys}
def label(s):
    if s["release_tag"] == "(unreleased)": return "_unreleased (main)_"
    t = s["tags"] if len(s["tags"]) < 40 else s["release_tag"] + " (+win)"
    return f"[{t}]({s['url']})" if s["url"] else t

def picture(repo, chart, alt):
    """A chart PNG from charts/, in the reader's light or dark theme (written by web/scripts/export-charts.mjs)."""
    return (f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/{repo}-{chart}.png">\n'
            f'  <img alt="{alt}" src="../charts/light/{repo}-{chart}.png">\n</picture>')
def bullets(sentences): return ["**What this shows**", ""] + [f"- {x}" for x in sentences] + [""]

for repo in repos:
    ss = [s for s in S if s["repo"] == repo]
    tagged = [s for s in ss if s["release_tag"] != "(unreleased)"]
    cs = [s for s in tagged if not s["uncategorised"]]
    unreleased = next((s for s in ss if s["release_tag"] == "(unreleased)"), None)
    out = [f"# {repo} — changes per release", "",
           f"{len(tagged)} releases, {tagged[0]['published']} → {tagged[-1]['published']}. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.", ""]
    out += ["## Changes by type", "",
            picture(repo, "changes-line", f"{repo}: changes per release, stacked by type, as lines"), "",
            picture(repo, "changes-bar", f"{repo}: changes per release, stacked by type, as bars"), ""]
    out += bullets(commentary.types(repo, cs, unreleased, [x for x in tagged if x["uncategorised"]]))
    lines = []
    for s in ss:
        if s["uncategorised"]:
            lines.append([label(s), s["published"], n(s["changes"])] + ["–"] * len(CATS)); continue
        lines.append([label(s), s["published"], n(s["changes"])] + [n(s[c]) for c in CATS])
    t = total(cs, ["changes"] + CATS)
    lines.append(["**Released total**", "", f"**{t['changes']}**"] + [f"**{t[c]}**" if t[c] else "·" for c in CATS])
    out += [table(["Release", "Published", "Changes"] + [HEAD[c] for c in CATS], lines), ""]
    if any(s["uncategorised"] for s in ss):
        out += ["`–` = not categorised: the first ArtCraft release sits on top of ~13,400 commits of earlier monorepo history (2015–2025), which is counted but not labelled.", ""]
    if t["changes"]:
        out += ["Share of released changes: " + ", ".join(f"{HEAD[c].lower()} {100 * t[c] / t['changes']:.0f}%" for c in CATS if t[c] / t["changes"] >= 0.005) + ".", ""]
    out += ["## How changes landed", ""]
    out += bullets(commentary.landing(cs))
    lines = [[label(s), n(s["commits"]), n(s["pr-merge"]), n(s["squash"]), n(s["direct"]), n(s["batch-commit"]), n(s["folded_pr_commits"]), n(s["sync_merges"]), n(s["community_prs"]), n(s["team_prs"])] for s in ss]
    t = total(tagged, ["commits", "pr-merge", "squash", "direct", "batch-commit", "folded_pr_commits", "sync_merges", "community_prs", "team_prs"])
    lines.append(["**Released total**"] + [f"**{t[k]}**" for k in ["commits", "pr-merge", "squash", "direct", "batch-commit", "folded_pr_commits", "sync_merges", "community_prs", "team_prs"]])
    out += [table(["Release", "Commits", "PR merges", "Squash merges", "Direct commits", "Batch commits", "Commits inside PRs", "Sync merges", "Community PRs", "Team PRs"], lines), ""]
    out += ["Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.", ""]
    out += ["## Contributors", "",
            picture(repo, "contributors", f"{repo}: unique contributors per release (returning humans, new humans, disclosed agents, bots)"), "",
            picture(repo, "agent-disclosure", f"{repo}: changes per release by agent disclosure"), ""]
    out += bullets(commentary.contributors(cs, C_REPO[repo], sum(x["changes"] for x in cs)))
    pct = lambda a, b: "·" if not b else "<1%" if 0 < a < b / 100 else f"{100 * a / b:.0f}%"
    lines = [[label(s), n(s["humans"]), n(s["new_humans"]), n(s["changes_agent_disclosed"]), pct(s["changes_agent_disclosed"], s["changes"]),
              n(s["changes_agent_authored"]), s["agent_names"] or "·", n(s["bots"])] for s in ss]
    cr = C_REPO[repo]; kinds_n = collections.Counter(d["kind"] for d in cr)
    mine = [r for r in released if r["repo"] == repo]
    lines.append(["**Released total**", f"**{kinds_n['human']}**", "", f"**{sum(1 for r in mine if agents(r))}**", pct(sum(1 for r in mine if agents(r)), len(mine)),
                  f"**{sum(1 for r in mine if r['agents_author'])}**", ", ".join(d["contributor"] for d in cr if d["kind"] == "agent") or "·", n(kinds_n["bot"])])
    out += [table(["Release", "Humans", "New", "Changes disclosing an agent", "Share", "Agent is git author", "Agents disclosed", "Bots"], lines).replace("|---|--:|--:|--:|--:|--:|--:|--:|", "|---|--:|--:|--:|--:|--:|---|--:|"), ""]
    out += ["Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.", ""]
    top = [d for d in cr if d["kind"] == "human"][:10]
    if top:
        out += ["Most active humans in released changes: " + ", ".join(f"{d['contributor']} ({d['changes_authored'] + d['changes_coauthored']})" for d in top) + ".", ""]
    open(f"{ROOT}/reports/{repo}.md", "w").write("\n".join(out))
    for ref in re.findall(r'(?:srcset|src)="([^"]+)"', "\n".join(out)):
        if not os.path.exists(os.path.join(ROOT, "reports", ref)): print(f"missing chart: reports/{repo}.md embeds {ref}", file=sys.stderr)

# README
cs = [s for s in S if s["release_tag"] != "(unreleased)" and not s["uncategorised"]]
lines = []
for repo in repos:
    ss = [s for s in cs if s["repo"] == repo]; t = total(ss, ["changes"] + CATS)
    nrel = len([s for s in S if s["repo"] == repo and s["release_tag"] != "(unreleased)"])
    rest = t["changes"] - t["feature"] - t["fix"] - t["perf"]
    lines.append([f"[{repo}](reports/{repo}.md)", n(nrel), ss[-1]["release_tag"].replace("artcraft-", ""), n(t["changes"]), n(t["feature"]), n(t["fix"]), n(t["perf"]), n(rest),
                  f"{100 * t['feature'] / t['changes']:.0f}%", f"{100 * t['fix'] / t['changes']:.0f}%", f"{100 * t['perf'] / t['changes']:.1f}%"])
T = total(cs, ["changes"] + CATS)
lines.append(["**All**", f"**{len([s for s in S if s['release_tag'] != '(unreleased)'])}**", "", f"**{T['changes']}**", f"**{T['feature']}**", f"**{T['fix']}**", f"**{T['perf']}**", f"**{T['changes'] - T['feature'] - T['fix'] - T['perf']}**",
              f"{100 * T['feature'] / T['changes']:.0f}%", f"{100 * T['fix'] / T['changes']:.0f}%", f"{100 * T['perf'] / T['changes']:.1f}%"])
summary = table(["Repo", "Releases", "Latest", "Changes", "Feature", "Fix", "Perf", "Everything else", "Feature %", "Fix %", "Perf %"], lines)
allcat = table(["Category", "Changes", "Share"], [[HEAD[c], n(T[c]), f"{100 * T[c] / T['changes']:.1f}%"] for c in CATS])
cl = [r for r in rows if r["category"] != "uncategorised"]
basis = collections.Counter(r["basis"] for r in cl); kinds = collections.Counter(r["kind"] for r in cl)
BASIS = {"prefix": "Conventional-commit prefix on the title (`fix(...)`, `feat:`, `perf:` …)", "branch": "PR branch name (`fix/…`, `feat/…`, `perf/…`, `docs/…`)",
         "label": "`bug` / `enhancement` label on the PR or the issue it closes", "review": "Title read and labelled by an LLM (Claude Haiku), for titles with no prefix, branch or label signal",
         "keyword": "Keyword rules on the title: version bumps, release prep and reverts, plus any title not yet read by the LLM", "integration-batch": "Integration-batch PR that only bundles other PRs (counted as Other)", "unclassified": "No signal at all (counted as Other)"}
basis_t = table(["How the category was decided", "Changes", "Share"], [[BASIS[b], n(v), f"{100 * v / len(cl):.1f}%"] for b, v in basis.most_common()])
open(f"{ROOT}/data/_summary.json", "w").write(json.dumps(dict(summary=summary, allcat=allcat, basis=basis_t, kinds=dict(kinds), total=len(cl), generated=datetime.date.today().isoformat()), ensure_ascii=False))
print(summary); print(); print(allcat); print(); print(basis_t); print(dict(kinds))

# ---- README ----
# Contributors
pct = lambda a, b: "·" if not b else "<1%" if 0 < a < b / 100 else f"{100 * a / b:.0f}%"
kinds_all = collections.Counter(d["kind"] for d in C_ALL)
n_disclosed = sum(1 for r in released if agents(r))
n_agent_author = sum(1 for r in released if r["agents_author"])
n_no_human = sum(1 for r in released if not people(r))
humans_all = [d for d in C_ALL if d["kind"] == "human"]
n_humans_disclosing = sum(1 for d in humans_all if d["changes_disclosing_agent"])
n_authors = sum(1 for d in humans_all if d["changes_authored"])
lines = []
for repo in repos:
    mine = [r for r in released if r["repo"] == repo]; k = collections.Counter(d["kind"] for d in C_REPO[repo])
    lines.append([f"[{repo}](reports/{repo}.md)", n(k["human"]), n(sum(1 for r in mine if agents(r))), pct(sum(1 for r in mine if agents(r)), len(mine)),
                  n(sum(1 for r in mine if r["agents_author"])), ", ".join(d["contributor"] for d in C_REPO[repo] if d["kind"] == "agent") or "·", n(k["bot"])])
lines.append(["**All**", f"**{kinds_all['human']}**", f"**{n_disclosed}**", pct(n_disclosed, len(released)), f"**{n_agent_author}**", f"{kinds_all['agent']} agents", n(kinds_all["bot"])])
contrib_t = table(["Repo", "Humans", "Changes disclosing an agent", "Share", "Agent is git author", "Agents disclosed", "Bots"], lines).replace("|---|--:|--:|--:|--:|--:|--:|", "|---|--:|--:|--:|--:|---|--:|")
fam_people = collections.defaultdict(set); fam_repos = collections.defaultdict(set); fam_models = collections.defaultdict(collections.Counter)
for r in released:
    for f in agents(r):
        fam_repos[f].add(r["repo"])
        if r["human"]: fam_people[f].add(r["human"])
agent_t = table(["Agent", "Changes", "As git author", "As co-author", "Humans authoring those changes", "Repos"],
                [[d["contributor"], n(d["changes_authored"] + d["changes_coauthored"]), n(d["changes_authored"]), n(d["changes_coauthored"]),
                  n(len(fam_people[d["contributor"]])), n(len(fam_repos[d["contributor"]]))] for d in C_ALL if d["kind"] == "agent"])
models = collections.Counter(m for r in released for m in r["agent_models"])
model_line = ", ".join(f"{m} ({c})" for m, c in models.most_common(8))
n_org = sum(1 for _ in open(f"{ROOT}/data/org_repos.jsonl"))
n_gh = sum(len(json.load(open(f"{ROOT}/data/releases_api/{r}.json"))) for r in repos)
n_points = len([s for s in S if s["release_tag"] != "(unreleased)"])
U = [s for s in S if s["release_tag"] == "(unreleased)"]
ut = total(U, ["changes", "feature", "fix", "perf"])
KT = {"pr-merge": "PR merge", "squash": "Squash merge", "direct": "Direct commit", "batch-commit": "Batch commit"}
KD = {"pr-merge": "a `Merge pull request #N` / `Merge PR #N` merge commit, at any depth of the history (PRs merged into an integration branch count too). The PR's own commits are folded into it.",
      "squash": "a single commit that is the squash of PR #N.",
      "direct": "a non-merge commit pushed straight to the mainline (or brought in by a plain branch merge) with no PR behind it.",
      "batch-commit": "a commit made directly on an integration-batch PR branch (follow-up fixes, formatting, conflict clean-up after merging a batch of contributor PRs)."}
kind_t = table(["Landing type", "Changes", "What it is"], [[KT[k], n(kinds.get(k, 0)), KD[k]] for k in KINDS]).replace("|---|--:|--:|", "|---|--:|---|")
readme = f"""# storytold — changes per release

Generated {datetime.date.today().isoformat()} from the public repos at https://github.com/storytold.

The org has {n_org} repos; {len(repos)} of them publish GitHub releases, and those are the ones covered here. Their {n_gh} GitHub releases make {n_points} distinct release points (ArtCraft tags macOS and Windows builds of one version separately, and one PhotoCraft release candidate shares a commit with v0.1.0).
Every change that landed in a release is put in one category (feature, fix, perf, …) and one landing type (PR merge, squash merge, direct commit, batch commit).

## Headline numbers (released changes only)

{summary}

"Everything else" is i18n, docs, tests, build/CI, release housekeeping, refactors, dependency bumps, security hardening, reverts and changes that could not be categorised. Per-release tables for every repo are in [`reports/`](reports/).

A further {ut['changes']} changes are on `main` but not yet in a release ({ut['feature']} features, {ut['fix']} fixes, {ut['perf']} perf); they appear as the "unreleased" row in each repo report and are not in the table above.

### All categories

{allcat}

## Contributors: humans, agents and bots

{kinds_all['human']} humans contributed to the released changes ({n_authors} as the author of at least one change, the rest only as co-authors), alongside {kinds_all['agent']} disclosed AI agents and {kinds_all['bot']} bot{'' if kinds_all['bot'] == 1 else 's'}. {n_disclosed} of the {len(released)} changes ({pct(n_disclosed, len(released))}) disclose an agent, and {n_humans_disclosing} of the humans authored at least one change that does.

{contrib_t}

A human is counted once per repo here, and once in the **All** row even if they contributed to several repos.

### Disclosed agents

{agent_t}

"As git author" means the commit's author is the agent itself; "as co-author" means a human is the author and the agent is named in a `Co-authored-by` trailer or a "Generated with" line. A change that discloses two agents counts for both. {n_no_human} changes have an agent as git author and no human named at all. The model names seen most often: {model_line}.

`csv/contributors.csv` lists every human, agent and bot per repo and across the org.

## How the numbers are produced

**Release ranges.** For each repo the release tags are ordered by version. A release's changes are the commits reachable from its tag but not from any earlier release tag; the first release gets everything before it.

**What counts as one change.** Counting raw commits would overstate repos that merge multi-commit PR branches, and counting only first-parent commits would hide the PRs that land through integration branches. So each release range is split into:

{kind_t}

Commits inside an ordinary PR branch and plain sync merges (`Merge branch 'main' into …`) are not changes; they are reported separately in each repo's "By how it landed" table. Counts are counts of changes, not of lines or effort: a one-line fix and a whole new subsystem each count once.

**Contributors.** The contributors of a change are read from its commits (for a PR merge, every commit in the PR branch) and its PR:

- **Human:** the PR's author, or the commit's git author when there is no PR, plus anyone named in a `Co-authored-by` trailer and anyone else who authored a commit in the PR branch. Each is resolved to a GitHub login where the history gives one (a GitHub noreply address, a squash-merge commit authored by the PR's author, or being the main committer in a PR that login opened) and otherwise kept as the git name.
- **Agent (disclosed):** a known AI agent identity appearing as a commit's git author (for example `Claude <noreply@anthropic.com>`), in a `Co-authored-by` trailer (`Claude Opus 5.5`, `Codex`, `Copilot`, …), or in a "Generated with …" line. Model variants are grouped under one agent: every Claude model is "Claude". The table of recognised agents is in `scripts/contributors.py`.
- **Bot:** a non-AI automation account, such as `dependabot[bot]`.

**Categories.**

| Category | Meaning |
|---|---|
| Feature | New user-visible capability or a deliberate extension/redesign of one |
| Fix | Corrects wrong behaviour: bugs, crashes, wrong output, regressions, parity corrections |
| Perf | Speed, memory or responsiveness is the point of the change |
| i18n | Translations, locale catalogs, new interface languages |
| Docs | README, AGENTS.md, roadmap/parity trackers, guides, licences |
| Test | Only tests, fixtures, fuzzers, corpora |
| Build/CI | CI workflows, release pipeline, packaging, signing, build tooling |
| Release | Version bumps and release prep |
| Refactor | Internal restructuring, formatting, clean-up, merge fix-ups, with no intended behaviour change |
| Deps | Dependency bumps and pins |
| Security | Hardening against hostile input, sandboxing, signature checks |
| Revert | Reverts an earlier change |
| Other | Integration-batch PRs, and titles that say too little to categorise |

**How each change got its category.** The strongest available signal wins, and the one used is recorded per change in `csv/changes.csv` (`basis` column):

{basis_t}

## Things to know before quoting these

- **The feature/fix split is partly a judgment call.** Roughly half of the changes have no prefix, branch name or label saying what they are; those were labelled from their title alone by an LLM (Claude Haiku, in 8 batches, plus one batch of 217 titles in a later refresh and three batches of 1,394 titles in the refresh after that). The labels were spot-checked against the titles and checked for row alignment; one run of 53 shifted labels was found and repaired. The 217-title batch was read against its titles in full and had no shifts; the three later batches were sampled against their titles, and the one run the alignment check flagged (40 rows) was read in full and found not to be shifted. No human has reviewed them one by one. Titles in these repos often just state the new behaviour ("Layers: the active layer falls back to the top layer when it is removed"), which reads as a fix but could be argued either way. Treat the split as indicative, not exact.
- **Agent figures are a floor.** They count what the history discloses. A change written with an agent but committed without a trailer looks human-only, and squash merges keep trailers only if the person merging left them in.
- **"Human" means "not a recognised agent or bot".** An account that is run by an agent but does not say so, or an agent whose name is not in the table yet, is counted as a human.
- **A few people may be counted twice.** {sum(1 for d in humans_all if not d["contributor"].startswith("@"))} of the {kinds_all['human']} humans could not be tied to a GitHub login and are identified by git name only; some of them may be the same person as a login.
- **GitHub labels were of no use.** Only a handful of PRs or linked issues carry `bug`/`enhancement` labels.
- **"fixes #123" is not treated as a bug-fix signal.** It is GitHub's issue-closing keyword and is used on feature PRs too.
- **ArtCraft's first release (`artcraft-v0.0.1`) is not categorised.** It sits on about 13,400 commits of earlier monorepo history going back to 2015. It is counted, not labelled, and is left out of every total above.
- **ArtCraft's history was reset before v0.41.0.** `main` was restarted on 2026-09-11, so v0.41.0 covers only the 11 commits on the new history. ArtCraft's macOS and Windows tags for the same version are treated as one release.
- **Not every version number has a release.** Several repos skip versions (e.g. v0.5.0 → v0.6.2); a row covers everything since the previous published release.
- **PhotoCraft `v0.1.0` and `v0.1.1-rc.4` are the same commit** and are shown as one row.
- **Community vs team PRs** uses GitHub's author association at the time of fetching (member/owner/collaborator = team).

## Files

- `reports/<repo>.md` — one repo's charts, a short plain-English commentary on its trends, and per-release tables: by change type, by how changes landed, and by contributor. The commentary rounds shares to whole percentages but never shows 0% or 100%: a share of zero is "none", a complete one is "all", and anything rounded to either end is "under 1%" or "over 99%"
- `csv/release_stats.csv` — the same numbers, one row per repo and release
- `csv/changes.csv` — every change with its release, category, basis, landing type, PR number, contributors (human, co-authors, agents, bots) and title
- `csv/contributors.csv` — every human, agent and bot with their change counts, per repo and across the org (`repo` = `(all)`)
- `web/` — SvelteKit + LayerChart app with a stacked line chart and a stacked bar chart per repo, flat or isometric (`cd web && pnpm install && pnpm dev`)
- `charts/light/`, `charts/dark/` — PNG exports of the four charts on each repo's page, embedded in the reports
- `data/` — inputs and per-change output: PR metadata (`prs/`, `prs_extra/`), release lists (`releases_api/`), LLM labels (`review_labels.jsonl`, batches in `review/`), and every classified change (`classified.jsonl`)
- `scripts/` — the pipeline
- `.agents/skills/` — instructions for an AI agent: `compile-stats` refreshes the stats from GitHub, `create-reports` generates the reports, their charts and their commentary

## Repos not covered

These have no GitHub releases, so there is nothing to break down per release: artcraft-services (the largest repo by history, ~15,000 commits), craft-libs, craft-repo-status-app, craft-common-actions, craft-launcher-assets, craft-fonts, photocraft-corpus, artcraftx, cloud-worker, github-media, storyteller-ml, storyteller-bevy, fakeyou-recast, and about 30 older, archived or forked repos (Unreal/Unity plugins, ML experiments, forks such as spark and winprint.rs).

## Licence

[MIT](LICENSE).
"""
open(f"{ROOT}/README.md", "w").write(readme)
