"""Assign a category to every change in data/changes.jsonl -> data/classified.jsonl.

Signals, strongest first (the one used is recorded in `basis`):
  prefix   conventional-commit prefix on the PR title / commit subject
  branch   PR head branch name (fix/…, feat/…, perf/…, docs/…)
  label    bug / enhancement / performance / documentation label on the PR or the issue it closes
  keyword  wording of the title
  review   manual/LLM reading of the title (data/review_labels.jsonl), for titles no rule decides
"""
import json, re, os, collections, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CATS = ["feature", "fix", "perf", "i18n", "docs", "test", "build-ci", "release", "refactor", "deps", "security", "revert", "other"]

ALIAS = {
    "feat": "feature", "feature": "feature", "features": "feature", "enhance": "feature", "enhancement": "feature", "add": "feature",
    "fix": "fix", "fixes": "fix", "bugfix": "fix", "hotfix": "fix", "bug": "fix",
    "perf": "perf", "performance": "perf",
    "docs": "docs", "doc": "docs", "readme": "docs",
    "test": "test", "tests": "test", "testing": "test",
    "ci": "build-ci", "build": "build-ci", "packaging": "build-ci",
    "release": "release",
    "refactor": "refactor", "style": "refactor", "chore": "refactor", "cleanup": "refactor",
    "i18n": "i18n", "l10n": "i18n", "translation": "i18n", "translations": "i18n",
    "deps": "deps", "dependabot": "deps",
    "security": "security", "harden": "security",
    "revert": "revert",
}
LABELS = {"bug": "fix", "enhancement": "feature", "performance": "perf", "documentation": "docs", "dependencies": "deps"}
CC = re.compile(r"^([A-Za-z0-9_-]+)(\([^)]*\))?!?:\s")
CLOSING = re.compile(r"\(?\b(?:fix(?:es|ed)?|close[sd]?|resolve[sd]?)\s+(?:issue\s+)?#\d+(?:\s*(?:,|and|&)\s*(?:fix(?:es|ed)?\s+)?#\d+)*\)?", re.I)

LANGS = r"(?:arabic|bulgarian|catalan|chinese|czech|danish|dutch|finnish|french|german|greek|hebrew|hindi|hungarian|indonesian|italian|japanese|korean|norwegian|persian|polish|portuguese|romanian|russian|serbian|slovak|spanish|swedish|thai|turkish|ukrainian|vietnamese|polski)"
KEYWORDS = [  # first match wins
    ("revert",   r"^revert\b"),
    ("release",  r"^release\b|^release prep|^bump (?:\w+ )?(?:version )?(?:to )?v?\d+\.\d+|^v?\d+\.\d+\.\d+\b|\bversion bump\b|^bump \w+ \d+\.\d+\s*->|^bump .* downloads? to"),
    ("deps",     r"^(?:bump|upgrade|update|pin) [\w./@:-]+ (?:from|to)\b.*\d|^cargo update|\bdependabot\b|^pin \w+ to =?\d|^cargo\.lock\b"),
    ("i18n",     r"\bi18n\b|\bl10n\b|\blocali[sz]\w*|\btranslat\w+|\b" + LANGS + r" (?:catalog|translation|strings|locale|interface|localization)|\bcatalog(?:s|ue)? (?:covers?|complete)|\binterface language\b|\blocales?\b"),
    ("security", r"\bsecurity\b|\bcve-\d|\bvulnerab\w+|\bsandbox(?:ed|ing)?\b|\bpath traversal\b|\bhostile[- ]input\b|\buntrusted\b|\bharden\w*"),
    ("perf",     r"\bperf\b|\bperformance\b|\bfaster\b|\bspeed(?:s|ed)? up\b|\bspeedup\b|\boptimi[sz]\w+|\bparallel(?:ise|ize|ism)?\b|\bmultithread\w*|\bavoid (?:re)?(?:alloc|copy|comput|decod|render)\w*|\bonce per\b|\bno longer re(?:build|decode|render|compute|read|allocat)\w*|\blatency\b|\bjank\b|\bthroughput\b|\bbenchmarks?\b|\bmemory (?:use|usage|footprint)\b|\bless memory\b|\blazy|\blazily\b|\bincremental(?:ly)?\b"),
    ("docs",     r"^docs?\b|^readme\b|\breadme\b|\bagents\.md\b|\bclaude\.md\b|\bchangelog\b|\bcontributing\b|\bdocumentation\b|\bgaps(?:\.md)? row|\bparity (?:summary|checklist|tracker|table|after)\b|\btracker rows?\b|\brelease notes\b|\buser guide\b|\bmanual\b: |\blicense\b|\brelicense\b|\bcredits?\b: |\bcontributors? (?:list|page)\b|^help: "),
    ("test",     r"^tests?\b|\btests?(?: suite| module| fixtures?)?\b(?!.*\bfix)|\bfuzz\w*|\bproptest\b|\bproperty-based\b|\boracles?\b|\bfixtures?\b|\bgolden\b|\bsnapshot tests?\b|\be2e\b|\bbehaviou?r suite\b|\bcorpus\b|\bcorpora\b"),
    ("build-ci", r"^ci\b|\bci\b(?: job| workflow| run| fails?| green|:)|\bworkflows?\b|\bgithub actions?\b|\brelease build\b|\bbuild script\b|\bmsi\b|\bdmg\b|\bflatpak\b|\bappimage\b|\bdeb/rpm\b|\binstaller\b|\bcodesign\w*|\bnotari[sz]\w+|\bflake\.nix\b|\bxtask\b|\bcargo (?:deny|audit|dist)\b|\bpackaging\b|\bdockerfile\b|\bfix (?:the )?(?:macos |windows |linux )?build\b|\bmain fails to compile\b"),
    ("fix",      r"^fix\b|^fix(?:es|ed)?[ :/]|^hotfix\b|^bug\b|\bbug ?fix\w*|\bfix(?:es|ed)? (?!#)|\bcrash\w*|\bpanic\w*|\bregression\b|\bno longer\b|\binstead of\b|\bincorrect(?:ly)?\b|\bwrong(?:ly)?\b|\bbroken\b|\bhang(?:s|ing)?\b|\bfreez\w+|\bdeadlock\w*|\boverflow\w*|\bunderflow\b|\bleak\w*|\bcorrupt\w*|\bstale\b|\bflicker\w*|\boff[- ]by[- ]one\b|\bnan\b|\bdoes(?: not|n't)\b|\bdid(?: not|n't)\b|\bnot only\b|\bkeeps? (?:its|their|the)\b|\bstays?\b|\bis not kept\b|\bis kept\b|\bpreserv\w+|\brestor\w+|\bhonou?rs?\b|\brespects?\b|\bmis(?:align|place|match|render|read)\w*|\bworkaround\b|\bhandle (?:missing|empty|invalid|zero|negative|signed)\b|\brefus\w+\b|\bcorrect(?:s|ed|ly)?\b|\btypo\b|\bnot? .{0,20} anymore\b|\bfails? (?:to|when|on)\b|\bactually\b|\bagain\b|\bproperly\b"),
    ("refactor", r"^refactor\w*|\brefactor\w*|^rename\b|\bclean ?up\b|\bcargo fmt\b|\brustfmt\b|\bclippy\b|\bdead code\b|\bunused (?:import|code|variable|dep)\w*|^remove (?:stale|unused|dead|old)\b|\bdedupe?\b|\bdeduplicat\w+|^move \w+ (?:to|into)\b|^split \b|\bextract \w+ (?:into|to)\b|^chore\b|^lint\b|^format\b|^wip\b|^work in progress\b|^merge\b|\bresolve the .* merge\b|\breconcile\b|\bgitignore\b"),
    ("feature",  r"^add(?:s|ed)?\b|\badd(?:s|ed)?\b|^new\b|^implement\w*|^support\b|\bsupports?\b|^introduc\w+|^allow\b|^enable\b|^show\b|\bnow (?:lists?|shows?|opens?|supports?)\b|^create\b|^wire\b|\bimport(?:s|er)?\b|\bexport(?:s|er)?\b|\bdialog\b|\bpanel\b|\bmenu\b|\btool\b|\bcommand\b|\bshortcut\b|\boption\b|\bpreset\b|\bpreference\b"),
]
KEYWORDS = [(c, re.compile(p, re.I)) for c, p in KEYWORDS]

