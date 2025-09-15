#!/bin/bash

set -e

PACKAGE="${PACKAGE:-commercial}"
REPO="${REPO:-https://github.com/openshift/openshift-docs.git}"
BRANCH="${BRANCH:-main}"
# Default to podman, but allow using docker through environment variable
CONTAINER_ENGINE="${CONTAINER_ENGINE:-podman}"
# By default, use container for building, but allow using local asciibinder
USE_LOCAL="${USE_LOCAL:-false}"
# Parameter to specify which distros to include (comma-separated)
DISTROS="${DISTROS:-}"
# Optional comma-separated list of specific branches to process
SPECIFIC_BRANCHES="${SPECIFIC_BRANCHES:-}"
# Parameter for offline mode (defaults to false)
OFFLINE="${OFFLINE:-false}"
# URL for the offline patch
OFFLINE_PATCH_URL="${OFFLINE_PATCH_URL:-https://github.com/openshift/openshift-docs/pull/92770.patch}"
# Parameter to control cleanup of _package folder (defaults to false)
CLEAN="${CLEAN:-false}"


# Determine if sudo is needed (typically only in GHA if files are created by root in container)
SUDO_CMD=""
if [ "$GITHUB_ACTIONS" == "true" ]; then
  echo "Running in GitHub Actions. Sudo prefix will be used if necessary."
  SUDO_CMD="sudo"
fi

## CLONE REPO
echo "---> Cloning docs from $BRANCH branch in $REPO"
# Clone OpenShift Docs into current directory
git clone --branch $BRANCH --depth 1 --no-single-branch $REPO .docs_source

cd .docs_source

# Filter distros in _distro_map.yml if DISTROS is provided
if [ -n "$DISTROS" ]; then
  echo "---> Filtering _distro_map.yml for distros: $DISTROS"

  # Create a backup of the original file
  cp _distro_map.yml _distro_map.yml.orig

  # Start with the document header
  echo "---" > _distro_map.yml

  # Convert comma-separated list to array
  IFS=',' read -ra DISTRO_ARRAY <<< "$DISTROS"

  # Process each distro in the list
  for distro in "${DISTRO_ARRAY[@]}"; do
    # Trim any whitespace from distro name
    distro=$(echo "$distro" | xargs)

    if [ -n "$distro" ]; then
      echo "---> Including distro: $distro"
      # Extract the section for this distro (from the distro name to the next distro or EOF)
      awk -v distro="$distro:" '
        # Check if line is a new distro section
        /^[a-zA-Z].*:/ {
          # If it matches our target distro, set flag to 1
          if ($0 ~ "^"distro) {
            flag=1
          }
          # If it is a different distro, set flag to 0
          else {
            flag=0
          }
        }
        # Only print if flag is 1
        flag == 1 {print}
      ' _distro_map.yml.orig >> _distro_map.yml
    fi
  done

  echo "---> _distro_map.yml filtered successfully"

  # Configure git for committing
  git config --local user.email "builder@example.com"
  git config --local user.name "Documentation Builder"

  # Add and commit the filtered _distro_map.yml file
  git add _distro_map.yml
  git commit -m "Filter _distro_map.yml for specified distros: $DISTROS"
else
  echo "---> Using original _distro_map.yml (DISTROS not specified)"
fi

# Configure git for committing (needed for all operations)
git config --local user.email "builder@example.com"
git config --local user.name "Documentation Builder"

