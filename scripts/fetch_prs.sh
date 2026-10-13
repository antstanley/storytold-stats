#!/bin/bash
# Fetch merged-PR metadata for one storytold repo into data/prs/<repo>.jsonl
set -euo pipefail
repo="$1"; out="$(dirname "$0")/../data/prs/$repo.jsonl"
gh api graphql --paginate -f owner=storytold -f name="$repo" -f query='
query($owner:String!,$name:String!,$endCursor:String){
  repository(owner:$owner,name:$name){
    pullRequests(states:MERGED,first:50,after:$endCursor,orderBy:{field:CREATED_AT,direction:ASC}){
      pageInfo{hasNextPage endCursor}
      nodes{
        number title headRefName baseRefName mergedAt additions deletions changedFiles
        authorAssociation author{login __typename}
        mergeCommit{oid}
        labels(first:10){nodes{name}}
        closingIssuesReferences(first:5){nodes{number title labels(first:10){nodes{name}}}}
      }
    }
  }
}' --jq '.data.repository.pullRequests.nodes[] | {number,title,head:.headRefName,base:.baseRefName,mergedAt,additions,deletions,changedFiles,assoc:.authorAssociation,author:.author.login,authorType:.author.__typename,mergeCommit:.mergeCommit.oid,labels:[.labels.nodes[].name],issues:[.closingIssuesReferences.nodes[]|{number,title,labels:[.labels.nodes[].name]}]}' > "$out.tmp"
mv "$out.tmp" "$out"
echo "$repo $(wc -l < "$out")"
