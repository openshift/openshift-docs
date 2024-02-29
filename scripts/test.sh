#!/bin/bash

COMMIT_ID=$(git log -n 1 --pretty=format:"%H")
PULL_NUMBER=$(curl -s "https://api.github.com/search/issues?q=$COMMIT_ID" | jq '.items[0].number')
#FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*.adoc" ':(exclude)_unused_topics/*')
FILE=welcome/index.adoc

vale_json=$(vale --minAlertLevel=error --output=.vale/templates/bot-comment-output.tmpl "$FILE" | jq)

pull_comments_json=$(curl -L -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" "https://api.github.com/repos/openshift/openshift-docs/pulls/$PULL_NUMBER/comments" | jq)

updated_comments_json=$(jq -n --argjson vale "$vale_json" --argjson comments "$pull_comments_json" '$vale | map(select(. as $v | $comments | any(.path == $v.path and .line == $v.line) | not))' | jq)

echo "$updated_comments_json"
