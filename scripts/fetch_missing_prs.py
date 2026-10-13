"""Fetch titles for PRs that were merged by hand ("Merge PR #N") but that GitHub records as closed.

fetch_prs.sh only lists PRs GitHub marks as merged, so these merges come out of build_changes.py
with no title. This appends them to data/prs_extra/<repo>.jsonl; re-run build_changes.py afterwards.
"""
import json, os, subprocess, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
rows = [json.loads(l) for l in open(f"{ROOT}/data/changes.jsonl")]
missing = sorted({(r["repo"], r["pr"]) for r in rows if r["kind"] == "pr-merge" and not r["pr_title"]
                  and not (r["repo"] == "artcraft" and r["release"] == "artcraft-v0.0.1")})
os.makedirs(f"{ROOT}/data/prs_extra", exist_ok=True)
added = 0
for repo, n in missing:
    p = subprocess.run(["gh", "api", f"repos/storytold/{repo}/pulls/{n}"], capture_output=True, text=True)
    if p.returncode:
        print(f"skip {repo}#{n}: {p.stderr.strip()[:80]}", file=sys.stderr)
        continue
    d = json.loads(p.stdout)
    rec = dict(number=n, title=d["title"], head=d["head"]["ref"], base=d["base"]["ref"], mergedAt=d["merged_at"],
               additions=d["additions"], deletions=d["deletions"], changedFiles=d["changed_files"],
               assoc=d["author_association"], author=d["user"]["login"], authorType=d["user"]["type"],
               mergeCommit=None, labels=[l["name"] for l in d["labels"]], issues=[], state=d["state"])
    with open(f"{ROOT}/data/prs_extra/{repo}.jsonl", "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    added += 1
print(f"fetched {added} of {len(missing)} missing PR titles" + ("; re-run build_changes.py" if added else ""))
