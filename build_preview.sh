#!/bin/bash
set -ev

if [ "$TRAVIS_PULL_REQUEST" != "false" ] && [ "$TRAVIS_BRANCH" == "master" ]; then
  NEW_BRANCH_NAME="preview-$TRAVIS_PULL_REQUEST_BRANCH"

  echo "RESETTING COMMIT"
  git reset --hard $TRAVIS_PULL_REQUEST_SHA

  echo "SETTING BRANCH NAME"
  git checkout -b $NEW_BRANCH_NAME

  echo "PUSHING TO GITHUB"
  git push -u origin $NEW_BRANCH_NAME --quiet --force

  echo "ADDING COMMENT on PR"
  COMMENT_DATA="The preview build for this PR is available at https://${NEW_BRANCH_NAME}--ocpdocs.netlify.com/"
  curl -H "Authorization: token ${DOCS_PREVIEW_TOKEN}" -X POST -d "{\"body\": \"${COMMENT_DATA}\"}" "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"
else
  echo "Skipping preview build, PR not for master"
fi
