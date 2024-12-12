#!/bin/bash

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${YELLOW}==========================================================================${NC}"

echo -e "${CYAN}Only run this script after you've generated the drupal-build directory.${NC}"

echo -e "${YELLOW}==========================================================================${NC}"

echo -e "${BLUE}Press Enter to continue or Ctrl+C to exit.${NC}"
read -r

BASE_DIR="./drupal-build/openshift-acs/rest_api"

if [[ ! -d "$BASE_DIR" ]]; then
    echo -e "${RED}Error: Directory '$BASE_DIR' does not exist.${NC}"
    exit 1
fi

echo -e "${BLUE}Enter the product version number, for example: 4.6 ${NC}"
read -r PRODUCT_VERSION

if [[ -z "$PRODUCT_VERSION" ]]; then
    echo -e "${RED}Error: Product version cannot be empty.${NC}"
    exit 1
fi

total_folders=0
folders_with_files=0
folders_without_files=0
total_generated_files=0

camel_to_space() {
    echo "$1" | sed -r 's/([a-z])([A-Z])/\1 \2/g; s/([A-Z]+)([A-Z][a-z])/\1 \2/g'
}

for dir in "$BASE_DIR"/*/; do
    if [[ ! -d "$dir" ]]; then
        echo -e "${YELLOW}Warning: '$dir' is not a directory.${NC}"
        continue
    fi

    folder_name=$(basename "$dir")
    if [[ "$folder_name" == "images" ]]; then
        echo -e "${YELLOW}Skipping 'images' directory.${NC}"
        continue
    fi

    total_folders=$((total_folders + 1))
    folder_name=$(basename "$dir")
    master_file="$dir/master.adoc"
    docinfo_file="$dir/docinfo.xml"

    if [[ -f "$master_file" && -f "$docinfo_file" ]]; then
        folders_with_files=$((folders_with_files + 1))
        continue
    fi

    folders_without_files=$((folders_without_files + 1))

    # Create master.adoc
    echo -e "${GREEN}Creating master.adoc in $dir${NC}"
    title=$(camel_to_space "$folder_name")
    includes=""

    for adoc_file in "$dir"/*.adoc; do
        if [[ ! -f "$adoc_file" ]]; then
            echo -e "${YELLOW}Warning: No .adoc files found in '$dir'.${NC}"
            continue
        fi

        if [[ "$adoc_file" != "$master_file" && "$adoc_file" != "$docinfo_file" ]]; then
            includes+="include::$(basename "$adoc_file")[leveloffset=+1]\n\n"
        fi
    done

    {
        echo "= $title"
        echo ":product-author: Red Hat OpenShift Documentation Team"
        echo ":product-title: Red Hat Advanced Cluster Security for Kubernetes"
        echo ":product-version: $PRODUCT_VERSION"
        echo ":openshift-acs:"
        echo ":imagesdir: images"
        echo ":idseparator: -"
        echo ""
        echo -e "$includes"
    } > "$master_file"
    total_generated_files=$((total_generated_files + 1))

    # Create docinfo.xml
    echo -e "${GREEN}Creating docinfo.xml in $dir${NC}"
    {
        echo "<title>$title</title>"
        echo "<productname>Red Hat Advanced Cluster Security for Kubernetes</productname>"
        echo "<productnumber>$PRODUCT_VERSION</productnumber>"
        echo "<subtitle>Reference guide for $title.</subtitle>"
        echo "<abstract>"
        echo "    <para>This document describes the Red Hat Advanced Cluster Security for Kubernetes API objects and their detailed specifications.</para>"
        echo "</abstract>"
        echo "<authorgroup>"
        echo "    <orgname>Red Hat OpenShift Documentation Team</orgname>"
        echo "</authorgroup>"
        echo "<xi:include href=\"Common_Content/Legal_Notice.xml\" xmlns:xi=\"http://www.w3.org/2001/XInclude\" />"
    } > "$docinfo_file"
    total_generated_files=$((total_generated_files + 1))
done

echo -e "${BLUE}Total folders checked: $total_folders${NC}"
echo -e "${BLUE}Folders with master.adoc and docinfo.xml: $folders_with_files${NC}"
echo -e "${BLUE}Folders without files (created files): $folders_without_files${NC}"
echo -e "${BLUE}Total generated files: $total_generated_files${NC}"
