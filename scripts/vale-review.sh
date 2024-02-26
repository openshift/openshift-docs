#!/bin/bash
# This script runs Vale on updated files, checks if the Vale alerts are on new/modified lines, and if so, builds a cURL request for GitHub review comment API.
# Also checks if a comment already exists before posting.
# To test locally, create a GitHub personal access token and authenticate using 'gh auth login'.

# Check if jq and gh are installed
if ! command -v jq &>/dev/null || ! command -v gh &>/dev/null; then
    echo >&2 "Error: jq or gh is not installed"
    exit 1
fi

COMMIT_ID=$(git log -n 1 --pretty=format:"%H")
PULL_NUMBER=$(gh pr view --json number --jq '.number')
REPO_OWNER="openshift"
REPO_NAME="openshift-docs"
FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*.adoc" ':(exclude)_unused_topics/*')

# Build cURL command for GitHub API review comment.
function post_variable_metadata {
    local LINE_NUMBER=$3
    local BODY=$1
    local FILENAME=$2
    echo "Sending review comment cURL request..."
    gh pr review --comment "$(printf '%s' "$BODY" | jq -s -R .)" --path "$FILENAME" --line $LINE_NUMBER --body "Alert on line $LINE_NUMBER of $FILENAME"
}

# Run Vale with the custom template on updated files
for FILE in ${FILES}; do
    # Run Vale
    vale_output=$(vale --minAlertLevel=error --output=.vale/templates/bot-comment-output.tmpl "$FILE" | jq -s '.')

    # Get PR comments
    pull_comments=$(gh pr review comments --jq '.comments')

    # Following logic checks if the line number is within the diff. If it's not part of the diff, it will be discarded.
    # We only want to check new/modified content, and the GitHub API only accepts comments within the diff for the review comments endpoint.

    # Iterate through the JSON objects
    while IFS= read -r object; do
        BODY=$(echo "$object" | jq -r '.body')
        FILENAME=$(echo "$object" | jq -r '.path')
        LINE_NUMBER=$(echo "$object" | jq -r '.line')
        
        # Check the unified diff for the alert and file
        FULL_DIFF=$(git diff --unified=0 --stat --diff-filter=AM HEAD~1 HEAD "$FILENAME" ':(exclude)_unused_topics/*')
        
        # Iterate through each line to find the line diff info and check if the alert is in the diff
        while read -r line; do
            # Check if the line contains the hunk beginning with @@
            if [[ $line =~ @@ ]]; then

                # Check if there is a comma in the number pairing before @@
                if [[ $line =~ \+.*\,.*\ @@ ]]; then
                    # There are comma-separated numbers before closing @@.
                    added_lines=$(echo "$line" | grep -oP '\d+\s+@@' | grep -oP '\d+')
                    diff_start_line=$(echo "$line" | awk -F'+' '{print $2}' | awk -F',' '{print $1}')
                else
                    # There are no comma-separated numbers.
                    added_lines=0
                    diff_start_line=$(echo "$line" | grep -oP '\+\d+\s+@@' | grep -oP '\d+')
                fi

                # If the diff_start_line is 0, disregard the hunk.
                if [ "$diff_start_line" -eq 0 ]; then
                    continue
                fi

                # Check if the LINE_NUMBER falls within the range (diff_start_line) to (diff_start_line + added_lines)
                if (( LINE_NUMBER >= diff_start_line && LINE_NUMBER <= diff_start_line + added_lines )); then
                    
                    post_variable_metadata "$BODY" "$FILENAME" "$LINE_NUMBER"
                    
                    break  # Exit the loop since the alert is within the diff, move on to the next JSON object
                fi
            fi
                
        done <<< "$FULL_DIFF"
     
    done <<< "$vale_output"

done
