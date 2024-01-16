#!/bin/bash
# Returns a list of updated _topic_map.yml files.
# The list includes any topic maps that are themselves modified, and indirectly modifed topic maps where incldued AsciiDoc files have been updated.

# Get the *.adoc and distro maps files in the pull request
FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=AMRD "*.yml" "*.adoc" ':(exclude)_unused_topics/*')

REPO_PATH=$(git rev-parse --show-toplevel)

# Init an empty array
DISTROS=()

# Get the modules in the PR, search for assemblies that include them, and concat with any updated assemblies files
MODULES=$(echo "$FILES" | awk '/modules\/(.*)\.adoc/')
if [ "${MODULES}" ]
then
    # $UPDATED_ASSEMBLIES is the list of assemblies that contains changed modules
    UPDATED_ASSEMBLIES=$(grep -rnwl "$REPO_PATH" --include=\*.adoc --exclude-dir={snippets,modules} -e "$MODULES")

    # Subtract $REPO_PATH from path with bash substring replacement
    UPDATED_ASSEMBLIES=${UPDATED_ASSEMBLIES//"$REPO_PATH/"/}
fi

# ASSEMBLIES is the list of modifed assemblies
ASSEMBLIES=$(echo "$FILES" | awk '!/modules\/(.*)\.adoc/')
# Concatenate both lists and remove dupe entries
ALL_ASSEMBLIES=$(echo "$UPDATED_ASSEMBLIES $ASSEMBLIES" | tr ' ' '\n' | sort -u)
# Check that assemblies are in a topic_map
for ASSEMBLY in $ALL_ASSEMBLIES; do
    # Get the page name to search the topic_map
    # Search for files only, not folders
    PAGE="File: $(basename "$ASSEMBLY" .adoc)"
    # Don't include the assembly if it is not in a topic map
    if grep -rq "$PAGE" --include "*.yml" _topic_maps ; then
        DISTROS+=("$(grep -rl "$PAGE" _topic_maps/*.yml)")
    fi
done

# Handle modified topic maps
UPDATED_DISTROS=$(echo "$FILES" | awk '/_topic_maps\/(.*)\.yml/')
# Concat all the updated topic maps
DISTROS+=("${UPDATED_DISTROS}")
# Clean up and remove duplicates
echo "${DISTROS[@]}" | tr ' ' '\n' | sort | uniq
