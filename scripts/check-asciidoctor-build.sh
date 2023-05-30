#!/bin/bash

set -e

# ensure asciidoctor is installed
if ! command -v asciidoctor &>/dev/null ;
then
    echo "Asciidoctor is not installed. Please install it and try again."
    exit 127
fi

# get the *.adoc modules and assemblies in the pull request
FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*.adoc" ':(exclude)_unused_topics/*')

REPO_PATH=$(git rev-parse --show-toplevel)

# get the modules in the PR, search for assemblies that include them, and concat with any updated assemblies files
check_updated_assemblies () {
    MODULES=$(echo "$FILES" | awk '/modules\/(.*)\.adoc/')
    if [ "${MODULES}" ]
    then
        # $UPDATED_ASSEMBLIES is the list of assemblies that contains changed modules
        UPDATED_ASSEMBLIES=$(grep -rnwl "$REPO_PATH" --include=\*.adoc --exclude-dir={snippets,modules} -e "$MODULES")
        # subtract $REPO_PATH from path with bash substring replacement
        UPDATED_ASSEMBLIES=${UPDATED_ASSEMBLIES//"$REPO_PATH/"/}
    fi
    # $ASSEMBLIES is the list of modifed assemblies
    ASSEMBLIES=$(echo "$FILES" | awk '!/modules\/(.*)\.adoc/')
    # concatenate both lists and remove dupe entries
    ALL_ASSEMBLIES=$(echo "$UPDATED_ASSEMBLIES $ASSEMBLIES" | tr ' ' '\n' | sort -u)
    # check that assemblies are in a topic_map
    for ASSEMBLY in $ALL_ASSEMBLIES; do
        # get the page name to search the topic_map
        PAGE=$(basename "$ASSEMBLY" .adoc)
        # don't validate the assembly if it is not in a topic map
        if grep -rq "$PAGE" --include "*.yml" _topic_maps ; then
            # validate the assembly
            echo "Validating $ASSEMBLY. Validation will fail with FAILED, ERROR, or WARNING messages..."
            asciidoctor "$ASSEMBLY" -a icons! -o /dev/null -v --failure-level WARN
        else
            echo "$ASSEMBLY is not in a topic_map"
        fi
    done
}

# check assemblies and fail if errors are reported
if [ -n "${FILES}" ] ;
then
    check_updated_assemblies
else
    echo "No modified AsciiDoc files found."
fi
