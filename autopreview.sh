#!/bin/bash

set -e

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}PR_BRANCH:${NC} ${TRAVIS_PULL_REQUEST_BRANCH}"
echo -e "${YELLOW}BASE_REPO:${NC} ${TRAVIS_REPO_SLUG}"
echo -e "${YELLOW}PR_NUMBER:${NC} ${TRAVIS_PULL_REQUEST}"
echo -e "${YELLOW}BASE_REF:${NC} ${TRAVIS_BRANCH}"
echo -e "${YELLOW}REPO_NAME:${NC} ${TRAVIS_PULL_REQUEST_SLUG}"
echo -e "${YELLOW}SHA:${NC} ${TRAVIS_PULL_REQUEST_SHA}"

USERNAME=${TRAVIS_PULL_REQUEST_SLUG}
if [ ${#USERNAME} -ge 15 ]; then
    USERNAME=${USERNAME::-15}
else
    USERNAME=""
fi

# Check if any of the variables are blank or TRAVIS_PULL_REQUEST_BRANCH is false
if [ -z "${TRAVIS_PULL_REQUEST_BRANCH}" ] || [ "${TRAVIS_PULL_REQUEST_BRANCH}" == "false" ] || [ -z "${TRAVIS_REPO_SLUG}" ] || [ -z "${TRAVIS_PULL_REQUEST}" ] || [ -z "${TRAVIS_BRANCH}" ] || [ -z "${TRAVIS_PULL_REQUEST_SLUG}" ] || [ -z "${TRAVIS_PULL_REQUEST_SHA}" ]; then
    echo -e "${RED}❌😬 One or more required variables are blank. Exiting the script.${NC}"
    echo -e "${YELLOW}PR_BRANCH:${NC} ${TRAVIS_PULL_REQUEST_BRANCH}"
    echo -e "${YELLOW}BASE_REPO:${NC} ${TRAVIS_REPO_SLUG}"
    echo -e "${YELLOW}PR_NUMBER:${NC} ${TRAVIS_PULL_REQUEST}"
    echo -e "${YELLOW}BASE_REF:${NC} ${TRAVIS_BRANCH}"
    echo -e "${YELLOW}REPO_NAME:${NC} ${TRAVIS_PULL_REQUEST_SLUG}"
    echo -e "${YELLOW}SHA:${NC} ${TRAVIS_PULL_REQUEST_SHA}"
    exit 1
fi

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
                echo -e "${GREEN}✅🥳 $response${NC}"
            fi
        else
            echo -e "${RED}❌😬 Curl request failed: $response${NC}"
            echo -e "${YELLOW}$json_data${NC}"
            exit 1
        fi

        echo -e "${GREEN}🚀🎉 Request sent successfully!${NC}"
    else
        echo -e "${YELLOW}⚠️🤔 No .adoc files, _topic_map.yml, or _distro_map.yml modified. Skipping the preview.${NC}"
    fi
else
    echo -e "${YELLOW}❗🙅‍♀️ Not a Pull request. Skipping the preview.${NC}"
fi
