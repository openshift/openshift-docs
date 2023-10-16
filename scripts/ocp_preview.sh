#!/bin/bash
set -ev

# Download the preview page
wget https://raw.githubusercontent.com/openshift/openshift-docs/main/scripts/ocpdocs/_previewpage

# Copy preview page into the _preview folder
cp --verbose _previewpage _preview/index.html

#Download robots.txt
wget https://raw.githubusercontent.com/openshift/openshift-docs/main/scripts/ocpdocs/robots_preview.txt

# Copy robots into the _preview folder
cp --verbose robots_preview.txt _preview/robots.txt

# Rename (head detached at fetch_head) folder to latest
find _preview/ -depth -name '*(HEAD detached at FETCH_HEAD)*' -execdir bash -c 'mv "$0" "${0//(HEAD detached at FETCH_HEAD)/latest}"' {} \;

# Rename (head detached at fetch_head) to latest in all html files
# find _preview/ -type f -name '*.html' -exec sed -i 's/(HEAD detached at FETCH_HEAD)/latest/g' {} + ;

# Show file paths (uncomment for debug)
find _preview/ -maxdepth 3
