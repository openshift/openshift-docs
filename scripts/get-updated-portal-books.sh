#!/bin/bash
# Returns a list of updated portal books
# To run locally or in Prow CI:
# ./get-updated-portal-books.sh

# Check if jq is installed
hash jq 2>/dev/null || { echo >&2 "Error: jq is not installed"; exit 1; }

assemblies=()
updated_books=()
files=$(git diff --name-only HEAD~1 HEAD --diff-filter=AMRD "*.adoc" ':(exclude)_unused_topics/*')

# Get the full list of master.adoc files in the drupal-build/ folder
if [ -e "drupal-build" ]; then
    master_files=$(find drupal-build -type f -name "master.adoc" -printf "drupal-build/%P\n")
else
    echo "drupal-build output folder not found"
    exit 1
fi

# Search for $file references in all *.adoc files that are not in a folder called modules/, snippets/, or _unused_topics/
for file in $files; do
    include_ref="include::$file"
    found_file=$(grep -rl --include='*.adoc' --exclude-dir={modules,snippets,_unused_topics} "^$include_ref")
    # Add the found updated assemblies, not directly included in PR
    assemblies+=("$found_file")
    # If not found, then it is a directly updated assembly file
    if [ -z "$found_file" ]; then
        assemblies+=("$file")
    fi
done

# Construct the drupal-build master.adoc folder paths
if [ ${#assemblies[@]} -gt 0 ]; then
    for assembly in "${assemblies[@]}"; do
        updated_master_files+=$(echo "$assembly" | awk -F'/' '{print "drupal-build/openshift-enterprise/" $1 "/master.adoc"}' | tr '\n' ' ')
    done
fi

# Search master_files for every entry in updated_master_files and add to updated_books array when it is found
for master_file in $updated_master_files; do
    updated_book=$(echo "${master_files}" | grep "${master_file}")
    updated_books+=("${updated_book}")
done

# Echo the updated master.adoc files
echo "${updated_books[@]}" | tr ' ' '\n' | sort | uniq
