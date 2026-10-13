"""Walk each release range and emit one row per change into data/changes.jsonl.

A "change" is one of:
  pr-merge      merge commit "Merge pull request #N" / "Merge PR #N" (any depth)
  squash        non-merge commit that is the squash of merged PR #N
  direct        non-merge commit that is not inside any PR branch
  batch-commit  non-merge commit sitting directly on an integration-batch PR branch
Commits inside an ordinary PR branch are folded into their PR (counted as pr_commits).
"""
import subprocess, re, json, os, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contributors import Identities, contributors, SUSPECTS

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REPOS = open(os.path.join(ROOT, "scripts", "repos.txt")).read().split()
PR_MERGE = re.compile(r"^Merge (?:pull request|PR) #(\d+)\b")
SQUASH = re.compile(r"\(#(\d+)\)\s*$")

def git(repo, *args):
    return subprocess.run(["git", "-C", f"{ROOT}/repos/{repo}.git", *args], capture_output=True, text=True, check=True).stdout

def vkey(tag):
    m = re.search(r"v(\d+)\.(\d+)\.(\d+)(?:-rc\.(\d+))?", tag)
    return (int(m[1]), int(m[2]), int(m[3]), int(m[4]) if m[4] else 10**6) if m else None

def load(repo):
    commits, order = {}, []
    out = git(repo, "log", "--all", "--topo-order", "--format=%H%x1f%P%x1f%an%x1f%ae%x1f%cI%x1f%s%x1f%b%x1e")
    for rec in out.split("\x1e"):
        rec = rec.strip("\n")
        if not rec: continue
        h, p, an, ae, cd, s, b = rec.split("\x1f")
        commits[h] = dict(sha=h, parents=p.split(), author=an, email=ae, date=cd, subject=s, body=b)
        order.append(h)
    return commits, order

def ancestors(commits, tips, stop=frozenset()):
    seen, stack = set(), [t for t in tips if t not in stop]
    while stack:
        c = stack.pop()
        if c in seen or c in stop: continue
        seen.add(c)
        stack.extend(p for p in commits[c]["parents"] if p in commits)
    return seen

def releases(repo, commits):
    tags = {}
    for line in git(repo, "for-each-ref", "--format=%(refname:short)%09%(*objectname)%09%(objectname)", "refs/tags").splitlines():
        name, peeled, obj = line.split("\t")
        if vkey(name) is None: continue
        tags[name] = peeled or obj
    by_commit = collections.OrderedDict()
    for name in sorted(tags, key=lambda t: (vkey(t), t)):
        by_commit.setdefault(tags[name], []).append(name)
    # artcraft: macOS + Windows tags for one version are one release
    rels = []
    for sha, names in by_commit.items():
        rels.append(dict(tags=names, sha=sha))
    if repo == "artcraft":
        merged = []
        for r in rels:
            v = vkey(r["tags"][0])
            if merged and vkey(merged[-1]["tags"][0]) == v:
                merged[-1]["tags"] += r["tags"]
                merged[-1]["extra_tips"] = merged[-1].get("extra_tips", []) + [r["sha"]]
            else:
                merged.append(r)
        rels = merged
    return rels

