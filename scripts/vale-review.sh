#!/bin/bash
# This runs Vale on updated files in last commit, checks if the Vale alerts are on new/modified lines, and if so, builds curl request 
# for GitHub review comment API. Also checks if a commment already exists before posting.
# To test locally, create a Github personal access token and export a $GITHUB_AUTH_TOKEN environmental variable to use the token

# Check if jq is installed
hash jq 2>/dev/null || { echo >&2 "Error: jq is not installed"; exit 1; }

#GITHUB_AUTH_TOKEN=$(cat ~/temp-scripts/github_token)

#export GITHUB_AUTH_TOKEN

# Set $PULL_NUMBER and $COMMIT_ID if not passed as variables
if [ $# -eq 0 ]; then
    COMMIT_ID=$(git log -n 1 --pretty=format:"%H")
    PULL_NUMBER=$(curl -s "https://api.github.com/search/issues?q=$COMMIT_ID" | jq '.items[0].number')
else
    PULL_NUMBER=$1
    COMMIT_ID=$2
fi

REPO_OWNER="openshift"
REPO_NAME="openshift-docs"

# Build curl command for Github API review comment.
function post_variable_metadata {

    BODY_NUMBER=$1
    PATH_NUMBER=$2
    LINE_NUMBER=$3
    echo "These are the values in the curl function"
    echo $BODY_NUMBER
    echo $PATH_NUMBER
    echo $LINE_NUMBER
    echo "Sending review comment curl request..."
    #curl -L -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls/$PULL_NUMBER/comments -d '{"body":"'"$BODY_NUMBER"'","commit_id":"'"$COMMIT_ID"'","path":"'"$PATH_NUMBER"'","line":'"$LINE_NUMBER"',"side":"RIGHT"}'"
}

# Get updated files in the last commit.
FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*.adoc" ':(exclude)_unused_topics/*')

# Compares body, path, and line values for Vale alerts vs already existing comments on PR. If values match, comment already exists, remove from temp json files.
function check_if_existing_comment {

    echo "Checking if existing comment..."

    local vale_json="$1"
    local pull_comment_json="$2"

    echo $vale_json

    # Outer loop to iterate through Vale alert JSON
    echo "$vale_json" | jq -c '.[]' | while IFS= read -r object; do
        echo $object
        BODY_VALE=$(jq -r '.body' <<< "${object}")
        echo $BODY_VALE
        PATH_VALE=$(jq -r '.path' <<< "${object}")
        LINE_VALE=$(jq -r '.line' <<< "${object}")

        # Inner loop to iterate through pull comment JSON to see if a comment exists
        echo "$pull_comment_json" | jq -c '.[]' | while IFS= read -r object2; do
            echo $object
            BODY_COMMENT=$(jq -r '.body' <<< "${object2}")
            PATH_COMMENT=$(jq -r '.path' <<< "${object2}")
            LINE_COMMENT=$(jq -r '.line' <<< "${object2}")
            echo "Inner loop"

            # If a there's a comment that matches the Vale body, line and path, remove it from both files
            if [ "$BODY_VALE" == "$BODY_COMMENT" ] && [ "$PATH_VALE" == "$PATH_COMMENT" ] && [ "$LINE_VALE" == "$LINE_COMMENT" ]; then
                echo "Found existing comment for $object"
                echo "Removing alert because review comment already exists... "

                vale_json=$(echo "$vale_json" | jq --argjson obj "$object" '. | del(.[index($obj)])')
                pull_comment_json=$(echo "$pull_comment_json" | jq --argjson obj "$object2" '. | del(.[index($obj)])')

                #jq --argjson obj "$object" '. | del(.[index($obj)])' "$vale_file" > processing.json
                #jq --argjson obj "$object2" '. | del(.[index($obj)])' "$pull_comments_file" > processing_comments.json

                #mv processing.json "$vale_file"
                #mv processing_comments.json "$pull_comments_file"

                break

            fi
        done

    done


}

# Run vale with the custom template on updated files
for FILE in ${FILES}; 
do
    vale_json=$(vale --minAlertLevel=error --output=.vale/templates/bot-comment-output.tmpl $FILE)
    
    # Converts JSON stream to array
    #finalJson=$(jq -s '.' <<< "$valeOutput")

    # Moved JSON to temp file for further parsing to avoid issues during development, but might not be neccessary(?)
    echo "$vale_json" #> vale_output_temp.json

    #Get comments in PR
    #curl -L -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls/$PULL_NUMBER/comments > pull_comments_temp.json

    pull_comment_json=$(curl -L -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls/$PULL_NUMBER/comments)
    echo "$pull_comment_json"

    if [[ $(echo "$pull_comment_json" | jq '. | length') -gt 0 ]]; then
        check_if_existing_comment "$vale_json" "$pull_comment_json"
    else
        echo "Pull comments JSON is empty or not an array."
    fi
    
    #check_if_existing_comment "$vale_json" "$pull_comment_json"

    # Following logic checks if the line number is a part of the git diff. If it's not part of the diff it will be discarded.
    # We only want to check new/modified content, plus the GitHub API only accepts comments within the diff for the review comments endpoint.
    #echo "Checking line number is within the diff..."

    # Iterate through the JSON objects
    echo "$vale_json" | jq -c '.[]' | while read object; do
        echo "$object"
        BODY_VALUE=$(jq -r '.body' <<< "$object")
        echo $BODY_VALUE
        PATH_VALUE=$(jq -r '.path' <<< "$object")
        echo $PATH_VALUE
        LINE_VALUE=$(jq -r '.line' <<< "$object")
        echo $LINE_VALUE

    # # Initialize vale_json within jq
    # echo "$vale_json" | jq -n --argjson jq "$vale_json" '

    # # Iterate through the JSON objects
    # $jq | .[] | 
    # (
    #     .body,
    #     .path,
    #     .line
    # )
    # '
    

        # Check the unified diff for the alert and file
        FULL_DIFF=$(git diff --unified=0 --stat --diff-filter=AM HEAD~1 HEAD "${PATH_VALUE}" ':(exclude)_unused_topics/*')

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

                # Check if the LINE falls within the range (diff_start_line) to (diff_start_line + added_lines)
                if (( LINE_VALUE >= diff_start_line && LINE_VALUE <= diff_start_line + added_lines )); then
                    echo "here's the body value"
                    echo $BODY_VALUE
                    post_variable_metadata "$BODY_VALUE" "$PATH_VALUE" "$LINE_VALUE"

                    break  # Exit the loop since the alert is within the diff, move on to the next JSON object
                fi
            fi

        done <<< "$FULL_DIFF"

    done

done