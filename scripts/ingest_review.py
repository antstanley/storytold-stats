"""Merge data/review/out_NN.tsv (key<TAB>category) into data/review_labels.jsonl; report gaps."""
import json, os, glob, sys, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import CATS
idx = json.load(open(f"{ROOT}/data/review/index.json"))
got, bad = {}, collections.Counter()
for p in sorted(glob.glob(f"{ROOT}/data/review/out_*.tsv")):
    for line in open(p, encoding="utf-8", errors="replace"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 2: bad["malformed"] += 1; continue
        k, c = parts[0].strip(), parts[1].strip().lower()
        if k not in idx: bad["unknown-key"] += 1; continue
        if c not in CATS: bad["bad-cat:" + c] += 1; continue
        if k in got: bad["duplicate"] += 1
        got[k] = c
with open(f"{ROOT}/data/review_labels.jsonl", "w") as f:
    for k, c in got.items(): f.write(json.dumps({"id": idx[k], "cat": c}) + "\n")
missing = [k for k in idx if k not in got]
per = collections.Counter(k[0] for k in missing)
print(f"labelled {len(got)}/{len(idx)}; missing by batch {dict(per)}; problems {dict(bad)}")
open(f"{ROOT}/data/review/missing.txt", "w").write("\n".join(missing))
