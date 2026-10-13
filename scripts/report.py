"""Write README.md, reports/<repo>.md, csv/release_stats.csv and csv/changes.csv from data/classified.jsonl."""
import json, os, csv, collections, datetime
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

def stats(rel):
    ch = by[(rel["repo"], rel["release"])]
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
                authors=len({r["author"] for r in ch}))

S = [stats(r) for r in rels]
fields = ["repo", "release_tag", "tags", "published", "commits", "changes"] + CATS + ["uncategorised"] + KINDS + ["folded_pr_commits", "sync_merges", "community_prs", "team_prs", "authors", "url"]
with open(f"{ROOT}/csv/release_stats.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(S)
with open(f"{ROOT}/csv/changes.csv", "w", newline="") as f:
    cols = ["repo", "release", "date", "category", "basis", "kind", "pr", "author", "assoc", "branch", "title", "sha"]
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)

def n(v): return str(v) if v else "·"
def table(header, lines): return "\n".join(["| " + " | ".join(header) + " |", "|" + "|".join(["---"] + ["--:"] * (len(header) - 1)) + "|"] + ["| " + " | ".join(l) + " |" for l in lines])
def total(ss, keys): return {k: sum(s[k] for s in ss) for k in keys}
def label(s):
    if s["release_tag"] == "(unreleased)": return "_unreleased (main)_"
    t = s["tags"] if len(s["tags"]) < 40 else s["release_tag"] + " (+win)"
    return f"[{t}]({s['url']})" if s["url"] else t

for repo in repos:
    ss = [s for s in S if s["repo"] == repo]
    tagged = [s for s in ss if s["release_tag"] != "(unreleased)"]
    out = [f"# {repo} — changes per release", "",
           f"{len(tagged)} releases, {tagged[0]['published']} → {tagged[-1]['published']}. Each row counts the changes that landed between the previous release tag and this one; the first row is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised.", ""]
    out += ["## By category", ""]
    lines = []
    for s in ss:
        if s["uncategorised"]:
            lines.append([label(s), s["published"], n(s["changes"])] + ["–"] * len(CATS)); continue
        lines.append([label(s), s["published"], n(s["changes"])] + [n(s[c]) for c in CATS])
    cs = [s for s in tagged if not s["uncategorised"]]
    t = total(cs, ["changes"] + CATS)
    lines.append(["**Released total**", "", f"**{t['changes']}**"] + [f"**{t[c]}**" if t[c] else "·" for c in CATS])
    out += [table(["Release", "Published", "Changes"] + [HEAD[c] for c in CATS], lines), ""]
    if any(s["uncategorised"] for s in ss):
        out += ["`–` = not categorised: the first ArtCraft release sits on top of ~13,400 commits of earlier monorepo history (2015–2025), which is counted but not labelled.", ""]
    if t["changes"]:
        out += ["Share of released changes: " + ", ".join(f"{HEAD[c].lower()} {100 * t[c] / t['changes']:.0f}%" for c in CATS if t[c] / t["changes"] >= 0.005) + ".", ""]
    out += ["## By how it landed", ""]
    lines = [[label(s), n(s["commits"]), n(s["pr-merge"]), n(s["squash"]), n(s["direct"]), n(s["batch-commit"]), n(s["folded_pr_commits"]), n(s["sync_merges"]), n(s["community_prs"]), n(s["team_prs"]), n(s["authors"])] for s in ss]
    t = total(tagged, ["commits", "pr-merge", "squash", "direct", "batch-commit", "folded_pr_commits", "sync_merges", "community_prs", "team_prs"])
    lines.append(["**Released total**"] + [f"**{t[k]}**" for k in ["commits", "pr-merge", "squash", "direct", "batch-commit", "folded_pr_commits", "sync_merges", "community_prs", "team_prs"]] + [""])
    out += [table(["Release", "Commits", "PR merges", "Squash merges", "Direct commits", "Batch commits", "Commits inside PRs", "Sync merges", "Community PRs", "Team PRs", "Authors"], lines), ""]
    out += ["Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.", ""]
    open(f"{ROOT}/reports/{repo}.md", "w").write("\n".join(out))

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
         "keyword": "Unambiguous title wording: version bumps / release prep and reverts", "integration-batch": "Integration-batch PR that only bundles other PRs (counted as Other)", "unclassified": "No signal at all (counted as Other)"}
basis_t = table(["How the category was decided", "Changes", "Share"], [[BASIS[b], n(v), f"{100 * v / len(cl):.1f}%"] for b, v in basis.most_common()])
open(f"{ROOT}/data/_summary.json", "w").write(json.dumps(dict(summary=summary, allcat=allcat, basis=basis_t, kinds=dict(kinds), total=len(cl), generated=datetime.date.today().isoformat()), ensure_ascii=False))
print(summary); print(); print(allcat); print(); print(basis_t); print(dict(kinds))

