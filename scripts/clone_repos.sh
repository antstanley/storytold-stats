#!/bin/bash
# Clone (or update) the commit history of every repo in scripts/repos.txt into repos/.
# Bare, tree-less clones: only commits and tags are needed, not file contents.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p repos
while read -r repo; do
  [ -n "$repo" ] || continue
  if [ -d "repos/$repo.git" ]; then
    git -C "repos/$repo.git" fetch --quiet --prune --tags origin '+refs/heads/*:refs/heads/*'
  else
    git clone --quiet --bare --filter=tree:0 "https://github.com/storytold/$repo.git" "repos/$repo.git"
  fi
  echo "$repo $(git -C "repos/$repo.git" rev-list --all --count) commits, $(git -C "repos/$repo.git" tag | wc -l | tr -d ' ') tags"
done < scripts/repos.txt