def branch_cat(branch):
    if not branch: return None
    for seg in branch.lower().split("/"):
        if seg in ALIAS: return ALIAS[seg]
        tok = re.split(r"[-_]", seg)[0]
        if tok in ALIAS and tok not in ("add", "release", "build", "style", "testing", "features", "bug", "translation", "translations", "readme", "cleanup"): return ALIAS[tok]
    return None

def prefix_cat(title):
    m = CC.match(title or "")
    if not m: return None
    p = m[1].lower()
    return ALIAS.get(p)

def keyword_cat(title):
    t = CLOSING.sub("", title or "")
    t = re.sub(r"^(?:[A-Z]{1,4}[\d.]*|[A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+|Batch \d+|Issue #\d+):\s*", "", t)  # milestone / tracker codes
    for cat, rx in KEYWORDS:
        if rx.search(t): return cat
    return None

def classify(r, review):
    for t in (r.get("pr_title"), r["title"], r["subject"]):
        c = prefix_cat(t)
        if c: return c, "prefix"
    if r["is_batch"] or re.search(r"\bintegrat(?:e|ion)[- ]batch", (r["title"] + " " + (r["branch"] or "")), re.I):
        return "other", "integration-batch"
    if r["id"] in review: return review[r["id"]], "review"
    c = branch_cat(r["branch"])
    if c: return c, "branch"
    for l in r["labels"] + r["issue_labels"]:
        if l in LABELS: return LABELS[l], "label"
    c = keyword_cat(r["title"])
    if c: return c, "keyword"
    return "other", "unclassified"

def main():
    review = {}
    p = f"{ROOT}/data/review_labels.jsonl"
    if os.path.exists(p):
        for line in open(p):
            line = line.strip()
            if not line: continue
            d = json.loads(line)
            if d.get("cat") in CATS: review[d["id"]] = d["cat"]
    out = open(f"{ROOT}/data/classified.jsonl", "w")
    basis = collections.Counter(); cats = collections.Counter()
    for line in open(f"{ROOT}/data/changes.jsonl"):
        r = json.loads(line)
        r["category"], r["basis"] = classify(r, review)
        basis[r["basis"]] += 1; cats[r["category"]] += 1
        out.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("basis", dict(basis), file=sys.stderr); print("category", dict(cats), file=sys.stderr)

if __name__ == "__main__":
    main()
