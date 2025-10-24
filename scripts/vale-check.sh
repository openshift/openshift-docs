#!/bin/bash
# shellcheck shell=bash

# A unified script to run Vale with different scopes and configurations.
#
# SCOPES:
#   pr:         Checks all .adoc files changed on the current branch.
#   dir:        Finds and checks all assemblies in a directory (grouped output).
#   assembly:   Checks a single assembly file AND its included modules.
#
# FLAGS:
#   --cqa:      Uses a temporary config with AsciiDocDITA rules enabled.
#   --repo:     (Default) Uses the standard .vale.ini in the repository.
#   --help, -h: Shows this help message.
#
# REQUIREMENTS:
#   - bash 3.2+
#   - git
#   - vale

# --- Version Check ---
# We check for Bash 3+ and rely on the read loop's
# compatibility back to Bash 3.2 (e.g., default macOS).
if [ "${BASH_VERSINFO[0]}" -lt 3 ]; then
  echo "Error: This script requires bash 3.2 or higher." >&2
  echo "Current version: $BASH_VERSION" >&2
  exit 1
fi

# --- Global Configuration ---
set -u  # Treat unset variables as errors
set +e  # Don't exit script if vale finds errors

# Use an array for Vale CLI arguments to avoid quoting/word-splitting pitfalls
VALE_ARGS=()
ORIGINAL_VALE_INI=".vale.ini"

# --- Help Function ---
show_help() {
  echo "Usage: $0 <scope> [path] [--cqa|--repo]"
  echo ""
  echo "A unified script to run Vale with different scopes and configurations."
  echo ""
  echo "SCOPES:"
  echo "  pr          Checks all files changed on the current branch (no path needed)."
  echo "  dir         Finds and checks all assemblies in a directory (grouped output)."
  echo "  assembly    Checks a single assembly file AND its included modules."
  echo ""
  echo "FLAGS:"
  echo "  --cqa       Uses a temporary config with AsciiDocDITA rules enabled."
  echo "  --repo      (Default) Uses the standard .vale.ini in the repository."
  echo "  --help, -h  Shows this help message."
  echo ""
  echo "EXAMPLES:"
  echo "  $0 pr"
  echo "  $0 pr --cqa"
  echo "  $0 dir extensions/"
  echo "  $0 assembly extensions/my-assembly.adoc --cqa"
}

# --- Config Function ---
# Sets VALE_ARGS based on the --cqa flag.
setup_vale_config() {
  local use_cqa=$1
  if [ "$use_cqa" -eq 1 ]; then
    if [ ! -f "$ORIGINAL_VALE_INI" ]; then
      echo "Error: $ORIGINAL_VALE_INI not found in current directory." >&2
      exit 1
    fi

    local TEMP_VALE_INI
    # Create the temp file in the CURRENT directory (./) so that
    # relative paths in the config (like StylesPath) resolve correctly.
    TEMP_VALE_INI=$(mktemp ./.vale.ini.temp.XXXXXX)
    
    if [ -z "$TEMP_VALE_INI" ]; then
      echo "Error: Could not create temporary config file." >&2
      exit 1
    fi

    sed 's/^\(BasedOnStyles = .*\)$/\1, AsciiDocDITA/' "$ORIGINAL_VALE_INI" > "$TEMP_VALE_INI"
    
    # Capture the actual path now, so cleanup works even after local scope ends.
    trap "rm -f '$TEMP_VALE_INI'" EXIT INT TERM

    VALE_ARGS=(--config "$TEMP_VALE_INI")
    echo "Using temporary CQA config ($TEMP_VALE_INI)..."
  else
    VALE_ARGS=()
    echo "Using default .vale.ini config..."
  fi
}

# --- Scope Function: pr ---
run_vale_pr() {
  echo "Checking all changed files on this branch..."

  if ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "Error: Not in a git repository." >&2
    exit 1
  fi

  local UPSTREAM_BRANCH
  UPSTREAM_BRANCH=$(git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}' 2>/dev/null)

  if [ -z "$UPSTREAM_BRANCH" ]; then
    echo "Error: No upstream branch configured for the current branch." >&2
    echo "Please set one with: git branch --set-upstream-to=<remote>/<branch>" >&2
    exit 1
  fi
  echo "Finding common ancestor with '$UPSTREAM_BRANCH'..."

  local MERGE_BASE
  MERGE_BASE=$(git merge-base HEAD "$UPSTREAM_BRANCH")
  if [ -z "$MERGE_BASE" ]; then
    echo "Error: Could not find a common merge base with '$UPSTREAM_BRANCH'." >&2
    exit 1
  fi

  if git diff --quiet --diff-filter=d "$MERGE_BASE" HEAD; then
    echo "No changed files found on this branch."
    exit 0
  fi

  echo "Running Vale..."
  
  local output
  output=$( (
    set -o pipefail
    git diff -z --name-only --diff-filter=d "$MERGE_BASE" HEAD \
      | xargs -0 vale --output CLI --minAlertLevel=suggestion --no-exit "${VALE_ARGS[@]}"
  ) )
  
  if [ -z "$output" ]; then
    echo "✅ No issues found in changed files."
  else
    echo "$output"
  fi
}

