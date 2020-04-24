#!/bin/bash
set -ev

# Set output colors
NC='\033[0m' # No Color
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'

ALLOWED_USERS=("gaurav-nelson" "mburke5678" "vikram-redhat" "abrennan89" "ahardin-rh" "kalexand-rh" "adellape" "bmcelvee" "ousleyp" "lamek" "JStickler" "rh-max" "bergerhoffer" "huffmanca" "sheriff-rh" "jboxman" "bobfuru" "joaedwar" "aburdenthehand" "boczkowska" "Preeticp" "neal-timpe" "codyhoag" "pmacko1" "apinnick" "bgaydosrh" "lmandavi" "nkakkar81" "maxwelldb" "pneedle-rh" "lbarbeevargas" "jeana-redhat")
USERNAME=${TRAVIS_PULL_REQUEST_SLUG::-15}
COMMIT_HASH="$(git rev-parse @~)"
mapfile -t FILES_CHANGED < <(git diff --name-only "$COMMIT_HASH")

buildpreview () {

    UPDATED_BRANCH_NAME="${TRAVIS_PULL_REQUEST_BRANCH//./-}" #converts all dots to dashes in URL's (fixes incorrect URLs in comments)
    PREVIEW_URL=https://${UPDATED_BRANCH_NAME}--ocpdocs.netlify.com
    COMMENT_FOUND=''

    echo -e "${YELLOW}==== CURRENT BRANCH ====${NC}"
    git rev-parse --abbrev-ref HEAD

    echo -e "${YELLOW}==== RESETTING REMOTES ====${NC}"
    git remote rm origin
    git remote add origin https://"${GH_PREVIEW_BOT_TOKEN}"@github.com/openshift-docs-preview-bot/openshift-docs.git > /dev/null 2>&1

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

    #set the remote to user repository
    echo -e "${YELLOW}==== SETTING REMOTE FOR ${BLUE}$TRAVIS_PULL_REQUEST_SLUG:$TRAVIS_PULL_REQUEST_BRANCH${YELLOW} ====${NC}"
    git remote add userrepo https://github.com/"$TRAVIS_PULL_REQUEST_SLUG".git

    #add branch to remote
    echo -e "${YELLOW}==== SETTING REMOTE BRANCH TRACKING ====${NC}"
    git remote set-branches --add userrepo "$TRAVIS_PULL_REQUEST_BRANCH"

    #fetch updated changes
    echo -e "${YELLOW}==== FETCHNING the BRANCH ${BLUE}$TRAVIS_PULL_REQUEST_BRANCH ====${NC}"
    git fetch userrepo "$TRAVIS_PULL_REQUEST_BRANCH"

    #checkout branch
    echo -e "${YELLOW}==== Checking out ${BLUE}$TRAVIS_PULL_REQUEST_BRANCH ====${NC}"
    git checkout -b preview_branch userrepo/"$TRAVIS_PULL_REQUEST_BRANCH"

    echo -e "${YELLOW}==== CHANGING NAME OF THE BRANCH ====${NC}"
    git branch -m "$TRAVIS_PULL_REQUEST_BRANCH"

    echo -e "${YELLOW}==== PUSHING TO GITHUB ====${NC}"
    git push origin -f "$TRAVIS_PULL_REQUEST_BRANCH" --quiet

    echo -e "${YELLOW}==== CHECKING PREVIEW BUILD COMMENTS ====${NC}"
    #get all users who commented in an array
    PREVIEW_BOT_COMMENTS=$(curl -H "Authorization: token ${GH_PREVIEW_BOT_TOKEN}" https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments | jq '.[].user.login' | tr -d '"')
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
    COMMENTS_JSON=$(curl -H "Authorization: token ${GH_PREVIEW_BOT_TOKEN}" "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments" | jq '.')
    mapfile -t BOT_COMMENTS < <(echo "${COMMENTS_JSON}" | jq '.[] | select(.user.login=="openshift-docs-bot") | .url')

    if [ ${#BOT_COMMENTS[@]} -eq 0 ]; then
        echo -e "${GREEN} No build failed comments.${NC}"
    else
        for COMMENT_URL in "${BOT_COMMENTS[@]}"
        do
            curl -H "Authorization: token ${GH_PREVIEW_BOT_TOKEN}" -X "DELETE" "${COMMENT_URL}"
            echo -e "${GREEN} Deleted comment ${BLUE}${COMMENT_URL}${NC}"
        done
    fi

    if [[ "$COMMENT_FOUND" = false ]]; then
        COMMENT_DATA1='The preview will be available shortly at: \n'
        COMMENT_DATA="${COMMENT_DATA1}- ${PREVIEW_URL}"
        echo -e "\033[31m COMMENT DATA: $COMMENT_DATA"
        curl -H "Authorization: token ${GH_PREVIEW_BOT_TOKEN}" -X POST -d "{\"body\": \"${COMMENT_DATA}\"}" "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"
    fi

    echo -e "${GREEN}DONE!${NC}"

}

if [ "$TRAVIS_PULL_REQUEST" != "false" ] ; then #to make sure it only runs on PRs and not all merges
    if [[ " ${ALLOWED_USERS[*]} " =~ " ${USERNAME} " ]]; then # to make sure it only runs on PRs from @openshift/team-documentation
        if [ "${TRAVIS_PULL_REQUEST_BRANCH}" != "master" ] ; then # to make sure it does not run for direct master changes
            if [[ " ${FILES_CHANGED[*]} " = *".adoc"* ]]; then # to make sure this doesn't run for genreal modifications
                echo -e "${GREEN}[✓] Running preview build.${NC}"
                buildpreview
            else
                echo -e "\\n\\033[1;33m[!] No .adoc files modified, not building a preview.\\033[0m"
            fi
        else
            echo -e "\\n\\033[1;33m[!] Direct PR for master branch, not building a preview.\\033[0m"
        fi
    else
        echo -e "\\n\\033[1;33m[!] ${USERNAME} is not a team member of @openshift/team-documentation, not building a preview.\\033[0m"
    fi
else
    echo -e "\\n\\033[1;33m[!] Not a PR, not building a preview.\\033[0m"
fi
