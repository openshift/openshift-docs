#!/bin/bash
# This runs Vale on updated files in last commit, checks if the Vale alerts are on new/modified lines, and if so, builds curl request 
# for GitHub review comment API. Also checks if a commment already exists before posting.
# To test locally, create a Github personal access token and export a $GITHUB_AUTH_TOKEN environmental variable to use the token

# Check if jq is installed
hash jq 2>/dev/null || { echo >&2 "Error: jq is not installed"; exit 1; }

# Set $PULL_NUMBER and $COMMIT_ID for local testing. Otherwise use variables passed by Prow
if [ $# -eq 0 ]; then
    COMMIT_ID=$(git log -n 1 --pretty=format:"%H")
    PULL_NUMBER=$(curl -s "https://api.github.com/search/issues?q=$COMMIT_ID" | jq '.items[0].number')
else
    PULL_NUMBER=$1
    COMMIT_ID=$2
fi

FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*.adoc" ':(exclude)_unused_topics/*' ':(exclude)rest_api/*' ':(exclude)microshift_rest_api/*' ':(exclude)modules/virt-runbook-*' ':(exclude)modules/oc-by-example-content.adoc' ':(exclude)modules/oc-adm-by-example-content.adoc' ':(exclude)monitoring/config-map-reference-for-the-cluster-monitoring-operator.adoc' ':(exclude)modules/microshift-oc-adm-by-example-content.adoc' ':(exclude)modules/microshift-oc-by-example-content.adoc')

function post_review_comment {

    LINE_NUMBER=$3
    BODY=$1
    FILENAME=$2
    echo "Sending review comment curl request..."
    curl -L -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/openshift/openshift-docs/pulls/$PULL_NUMBER/comments -d '{"body":"'"$BODY"'","commit_id":"'"$COMMIT_ID"'","path":"'"$FILENAME"'","line":'"$LINE_NUMBER"',"side":"RIGHT"}'

}

function get_vale_errors {
    echo "Getting the Vale errors and PR comments and filtering out existing comments..."
    local vale_json="$1"
    local pull_comments_json="$2"

    # jq map and filter to retain only Vale alerts that don't already have a corresponding review comment on the PR
    updated_vale_json=$(jq -n --argjson vale "$vale_json" --argjson comments "$pull_comments_json" '$vale | map(select(. as $v | $comments | any(.path == $v.path and .line == $v.line and .body == $v.body) | not))' | jq)

    export updated_vale_json

}

# Run vale with the custom template on updated files and determine if a review comment should be posted
for FILE in ${FILES};
do
    # Clean out conditional markup in place and parse for vale errors
    sed -i 's/ifdef::.*\|ifndef::.*\|ifeval::.*\|endif::.*/ /' "$FILE"
    vale_json=$(vale --minAlertLevel=error --output=.vale/templates/bot-comment-output.tmpl "$FILE" | jq)

    # Check if there are Vale errors before processing the file further.
    if [[ "$vale_json" != "[]" ]]; then
        echo "Vale errors found in the file..."

        #Check if Vale review comments already exist in the PR
        pull_comments_json=$(curl -L -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/openshift/openshift-docs/pulls/$PULL_NUMBER/comments | jq)

        # If there are existing comments in the response, compare with Vale errors, otherwise proceed with existing Vale errors
        if [[ "$pull_comments_json" != "[]" ]]; then
            get_vale_errors "$vale_json" "$pull_comments_json"
        else 
            echo "No existing comments found..."
            updated_vale_json="$vale_json"
        fi
    else 
        echo "No Vale errors found in the file, moving to next file..."
        continue # move to next file
    fi

    # Following logic checks if the line number is a part of the git diff. If it's not part of the diff it will be discarded.
    # We only want to check new/modified content, plus the GitHub API only accepts comments within the diff for the review comments endpoint.
    if [[ "$updated_vale_json" == "[]" ]]; then
        echo "All Vale alerts already have existing comments, moving to next file..."
        continue # move to next file
    else 
        echo "Checking if Vale alerts without existing comments are part of added or modified content..."
    fi
    
    # Iterate through $updated_vale_json and post a comment if required
    jq -c '.[]' <<< "$updated_vale_json" | while IFS= read -r object; do
        BODY=$(echo "$object" | jq -r '.body')
        FILENAME=$(echo "$object" | jq -r '.path')
        LINE_NUMBER=$(echo "$object" | jq -r '.line')
        
        # Check the unified file diff for the alert and file
        file_diff=$(git diff --unified=0 --stat --diff-filter=AM HEAD~1 HEAD "${FILENAME}" ':(exclude)_unused_topics/*')
        
        # Iterate through each line to find the line diff info and check if the alert is in the diff
        while read -r line; do
            # Check if the line contains the hunk beginning with @@
            if [[ $line =~ @@ ]]; then

                # Valid:
                # @@ -35 +31 @@
                # @@ -35 +31,5 @@

                # Check if there is a comma in the number pairing before @@
                if [[ $line =~ \+.*\,.*\ @@ ]]; then
                    # There are comma separated numbers before closing @@. Grab the number before the comma as the diff_start_line, after the comma is the added_lines. 
                    added_lines=$(echo "$line" | grep -oP '\d+\s+@@' | grep -oP '\d+')
                    diff_start_line=$(echo "$line" | awk -F'+' '{print $2}' | awk -F',' '{print $1}')
                else
                    # There are no comma seperated numbers. Consider the number after the plus as diff_start_line with no added lines - this means there's a modification on a single line
                    added_lines=0
                    diff_start_line=$(echo "$line" | grep -oP '\+\d+\s+@@' | grep -oP '\d+')
                fi

                # If the last_number is 0, disregard the hunk and move to the next hunk as zero lines were modified (deletions only)
                if [ "$diff_start_line" -eq 0 ]; then
                    continue
                fi

                # Check if the LINE_NUMBER falls within the range (diff_start_line) to (diff_start_line + added_lines)
                if (( LINE_NUMBER >= diff_start_line && LINE_NUMBER <= diff_start_line + added_lines )); then

                    post_review_comment "$BODY" "$FILENAME" "$LINE_NUMBER"
                    
                    break  # Exit the loop since the alert is within the diff, move on to the next JSON object
                else
                    echo "Vale error alert not part of the file's added/modified content..."
                fi
            fi

        done <<< "$file_diff"

    done

done