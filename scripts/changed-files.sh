#!/bin/bash

echo "================================================================"
echo "Travis variables:"
echo "Travis commit range: $TRAVIS_COMMIT_RANGE"
echo "Travis commit message: $TRAVIS_COMMIT_MESSAGE"
echo "Travis commit: $TRAVIS_COMMIT"
echo "Travis PR branch: $TRAVIS_PULL_REQUEST_BRANCH"
echo "Travis SHA: $TRAVIS_PULL_REQUEST_SHA"
echo "Travis slug: $TRAVIS_PULL_REQUEST_SLUG"
echo "Travis repo slug: $TRAVIS_REPO_SLUG"
echo "================================================================"

CHANGED_FILES=$(git diff --name-only "$TRAVIS_COMMIT_RANGE" --diff-filter=d "*.yml" "*.adoc" ':(exclude)_unused_topics/*')

echo "================================================================"
echo "Modified files in pull request from $TRAVIS_PULL_REQUEST_BRANCH:"
echo "$CHANGED_FILES"
echo "================================================================"
