#!/bin/bash
set -ev

ALLOWED_USERS=("aireilly" "mburke5678" "vikram-redhat" "abrennan89" "ahardin-rh" "kalexand-rh" "adellape" "bmcelvee" "ousleyp" "lamek" "JStickler" "rh-max" "bergerhoffer" "sheriff-rh" "jboxman" "bobfuru" "aburdenthehand" "boczkowska" "Preeticp" "neal-timpe" "codyhoag" "apinnick" "bgaydosrh" "lmandavi" "maxwelldb" "pneedle-rh" "lbarbeevargas" "jeana-redhat" "RichardHoch" "johnwilkins" "sjhala-ccs" "mgarrellRH" "SNiemann15" "sfortner-RH" "jonquilwilliams" "ktania46" "wking" "
jc-berger" "rishumehra" "iranzo" "abhatt-rh" "@mohit-sheth" "stoobie" "emarcusRH" "kquinn1204" "mikemckiernan" "skrthomas" "sagidlow" "rolfedh")
USERNAME=${TRAVIS_PULL_REQUEST_SLUG::-15}
COMMIT_HASH="$(git rev-parse @~)"
mapfile -t FILES_CHANGED < <(git diff --name-only "$COMMIT_HASH")

if [[ "$USERNAME" == "openshift-cherrypick-robot" ]]; then
    echo -e "${YELLOW}🤖 PR by openshift-cherrypick-robot. Skipping the preview.${NC}"
    exit 0
fi

if [[ "$TRAVIS_PULL_REQUEST" ]]; then
    # Check if modified files meet the conditions
    COMMIT_HASH="$(git rev-parse @~)"
    modified_files=$(git diff --name-only "$COMMIT_HASH")
    send_request=false

    for file in $modified_files; do
        if [[ $file == *.adoc || $file == "_topic_map.yml" || $file == "_distro_map.yml" || $file == "_topic_maps/"* ]]; then
            send_request=true
            break
        fi
    done

    if [ "$send_request" = true ]; then
        # Build the JSON
        json_data=$(
            cat <<EOF
{
"PR_BRANCH": "${TRAVIS_PULL_REQUEST_BRANCH}",
"BASE_REPO": "${TRAVIS_REPO_SLUG}",
"PR_NUMBER": "${TRAVIS_PULL_REQUEST}",
"USER_NAME": "${USERNAME}",
"BASE_REF": "${TRAVIS_BRANCH}",
"REPO_NAME": "${TRAVIS_PULL_REQUEST_SLUG}",
"SHA": "${TRAVIS_PULL_REQUEST_SHA}"
}
EOF
        )

        # Send the curl request
        if response=$(curl -s -X POST -H "Content-Type: application/json" --data "$json_data" https://ocpdocs-preview-receiver.vercel.app/api/buildPreview); then
            if echo "$response" | jq -e '.message == "Invalid data!"' >/dev/null; then
                echo -e "${RED}❌😔 Curl request failed: Invalid data!${NC}"
                echo -e "${YELLOW}$json_data${NC}"
                exit 1
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
