#!/bin/bash
set -ev

#ALLOWED_USERS=("aireilly" "mburke5678" "vikram-redhat" "abrennan89" "ahardin-rh" "kalexand-rh" "adellape" "bmcelvee" "ousleyp" "lamek" "JStickler" "rh-max" "bergerhoffer" "sheriff-rh" "jboxman" "bobfuru" "aburdenthehand" "boczkowska" "Preeticp" "neal-timpe" "codyhoag" "apinnick" "bgaydosrh" "lmandavi" "maxwelldb" "pneedle-rh" "lbarbeevargas" "jeana-redhat" "RichardHoch" "johnwilkins" "sjhala-ccs" "mgarrellRH" "SNiemann15" "sfortner-RH" "jonquilwilliams" "ktania46" "wking" "
#jc-berger" "rishumehra" "iranzo" "abhatt-rh" "@mohit-sheth" "stoobie" "emarcusRH" "kquinn1204" "mikemckiernan" "skrthomas" "sagidlow" "rolfedh")

if [ "$TRAVIS_PULL_REQUEST" != "false" ] ; then #to make sure it only runs on PRs and not all merges
    USERNAME=${TRAVIS_PULL_REQUEST_SLUG::-15}
    COMMIT_HASH="$(git rev-parse @~)"
    mapfile -t FILES_CHANGED < <(git diff --name-only "$COMMIT_HASH")

    if [ "${TRAVIS_PULL_REQUEST_BRANCH}" != "main" ] ; then # to make sure it does not run for direct main changes
        if [[ " ${FILES_CHANGED[*]} " = *".adoc"* ]] || [[ " ${FILES_CHANGED[*]} " = *"_topic_map.yml"* ]] || [[ " ${FILES_CHANGED[*]} " = *"_distro_map.yml"* ]] ; then # to make sure this doesn't run for general modifications
            if [ "$USERNAME" != "openshift-cherrypick-robot" ] ; then # to make sure it doesn't run for USERNAME openshift-cherrypick-robot
                echo "{\"PR_BRANCH\":\"${TRAVIS_PULL_REQUEST_BRANCH}\",\"BASE_REPO\":\"${TRAVIS_REPO_SLUG}\",\"PR_NUMBER\":\"${TRAVIS_PULL_REQUEST}\",\"USER_NAME\":\"${USERNAME}\",\"BASE_REF\":\"${TRAVIS_BRANCH}\",\"REPO_NAME\":\"${TRAVIS_PULL_REQUEST_SLUG}\",\"SHA\":\"${TRAVIS_PULL_REQUEST_SHA}\"}" > buildset.json

                curl -H 'Content-Type: application/json' --request POST --data @buildset.json "https://eoa6vg2jiwjbnh6.m.pipedream.net"

                echo -e "\\n\\033[0;32m[✓] Sent request for building a preview.\\033[0m"
            else
                echo -e "\\n\\033[0;32m[✓] Skipping preview build for openshift-cherrypick-robot.\\033[0m"
            fi
        else
            echo -e "\\n\\033[1;33m[!] No .adoc files modified, not building a preview.\\033[0m"
        fi
    else
        echo -e "\\n\\033[1;33m[!] Direct PR for main branch, not building a preview.\\033[0m"
    fi
else
    echo -e "\\n\\033[1;33m[!] Not a PR, not building a preview.\\033[0m"
fi
