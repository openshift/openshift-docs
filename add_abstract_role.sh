#!/bin/bash

# Script to add [role="_abstract"] after zero-level headings in .adoc files

# Function to process a module file
process_module() {
    local file="$1"
    echo "Processing module: $file"

    # Create a temporary file
    local temp_file=$(mktemp)

    # Check if there's a blank line after the heading, if not add one
    sed '/^= /{
        n
        /^$/{
            # Blank line exists, add role after it
            a\
[role="_abstract"]
        }
        /^[^$]/{
            # No blank line, add blank line and role
            i\
\
[role="_abstract"]
        }
    }' "$file" > "$temp_file"

    # Replace the original file with the modified content
    mv "$temp_file" "$file"

    echo "✓ Added [role=\"_abstract\"] to module $file"
}

# Function to process an assembly file
process_assembly() {
    local file="$1"
    echo "Processing assembly: $file"

    # Check if file contains toc::[]
    if ! grep -q '^toc::\[\]' "$file"; then
        echo "⚠ Warning: Assembly file $file does not contain 'toc::[]' line - skipping"
        return 1
    fi

    # Create a temporary file
    local temp_file=$(mktemp)

    # Check if there's a blank line after toc::[], if not add one
    sed '/^toc::\[\]/{
        n
        /^$/{
            # Blank line exists, add role after it
            a\
[role="_abstract"]
        }
        /^[^$]/{
            # No blank line, add blank line and role
            i\
\
[role="_abstract"]
        }
    }' "$file" > "$temp_file"

    # Replace the original file with the modified content
    mv "$temp_file" "$file"

    echo "✓ Added [role=\"_abstract\"] to assembly $file"
}

# Find all .adoc files and process them
find . -name "*.adoc" -type f | while read -r file; do
    # Check if the file already has [role="_abstract"]
    if grep -q '\[role="_abstract"\]' "$file"; then
        echo "⚠ Skipping $file - already has [role=\"_abstract\"]"
    else
        # Check if it's an assembly or module file
        if grep -q ':_mod-docs-content-type: ASSEMBLY' "$file"; then
            process_assembly "$file"
        elif grep -q ':_mod-docs-content-type: REFERENCE\|:_mod-docs-content-type: CONCEPT\|:_mod-docs-content-type: PROCEDURE' "$file"; then
            process_module "$file"
        else
            echo "⚠ Skipping $file - unknown content type (not ASSEMBLY, REFERENCE, CONCEPT, or PROCEDURE)"
        fi
    fi
done

echo "Done processing all .adoc files!"