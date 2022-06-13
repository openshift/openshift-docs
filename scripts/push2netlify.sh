#!/bin/bash
set -ev

NC='\033[0m' # No Color
#RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'

PREVIEW_URL=https://${TRAVIS_PULL_REQUEST}--docspreview.netlify.com
NEW_PR=''

echo -e "${YELLOW}==== CURRENT BRANCH ====${NC}"
git rev-parse --abbrev-ref HEAD

echo -e "${YELLOW}==== SETTING GIT USER ====${NC}"
git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

echo -e "${YELLOW}==== RESETTING REMOTES ====${NC}"
git remote -v
git remote rm origin
git remote add origin https://"${GH_BOT_TOKEN}"@github.com/ocpdocs-previewbot/openshift-docs.git > /dev/null 2>&1
git remote -v

#checkout branch
echo -e "${YELLOW}==== Checking out a PR ${BLUE}$TRAVIS_PULL_REQUEST branch ====${NC}"
git branch "${TRAVIS_PULL_REQUEST}" && git checkout "${TRAVIS_PULL_REQUEST}"

echo -e "${YELLOW}==== PUSHING TO GITHUB ====${NC}"
git push origin -f "${TRAVIS_PULL_REQUEST}" --quiet

echo -e "${YELLOW}==== CHECKING PREVIEW BUILD COMMENTS ====${NC}"
# Check if netlify site exists, if it doesn't that means either the build failed or the this is a new PR
if curl --output /dev/null --silent --head --fail "$PREVIEW_URL"; then
    echo -e "${GREEN}PR exists. No new comment on the PR.${NC}"
    NEW_PR=false
    else
    echo -e "${GREEN}PR does not exist. Add a new comment on the PR.${NC}"
    NEW_PR=true
fi

if [[ "$NEW_PR" = true ]]; then
    COMMENT_DATA="The preview will be available shortly at: \n ${PREVIEW_URL}"
    echo -e "${YELLOW}ADDING COMMENT on PR${NC}"
    echo -e "${BLUE}COMMENT DATA:${NC}$COMMENT_DATA"
    curl -H "Authorization: token ${GH_BOT_TOKEN}" -X POST -d "{\"body\": \"${COMMENT_DATA}\"}" "https://api.github.com/repos/openshift/openshit-docs/issues/${TRAVIS_PULL_REQUEST}/comments" > /dev/null 2>&1
fi

echo -e "${GREEN}DONE!${NC}"
