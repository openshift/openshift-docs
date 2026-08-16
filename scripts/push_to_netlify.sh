#!/bin/bash
set -ev

NC='\033[0m' # No Color
#RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'

UPDATED_BRANCH_NAME="${PR_BRANCH//./-}" #converts all dots to dashes in URL's (fixes incorrect URLs in comments)
PREVIEW_URL=https://${UPDATED_BRANCH_NAME}--ocpdocs.netlify.com
COMMENT_FOUND=''

echo -e "${YELLOW}==== CURRENT BRANCH ====${NC}"
git rev-parse --abbrev-ref HEAD

echo -e "${YELLOW}==== RESETTING REMOTES ====${NC}"
git remote rm origin
git remote add origin https://"${GH_TOKEN}"@github.com/openshift-docs-preview-bot/openshift-docs.git > /dev/null 2>&1

echo -e "${YELLOW}==== SETTING GIT USER ====${NC}"
git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

echo -e "${YELLOW}==== SETTING UPSTREAM ====${NC}"
git remote add upstream git://github.com/openshift/openshift-docs

echo -e "${YELLOW}==== SETTING MASTER BRANCH ====${NC}"
git fetch origin master
git rev-parse master
git fetch upstream master
git rev-parse upstream/master

#if [ "$(git rev-parse master)" != "$(git rev-parse upstream/master)" ]
#then
#    echo -e "${YELLOW}==== PUSHING UPSTRAM CHANGES TO MASTER ====${NC}"
#    git stash
#    git checkout master
#    git fetch upstream master
#    git rebase upstream/master
#    git push -f origin master
#else
#    echo -e "${GREEN}==== MASTER UP TO DATE WITH UPSTREAM MASTER ====${NC}"
#fi

#set the remote to user repository
echo -e "${YELLOW}==== SETTING REMOTE FOR ${BLUE}$REPO_NAME:$PR_BRANCH${YELLOW} ====${NC}"
git remote add userrepo https://github.com/"$REPO_NAME".git

#add branch to remote
echo -e "${YELLOW}==== SETTING REMOTE BRANCH TRACKING ====${NC}"
git remote set-branches --add userrepo "$PR_BRANCH"

#fetch updated changes
echo -e "${YELLOW}==== FETCHNING the BRANCH ${BLUE}$PR_BRANCH ====${NC}"
git fetch userrepo "$PR_BRANCH"

#checkout branch
echo -e "${YELLOW}==== Checking out ${BLUE}$PR_BRANCH ====${NC}"
git checkout -b preview_branch userrepo/"$PR_BRANCH"

echo -e "${YELLOW}==== CHANGING NAME OF THE BRANCH ====${NC}"
git branch -m "$PR_BRANCH"

echo -e "${YELLOW}==== PUSHING TO GITHUB ====${NC}"
git push origin -f "$PR_BRANCH" --quiet

# This logic fails when a user uses same branch names for different PRs
# echo -e "${YELLOW}==== CHECKING IF BRANCH ALREADY EXIST ====${NC}"
# if curl --output /dev/null --silent --head --fail "$PREVIEW_URL"; then
#     echo -e "${GREEN}Branch exists. No new comment on the PR.${NC}"
#     NEW_BRANCH=false
#     else
#     echo -e "${GREEN}Branch does not exist. Add a new comment on the PR.${NC}"
#     NEW_BRANCH=true
# fi
# Updated logic below, it checks if there is already a comment from preview bot,

