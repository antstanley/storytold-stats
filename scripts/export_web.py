"""Write web/src/lib/data/stats.json (per-repo, per-release category counts) for the SvelteKit charts app."""
import csv, json, os, datetime
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CATS = ["feature", "fix", "perf", "i18n", "docs", "test", "build-ci", "release", "refactor", "deps", "security", "revert", "other"]

head = {json.loads(l)["repo"] + "\t" + json.loads(l)["release"]: json.loads(l) for l in open(f"{ROOT}/data/releases.jsonl")}
repos = {}
for s in csv.DictReader(open(f"{ROOT}/csv/release_stats.csv")):
    repo, tag = s["repo"], s["release_tag"]
    api = {a["tag"]: a for a in json.load(open(f"{ROOT}/data/releases_api/{repo}.json"))}
    tags = s["tags"].split(", ")
    published = next((api[t]["published_at"] for t in tags if t in api), None) or head[f"{repo}\t{tag}"]["date"]
    unreleased = tag == "(unreleased)"
    repos.setdefault(repo, []).append({
        "key": "unreleased" if unreleased else tag,
        "label": "Unreleased" if unreleased else tag.replace("artcraft-", ""),
        "tags": [] if unreleased else tags,
        "date": datetime.datetime.fromisoformat(published.replace("Z", "+00:00")).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "url": s["url"],
        "unreleased": unreleased,
        "uncategorised": int(s["uncategorised"]) > 0,
        "commits": int(s["commits"]),
        "changes": int(s["changes"]),
        "counts": {c: int(s[c]) for c in CATS},
    })
out = {"generated": datetime.date.today().isoformat(), "repos": [{"name": r, "releases": sorted(v, key=lambda x: (x["unreleased"], x["date"]))} for r, v in repos.items()]}
os.makedirs(f"{ROOT}/web/src/lib/data", exist_ok=True)
json.dump(out, open(f"{ROOT}/web/src/lib/data/stats.json", "w"), indent=1)
print("repos", len(out["repos"]), "rows", sum(len(r["releases"]) for r in out["repos"]))
