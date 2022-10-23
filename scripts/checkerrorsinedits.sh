#!/usr/bin/env bash

#Find the modifid files and line numbers from git diff
FILES_AND_LINES=$(git diff --unified=0 --diff-filter=M HEAD~2 HEAD~1 "*.adoc" ':(exclude)rest_api/*' ':(exclude)modules/example-content.adoc' ':(exclude)modules/oc-adm-by-example-content.adoc' | \
grep -v -e '^[+-]' -e '^index' | \
sed 's/diff --git a.* b\//\//g; s/.*+\(.*\)@@.*/\1/g; s/^ -//g; s/,+[0-9]*//g; s/\(^[0-9]*\) +/\1-/g;' | grep -v '\\')

FILES=$(git diff --name-only HEAD~2 HEAD~1 --diff-filter=d "*.adoc" ':(exclude)rest_api/*' ':(exclude)modules/example-content.adoc' ':(exclude)modules/oc-adm-by-example-content.adoc')

VALE_DATA=$(vale ${FILES} --glob='*.adoc' --minAlertLevel=error --glob='*.adoc' --output=line)

PREVIOUS_LINE=""
SEARCH_STRING=""

while read CURRENT_LINE; do
    if [[ $PREVIOUS_LINE == "" ]] &&  [[ $CURRENT_LINE == /* ]]; then
        #echo "${CURRENT_LINE}"
        SEARCH_STRING="${SEARCH_STRING}${CURRENT_LINE}\n"
        PREVIOUS_LINE="filename"
    else
        if [[ $PREVIOUS_LINE == "filename" || "number" ]] &&  [[ $CURRENT_LINE =~ ^[[:digit:]] ]]; then
            START_DIGIT=""
            END_DIGIT=""
            if [[ $CURRENT_LINE =~ "," ]]; then
                START_DIGIT="${CURRENT_LINE%,*}"
                TEMP_DIGIT="${CURRENT_LINE#*,}"
                END_DIGIT=$(( START_DIGIT + TEMP_DIGIT - 1 ))
                LINE_NUMBERS=$(seq -s ' ' ${START_DIGIT} ${END_DIGIT})
                #echo "${LINE_NUMBERS}"
                SEARCH_STRING="${SEARCH_STRING} ${LINE_NUMBERS}"
            else
                #echo "${CURRENT_LINE}"
                SEARCH_STRING="${SEARCH_STRING} ${CURRENT_LINE}"
            fi
            PREVIOUS_LINE="number"
        else
            if [[ $PREVIOUS_LINE == "number" ]] &&  [[ $CURRENT_LINE == /* ]]; then
                #echo "END"
                SEARCH_STRING="${SEARCH_STRING}\nEND\n"
                #echo "${CURRENT_LINE}"
                SEARCH_STRING="${SEARCH_STRING} ${CURRENT_LINE}\n"
            fi
        fi
    fi
done <<< "$FILES_AND_LINES"

#echo "END"
SEARCH_STRING="${SEARCH_STRING}\nEND"

#echo -e "${SEARCH_STRING}"

while IFS= read -r LINE; do
    #echo "Text read from file: $LINE"
    #echo $LINE | tr ":" "\n"
    IFS=':' read -ra ERROR <<< $LINE
    #FILENAME=$(echo ${ERROR[0]} | sed -r 's/[/]+/\//g')
    #echo ${FILENAME}
    #echo "LINE: ${ERROR[1]}"
    ESC_FILEPATH=$(echo "${ERROR[0]}" | sed 's/\//\\\//g')
    #echo "${ESC_FILEPATH}"
    MATCH=$(echo -e ${SEARCH_STRING} | sed "/${ESC_FILEPATH}/,/END/!d;/END/q")
    #echo "${MATCH}" | grep -q "${ERROR[1]}"
    #echo $?
    if [[ $MATCH == *"${ERROR[1]}"* ]]; then
        echo -e "FILE: ${ERROR[0]}\nLINE: ${ERROR[1]}\nERROR: ${ERROR[3]} ${ERROR[4]}"
        sleep 2
    fi
done <<< "$VALE_DATA"

#sed '/rosa_planning\/rosa-sts-aws-prereqs.adoc/,/END/!d;/END/q'
