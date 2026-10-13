#!/usr/bin/env bash
#
# run-adoc-prechecks.sh - Automated AsciiDoc pre-conversion validation
#
# Runs three validation checks:
# 1. Map completeness (asciidoctor)
# 2. Vale DITA style validation
# 3. Exploration (Vale suggestions)
#
# Usage:
#   ./run-adoc-prechecks.sh <product-name>
#   ./run-adoc-prechecks.sh --all

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

# Ensure logs directory exists
mkdir -p logs

# Available products
AVAILABLE_PRODUCTS=(ocp osd rosa-classic rosa-hcp virt microshift)

# Check prerequisites
check_prerequisites() {
    local missing=()

    if ! command -v asciidoctor &>/dev/null; then
        missing+=("asciidoctor (gem install asciidoctor)")
    fi

    if ! command -v list-content &>/dev/null; then
        missing+=("list-content (gem install asciidoctor-list-content)")
    fi

    if ! command -v vale &>/dev/null; then
        missing+=("vale (https://docs.vale.sh/topics/installation)")
    fi

    if [ ! -f "$HOME/.dita.ini" ]; then
        missing+=("~/.dita.ini (AsciiDocDITA Vale configuration)")
    fi

    if [ ${#missing[@]} -gt 0 ]; then
        echo -e "${RED}ERROR: Missing prerequisites:${NC}"
        printf '  - %s\n' "${missing[@]}"
        echo ""
        echo -e "${YELLOW}Please install missing tools before running conversion pre-checks.${NC}"
        exit 1
    fi
}

# Get log file name (no prefix for OCP, product prefix for others, category suffix if applicable)
get_log_file() {
    local product=$1
    local log_type=$2
    local category=$3

    local base_name="${log_type}"

    # Add category suffix if specified
    if [ -n "$category" ]; then
        base_name="${category}-${log_type}"
    fi

    if [ "$product" == "ocp" ] && [ -z "$category" ]; then
        echo "logs/${log_type}.log"
    elif [ "$product" == "ocp" ] && [ -n "$category" ]; then
        echo "logs/${category}-${log_type}.log"
    else
        echo "logs/${product}-${base_name}.log"
    fi
}

# Run check 1: Map completeness
check_map_completeness() {
    local product=$1
    local nav_file=$2
    local category=$3
    local log_file=$(get_log_file "$product" "asciidoctor" "$category")

    echo -e "${BLUE}[1/3] Checking map completeness for ${product}...${NC}"

    if [ ! -f "$nav_file" ]; then
        echo -e "${RED}  ERROR: Navigation file not found: ${nav_file}${NC}"
        return 1
    fi

    # Run asciidoctor and capture errors
    if asciidoctor "$nav_file" 2>&1 | tee "$log_file" | grep -q ERROR; then
        local error_count=$(grep -c ERROR "$log_file" || echo "0")
        echo -e "${RED}  ✗ Found ${error_count} error(s) - see ${log_file}${NC}"
        return 1
    else
        echo -e "${GREEN}  ✓ No errors found${NC}"
        return 0
    fi
}

# Run check 2: Vale DITA validation
check_vale_dita() {
    local product=$1
    local nav_file=$2
    local category=$3
    local log_file=$(get_log_file "$product" "vale" "$category")

    echo -e "${BLUE}[2/3] Running Vale DITA validation for ${product}...${NC}"

    # Sync Vale styles
    echo "  Syncing Vale styles..."
    vale --config ~/.dita.ini sync 2>&1 | grep -v "^$" || true

    # Run Vale on all content
    echo "  Validating content..."
    local temp_list=$(mktemp)
    list-content "$nav_file" 2>/dev/null | sort -u > "$temp_list" || true

    if [ ! -s "$temp_list" ]; then
        echo -e "${YELLOW}  ⚠ No content files found${NC}"
        rm "$temp_list"
        return 0
    fi

    # Run vale and capture output
    cat "$temp_list" | xargs vale --config ~/.dita.ini --output line > "$log_file" 2>&1 || true
    rm "$temp_list"

    # Count issues by type
    if [ -s "$log_file" ]; then
        echo "  Summary of issues found:"
        cut -d : -f 4 "$log_file" | sort | uniq -c | sort -rn | sed 's/^/    /'
        echo -e "${YELLOW}  ⚠ Issues found - see ${log_file}${NC}"
        return 1
    else
        echo -e "${GREEN}  ✓ No issues found${NC}"
        return 0
    fi
}

# Run check 3: Exploration (suggestions)
check_exploration() {
    local product=$1
    local nav_file=$2
    local category=$3
    local log_file=$(get_log_file "$product" "exploration" "$category")

    echo -e "${BLUE}[3/3] Running exploration check for ${product}...${NC}"

    # Run Vale with suggestions filter
    local temp_list=$(mktemp)
    list-content "$nav_file" 2>/dev/null | sort -u > "$temp_list" || true

    if [ ! -s "$temp_list" ]; then
        echo -e "${YELLOW}  ⚠ No content files found${NC}"
        rm "$temp_list"
        return 0
    fi

    # Run vale with suggestion filter
    cat "$temp_list" | xargs vale --config ~/.dita.ini --output line --filter '.Level=="suggestion"' > "$log_file" 2>&1 || true
    rm "$temp_list"

    # Display summary
    if [ -s "$log_file" ]; then
        echo "  Summary of suggestions:"
        cut -d : -f 4 "$log_file" | sort | uniq -c | sort -rn | sed 's/^/    /'
        echo -e "${YELLOW}  ℹ Suggestions logged - see ${log_file}${NC}"

        # Highlight specific concerning patterns
        if grep -q "AttributeDefinition" "$log_file"; then
            echo -e "${YELLOW}  ⚠ Found problematic AttributeDefinition - review required${NC}"
        fi

        if grep -q "SnippetLink" "$log_file"; then
            echo -e "${YELLOW}  ℹ Found SnippetLink - may need post-conversion cleanup${NC}"
        fi

        return 0
    else
        echo -e "${GREEN}  ✓ No suggestions${NC}"
        return 0
    fi
}

# Run checks for a single product or category
run_checks_for_product() {
    local product=$1
    local nav_file=$2
    local category=$3
    local status=0

    local check_target="$product"
    if [ -n "$category" ]; then
        check_target="${product}/${category}"
    fi

    echo -e "\n${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}Running pre-checks for: ${check_target}${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

    # Run all three checks
    check_map_completeness "$product" "$nav_file" "$category" || status=1
    echo ""
    check_vale_dita "$product" "$nav_file" "$category" || status=1
    echo ""
    check_exploration "$product" "$nav_file" "$category"

    echo ""
    if [ $status -eq 0 ]; then
        echo -e "${GREEN}✓ All critical checks passed for ${check_target}${NC}"
    else
        echo -e "${RED}✗ Some checks failed for ${check_target} - review logs${NC}"
    fi

    return $status
}

# Main execution
main() {
    local check_items=()  # Array of "product:nav_file:category" tuples
    local overall_status=0

    # Parse arguments
    if [ $# -eq 0 ]; then
        # Default: check OCP navigation
        check_items+=("ocp:maps/ocp/navigation.adoc:")
    elif [ "$1" == "--all" ]; then
        # Check all products
        for product in "${AVAILABLE_PRODUCTS[@]}"; do
            if [ -f "maps/${product}/navigation.adoc" ]; then
                check_items+=("${product}:maps/${product}/navigation.adoc:")
            fi
        done
    else
        local arg="$1"

        # Check if argument is a category file (install, secure, etc.)
        if [ -f "maps/ocp/${arg}.adoc" ]; then
            # Category for OCP
            check_items+=("ocp:maps/ocp/${arg}.adoc:${arg}")
        elif [ -f "maps/ocp/${arg}" ]; then
            # Category with .adoc extension
            local category=$(basename "$arg" .adoc)
            check_items+=("ocp:maps/ocp/${arg}:${category}")
        elif [ -f "$arg" ] && [[ "$arg" == maps/* ]]; then
            # Full path to a map file
            local product=$(echo "$arg" | cut -d/ -f2)
            local category=$(basename "$arg" .adoc)
            if [ "$category" == "navigation" ]; then
                check_items+=("${product}:${arg}:")
            else
                check_items+=("${product}:${arg}:${category}")
            fi
        elif [ -f "maps/${arg}/navigation.adoc" ]; then
            # Product name
            check_items+=("${arg}:maps/${arg}/navigation.adoc:")
        else
            echo -e "${RED}ERROR: Could not find map file for: ${arg}${NC}"
            echo ""
            echo "Available products: ${AVAILABLE_PRODUCTS[*]}"
            echo ""
            echo "Available OCP categories:"
            ls maps/ocp/*.adoc 2>/dev/null | grep -v navigation.adoc | xargs -n1 basename | sed 's/\.adoc$//' | sed 's/^/  /'
            exit 1
        fi
    fi

    echo -e "${BLUE}AsciiDoc Pre-Conversion Checks${NC}"
    echo -e "${BLUE}===============================${NC}"

    # Check prerequisites
    check_prerequisites

    echo ""

    # Run checks for each item
    for item in "${check_items[@]}"; do
        IFS=':' read -r product nav_file category <<< "$item"
        if ! run_checks_for_product "$product" "$nav_file" "$category"; then
            overall_status=1
        fi
    done

    # Final summary
    echo -e "\n${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Summary${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

    echo "Log files created:"
    for item in "${check_items[@]}"; do
        IFS=':' read -r product nav_file category <<< "$item"

        local display_name="$product"
        if [ -n "$category" ]; then
            display_name="${product}/${category}"
        fi

        echo "  ${display_name}:"

        if [ "$product" == "ocp" ] && [ -z "$category" ]; then
            # OCP navigation uses unprefixed log names
            for log_type in asciidoctor vale exploration; do
                if [ -f "logs/${log_type}.log" ]; then
                    ls -lh "logs/${log_type}.log" | awk '{print "    " $9 " (" $5 ")"}'
                fi
            done
        elif [ "$product" == "ocp" ] && [ -n "$category" ]; then
            # OCP category uses category-prefixed names
            for log_type in asciidoctor vale exploration; do
                if [ -f "logs/${category}-${log_type}.log" ]; then
                    ls -lh "logs/${category}-${log_type}.log" | awk '{print "    " $9 " (" $5 ")"}'
                fi
            done
        else
            # Other products use product-prefixed log names
            if [ -n "$category" ]; then
                ls -lh logs/${product}-${category}-*.log 2>/dev/null | awk '{print "    " $9 " (" $5 ")"}'
            else
                ls -lh logs/${product}-*.log 2>/dev/null | awk '{print "    " $9 " (" $5 ")"}'
            fi
        fi
    done

    echo ""
    if [ $overall_status -eq 0 ]; then
        echo -e "${GREEN}✓ All products passed critical checks${NC}"
    else
        echo -e "${RED}✗ Some products have issues - review logs and fix before conversion${NC}"
    fi

    exit $overall_status
}

main "$@"