def main():
    rows, relrows, pending = [], [], []
    loaded, ids = {}, Identities()
    for repo in REPOS:
        commits, order = load(repo)
        prs = {}
        # prs_extra holds PRs merged by hand that GitHub lists as closed (see fetch_missing_prs.py)
        for path in (f"{ROOT}/data/prs_extra/{repo}.jsonl", f"{ROOT}/data/prs/{repo}.jsonl"):
            if not os.path.exists(path): continue
            with open(path) as f:
                for line in f:
                    pr = json.loads(line); prs[pr["number"]] = pr
        by_oid = {pr["mergeCommit"]: n for n, pr in prs.items() if pr.get("mergeCommit")}
        loaded[repo] = commits, order, prs, by_oid
        # A squash merge's git author is the PR's author: that ties a name and email to a login
        for oid, n in by_oid.items():
            cm = commits.get(oid)
            if cm and len(cm["parents"]) < 2 and prs[n].get("authorType") == "User":
                ids.learn(cm["author"], cm["email"], prs[n].get("author"))
    for repo in REPOS:
        commits, order, prs, by_oid = loaded[repo]
        rels = releases(repo, commits)
        head = git(repo, "rev-parse", "main").strip()
        rels.append(dict(tags=["(unreleased)"], sha=head))
        done = set()
        for i, rel in enumerate(rels):
            tips = [rel["sha"]] + rel.get("extra_tips", [])
            rng = ancestors(commits, tips, stop=done)
            done |= rng
            if rel["tags"][0] == "(unreleased)" and not rng: continue
            # PR-merge commits and the commits each one brought in
            brought = {}
            for c in rng:
                cm = commits[c]
                if len(cm["parents"]) > 1 and PR_MERGE.match(cm["subject"]):
                    base = ancestors(commits, [cm["parents"][0]])
                    brought[c] = ancestors(commits, cm["parents"][1:], stop=base) & rng
            is_batch = {m: any(x in brought for x in s) for m, s in brought.items()}
            owner = {}
            # Smallest first, so a commit belongs to the innermost PR; the sha breaks ties so runs agree
            for m, s in sorted(brought.items(), key=lambda kv: (len(kv[1]), kv[0])):
                for x in s: owner.setdefault(x, m)
            pr_commits = collections.Counter(o for x, o in owner.items() if len(commits[x]["parents"]) < 2)
            n_change = 0; sync_merges = 0; folded = 0
            for c in order:
                if c not in rng: continue
                cm = commits[c]; merge = len(cm["parents"]) > 1
                pm = PR_MERGE.match(cm["subject"]) if merge else None
                num = None
                if pm:
                    kind, num = "pr-merge", int(pm[1])
                elif merge:
                    sync_merges += 1; continue
                else:
                    sq = SQUASH.search(cm["subject"])
                    if c in by_oid: kind, num = "squash", by_oid[c]
                    elif sq and int(sq[1]) in prs and c not in owner: kind, num = "squash", int(sq[1])
                    elif c in owner and not is_batch[owner[c]]: folded += 1; continue
                    elif c in owner: kind = "batch-commit"
                    else: kind = "direct"
                pr = prs.get(num) if num else None
                title = cm["subject"]
                if kind == "pr-merge":
                    title = (pr["title"] if pr else None) or cm["body"].strip().split("\n")[0] or re.sub(r"^Merge PR #\d+:?\s*", "", cm["subject"]) or cm["subject"]
                # A PR merge speaks for the commits folded into it; a batch PR's own commits are changes themselves
                mine = [cm] + ([commits[x] for x in sorted(brought[c]) if owner.get(x) == c] if kind == "pr-merge" and not is_batch[c] else [])
                rows.append(dict(
                    id=f"{repo}@{c[:10]}", repo=repo, release=rel["tags"][0], sha=c, date=cm["date"], kind=kind, pr=num,
                    title=title, subject=cm["subject"], author=(pr or {}).get("author") or cm["author"],
                    assoc=(pr or {}).get("assoc"), author_type=(pr or {}).get("authorType"),
                    branch=(pr or {}).get("head"), labels=(pr or {}).get("labels", []),
                    issue_labels=sorted({l for i in (pr or {}).get("issues", []) for l in i["labels"]}),
                    pr_title=(pr or {}).get("title"), pr_commits=pr_commits.get(c, 0) if kind == "pr-merge" else 0,
                    is_batch=bool(is_batch.get(c)), additions=(pr or {}).get("additions"), deletions=(pr or {}).get("deletions"),
                ))
                pending.append((rows[-1], mine, pr))
                # Whoever wrote most of a PR's commits is usually the person who opened it
                if kind == "pr-merge" and len(mine) > 1 and pr and pr.get("authorType") == "User":
                    (who, email), _ = collections.Counter((x["author"], x["email"]) for x in mine[1:] if len(x["parents"]) < 2).most_common(1)[0] if any(len(x["parents"]) < 2 for x in mine[1:]) else ((None, None), 0)
                    if who: ids.vote(who, email, pr.get("author"))
                n_change += 1
            relrows.append(dict(repo=repo, release=rel["tags"][0], tags=rel["tags"], sha=rel["sha"], date=commits[rel["sha"]]["date"],
                                commits=len(rng), changes=n_change, sync_merges=sync_merges, folded_pr_commits=folded,
                                initial=(i == 0)))
        print(repo, "releases", len(rels), "changes", sum(1 for r in rows if r["repo"] == repo), file=sys.stderr)
    # Contributors are resolved last, once every repo has added what it knows about who is who
    ids.settle_votes()
    for row, mine, pr in pending: row.update(contributors(mine, pr, ids))
    if SUSPECTS:
        print("counted as human, but the address looks automated; add to AGENTS in contributors.py if it is an agent:",
              ", ".join(f"{n} ({c})" for n, c in SUSPECTS.most_common(15)), file=sys.stderr)
    with open(f"{ROOT}/data/changes.jsonl", "w") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(f"{ROOT}/data/releases.jsonl", "w") as f:
        for r in relrows: f.write(json.dumps(r, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()
