#!/bin/bash

set -e

declare -i ERROR=0

echo ""
echo "==================================================================="
echo "Asciidoc files must meet the following requirements:"
echo "1. no xrefs in asciidoc modules"
echo "2. xrefs in asciidoc assembly files must not reference *.html files"
echo "3. xrefs must have anchor IDs"
echo "==================================================================="
echo ""

#check modules

FILES=$(git diff-tree HEAD HEAD~1 --no-commit-id -r --name-only "modules/*.adoc")

if [ -n "${FILES}" ]
    then
        for FILE in ${FILES}; do
            echo ""
            if cat $FILE | sed -E '/\/\/\/\//,/\/\/\/\//d' | grep "^[^\/\/].*xref:.*\." | sed -e 's/^/ERROR: /' ; then
                echo "xref found in $FILE. You can't use xrefs in module files."
                ERROR=1
            fi
        done
    else
        echo "No asciidoc modules found in PR."
fi

#check assemblies

FILES=$(git diff-tree HEAD HEAD~1 --no-commit-id -r --name-only "*.adoc" ':(exclude)modules/*')

if [ -n "${FILES}" ]
    then
        for FILE in ${FILES}; do
            echo ""
            if cat $FILE | sed -E '/\/\/\/\//,/\/\/\/\//d' | grep "^[^\/\/].*xref:.*\.html" | sed -e 's/^/ERROR: /' ; then
                echo "xref error found in $FILE. You can't link to *.html files in an xref."
                ERROR=1
            fi
            echo ""
            if cat $FILE | sed -E '/\/\/\/\//,/\/\/\/\//d' | grep "^[^\/\/].*xref.*\.adoc[^#]" | sed -e 's/^/ERROR: /' ; then
                echo "xref error found in $FILE. There is no anchor id ('#') specified for the xref."
                ERROR=1
            fi
        done
    else
        echo "No asciidoc assembly files found in PR."
fi

echo "==============================================================================================================================="
echo ""

if [[ $ERROR == 1 ]]; then
    exit 1
else 
    true
fi
