#!/bin/bash

# Script to add [role="_abstract"] to .adoc files that don't already have it

# Function to remove empty line after [role="_abstract"] if it exists
cleanup_empty_line_after_role() {
    local file="$1"
    local temp_file=$(mktemp)

    # Remove empty line after [role="_abstract"] if present
    sed '/^\[role="_abstract"\]$/{
        n
        /^$/d
    }' "$file" > "$temp_file"

    mv "$temp_file" "$file"
}

# Function to process files with :context: attribute
process_with_context() {
    local file="$1"
    echo "Processing file with :context: $file"

    # Create a temporary file
    local temp_file=$(mktemp)

    # Add after :context: line
    sed '/^:context:/{
        n
        /^$/{
            # Blank line exists after :context:, add role after it
            a\
[role="_abstract"]
        }
        /^[^$]/{
            # No blank line after :context:, add blank line and role
            i\
\
[role="_abstract"]
        }
    }' "$file" > "$temp_file"

    # Replace the original file with the modified content
    mv "$temp_file" "$file"

    # Remove empty line after [role="_abstract"] if present
    cleanup_empty_line_after_role "$file"

    echo "✓ Added [role=\"_abstract\"] after :context: in $file"
}

# Function to process a module file (REFERENCE, CONCEPT, PROCEDURE, CONTEXT, SNIPPET)
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

    # Remove empty line after [role="_abstract"] if present
    cleanup_empty_line_after_role "$file"

    echo "✓ Added [role=\"_abstract\"] to module $file"
}

# Function to process an assembly file with toc::[]
process_assembly_with_toc() {
    local file="$1"
    echo "Processing assembly (with toc): $file"

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

    # Remove empty line after [role="_abstract"] if present
    cleanup_empty_line_after_role "$file"

    echo "✓ Added [role=\"_abstract\"] to assembly $file"
}

# Function to process an assembly file without toc::[]
process_assembly_without_toc() {
    local file="$1"
    echo "Processing assembly (without toc): $file"

    # Create a temporary file
    local temp_file=$(mktemp)

    # Add after the heading, same as modules
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

    # Remove empty line after [role="_abstract"] if present
    cleanup_empty_line_after_role "$file"

    echo "✓ Added [role=\"_abstract\"] to assembly $file (no toc)"
}

# Find all .adoc files and process them
find . -name "*.adoc" -type f | while read -r file; do
    # Check if the file already has [role="_abstract"]
    if grep -q '\[role="_abstract"\]' "$file"; then
        echo "⏭ Skipping $file - already has [role=\"_abstract\"]"
    else
        # Check if it has :_mod-docs-content-type:
        if ! grep -q ':_mod-docs-content-type:' "$file"; then
            echo "⏭ Skipping $file - no :_mod-docs-content-type: attribute"
        else
            # Check if file has :context: attribute - handle this case first
            if grep -q '^:context:' "$file"; then
                process_with_context "$file"
            # Check if it's an assembly or module file (case-insensitive)
            elif grep -qi ':_mod-docs-content-type: ASSEMBLY' "$file"; then
                # Check if assembly has toc::[]
                if grep -q '^toc::\[\]' "$file"; then
                    process_assembly_with_toc "$file"
                else
                    process_assembly_without_toc "$file"
                fi
            elif grep -qiE ':_mod-docs-content-type: (REFERENCE|CONCEPT|PROCEDURE|CONTEXT)' "$file"; then
                process_module "$file"
            else
                echo "⏭ Skipping $file - unknown content type"
            fi
        fi
    fi
done

echo ""
echo "Done processing all .adoc files!"
