"""Merge labelled batches (data/review/pending/out_NN.tsv, `id<TAB>category`) into data/review_labels.jsonl.

Checks every batch before merging: unknown ids, invalid categories, missing ids, and labels that
have slipped a row against their titles (a labeller that writes 600 lines sometimes repeats or
drops one, shifting every label after it).
"""
import json, os, glob, sys, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import CATS, keyword_cat

labels_path = f"{ROOT}/data/review_labels.jsonl"
labels = {}
if os.path.exists(labels_path):
    for line in open(labels_path):
        if line.strip():
            d = json.loads(line); labels[d["id"]] = d["cat"]
before = len(labels)
problems = 0

def shifted_windows(titles, cats, window=40):
    """Row ranges where labels agree with the keyword rules better one row up or down than in place."""
    hits = []
    kw = [keyword_cat(t) for t in titles]
    for s in range(0, len(titles), window):
        score = {}
        for off in (-1, 0, 1):
            pairs = [(kw[i], cats[i + off]) for i in range(s, min(s + window, len(titles))) if kw[i] and 0 <= i + off < len(cats) and cats[i + off]]
            score[off] = sum(a == c for a, c in pairs) / max(1, len(pairs))
        best = max(score, key=score.get)
        if best != 0 and score[best] - score[0] >= 0.12:
            hits.append((s + 1, min(s + window, len(titles)), best, round(score[0], 2), round(score[best], 2)))
    return hits

for inp in sorted(glob.glob(f"{ROOT}/data/review/pending/in_*.tsv")):
    name = os.path.basename(inp)
    out = inp.replace("/in_", "/out_")
    rows = [l.rstrip("\n").split("\t") for l in open(inp)]
    ids = [r[0] for r in rows]
    if not os.path.exists(out):
        print(f"{name}: no {os.path.basename(out)} yet ({len(ids)} titles unlabelled)"); problems += 1; continue
    got, bad = {}, collections.Counter()
    for line in open(out, encoding="utf-8", errors="replace"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 2: bad["malformed line"] += 1; continue
        k, c = parts[0].strip(), parts[1].strip().lower()
        if k not in set(ids): bad["unknown id"] += 1; continue
        if c not in CATS: bad[f"invalid category '{c}'"] += 1; continue
        if k in got: bad["duplicate id"] += 1
        got[k] = c
    missing = [k for k in ids if k not in got]
    shifts = shifted_windows([r[2] for r in rows], [got.get(k) for k in ids])
    print(f"{name}: {len(got)}/{len(ids)} labelled" + (f"; problems {dict(bad)}" if bad else "") + (f"; {len(missing)} missing" if missing else ""))
    for a, b, off, s0, s1 in shifts:
        print(f"  CHECK rows {a}-{b}: labels look shifted by {off:+d} row (agreement {s0} in place, {s1} shifted). Read these rows against their titles before trusting them.")
    problems += bool(bad) + bool(missing) + len(shifts)
    labels.update(got)

with open(labels_path, "w") as f:
    for k, c in labels.items(): f.write(json.dumps({"id": k, "cat": c}) + "\n")
print(f"review_labels.jsonl: {before} -> {len(labels)} labels" + (f"; {problems} thing(s) to look at above" if problems else ""))
