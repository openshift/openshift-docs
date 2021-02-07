#!/bin/bash
set -ev

ALLOWED_USERS=("openshift-cherrypick-robot")
USERNAME=${TRAVIS_PULL_REQUEST_SLUG::-15}

echo -e  "{\"PR_BRANCH\":\"${TRAVIS_PULL_REQUEST_BRANCH}\",\"BASE_REPO\":\"${TRAVIS_REPO_SLUG}\",\"PR_NUMBER\":\"${TRAVIS_PULL_REQUEST}\",\"USER_NAME\":\"${USERNAME}\",\"BASE_REF\":\"${TRAVIS_BRANCH}\",\"REPO_NAME\":\"${TRAVIS_PULL_REQUEST_SLUG}\"}"

if [ "$TRAVIS_PULL_REQUEST" != "false" ] ; then #to make sure it only runs on PRs and not all merges
    if [[ " ${ALLOWED_USERS[*]} " =~ " ${USERNAME} " ]]; then # to make sure it only runs on PRs from the bot
        if [ "${TRAVIS_PULL_REQUEST_BRANCH}" != "master" ] ; then # to make sure it does not run for direct master changes
          curl  -X PUT -H "Authorization: token ${GHAUTH}" "https://api.github.com/repos/openshift/openshift-docs/pulls/${TRAVIS_PULL_REQUEST}/merge"
          echo -e "\\n\\033[0;32m[✓] Automerged.\\033[0m"
        else
            echo -e "\\n\\033[1;33m[!] Direct PR for master branch, not building a preview.\\033[0m"
        fi
    else
        echo -e "\\n\\033[1;33m[!] Automerge is only for the bot\\033[0m"
    fi
else
    echo -e "\\n\\033[1;33m[!] Not a valid PR.\\033[0m"
fi
