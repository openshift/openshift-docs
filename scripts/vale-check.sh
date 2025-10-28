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
#   --cqa:               Uses a temporary config with all AsciiDocDITA rules enabled.
#   --rule <Style.Rule>: Checks for only one specific rule (e.g., AsciiDocDITA.RelatedLinks).
#   --repo:              (Default) Uses the standard .vale.ini in the repository.
#   --help, -h:          Shows this help message.
#
# REQUIREMENTS:
#   - bash 3.2+
#   - git
#   - vale

# --- Version Check ---
if [ "${BASH_VERSINFO[0]}" -lt 3 ]; then
  echo "Error: This script requires bash 3.2 or higher." >&2
  echo "Current version: $BASH_VERSION" >&2
  exit 1
fi

# --- Global Configuration ---
set -u  # Treat unset variables as errors
set +e  # Don't exit script if vale finds errors

VALE_ARGS=()
ORIGINAL_VALE_INI=".vale.ini"

# --- Help Function ---
show_help() {
  echo "Usage: $0 <scope> [path] [--cqa|--repo] [--rule <Rule.Name>]"
  echo ""
  echo "A unified script to run Vale with different scopes and configurations."
  echo ""
  echo "SCOPES:"
  echo "  pr          Checks all files changed on the current branch (no path needed)."
  echo "  dir         Finds and checks all assemblies in a directory (grouped output)."
  echo "  assembly    Checks a single assembly file AND its included modules."
  echo ""
  echo "FLAGS:"
  echo "  --cqa         Uses a temporary config with AsciiDocDITA rules enabled."
  echo "  --repo        (Default) Uses the standard .vale.ini in the repository."
  echo "  --rule <Style.Rule> Checks for only one specific rule (e.g., AsciiDocDITA.RelatedLinks)."
  echo "  --help, -h    Shows this help message."
  echo ""
  echo "EXAMPLES:"
  echo "  $0 pr"
  echo "  $0 pr --cqa"
  echo "  $0 dir extensions/"
  echo "  $0 assembly extensions/my-assembly.adoc --cqa"
  echo "  $0 dir extensions/ --rule AsciiDocDITA.RelatedLinks"
}

# --- Setup Vale config and rule filtering ---
setup_vale_config_and_rule() {
  local use_cqa=$1
  local single_rule=$2
  local base_ini="$ORIGINAL_VALE_INI"
  local style_to_add=""

  if [ -n "$single_rule" ]; then
    style_to_add="${single_rule%%.*}"  # Extract style from rule
  fi

  if [ "$use_cqa" -eq 1 ]; then
    TEMP_VALE_INI=$(mktemp ./.vale.ini.temp.XXXXXX)
    sed 's/^\(BasedOnStyles = .*\)$/\1, AsciiDocDITA/' "$base_ini" > "$TEMP_VALE_INI"
    trap "rm -f '$TEMP_VALE_INI'" EXIT INT TERM
    VALE_ARGS=(--config "$TEMP_VALE_INI")

  elif [ -n "$style_to_add" ]; then
    if ! grep -q "BasedOnStyles.*$style_to_add" "$base_ini"; then
      TEMP_VALE_INI=$(mktemp ./.vale.ini.temp.XXXXXX)
      sed "s/^\(BasedOnStyles = .*\)$/\1, $style_to_add/" "$base_ini" > "$TEMP_VALE_INI"
      trap "rm -f '$TEMP_VALE_INI'" EXIT INT TERM
      VALE_ARGS=(--config "$TEMP_VALE_INI")
    else
      VALE_ARGS=()
    fi
  else
    VALE_ARGS=()
  fi

  if [ -n "$single_rule" ]; then
    VALE_ARGS+=(--filter=".Name=='$single_rule'")
  fi
}

# --- Scope: pr ---
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

# --- Scope: assembly ---
run_vale_assembly() {
  local assembly_file=$1
  if [ ! -f "$assembly_file" ]; then
    echo "Error: Assembly file not found: $assembly_file" >&2
    exit 1
  fi

  echo "--- Linting Assembly: $assembly_file ---"
  local assembly_output
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
  modules_output=$(printf '%s\n' "$FILTERED_MODULES" | xargs vale --output CLI "${VALE_ARGS[@]}")

  if [ -z "$modules_output" ]; then
    echo "✅ No issues found in modules."
  else
    echo "$modules_output"
  fi
}

# --- Scope: dir ---
run_vale_dir() {
  local scan_dir=$1
  if [ ! -d "$scan_dir" ]; then
    echo "Error: Directory not found: $scan_dir" >&2
    exit 1
  fi

  echo "Scanning $scan_dir for assemblies..."

  local -a ASSEMBLIES
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

# --- Main ---
if ! command -v vale >/dev/null 2>&1; then
  echo "Error: vale is not installed or not in PATH." >&2
  echo "Please install vale: https://vale.sh/docs/vale-cli/installation/" >&2
  exit 1
fi

USE_CQA=0
SINGLE_RULE=""
SCOPE=""
ARGS=()

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --cqa) USE_CQA=1; shift ;;
    --repo) USE_CQA=0; shift ;;
    --rule=*)
      SINGLE_RULE="${1#*=}"
      shift
      ;;
    --rule)
      if [[ -n "$2" && "${2:0:1}" != "-" ]]; then
        SINGLE_RULE="$2"
        shift 2
      else
        echo "Error: --rule requires a <Rule.Name> argument." >&2
        show_help
        exit 1
      fi
      ;;
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

setup_vale_config_and_rule "$USE_CQA" "$SINGLE_RULE"

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
