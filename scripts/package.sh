#!/bin/bash

set -e

PACKAGE="${PACKAGE:-commercial}"
REPO="${REPO:-https://github.com/openshift/openshift-docs.git}"
BRANCH="${BRANCH:-standalone-logging-docs-main}"


## CLONE REPO
echo "---> Cloning docs from $BRANCH branch in $REPO"
# Clone OpenShift Docs into current directory
git clone --branch $BRANCH --depth 1 $REPO .docs_source

cd .docs_source
# it's necessary to enforce a * ref so that all branches are referenced
#sed -i 's%fetch = +refs.*%fetch = +refs/heads/*:refs/remotes/origin/*%' .git/config
git fetch --all --quiet
for remote in $(cat _distro_map.yml | yq eval ".*.branches | keys | .[]" - | sort | uniq)
do
    git checkout $remote 2>/dev/null || git checkout --force --track remotes/origin/$remote
done

echo "---> Packaging $PACKAGE docs content"
git checkout $BRANCH

asciibinder package --site=$PACKAGE 2>/dev/null


cd ..
rm -rf .docs_source