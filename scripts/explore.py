import subprocess, re, sys, collections, os
REPOS = os.path.join(os.path.dirname(__file__), "..", "repos")
repos = "cadcraft soundcraft craft-launcher deckcraft gridcraft vectorcraft photocraft pdfcraft designcraft filmcraft figcraft lightcraft effectcraft wordcraft".split()
conv = collections.Counter(); kinds = collections.Counter(); noconv = []
for r in repos:
    out = subprocess.run(["git","-C",f"{REPOS}/{r}.git","log","--first-parent","--format=%H%x1f%P%x1f%s%x1f%b%x1e","main"],capture_output=True,text=True).stdout
    for rec in out.split("\x1e"):
        rec = rec.strip("\n")
        if not rec: continue
        h,p,s,b = rec.split("\x1f")
        nparents = len(p.split())
        m = re.match(r"Merge pull request #(\d+) from (\S+)", s)
        if m:
            kinds["merge-pr"] += 1
            title = b.strip().split("\n")[0]
            br = m.group(2).split("/",1)[1] if "/" in m.group(2) else m.group(2)
            conv["branch:"+ (br.split("/")[0] if "/" in br else "(none)")] += 1
            continue
        if nparents > 1: kinds["merge-other"] += 1; noconv.append((r,s)); continue
        kinds["squash-pr" if re.search(r"\(#\d+\)\s*$", s) else "direct"] += 1
        m = re.match(r"^([a-zA-Z0-9_-]+)(\([^)]*\))?(!)?:\s", s)
        if m and m.group(1).lower() in "feat fix perf docs doc test tests chore ci build refactor style i18n l10n revert release deps a11y security ui ux".split():
            conv["cc:"+m.group(1).lower()] += 1
        else:
            conv["cc:(none)"] += 1; noconv.append((r,s))
print(kinds); 
for k,v in conv.most_common(60): print(v,k)
import random; random.seed(1)
for r,s in random.sample(noconv,70): print(f"{r:14} {s[:150]}")
