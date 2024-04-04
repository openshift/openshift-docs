#!/bin/bash
# Returns a list of page preview URLs
# To run locally, clean the _preview folder and do a new asciibinder build before running the script
# To run in Prow CI, run with 
# ./get-updated-preview-urls.sh $PULL_NUMBER

# Check if jq is installed
hash jq 2>/dev/null || { echo >&2 "Error: jq is not installed"; exit 1; }

# Set $pull_number if it is not passed as variable
if [ $# -eq 0 ]; then
commit_id=$(git log -n 1 --pretty=format:"%H")
pull_number="$(curl -s "https://api.github.com/search/issues?q=$commit_id" | jq '.items[0].number')"
pr_branch="$(git rev-parse --abbrev-ref HEAD)"
else
    pull_number=$1
    pr_branch="latest"
fi

preview_url_slug="ocpdocs-pr"
preview_url="https://${pull_number}--${preview_url_slug}.netlify.app"
assemblies=()
pages=()
files=$(git diff --name-only HEAD~1 HEAD --diff-filter=AMRD "*.adoc" ':(exclude)_unused_topics/*')

# Get the full list of HTML build files
if [ -e "_preview" ]; then
    built_pages=$(find _preview -type f -name "*.html" -printf "%P\n")
else
    echo "_preview output folder not found"
    exit 1
fi

# Search for $file references in all *.adoc files that are not in a folder called modules/, snippets/, or _unused_topics/
for file in $files; do
    include_ref="include::$file"
    found_file=$(find . -name '*.adoc' -not -path "modules/*" -not -path "snippets/*" -not -path "_unused_topics/*" -exec grep -rl "^$include_ref" {} +)
    # Add the found updated assemblies, not directly included in PR
    assemblies+=("$found_file")
    # If not found, then it is a directly updated assembly file
    if [ -z "$found_file" ]; then
        assemblies+=("$file")
    fi
done

# Make the HTML URL slug
if [ ${#assemblies[@]} -gt 0 ]; then
    updated_pages=$(echo "${assemblies[@]}" | sed 's/\.adoc$/.html/' | sort | uniq)
fi

# Search built_pages for every entry in updated_pages and add to pages array when it is found
for updated_page in $updated_pages; do
    # sed s/$pr_branch/latest to match the Prow build URL
    found_page=$(echo "${built_pages}" | grep "${updated_page}" | sed "s|/$pr_branch/|/latest/|")
    pages+=("${found_page}")
done

#Echo the results, prepending the $preview_url to every line
echo "${pages[@]}" | tr ' ' '\n' | sort | uniq | sed "s|^|$preview_url/|"
