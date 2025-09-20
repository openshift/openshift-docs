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
        BEGIN { mode=""; count=0 }

        # [discrete] starts possible collapse
        /^\[discrete\]/ { mode="discrete"; next }

        # [id=...] handling
        /^\[id=/ {
            if (mode=="discrete") {
                mode="discrete_id"; next
            } else {
                mode="id"; buf=$0; next
            }
        }

        # Heading after [discrete]
        mode=="discrete" && /^=+ / {
            sub(/^=+ +/, "")
            print $0 "::"
            mode=""
            count++
            next
        }

        # Heading after [discrete]+[id]
        mode=="discrete_id" && /^=+ / {
            sub(/^=+ +/, "")
            print $0 "::"
            mode=""
            count++
            next
        }

        # Heading:: after [id]
        mode=="id" && /::$/ {
            print $0
            mode=""
            count++
            next
        }

        # If [id] wasn’t followed by Heading::, restore it
        mode=="id" {
            print buf
            buf=""
            mode=""
        }

        # Reset if discrete marker wasn’t followed by heading
        mode=="discrete" { mode=""; }
        mode=="discrete_id" { mode=""; }

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
        echo " -> Modified ($COUNT replacements)"
    else
        echo -ne "\r\033[K"
    fi
done