#!/bin/sh

set -e

if [ -z "${GITHUB_BASE_REF}" ]
    then 
        MAINBRANCH="origin/main"
    else
        MAINBRANCH="origin/$GITHUB_BASE_REF"
fi

FILES=$(git diff --name-only --diff-filter=AM "$MAINBRANCH")

if [ -n "${FILES}" ]
    then
        echo "Validating xrefs on file added or modified in comparison to $MAINBRANCH"
        echo ""
        echo "==============================================================================================================================="
        echo "1. xrefs in modules are not allowed."
        echo "2. xrefs cannot contain references to html files."
        echo "==============================================================================================================================="
        for FILE in ${FILES}; do
            if [[ $FILE == *.adoc ]]; then
                if grep -q -r --include=\*.adoc -s 'xref:.*\.html' $FILE
                    then
                        echo "Errors found in $FILE" 
                    else echo "Errors not found in $FILE."
                fi
            fi
        done
    else
        echo "No files added or modified in comparison to $MAINBRANCH"
fi