#!/bin/bash

set -e

# list of *.adoc files excluding files in /rest_api, generated files, and deleted files
#FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*.adoc" ':(exclude)rest_api/*' ':(exclude)modules/example-content.adoc' ':(exclude)modules/oc-adm-by-example-content.adoc')

#exclude symlinks (-type f)
FILES=$(find -type f -name "*.adoc")

if [ -n "${FILES}" ] ;
    then
        echo "Validating language usage in asciidoc files with $(vale -v)"
        echo ""
        for FILE in ${FILES}
            do vale $FILE --output=line --minAlertLevel=error --no-exit
        done
    else
        echo "No asciidoc files found."
fi
