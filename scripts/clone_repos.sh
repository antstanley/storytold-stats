#!/bin/bash
# Clone (or update) the commit history of every storytold repo that publishes releases into repos/.
# Bare, tree-less clones: only commits and tags are needed, not file contents.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p repos
for repo in cadcraft soundcraft craft-launcher deckcraft gridcraft vectorcraft photocraft pdfcraft \
            designcraft filmcraft figcraft lightcraft effectcraft wordcraft artcraft; do
  if [ -d "repos/$repo.git" ]; then
    git -C "repos/$repo.git" fetch --quiet --tags origin '+refs/heads/*:refs/heads/*'
  else
    git clone --quiet --bare --filter=tree:0 "https://github.com/storytold/$repo.git" "repos/$repo.git"
  fi
  echo "$repo $(git -C "repos/$repo.git" rev-list --all --count) commits"
done
