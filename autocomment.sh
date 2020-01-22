#!/bin/bash
set -ev

#download build log
wget https://api.travis-ci.org/v3/job/"${TRAVIS_JOB_ID}"/log.txt

# since all errors are Red (\033[0;31m), grep gets them and then sed
# removes all color information.
ERROR_LIST=$(grep '31m' travis-log-408052641.txt | sed -r "s/[[:cntrl:]]\[[0-9]{1,3}m//g")
echo "" > errors.txt

ALLOWED_USERS=("mburke5678" "vikram-redhat" "abrennan89" "ahardin-rh" "kalexand-rh" "adellape" "bmcelvee" "ousleyp" "lamek" "JStickler" "rh-max" "bergerhoffer" "huffmanca" "sheriff-rh" "jboxman" "bobfuru" "joaedwar" "aburdenthehand" "boczkowska" "Preeticp" "neal-timpe" "codyhoag" "pmacko1" "apinnick" "bgaydosrh" "lmandavi")
USERNAME=${TRAVIS_PULL_REQUEST_SLUG::-15}

if [ "$TRAVIS_PULL_REQUEST" != "false" ] ; then #to make sure it only runs on PRs and not all merges
    if [[ " ${ALLOWED_USERS[*]} " =~ " ${USERNAME} " ]]; then # to make sure it only runs on PRs from @openshift/team-documentation
        if [ "${TRAVIS_PULL_REQUEST_BRANCH}" != "master" ] ; then # to make sure it does not run for direct master changes
          echo "$ERROR_LIST" >> errors.txt

          #add metadta for errors (required for adding GH comment)
          {
          echo -e "USERNAME:${USERNAME}"
          echo "PR_NUMBER:${TRAVIS_PULL_REQUEST}"
          echo "BASE_REPO:${TRAVIS_REPO_SLUG}"
          } >> info.txt

          #bundle errors and metadata as json
          cat errors.txt info.txt | jq  --raw-input . | jq --slurp . > buildlog.json
          #send json to ocp-docs-bot
          curl -H 'Content-Type: application/json' --request POST --data @buildlog.json "https://ocp-docs-bot.glitch.me/travis-error"
        else
            echo -e "\\n\\033[1;33m[!] Direct PR for master branch, not building a preview.\\033[0m"
        fi
    else
        echo -e "\\n\\033[1;33m[!] ${USERNAME} is not a team member of @openshift/team-documentation, not building a preview.\\033[0m"
    fi
else
    echo -e "\\n\\033[1;33m[!] Not a PR, not building a preview.\\033[0m"
fi
