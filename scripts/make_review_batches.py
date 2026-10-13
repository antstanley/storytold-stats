"""Write the titles that still need a judgment-based category to data/review/pending/in_NN.tsv.

A change needs review when no prefix, branch or label decided its category and it has no label
in data/review_labels.jsonl yet (classify.py marks these `keyword` or `unclassified`). Release and
revert titles are left to the keyword rules, which are reliable for them.

Each line is `id<TAB>repo<TAB>title`. A labeller writes `id<TAB>category` lines to out_NN.tsv
beside it; ingest_review.py merges them.
"""
import json, os, re, glob, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BATCH = 600
pending = f"{ROOT}/data/review/pending"

rows = [json.loads(l) for l in open(f"{ROOT}/data/classified.jsonl")]
todo = [r for r in rows if r["basis"] == "unclassified" or (r["basis"] == "keyword" and r["category"] not in ("release", "revert"))]
todo.sort(key=lambda r: (r["repo"], r["date"]))

os.makedirs(pending, exist_ok=True)
for old in glob.glob(f"{pending}/*.tsv"): os.remove(old)
for b in range(0, len(todo), BATCH):
    path = f"{pending}/in_{b // BATCH + 1:02d}.tsv"
    with open(path, "w") as f:
        for r in todo[b:b + BATCH]:
            f.write(f"{r['id']}\t{r['repo']}\t{re.sub(r'\\s+', ' ', r['title'])[:170]}\n")
    print(path, len(todo[b:b + BATCH]))
print(f"{len(todo)} titles need a label" if todo else "nothing to label")