# Make a copy of the _templates folder from the main branch
echo "---> Making a copy of _templates folder from main branch"
if [ -d "_templates" ]; then
  # Create a temporary directory to store the templates
  mkdir -p /tmp/openshift_templates_backup
  cp -r _templates/* /tmp/openshift_templates_backup/
  echo "---> _templates folder backed up successfully"
else
  echo "---> Warning: _templates folder not found in main branch"
fi

# Prepare for offline mode if OFFLINE is true
PATCH_FILE=""
if [ "$OFFLINE" = "true" ]; then
  echo "---> Downloading offline patch from $OFFLINE_PATCH_URL"
  # Download the patch once and save it to a temporary file
  PATCH_FILE=$(mktemp)
  curl -L "$OFFLINE_PATCH_URL" -o "$PATCH_FILE"

  # Apply patch to each branch if in offline mode
  if [ "$OFFLINE" = "true" ] && [ -f "$PATCH_FILE" ]; then
    echo "---> Applying offline patch to branch $remote"
    # Apply the patch and commit the changes
    git apply --ignore-whitespace "$PATCH_FILE" || echo "Warning: Could not apply patch to $BRANCH"
    # If the patch applied successfully, commit the changes
    if [ $? -eq 0 ]; then
      git add -A
      git commit -m "Apply offline patch (temporary)" || echo "Nothing to commit"
    fi
  fi

else
  echo "---> Skipping offline patch (OFFLINE=false)"
fi

# Convert comma-separated list to array
IFS=',' read -ra BRANCH_ARRAY <<< "$SPECIFIC_BRANCHES"

if [ -z "$SPECIFIC_BRANCHES" ]; then
  echo "---> No specific branches provided, processing all branches from _distro_map.yml"
  # Original behavior - process all branches in the _distro_map.yml
  for remote in $(cat _distro_map.yml | yq eval ".*.branches | keys | .[]" - | sort | uniq)
  do
      git fetch origin $remote
      echo "checkout $remote"
      git checkout $remote 2>/dev/null || git checkout --force --track remotes/origin/$remote

      # Copy _templates folder to this branch if backup exists
      if [ -d "/tmp/openshift_templates_backup" ] && [ "$(ls -A /tmp/openshift_templates_backup)" ]; then
        echo "---> Copying _templates folder to branch $remote"
        mkdir -p _templates
        cp -rf /tmp/openshift_templates_backup/* _templates/
        git add _templates
        git commit -m "Update _templates folder from main branch" || echo "No changes to _templates folder"
      fi

      # Apply patch to each branch if in offline mode
      if [ "$OFFLINE" = "true" ] && [ -f "$PATCH_FILE" ]; then
        echo "---> Applying offline patch to branch $remote"
        # Apply the patch and commit the changes
        git apply --ignore-whitespace "$PATCH_FILE" || echo "Warning: Could not apply patch to $remote"
        # If the patch applied successfully, commit the changes
        if [ $? -eq 0 ]; then
          git add -A
          git commit -m "Apply offline patch (temporary)" || echo "Nothing to commit"
        fi
      fi
  done
else
  echo "---> Processing only specified branches: $SPECIFIC_BRANCHES"
  # Process only the specified branches
  for remote in "${BRANCH_ARRAY[@]}"
  do
      # Trim any whitespace from branch name
      remote=$(echo "$remote" | xargs)
      if [ -n "$remote" ]; then
          git fetch origin $remote
          echo "checkout $remote"
          git checkout $remote 2>/dev/null || git checkout --force --track remotes/origin/$remote

          # Copy _templates folder to this branch if backup exists
          if [ -d "/tmp/openshift_templates_backup" ] && [ "$(ls -A /tmp/openshift_templates_backup)" ]; then
            echo "---> Copying _templates folder to branch $remote"
            mkdir -p _templates
            cp -rf /tmp/openshift_templates_backup/* _templates/
            git add _templates
            git commit -m "Update _templates folder from main branch" || echo "No changes to _templates folder"
          fi

          # Apply patch to each branch if in offline mode
          if [ "$OFFLINE" = "true" ] && [ -f "$PATCH_FILE" ]; then
            echo "---> Applying offline patch to branch $remote"
            # Use the cached patch file instead of downloading again
            git apply --ignore-whitespace "$PATCH_FILE" || echo "Warning: Could not apply patch to $remote"
            # If the patch applied successfully, commit the changes
            if [ $? -eq 0 ]; then
              git add -A
              git commit -m "Apply offline patch (temporary)" || echo "Nothing to commit"
            fi
          fi
      fi
  done
fi

echo "---> Packaging $PACKAGE docs content"
git checkout $BRANCH

# Handle the _package directory based on CLEAN setting
if [ "$CLEAN" = "true" ]; then
  echo "---> Cleaning _package directory (CLEAN=true)"
  $SUDO_CMD rm -rf ../_package
fi

# Create _package directory (mkdir -p will not fail if directory already exists)
echo "---> Ensuring _package directory exists"
mkdir -p ../_package

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
$SUDO_CMD cp -rf _package/${PACKAGE}/* ../_package/

# Make sure to clean up any uncommited changes from patches
echo "---> Cleaning up repository"
git checkout $BRANCH
$SUDO_CMD cp -rf _javascripts/ ../_package/

git reset --hard HEAD
git clean -fd

# Clean up the temporary patch file if it exists
if [ -n "$PATCH_FILE" ] && [ -f "$PATCH_FILE" ]; then
  rm -f "$PATCH_FILE"
fi

# Clean up the temporary templates backup
if [ -d "/tmp/openshift_templates_backup" ]; then
  echo "---> Cleaning up templates backup"
  rm -rf /tmp/openshift_templates_backup
fi

cd ..
$SUDO_CMD rm -rf .docs_source
