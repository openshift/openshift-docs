#!/usr/bin/env bash

#Find the modifid files and line numbers from git diff
FILES_AND_LINES=$(git diff --unified=0 --diff-filter=M HEAD~1 HEAD | \
grep -v -e '^[+-]' -e '^index' | \
sed 's/diff --git a.* b\//\//g; s/.*+\(.*\)@@.*/\1/g; s/^ -//g; s/,+[0-9]*//g; s/\(^[0-9]*\) +/\1-/g;' | grep -v '\\')

PREVIOUS_LINE=""
DIFF_JSON=""

#Convert git diff output to JSON
while read CURRENT_LINE; do
        if [[ $PREVIOUS_LINE == "" ]] &&  [[ $CURRENT_LINE == /* ]]; then
            #echo -e "[\n\t{\n\t\"file\": \"${CURRENT_LINE}\",\n\t\t\"lines\":[\n\t\t\t{\n"
            DIFF_JSON="$DIFF_JSON[\n\t{\n\t\"file\": \"${CURRENT_LINE}\",\n\t\t\"lines\":[\n\t\t\t{\n"
            PREVIOUS_LINE="filename"
        else
            if [[ $PREVIOUS_LINE == "filename" ]] &&  [[ $CURRENT_LINE =~ ^[[:digit:]] ]]; then
                START_DIGIT=""
                END_DIGIT=""
                if [[ $CURRENT_LINE =~ "," ]]; then
                    START_DIGIT="${CURRENT_LINE%,*}"
                    TEMP_DIGIT="${CURRENT_LINE#*,}"
                    END_DIGIT=$(( START_DIGIT + TEMP_DIGIT - 1 ))
                    #echo -e "\t\t\t\t\"start\":${START_DIGIT},\n\t\t\t\t\"end\":${END_DIGIT}\n\t\t\t}"
                    DIFF_JSON="$DIFF_JSON\t\t\t\"start\":${START_DIGIT},\n\t\t\t\"end\":${END_DIGIT}\n\t\t\t}"
                else
                    #echo -e "\t\t\t\t\"start\":${CURRENT_LINE},\n\t\t\t\t\"end\":${CURRENT_LINE}\n\t\t\t}"
                    DIFF_JSON="$DIFF_JSON\t\t\t\"start\":${CURRENT_LINE},\n\t\t\t\"end\":${CURRENT_LINE}\n\t\t\t}"
                fi
                PREVIOUS_LINE="number"
            else
                if [[ $PREVIOUS_LINE == "number" ]] &&  [[ $CURRENT_LINE =~ ^[[:digit:]] ]]; then
                    START_DIGIT=""
                    END_DIGIT=""
                    if [[ $CURRENT_LINE =~ "," ]]; then
                        START_DIGIT="${CURRENT_LINE%,*}"
                        TEMP_DIGIT="${CURRENT_LINE#*,}"
                        END_DIGIT=$(( START_DIGIT + TEMP_DIGIT - 1 ))
                        #echo -e "\t\t\t,\n\t\t\t{\n\t\t\t\t\"start\":${START_DIGIT},\n\t\t\t\t\"end\":${END_DIGIT}\n\t\t\t}"
                        DIFF_JSON="$DIFF_JSON,\n\t\t\t{\n\t\t\t\"start\":${START_DIGIT},\n\t\t\t\"end\":${END_DIGIT}\n\t\t\t}"
                    else
                        #echo -e "\t\t\t,\n\t\t\t{\n\t\t\t\t\"start\":${CURRENT_LINE},\n\t\t\t\t\"end\":${CURRENT_LINE}\n\t\t\t}"
                        DIFF_JSON="$DIFF_JSON,\n\t\t\t{\n\t\t\t\"start\":${CURRENT_LINE},\n\t\t\t\"end\":${CURRENT_LINE}\n\t\t\t}"
                    fi
                    PREVIOUS_LINE="number"
                else
                     if [[ $PREVIOUS_LINE == "number" ]] &&  [[ $CURRENT_LINE == /* ]]; then
                        #echo -e "\t\t]\n\t},\n\t{\n\t\t\"file\": \"${CURRENT_LINE}\",\n\t\t\"lines\":[\n\t\t\t{\n"
                        DIFF_JSON="$DIFF_JSON\n\t\t]\n\t},\n\t{\n\t\"file\": \"${CURRENT_LINE}\",\n\t\t\"lines\":[\n\t\t\t{\n"
                        PREVIOUS_LINE="filename"
                     else
                        #echo -e "]\n},"
                        DIFF_JSON="$DIFF_JSON]\n},"
                    fi
                fi
            fi
        fi
done <<< "$FILES_AND_LINES"

#echo -e "\t\t]\n\t}\n]"
DIFF_JSON="$DIFF_JSON\n\t\t]\n\t}\n]"

echo -e "${DIFF_JSON}" > difflines.json
echo "✓ DONE!"
