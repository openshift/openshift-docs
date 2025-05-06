#!/bin/bash

set -e

PACKAGE="${PACKAGE:-commercial}"
REPO="${REPO:-https://github.com/openshift/openshift-docs.git}"
BRANCH="${BRANCH:-standalone-logging-docs-main}"
# Default to podman, but allow using docker through environment variable
CONTAINER_ENGINE="${CONTAINER_ENGINE:-podman}"
# By default, use container for building, but allow using local asciibinder
USE_LOCAL="${USE_LOCAL:-false}"

## CLONE REPO
echo "---> Cloning docs from $BRANCH branch in $REPO"
# Clone OpenShift Docs into current directory
git clone --branch $BRANCH --depth 1 --no-single-branch $REPO .docs_source

cd .docs_source


for remote in $(cat _distro_map.yml | yq eval ".*.branches | keys | .[]" - | sort | uniq)
do
    git fetch origin $remote
    echo "checkout $remote"
    git checkout $remote 2>/dev/null || git checkout --force --track remotes/origin/$remote
done

echo "---> Packaging $PACKAGE docs content"
git checkout $BRANCH

# Check if we're using local asciibinder or container
if [ "$USE_LOCAL" = "true" ]; then
  # Check if asciibinder is actually installed
  if command -v asciibinder >/dev/null 2>&1; then
    echo "Using local asciibinder installation"
    asciibinder package --site=$PACKAGE 2>/dev/null
  else
    echo "Warning: Local asciibinder not found. Falling back to container."
    $CONTAINER_ENGINE run --rm -v `pwd`:/docs:Z quay.io/openshift-cs/asciibinder asciibinder package --site=$PACKAGE 2>/dev/null
  fi
else
  echo "Using $CONTAINER_ENGINE container for build"
  $CONTAINER_ENGINE run --rm -v `pwd`:/docs:Z quay.io/openshift-cs/asciibinder sh -c "git config --global --add safe.directory /docs && asciibinder package --site=$PACKAGE" 2>/dev/null
fi

## MOVING FILES INTO THE RIGHT PLACES
rm -rf ../_package
mkdir -p ../_package
sudo mv _package/${PACKAGE}/* ../_package/
git checkout $BRANCH

cd ..
sudo rm -rf .docs_source
