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

if [ "${BASH_VERSINFO[0]}" -lt 3 ]; then
  echo "Error: This script requires bash 3.2 or higher." >&2
  echo "Current version: $BASH_VERSION" >&2
  exit 1
fi

set -u
set +e

VALE_ARGS=()
ORIGINAL_VALE_INI=".vale.ini"
TEMP_FILES=()

# Cleanup function for temp files
cleanup_temp_files() {
  for temp_file in "${TEMP_FILES[@]}"; do
    [ -f "$temp_file" ] && rm -f "$temp_file"
  done
}

# Set trap once for all cleanup
trap cleanup_temp_files EXIT INT TERM

show_help() {
  echo "Usage: $0 <scope> [path] [--cqa|--repo] [--rule <Rule.Name>]"
  echo ""
  echo "SCOPES:"
  echo "  pr          Checks all changed .adoc files on current branch"
  echo "  dir         Finds and checks assemblies in directory (grouped output)"
  echo "  assembly    Checks one assembly file and its modules"
  echo ""
  echo "FLAGS:"
  echo "  --cqa         Use temporary config with AsciiDocDITA style enabled"
  echo "  --repo        Use repository .vale.ini config (default)"
  echo "  --rule <Rule.Name>    Run only one specific Vale rule"
  echo "  --help, -h    Show this help message"
  echo ""
  echo "EXAMPLES:"
  echo "  $0 pr"
  echo "  $0 pr --cqa"
  echo "  $0 dir extensions/"
  echo "  $0 assembly path/to/file.adoc --rule AsciiDocDITA.RelatedLinks"
}