echo -e "${YELLOW}==== CHECKING PREVIEW BUILD COMMENTS ====${NC}"
#get all users who commented in an array
PREVIEW_BOT_COMMENTS=$(curl -H "Authorization: token ${GH_BOT_TOKEN}" https://api.github.com/repos/${BASE_REPO}/issues/${PR_NUMBER}/comments | jq '.[].user.login' | tr -d '"')
echo "-------------------------------------------------COMMENT AUTHOR-----------------------------------------------------"
echo "${PREVIEW_BOT_COMMENTS}"
echo "--------------------------------------------------------------------------------------------------------------------"
if [[ " ${PREVIEW_BOT_COMMENTS[@]} " =~ "openshift-docs-preview-bot" ]]; then
    echo -e "${GREEN}Preview comment exists. No new comment on the PR.${NC}"
    COMMENT_FOUND=true
else
    echo -e "${GREEN}Preview comment does not exist. Add a new comment on the PR.${NC}"
    COMMENT_FOUND=false
fi

echo -e "$YELLOW==== REMOVING TRAVIS CI BUILD ERROR COMMENTS IF ANY ====${NC}"
COMMENTS_JSON=$(curl -H "Authorization: token ${GH_BOT_TOKEN}" "https://api.github.com/repos/${BASE_REPO}/issues/${PR_NUMBER}/comments" | jq '.')
mapfile -t BOT_COMMENTS < <(echo "${COMMENTS_JSON}" | jq '.[] | select(.user.login=="openshift-docs-bot") | .url')

if [ ${#BOT_COMMENTS[@]} -eq 0 ]; then
    echo -e "${GREEN} No build failed comments.${NC}"
else
    for COMMENT_URL in "${BOT_COMMENTS[@]}"
    do
        curl -H "Authorization: token ${GH_BOT_TOKEN}" -X "DELETE" "${COMMENT_URL}"
        echo -e "${GREEN} Deleted comment ${BLUE}${COMMENT_URL}${NC}"
    done
fi

echo -e "${YELLOW}==== FINDING MODIFIED FILES ====${NC}"
COMMIT_HASH="$(git rev-parse @~)"
mapfile -t FILES_CHANGED < <(git diff --name-only "$COMMIT_HASH")

echo -e "${YELLOW}==== REFERENCE CHECK ====${NC}"
for i in "${FILES_CHANGED[@]}"
            do
                #only do this for adoc files
                if [ "${i: -5}" == ".adoc" ] ; then
                    echo -e "${BLUE}******** CHECKING REFERENCES for ${i} ********${NC}"
                    node checkrefs.js "${i}"
                    echo $'******** DONE ********\n'
                fi
            done

if [[ "$COMMENT_FOUND" = false ]]; then
    #FILES_CHANGED=$(git diff --name-only HEAD HEAD~"${COMMITS_IN_PR}")
    COMMENT_DATA1='The preview will be available shortly at: \n'
    COMMENT_DATA2=''

    #only list the individual urls if modified files is upto 5
    if [ ${#FILES_CHANGED[@]} -lt 6 ] ; then
        for i in "${FILES_CHANGED[@]}"
            do
                #only do this for adoc files
                if [ "${i: -5}" == ".adoc" ] ; then
                    #ignore adoc files which are modules or topics
                    if [[ ${i} != *"topic"* || ${i} != *"module"* ]] ; then
                        FILE_NAME="${i::-5}"
                        CHECK_DOCS_URL="https://docs.openshift.com/container-platform/3.9/$FILE_NAME.html"
                        if curl --output /dev/null --silent --head --fail "$CHECK_DOCS_URL"; then
                            FINAL_URL="https://${PR_BRANCH}--ocpdocs.netlify.com/openshift-enterprise/latest/$FILE_NAME.html"
                            #COMMENT_DATA2="- *$i*: ${COMMENT_DATA2}${FINAL_URL}\\n"
                            echo "- *$i*: ${FINAL_URL}" >> comments.txt
                        fi
                    fi
                fi
            done
    fi

    echo -e "${YELLOW}ADDING COMMENT on PR${NC}"
    #if there is a comment file show individual file URLs otherwise show the main URL
    if [ ! -f comments.txt ]; then
	    COMMENT_DATA="${COMMENT_DATA1}- https://${PR_BRANCH}--ocpdocs.netlify.com/"
    else
	    COMMENT_DATA2=$(cat comments.txt)
	    COMMENT_DATA="${COMMENT_DATA1}${COMMENT_DATA2}"
    fi
    echo -e "\033[31m COMMENT DATA: $COMMENT_DATA"
    curl -H "Authorization: token ${GH_TOKEN}" -X POST -d "{\"body\": \"${COMMENT_DATA}\"}" "https://api.github.com/repos/${BASE_REPO}/issues/${PR_NUMBER}/comments"
fi

echo -e "${GREEN}DONE!${NC}"
