#!/bin/bash

set -e

git_root=$(git rev-parse --show-toplevel)

# Exit if Travis is not being used
if [ -f "${git_root}/.travis.yml.old" ]; then
    echo "Travis CI is not in use. Exiting..."
    exit 0
fi

# Check if jq is installed
hash jq 2>/dev/null || { echo >&2 "Error: jq is not installed. Please install jq before running this script."; exit 1; }

# Check if gh is installed
hash gh 2>/dev/null || { echo >&2 "Error: GitHub CLI (gh) is not installed. Please install gh before running this script."; exit 1; }

# Check if inside a repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "ERROR: you must execute this script from the OpenShift Git repository." 1>&2
  exit 1
fi

PR_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
PR_NUMBER="$(gh pr list -H "$PR_BRANCH" --json number | jq -r '.[0].number')"
PR_COUNT="$(gh pr list -H $PR_BRANCH -s open | wc -l)"
AUTHOR="$(gh pr view $PR_NUMBER --json author | jq -r '.author.login')"
BASE_REF="$(gh pr view $PR_NUMBER --json baseRefName | jq -r '.baseRefName')"
SHA=$(git rev-parse HEAD)

# Check if there are more than one PRs associated with the branch
if [ "$PR_COUNT" -gt 1 ]; then
  echo "ERROR: there are multiple PRs referencing your working branch." >&2
  exit 1
fi

# Function to create the data to send
generate_pr_data()
{
  cat <<EOF
    {
    "PR_BRANCH": "$PR_BRANCH",
    "BASE_REPO": "openshift/openshift-docs",
    "PR_NUMBER": "$PR_NUMBER",
    "USER_NAME": "$AUTHOR",
    "BASE_REF": "$BASE_REF",
    "REPO_NAME": "$AUTHOR/openshift-docs",
    "SHA": "$SHA"
    }
EOF
}


# Send the curl request
if response=$(curl -s -X POST -H "Content-Type: application/json" -d "$(generate_pr_data)" https://eoa6vg2jiwjbnh6.m.pipedream.net); then
    if echo "$response" | grep -q -e "✅ Success! 🤖 Building the preview"; then
        echo "Preview build started successfully"
        echo "$response"
    else
        echo "Curl request failed: Invalid data!"
        exit 1
    fi
else
    echo "Curl request failed: $response"
    exit 1
fi
