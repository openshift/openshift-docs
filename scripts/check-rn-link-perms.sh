#!/bin/bash
# Report errors for links to Red Hat JIRA bugs that are behind a login

# These are the populated variables required for the curl request to post a Github API review comment.
# This function should be a separate, generic review bot comment script. Print to terminal for testing. 

function post_variable_metadata {
    LINE_NUMBER=$1
    COMMIT_ID=$(git log -n 1 --pretty=format:"%H")
    PULL_NUMBER=$(curl -s "https://api.github.com/search/issues?q=$COMMIT_ID" | jq '.items[0].number')
    BODY="Do not include links to internal JIRA issues $2"
    FILENAME="placeholder_filename"
    GITHUB_AUTH_TOKEN="placeholder_token"
    REPO_OWNER="openshift"
    REPO_NAME="openshift-docs"
    echo ${LINE_NUMBER}
    echo ${COMMIT_ID}
    echo ${PULL_NUMBER}
    echo ${BODY}
    echo ${FILENAME}
    echo ${GITHUB_AUTH_TOKEN}
    echo ${REPO_OWNER}
    echo ${REPO_NAME}

    echo "curl -L -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_AUTH_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls/$PULL_NUMBER/comments -d '{"body":"$BODY","commit_id":"${COMMIT_ID}","path":"$FILENAME","line":$LINE_NUMBER,"side":"RIGHT"}'"
}

# Gets the line number in the updated file for the link to an internal JIRA bug
function get_line_number_for_link() {
    local internal_link=$1
    
    # Gets the unified diff including hunk headers with line info
    FULL_DIFF=$(git diff --unified=0 --stat --diff-filter=AM HEAD~1 HEAD "*release-notes*.adoc" ':(exclude)_unused_topics/*')
    
    # Initialize counter
    counter=0

    # Flag to indicate if the link is found
    link_found=false

    # Flag to indicate when to start counting lines
    start_counting=false

    # Iterate through each line to find the link and the line number
    while read -r line; do
        # Check if the line contains the hunk beginning with @@
        if [[ $line =~ @@ ]]; then
                      
            # Valid:
            # @@ -35 +31 @@
            # @@ -35 +31,5 @@

            # +31 @@ means line 31 was modified in the updated file
            # +31,5 @@ means 5 lines were added from line 31 in the updated file
            
            # Extract the last number before closing @@. 
            # If it's 0, no lines modified, continue to next hunk.
            # If != 0 grab the number before the comma
            # if no comma is present, just grab the last number before the @@

            # TO DO: These two ifs are a bit messy. 
            # Check if there is a comma in the number pairing before @@
            if [[ $line =~ \+.*\,.*\ @@ ]]; then
                # There are comma separated numbers before closing @@. Grab the number before the comma as the start_line_number. 
                last_number=$(echo "$line" | grep -oP '\d+\s+@@' | grep -oP '\d+')
                start_line_number=$(echo "$line" | awk -F'+' '{print $2}' | awk -F',' '{print $1}')
            else
                # There are no comma seperated numbers. Consider the number after the plus as last_number and the start_lin_number for the counter
                last_number=$(echo "$line" | grep -oP '\+\d+\s+@@' | grep -oP '\d+')
                start_line_number=$(echo "$line" | grep -oP '\+\d+\s+@@' | grep -oP '\d+')
            fi
            
            # If the last_number is 0, disregard the hunk and move to the next hunk as zero lines were modified (deletions only)
            if [ "$last_number" -eq 0 ]; then
                continue
            fi

            # Initialize counter with the start_line_number of the updated file
            counter=$start_line_number

            start_counting=true
            continue  # Skip the line with @@ # I forget why I have this here
        fi

        # Start counting addition lines (+) after the hunk beginning with @@
        if [[ $start_counting == true && $line =~ ^\+ ]]; then
            # Check if the line contains the link
            if [[ $line =~ $internal_link ]]; then
                link_found=true
                # Send the link and link line number to function handling the curl command
                post_variable_metadata $counter $internal_link
                continue  # Find any further instances
            fi

            # Increment the counter for each added line
            ((counter++))
        fi
    done <<< "$FULL_DIFF"

    # If the link is not found, provide a message
    if [[ $link_found == false ]]; then
        echo "Link not found in the unified git diff output."
    fi

}

# Get modifed lines, remove deleted lines from the diff 
git_diff=$(git diff --unified=0 --stat --diff-filter=AM HEAD~1 HEAD "*release-notes*.adoc" ':(exclude)_unused_topics/*' | grep '^+' | grep -Ev '^(\+\+\+ a/ b/)')

# Exit zero if there are no release-notes changes 
if [ -z "${git_diff}" ]; then
    exit 0
fi

# Remove all multi-line comments and single line comments
git_diff=$(echo "${git_diff}" | sed '\|^+////|,\|^+////|c\\' | sed '\|^+//| s|.*|//|')

# Search the git diff for links
link_regex='https://issues\.redhat\.com/browse/[A-Z]+-[0-9]+'
links=$(echo "${git_diff}" | grep -o -E "$link_regex" | sort -u)

for link in ${links}; do
    # Check for links that require a login
    response=$(curl -I "${link}" 2>&1)
    if echo "${response}" | grep -q "permissionViolation"; then
        errors=true
        echo -e "\e[31mERROR: Do not include links to JIRA issues that require a login (${link})\n"
        get_line_number_for_link "$link"
    fi
done

if [ "$errors" = true ]; then
    exit 1
fi
