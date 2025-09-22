#!/bin/bash

# Spinner function
spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\'
    while kill -0 $pid 2>/dev/null; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

# Ask user for the base directory
read -rp "Enter the path to the base directory: " BASE_DIR

# Validate directory
if [[ ! -d "$BASE_DIR" ]]; then
    echo "Error: $BASE_DIR is not a valid directory."
    exit 1
fi

echo "Processing directory: $BASE_DIR"

FILES=$(find "$BASE_DIR" -type f -name "*.adoc")
TOTAL_COUNT=$(echo "$FILES" | wc -l | tr -d ' ')

CURRENT=0
echo "Found $TOTAL_COUNT .adoc files."

# Process files
echo
for FILE in $FILES; do
    CURRENT=$((CURRENT+1))
    printf "Processing file %d/%d: %s" "$CURRENT" "$TOTAL_COUNT" "$FILE"

    (
        REPLACEMENTS=$(awk '
        BEGIN { count=0 }
        # Remove [discrete] and prevent blank line
        /^\[discrete\]$/ { count++; next }
        { print }
        END { print "###REPLACEMENTS###" count }
        ' "$FILE")

        COUNT=$(echo "$REPLACEMENTS" | tail -n1 | sed 's/###REPLACEMENTS###//')

        if [[ "$COUNT" -gt 0 ]]; then
            echo "$REPLACEMENTS" | sed '/###REPLACEMENTS###/d' > "${FILE}.tmp" && mv "${FILE}.tmp" "$FILE"
            echo "###SUMMARY### $COUNT"
        fi
    ) &
    spinner $!
    RESULT=$(wait $! 2>/dev/null; true)

    COUNT=$(echo "$RESULT" | grep "###SUMMARY###" | awk '{print $2}')

    if [[ -n "$COUNT" && "$COUNT" -gt 0 ]]; then
        echo " -> Modified ($COUNT [discrete] removed)"
    else
        echo -ne "\r\033[K"
    fi
done
