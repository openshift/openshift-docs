#!/bin/bash
# Report errors for links to Red Hat JIRA bugs that are behind a login

# Get modifed lines, remove deleted lines from the diff 
git_diff=$(git diff --unified=0 --stat --diff-filter=AM HEAD~1 HEAD "*release-notes*.adoc" ':(exclude)_unused_topics/*' | grep '^+' | grep -Ev '^(\+\+\+ a/ b/)')

# Remove all multi-line comments and single line comments
git_diff=$(echo "${git_diff}" | sed '\|^+////|,\|^+////|c\\' | sed '\|^+//| s|.*|//|')

# Search the git diff for links
link_regex='https://issues\.redhat\.com/browse/[A-Z]+-[0-9]+'
links=$(echo ${git_diff} | grep -o -E $link_regex | sort -u)

for link in ${links}; do
    # Check for links that require a login
    response=$(curl -I "${link}" 2>&1)
    if echo "${response}" | grep -q "permissionViolation"; then
        errors=true
        # Get the modified files and line numbers
        file_line_number=$(git grep -n "${link}" -- '*release-notes*.adoc' ':(exclude)_unused_topics/*' --diff-filter=AM HEAD~1 HEAD | awk -F':' '{print $1":"$2}')
        echo -e "\e[31mERROR: \n${file_line_number} \n\e[0mDo not include links to JIRA issues that require a login (${link})\n\e[0m"
    fi
done

if [ "$errors" = true ]; then
    exit 1
fi