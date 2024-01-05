#!/bin/bash

# Script to update Prow configuration

# Check if required parameters are provided
if [ $# -lt 3 ]; then
    echo "Provide values for \$VERSION \$BRANCH \$DISTROS"
    exit 1
fi

# Assign input parameters to variables
VERSION=$1
BRANCH=$2
DISTROS=$3

# Export variables for use in subshells
export VERSION BRANCH DISTROS

# Define folder path
folder="$(git rev-parse --show-toplevel)/scripts/prow"

# Check if the scripts/prow directory exists
if [ ! -d "$folder" ]; then
    echo "The scripts/prow directory does not exist. Make sure your repository structure is correct."
    exit 1
fi

# Define template and new Prow config paths
template="${folder}/openshift-openshift-docs-BRANCH.yaml"
new_prow_config="${folder}/openshift-openshift-docs-${BRANCH}.yaml"

# Check if the release directory exists
if [ -d "$HOME/release" ]; then
    # Create a new Prow config using environment variables
    envsubst < "$template" > "$new_prow_config"
    
    # Copy the new Prow config to the release directory
    cp "$new_prow_config" "$HOME/release/ci-operator/config/openshift/openshift-docs/"
    
    # Remove the temporary Prow config file
    rm "$new_prow_config"
    
    echo "New Prow job created: $HOME/release/ci-operator/config/openshift/openshift-docs/$(basename "$new_prow_config")"
else
    echo "Fork and clone the git@github.com:openshift/release.git repo to $HOME/release and run the script again"
    exit 1
fi
