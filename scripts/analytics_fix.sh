#!/bin/bash
set -ev

NC='\033[0m' # No Color
GREEN='\033[0;32m'

# Download analytics related files and move them to correct folders
echo -e "${GREEN}==== Download files with removed analytics ====${NC}"
wget https://raw.githubusercontent.com/openshift/openshift-docs/main/scripts/ocpdocs/_analytics_other.html -O _templates/_analytics_other.html
wget https://raw.githubusercontent.com/openshift/openshift-docs/main/scripts/ocpdocs/_footer_other.html.erb -O _templates/_footer_other.html.erb
wget https://raw.githubusercontent.com/openshift/openshift-docs/main/scripts/ocpdocs/_topnav_other.html -O _templates/_topnav_other.html
wget https://raw.githubusercontent.com/openshift/openshift-docs/main/scripts/ocpdocs/index-commercial.html -O index-commercial.html
wget https://raw.githubusercontent.com/openshift/openshift-docs/main/scripts/ocpdocs/search-commercial.html -O search-commercial.html