# --- Scope Function: assembly ---
run_vale_assembly() {
  local assembly_file=$1
  if [ ! -f "$assembly_file" ]; then
    echo "Error: Assembly file not found: $assembly_file" >&2
    exit 1
  fi

  echo "--- Linting Assembly: $assembly_file ---"
  local assembly_output
  # Use --output CLI for cleaner, grouped results
  assembly_output=$(vale --output CLI "${VALE_ARGS[@]}" "$assembly_file")
  
  if [ -z "$assembly_output" ]; then
    echo "✅ No issues found."
  else
    echo "$assembly_output"
  fi
  echo ""

  echo "--- Linting Modules from $assembly_file ---"
  local MODULES
  MODULES=$(awk -F'::|\\[|]' '/^include::/ { print $2 }' "$assembly_file")

  if [ -z "$MODULES" ]; then
    echo "No modules found to lint."
    return
  fi

  local FILTERED_MODULES
  FILTERED_MODULES=$(printf '%s\n' "$MODULES" | grep -v -E '(^|/)_' || true)
  
  if [ -z "$FILTERED_MODULES" ]; then
    echo "All modules are partials (skipped)."
    return
  fi

  local modules_output
  # Use --output CLI for cleaner, grouped results
  modules_output=$(printf '%s\n' "$FILTERED_MODULES" | xargs vale --output CLI "${VALE_ARGS[@]}")
  
  if [ -z "$modules_output" ]; then
    echo "✅ No issues found in modules."
  else
    echo "$modules_output"
  fi
}

# --- Scope Function: dir (replaces 'assemblies') ---
run_vale_dir() {
  local scan_dir=$1
  if [ ! -d "$scan_dir" ]; then
    echo "Error: Directory not found: $scan_dir" >&2
    exit 1
  fi

  echo "Scanning $scan_dir for assemblies..."

  local -a ASSEMBLIES
  # Use the universally compatible while-read loop
  while IFS= read -r line; do
    ASSEMBLIES+=("$line")
  done < <(find "$scan_dir" \
    \( -type d -name "_*" -prune \) \
    -o \
    \( -type f -name "*.adoc" -exec grep -lq "^include::.*modules/" {} \; -print \))

  if [ ${#ASSEMBLIES[@]} -eq 0 ]; then
    echo "No assembly files (containing 'include::...modules/...') found in $scan_dir."
    exit 0
  fi

  echo "Found assemblies. Running grouped Vale scan..."
  for assembly in "${ASSEMBLIES[@]}"; do
    echo "====================================================================="
    echo "Checking Assembly and its Modules: $assembly"
    echo "====================================================================="
    run_vale_assembly "$assembly"
    echo ""
  done
}

# --- Main Script Logic ---

if ! command -v vale >/dev/null 2>&1; then
  echo "Error: vale is not installed or not in PATH." >&2
  echo "Please install vale: https://vale.sh/docs/vale-cli/installation/" >&2
  exit 1
fi

USE_CQA=0
SCOPE=""
ARGS=()

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --cqa) USE_CQA=1; shift ;;
    --repo) USE_CQA=0; shift ;;
    --help|-h) show_help; exit 0 ;;
    -*) echo "Error: Unknown flag $1"; show_help; exit 1 ;;
    *)
      if [ -z "$SCOPE" ]; then
        SCOPE="$1"
      else
        ARGS+=("$1")
      fi
      shift
      ;;
  esac
done

if [ -z "$SCOPE" ]; then
  echo "Error: No scope (pr, dir, assembly) provided." >&2
  show_help
  exit 1
fi

setup_vale_config "$USE_CQA"

case "$SCOPE" in
  pr)
    if [ ${#ARGS[@]} -ne 0 ]; then
      echo "Error: 'pr' scope takes no path arguments." >&2
      show_help; exit 1
    fi
    run_vale_pr
    ;;
  dir)
    if [ ${#ARGS[@]} -ne 1 ]; then
      echo "Error: 'dir' scope requires one directory path." >&2
      show_help; exit 1
    fi
    run_vale_dir "${ARGS[0]}"
    ;;
  assembly)
    if [ ${#ARGS[@]} -ne 1 ]; then
      echo "Error: 'assembly' scope requires one file path." >&2
      show_help; exit 1
    fi
    run_vale_assembly "${ARGS[0]}"
    ;;
  *)
    echo "Error: Unknown scope '$SCOPE'." >&2
    show_help
    exit 1
    ;;
esac
