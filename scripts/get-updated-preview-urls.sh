#!/bin/bash
# Returns a list of page preview URLs for use with Prow CI jobs
# To run locally, clean the _preview folder and do a new asciibinder build before running the script

# Check if jq is installed
hash jq 2>/dev/null || { echo >&2 "Error: jq is not installed"; exit 1; }

pr_branch="$(git rev-parse --abbrev-ref HEAD)"
commit_id=$(git log -n 1 --pretty=format:"%H")
pr_number="$(curl -s "https://api.github.com/search/issues?q=$commit_id" | jq '.items[0].number')"
preview_url_slug="ocpdocs-pr"
preview_url="https://${pr_number}--${preview_url_slug}.netlify.app"
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
    found_file=$(find . -name '*.adoc' -not -path "./modules/*" -not -path "./snippets/*" -not -path "./_unused_topics/*" -exec grep -rl "^$include_ref" {} +)
    if [ -z "$found_file" ]; then
        assemblies+=("$file")
    fi
done

# Make the HTML URL slug
if [ ${#assemblies[@]} -gt 0 ]; then
    updated_pages=$(echo "${assemblies[@]}" | xargs -n1 basename | sed 's/\.adoc$/.html/' | sort | uniq)
else
    # No updated pages, just add default URL
    pages+=("${preview_url}")
fi

# Search built_pages for every entry in updated_pages and add to pages array when it is found
for updated_page in $updated_pages; do
    # sed $pr_branch > "latest" to match the Prow build URL
    found_page=$(echo "${built_pages}" | grep "${updated_page}" | sed "s/$pr_branch/latest/")
    pages+=("${preview_url}/${found_page}")
done

printf '%s\n' "${pages[@]}" | sort | uniq
