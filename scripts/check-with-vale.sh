#!/bin/bash

set -e

# list of *.adoc files excluding files in /rest_api, generated files, and deleted files
FILES=$(git diff --name-only HEAD~1 HEAD --diff-filter=d "*.adoc" ':(exclude)rest_api/*' ':(exclude)modules/example-content.adoc' ':(exclude)modules/oc-adm-by-example-content.adoc')

if [ -n "${FILES}" ] ;
    then
        echo "Validating language usage in added or modified asciidoc files with $(vale -v)"
        echo ""
        echo "==============================================================================================================================="
        echo "Read about the error terms that cause the build to fail at https://redhat-documentation.github.io/vale-at-red-hat/docs/reference-guide/termserrors/"
        echo "==============================================================================================================================="
        if [ "$TRAVIS" = true ] ; then
            #clean out conditional markup in Travis CI
            sed -i -e 's/ifdef::.*\|ifndef::.*\|ifeval::.*\|endif::.*/ /' ${FILES}
            vale ${FILES} --glob='*.adoc' --minAlertLevel=error
        else
            vale ${FILES} --glob='*.adoc' --minAlertLevel=suggestion
        fi
    else
        echo "No asciidoc files added or modified."
fi
