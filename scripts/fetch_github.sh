#!/bin/bash
# Fetch everything the pipeline needs from the GitHub API (needs an authenticated `gh`):
#   data/org_repos.jsonl        every repo in the org with its release count
#   data/releases_api/<repo>.json  published releases of each repo in scripts/repos.txt
#   data/prs/<repo>.jsonl       merged-PR metadata of each repo in scripts/repos.txt
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p data/prs data/releases_api

gh api graphql --paginate -f query='
query($endCursor:String){
  organization(login:"storytold"){
    repositories(first:100,after:$endCursor){
      pageInfo{hasNextPage endCursor}
      nodes{name isArchived isFork releases{totalCount}}
    }
  }
}' --jq '.data.organization.repositories.nodes[] | {name,isArchived,isFork,releases:.releases.totalCount}' > data/org_repos.jsonl.tmp
mv data/org_repos.jsonl.tmp data/org_repos.jsonl

while read -r repo; do
  [ -n "$repo" ] || continue
  gh api --paginate "repos/storytold/$repo/releases?per_page=100" \
    --jq '.[] | select(.draft | not) | {tag:.tag_name,name,published_at,prerelease,url:.html_url}' \
    | python3 -c 'import sys, json; print(json.dumps([json.loads(l) for l in sys.stdin if l.strip()]))' \
    > "data/releases_api/$repo.json"
  # The GraphQL pagination occasionally drops a page ("unexpected end of JSON input"); one retry clears it
  scripts/fetch_prs.sh "$repo" || scripts/fetch_prs.sh "$repo"
done < scripts/repos.txt

# Repos that publish releases but are not covered yet (scripts/excluded_repos.txt are left out on purpose)
python3 - <<'PY'
import json
covered = set(open("scripts/repos.txt").read().split()) | set(open("scripts/excluded_repos.txt").read().split())
new = [r["name"] for r in map(json.loads, open("data/org_repos.jsonl")) if r["releases"] > 0 and r["name"] not in covered]
if new:
    print("NOT COVERED (has releases, missing from scripts/repos.txt):", ", ".join(new))
PY
