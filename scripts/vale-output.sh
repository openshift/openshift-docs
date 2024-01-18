#!/bin/bash
# This runs Vale on updated files, checks if the Vale alerts are on new/modified lines, and if so, builds curl request for GitHub review comment API

#GITHUB_AUTH_TOKEN=$(cat /tmp/vault/ocp-docs-github-secret/GITHUB_AUTH_TOKEN)
GITHUB_AUTH_TOKEN=$(cat ~/temp-scripts/github_token)

export GITHUB_AUTH_TOKEN

COMMIT_ID=$(git log -n 1 --pretty=format:"%H")
PULL_NUMBER=$(curl -s "https://api.github.com/search/issues?q=$COMMIT_ID" | jq '.items[0].number')
REPO_OWNER="openshift"
REPO_NAME="openshift-docs"
echo "This is the $PULL_NUMBER"

# Build curl command for Github API review comment.
function post_variable_metadata {

    LINE_NUMBER=$3
    BODY=$1
    FILENAME=$2
    
    #curl -L -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls/$PULL_NUMBER/comments -d '{"body":"'"$BODY"'","commit_id":"'"$COMMIT_ID"'","path":"'"$FILENAME"'","line":'"$LINE_NUMBER"',"side":"RIGHT"}'

    # Echoing to cmd line instead of sending 1 million curl requests
    echo ""
    echo "Send peer review comment..."
    echo "curl -L -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls/$PULL_NUMBER/comments -d '{\"body\":\"$BODY\",\"commit_id\":\"$COMMIT_ID\",\"path\":\"$FILENAME\",\"line\":$LINE_NUMBER,\"side\":\"RIGHT\"}'"

}

# Get update files - this only gets files updated  in the last commit. For unsquashed commits, it will only run on last commit
# This might be helpful to find all commits since head if the needs arises: https://stackoverflow.com/questions/7693249/how-to-list-commits-since-certain-commit
FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*.adoc" ':(exclude)_unused_topics/*')

# Compares body, path, and line values for Vale alerts vs already existing comments on PR. If values match, comment already exists, remove from temp json files.
function check_if_existing_comment {

    local vale_file="$1"
    local pull_comments_file="$2"

    # Iterate through Vale alert JSON
    jq -c '.[]' "$vale_file" | while IFS= read -r object; do
    BODY_VALE=$(echo "$object" | jq -r '.body')
    FILENAME_VALE=$(echo "$object" | jq -r '.path')
    LINE_NUMBER_VALE=$(echo "$object" | jq -r '.line')

        # Iterate through pull comment JSON to see if a comment exists
        jq -c '.[]' "$pull_comments_file" | while IFS= read -r object2; do
            BODY_COMMENT=$(echo "$object2" | jq -r '.body')
            FILENAME_COMMENT=$(echo "$object2" | jq -r '.path')
            LINE_NUMBER_COMMENT=$(echo "$object2" | jq -r '.line')

            # If a there's a comment that matches the Vale body, line and path, remove it from both files
            if [ "$BODY_VALE" == "$BODY_COMMENT" ] && [ "$FILENAME_VALE" == "$FILENAME_COMMENT" ] && [ "$LINE_NUMBER_VALE" == "$LINE_NUMBER_COMMENT" ]; then
                echo "Found existing comment for $object"
                echo "Deleteing... "
                
                jq --argjson obj "$object" '. | del(.[index($obj)])' "$vale_file" > processing.json
                jq --argjson obj "$object2" '. | del(.[index($obj)])' "$pull_comments_file" > processing_comments.json

                mv processing.json "$vale_file"
                mv processing_comments.json "$pull_comments_file"

                break

            fi
        done

    done


}

# Run vale with the custom template on updated files
for FILE in ${FILES}; 
do
    valeOutput=$(vale --output=.vale/templates/bot-comment-output.tmpl $FILE)

    # Converts JSON stream to array
    finalJson=$(jq -s '.' <<< "$valeOutput")
        
    # Moved JSON to temp file for further parsing to avoid issues during development, but might not be neccessary(?)
    echo "$finalJson" > vale_output_temp.json

    #Get comments in PR
    curl -L -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls/$PULL_NUMBER/comments > pull_comments_temp.json

    check_if_existing_comment "vale_output_temp.json" "pull_comments_temp.json"

    # Iterate through Vale alert JSON
    jq -c '.[]' vale_output_temp.json | while IFS= read -r object; do
    BODY_VALE=$(echo "$object" | jq -r '.body')
    FILENAME_VALE=$(echo "$object" | jq -r '.path')
    LINE_NUMBER_VALE=$(echo "$object" | jq -r '.line')

        # Iterate through pull comment JSON to see if a comment exists
        jq -c '.[]' pull_comments_temp.json | while IFS= read -r object2; do
            BODY_COMMENT=$(echo "$object2" | jq -r '.body')
            FILENAME_COMMENT=$(echo "$object2" | jq -r '.path')
            LINE_NUMBER_COMMENT=$(echo "$object2" | jq -r '.line')

            # If a there's a comment that matches the Vale body, line and path, remove it from both files
            if [ "$BODY_VALE" == "$BODY_COMMENT" ] && [ "$FILENAME_VALE" == "$FILENAME_COMMENT" ] && [ "$LINE_NUMBER_VALE" == "$LINE_NUMBER_COMMENT" ]; then
                echo "Body is the same between $object"
                echo "and $object2"
                echo "Deleteing??? "

                jq --argjson obj "$object" '. | del(.[index($obj)])' vale_output_temp.json > processing.json
                jq --argjson obj "$object2" '. | del(.[index($obj)])' pull_comments_temp.json > processing_comments.json

                mv processing.json vale_output_temp.json
                mv processing_comments.json pull_comments_temp.json
                
                break

                
            fi
        done

    done


    # Compare JSON files to see if comments already exist for alerts, remove objects that correspond to existing comments.


    # Following logic checks if the line number is a part of the git diff. If it's not part of the diff it will be discarded.
    # We only want to check new/modified content, plus the GitHub API only accepts comments within the diff for the review comments endpoint.
    #echo "Checking line number is within the diff..."

    # Iterate through the JSON objects
    jq -c '.[]' vale_output_temp.json | while IFS= read -r object; do
        #echo "$object"
        BODY=$(echo "$object" | jq -r '.body')
        FILENAME=$(echo "$object" | jq -r '.path')
        LINE_NUMBER=$(echo "$object" | jq -r '.line')
        
        # Check the unified diff for the alert and file
        FULL_DIFF=$(git diff --unified=0 --stat --diff-filter=AM HEAD~1 HEAD "${FILENAME}" ':(exclude)_unused_topics/*')
        
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
                    
                    post_variable_metadata "$BODY" "$FILENAME" "$LINE_NUMBER"
                    
                    break  # Exit the loop since the alert is within the diff, move on to the next JSON object
                fi
            fi
                
        done <<< "$FULL_DIFF"
     
    done

done

#rm vale_output_temp.json