# ---- README ----
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

The org has 59 repos; 15 of them publish GitHub releases, and those are the ones covered here. Their 128 GitHub releases make 122 distinct release points (ArtCraft tags macOS and Windows builds of one version separately, and one PhotoCraft release candidate shares a commit with v0.1.0).
Every change that landed in a release is put in one category (feature, fix, perf, …) and one landing type (PR merge, squash merge, direct commit, batch commit).

## Headline numbers (released changes only)

{summary}

"Everything else" is i18n, docs, tests, build/CI, release housekeeping, refactors, dependency bumps, security hardening, reverts and changes that could not be categorised. Per-release tables for every repo are in [`reports/`](reports/).

A further {ut['changes']} changes are on `main` but not yet in a release ({ut['feature']} features, {ut['fix']} fixes, {ut['perf']} perf); they appear as the "unreleased" row in each repo report and are not in the table above.

### All categories

{allcat}

## How the numbers are produced

**Release ranges.** For each repo the release tags are ordered by version. A release's changes are the commits reachable from its tag but not from any earlier release tag; the first release gets everything before it.

**What counts as one change.** Counting raw commits would overstate repos that merge multi-commit PR branches, and counting only first-parent commits would hide the PRs that land through integration branches. So each release range is split into:

{kind_t}

Commits inside an ordinary PR branch and plain sync merges (`Merge branch 'main' into …`) are not changes; they are reported separately in each repo's "By how it landed" table. Counts are counts of changes, not of lines or effort: a one-line fix and a whole new subsystem each count once.

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

- **The feature/fix split is partly a judgment call.** Roughly half of the changes have no prefix, branch name or label saying what they are; those were labelled from their title alone by an LLM (Claude Haiku, in 8 batches). The labels were spot-checked against the titles and checked for row alignment; one run of 53 shifted labels was found and repaired. No human has reviewed them one by one. Titles in these repos often just state the new behaviour ("Layers: the active layer falls back to the top layer when it is removed"), which reads as a fix but could be argued either way. Treat the split as indicative, not exact.
- **GitHub labels were of no use.** Only a handful of PRs or linked issues carry `bug`/`enhancement` labels.
- **"fixes #123" is not treated as a bug-fix signal.** It is GitHub's issue-closing keyword and is used on feature PRs too.
- **ArtCraft's first release (`artcraft-v0.0.1`) is not categorised.** It sits on about 13,400 commits of earlier monorepo history going back to 2015. It is counted, not labelled, and is left out of every total above.
- **ArtCraft's history was reset before v0.41.0.** `main` was restarted on 2026-09-11, so v0.41.0 covers only the 11 commits on the new history. ArtCraft's macOS and Windows tags for the same version are treated as one release.
- **Not every version number has a release.** Several repos skip versions (e.g. v0.5.0 → v0.6.2); a row covers everything since the previous published release.
- **PhotoCraft `v0.1.0` and `v0.1.1-rc.4` are the same commit** and are shown as one row.
- **Community vs team PRs** uses GitHub's author association at the time of fetching (member/owner/collaborator = team).

## Files

- `reports/<repo>.md` — per-release tables for one repo: by category, and by how changes landed
- `csv/release_stats.csv` — the same numbers, one row per repo and release
- `csv/changes.csv` — every change with its release, category, basis, landing type, PR number, author and title
- `web/` — SvelteKit + LayerChart app with a stacked line chart and a stacked bar chart per repo, flat or isometric (`cd web && pnpm install && pnpm dev`)
- `charts/dark/` — PNG exports of each repo's stacked line chart
- `data/` — inputs and per-change output: PR metadata (`prs/`), release lists (`releases_api/`), LLM labels (`review/`), and every classified change (`classified.jsonl`)
- `scripts/` — the pipeline, in order:
  1. `clone_repos.sh` — bare clones of the 15 repos into `repos/` (not committed)
  2. `fetch_prs.sh <repo>` — merged-PR metadata for one repo (needs the `gh` CLI)
  3. `build_changes.py` — splits each release range into changes
  4. `classify.py` — assigns categories (`ingest_review.py` merges LLM labels first; a change without a label falls back to keyword rules)
  5. `report.py` — writes this README, `reports/` and `csv/`
  6. `export_web.py` — refreshes the web app's data

## Repos not covered

These have no GitHub releases, so there is nothing to break down per release: artcraft-services (the largest repo by history, ~15,000 commits), craft-libs, craft-repo-status-app, craft-common-actions, craft-launcher-assets, craft-fonts, photocraft-corpus, artcraftx, cloud-worker, github-media, storyteller-ml, storyteller-bevy, fakeyou-recast, and about 30 older, archived or forked repos (Unreal/Unity plugins, ML experiments, forks such as spark and winprint.rs).
"""
open(f"{ROOT}/README.md", "w").write(readme)
