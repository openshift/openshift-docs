#!/bin/bash
# Checks if a release notes file is updated. If true, searches the release notes file for links to bugs that are behind a login and fails the build.
# We should not include internal bugs in our release notes.

# Get the repo path and files changed
REPO_PATH="$(git rev-parse --show-toplevel)"
FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*release-notes*.adoc" ':(exclude)_unused_topics/*')

# Function to check links in updated release notes
check_rn_links () {

    # Iterate through RN files because could potentially be more than one (e.g. OCP + ROSA)
    for RELEASE_FILE in ${FILES}; do
        echo ""
        echo "#########"
        echo "You updated the following release notes file:"
        echo "$RELEASE_FILE"
        echo "#########"
        echo ""

        # Read the content from the local release note file
        content=$(cat "$REPO_PATH/$RELEASE_FILE")

        # Exclude content within //// multi-line comments
        content=$(echo "${content}" | sed ':a;N;$!ba;s#////\n.*////##g')

        # Extract links from the content, excluding single-line comments
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
                echo "The link $link points to an internal bug."
                protected_links+=("$link")         
            fi
        done

    done

    # Print the list of links that require authentication
        if [ ${#protected_links[@]} -eq 0 ]; then
            echo "No links require authentication, exiting."
            exit 0
        else
            echo "Links that require authentication:"
            printf '%s\n' "${protected_links[@]}"
            echo "Build failed. Ensure there are no links to internal JIRA bugs, which have a security level of Red Hat Employee only."
            exit 1
        fi
}

if [[ $FILES == *"release-notes"* ]]; then
    check_rn_links
else
    echo "No release notes updated, exiting."
    exit 0
fi
