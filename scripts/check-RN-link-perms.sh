#!/bin/bash
# Checks if a release notes file is updated. If true, searches the release notes file for links to bugs that are behind a login and fails the build.
# We should not include internal bugs in our release notes.

# TO DO
# Need to discount links in comments.
# Better failing out? Is this robost enough?
# Test microshift release notes. Test without update to any RN file.

# Get the repo path and files changed
REPO_PATH="$(git rev-parse --show-toplevel)"
FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*.adoc" ':(exclude)_unused_topics/*')

# Function to check links in updated release notes
check_rn_links () {
    
    # Array for release files in case more than one are edited in a PR.
    release_files=()

    #Extract the release notes file from all the updated files
    while IFS= read -r line; do
        if echo "$line" | grep -q "release-notes"; then
            release_files+=("$line")
        fi
    done <<< "$FILES"
    
    for RELEASE_FILE in "${release_files[@]}"; do
        echo ""
        echo "#########"
        echo "You updated the following release notes file:"
        echo "$RELEASE_FILE"
        echo "#########"
        echo ""

        # Read the content from the local release note file
        content=$(cat "$REPO_PATH/$RELEASE_FILE")

        # Extract links from the content
        links=$(echo "$content" | grep -v '^//.*' | grep -o 'https://issues[^]]*' | sed 's/\[.*//')
        protected_links=()

        echo ""
        echo "#########"
        echo "Checking for internal bug links in $REPO_PATH/$RELEASE_FILE"
        echo "#########"
        echo ""

        # Iterate over the links and check their authorization status
        for link in $links
        do
            response=$(curl -I "$link" 2>&1)

            if echo "$response" | grep -q "permissionViolation"; then
                echo "The link $link requires authentication."
                protected_links+=("$link")
            else
                echo "The link $link does not require authentication."
            fi
        done
     
    done

    # Print the list of links that require authentication
        if [ ${#protected_links[@]} -eq 0 ]; then
            echo "No links require authentication."
            exit 0
        else
            echo "Links that require authentication:"
            printf '%s\n' "${protected_links[@]}"
            echo "Build failed. Ensure there are no links to JIRA bugs that have a security level of Red Hat Employee only."
            exit 1
        fi
}

        

if [[ $FILES == *"release-notes"* ]]; then
    check_rn_links
else
    echo "No release notes updated, exiting."
    exit 0
fi