setup_vale_config_and_rule() {
  local use_cqa=$1
  local single_rule=$2
  local base_ini="$ORIGINAL_VALE_INI"
  local style_to_add=""

  if [ -n "$single_rule" ]; then
    style_to_add="${single_rule%%.*}"
  fi

  if [ "$use_cqa" -eq 1 ]; then
    # Cross-platform temp file creation
    TEMP_VALE_INI=$(mktemp "${TMPDIR:-.}/.vale.ini.temp.XXXXXX" 2>/dev/null || mktemp -t .vale.ini.temp)
    TEMP_FILES+=("$TEMP_VALE_INI")
    sed 's/^\(BasedOnStyles = .*\)$/\1, AsciiDocDITA/' "$base_ini" > "$TEMP_VALE_INI"
    VALE_ARGS=(--config "$TEMP_VALE_INI")

  elif [ -n "$style_to_add" ]; then
    if ! grep -q "BasedOnStyles.*$style_to_add" "$base_ini"; then
      # Cross-platform temp file creation
      TEMP_VALE_INI=$(mktemp "${TMPDIR:-.}/.vale.ini.temp.XXXXXX" 2>/dev/null || mktemp -t .vale.ini.temp)
      TEMP_FILES+=("$TEMP_VALE_INI")
      sed "s/^\(BasedOnStyles = .*\)$/\1, $style_to_add/" "$base_ini" > "$TEMP_VALE_INI"
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

run_vale_pr() {
  echo "Checking changed files on this branch..."

  if ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "Error: Not a git repo." >&2
    exit 1
  fi

  local upstream
  upstream=$(git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}' 2>/dev/null)

  if [ -z "$upstream" ]; then
    echo "Error: No upstream set. Please set with git branch --set-upstream-to=<remote>/<branch>" >&2
    exit 1
  fi

  local base
  base=$(git merge-base HEAD "$upstream")
  if [ -z "$base" ]; then
    echo "Error: Could not find merge base with $upstream." >&2
    exit 1
  fi

  if git diff --quiet --diff-filter=d "$base" HEAD; then
    echo "No changed files found."
    exit 0
  fi

  echo "Running Vale..."

  local output
  local changed_files
  changed_files=$(git diff -z --name-only --diff-filter=d "$base" HEAD)

  if [ -z "$changed_files" ]; then
    output=""
  else
    output=$(
      set -o pipefail
      printf '%s' "$changed_files" \
        | xargs -0 vale --output CLI --minAlertLevel=suggestion --no-exit "${VALE_ARGS[@]}" 2>/dev/null || true
    )
  fi

  if [ -z "$output" ]; then
    echo "✅ No issues found."
  else
    echo "$output"
  fi
}

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
  local modules
  modules=$(awk -F'::|\\[|]' '/^include::/ { print $2 }' "$assembly_file")

  if [ -z "$modules" ]; then
    echo "No modules found."
    return
  fi

  local filtered_modules
  filtered_modules=$(printf '%s\n' "$modules" | grep -v -E '(^|/)_')

  if [ -z "$filtered_modules" ]; then
    echo "All modules are partials (skipped)."
    return
  fi

  local repo_root
  repo_root=$(git rev-parse --show-toplevel)

  local missing_files=()
  local abs_modules=()
  while IFS= read -r module_path; do
    local clean_path="${module_path#./}"
    local full_path="$repo_root/$clean_path"
    if [ ! -f "$full_path" ]; then
      missing_files+=("$full_path")
    else
      abs_modules+=("$full_path")
    fi
  done <<< "$filtered_modules"

  if [ ${#missing_files[@]} -gt 0 ]; then
    echo "Warning: The following included module files do not exist:" >&2
    for missing_file in "${missing_files[@]}"; do
      echo "  $missing_file" >&2
    done
    echo "Continuing linting, ignoring missing includes." >&2
  fi

  if [ ${#abs_modules[@]} -eq 0 ]; then
    echo "No existing modules found to lint."
    return
  fi

  local modules_output
  if [ ${#abs_modules[@]} -gt 0 ]; then
    modules_output=$(printf '%s\n' "${abs_modules[@]}" | xargs vale --output CLI "${VALE_ARGS[@]}" 2>/dev/null || true)
  else
    modules_output=""
  fi

  if [ -z "$modules_output" ]; then
    echo "✅ No issues found in modules."
  else
    echo "$modules_output"
  fi
}

run_vale_dir() {
  local scan_dir=$1
  if [ ! -d "$scan_dir" ]; then
    echo "Error: Directory not found: $scan_dir" >&2
    exit 1
  fi

  echo "Scanning $scan_dir for assemblies..."

  local -a assemblies=()
  # Find .adoc files, exclude directories starting with _, then grep for assemblies
  local adoc_files
  adoc_files=$(find "$scan_dir" -type f -name "*.adoc" ! -path "*/_*" -print0 2>/dev/null)

  if [ -n "$adoc_files" ]; then
    while IFS= read -r line; do
      [ -n "$line" ] && assemblies+=("$line")
    done < <(printf '%s' "$adoc_files" | xargs -0 grep -l "^include::.*modules/" 2>/dev/null || true)
  fi

  if [ ${#assemblies[@]} -eq 0 ]; then
    echo "No assembly files found."
    exit 0
  fi

  echo "Found assemblies. Running grouped scans..."

  for assembly in "${assemblies[@]}"; do
    echo "====================================================================="
    echo "Checking Assembly and Modules: $assembly"
    echo "====================================================================="
    run_vale_assembly "$assembly"
    echo ""
  done
}

# Check required dependencies
if ! command -v vale >/dev/null 2>&1; then
  echo "Error: vale is not installed or not in PATH." >&2
  echo "Install: https://vale.sh/docs/vale-cli/installation/" >&2
  exit 1
fi

if ! command -v git >/dev/null 2>&1; then
  echo "Error: git is not installed or not in PATH." >&2
  exit 1
fi

if ! command -v awk >/dev/null 2>&1; then
  echo "Error: awk is not installed or not in PATH." >&2
  exit 1
fi

# Validate .vale.ini exists
if [ ! -f "$ORIGINAL_VALE_INI" ]; then
  echo "Error: Configuration file '$ORIGINAL_VALE_INI' not found." >&2
  echo "Please run this script from the repository root." >&2
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
        echo "Error: --rule requires <Rule.Name>." >&2
        show_help
        exit 1
      fi
      ;;
    --help|-h) show_help; exit 0 ;;
    -*) echo "Error: Unknown flag $1" >&2; show_help; exit 1 ;;
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
  echo "Error: No scope provided." >&2
  show_help
  exit 1
fi

setup_vale_config_and_rule "$USE_CQA" "$SINGLE_RULE"

case "$SCOPE" in
  pr)
    if [ ${#ARGS[@]} -ne 0 ]; then
      echo "Error: 'pr' scope takes no args." >&2
      show_help
      exit 1
    fi
    run_vale_pr
    ;;
  dir)
    if [ ${#ARGS[@]} -ne 1 ]; then
      echo "Error: 'dir' scope requires one directory arg." >&2
      show_help
      exit 1
    fi
    run_vale_dir "${ARGS[0]}"
    ;;
  assembly)
    if [ ${#ARGS[@]} -ne 1 ]; then
      echo "Error: 'assembly' scope requires one file arg." >&2
      show_help
      exit 1
    fi
    run_vale_assembly "${ARGS[0]}"
    ;;
  *)
    echo "Error: Unknown scope '$SCOPE'." >&2
    show_help
    exit 1
    ;;
esac
