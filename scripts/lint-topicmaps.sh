#!/bin/bash

# Use yamllint to lint and report errors for modified topic_map.yml files

# Ensure yamllint is installed
if ! command -v yamllint &>/dev/null; then
    echo "yamllint is not installed. Please install it and try again 👻"
    exit 127
fi

# List of modified topic_map files
FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "./_topic_maps/*.yml")

if [ -n "${FILES}" ]; then
    has_errors=0
    for FILE in ${FILES[@]}; do
        if ! yamllint "$FILE"; then
            echo "YAML error(s) found in $FILE 😥"
            has_errors=1
        fi
    done

    if [ $has_errors -eq 1 ]; then
        exit 1
    else
        echo "No YAML errors found 🥳"
        exit 0
    fi
else
    echo "No updated topic_maps... 😙"
    exit 0
fi
