#!/bin/bash
# shellcheck shell=bash

################################################################################
# vale-check.sh - A unified Vale linter script with multiple scopes
#
# This script runs Vale (a linting tool) on AsciiDoc documentation with
# different scopes and configurations. It supports checking changed files,
# directories, or individual assemblies with their modules.
#
# SCOPES:
#   pr:       Checks all .adoc files changed on the current branch
#   dir:      Finds and checks all assemblies in a directory (grouped output)
#   assembly: Checks a single assembly file AND its included modules
#
# FLAGS:
#   --cqa:               Uses a temporary config with all AsciiDocDITA rules enabled
#   --style <StyleName>: Enables a specific style package (e.g., AsciiDocDITA, RedHat)
#   --rule <Style.Rule>: Checks for only one specific rule (e.g., AsciiDocDITA.RelatedLinks)
#   --level <level>:     Filter output by severity: 'error', 'warning', or 'all' (default: all)
#   --repo:              (Default) Uses the standard .vale.ini in the repository
#   --help, -h:          Shows this help message
#
# REQUIREMENTS:
#   - bash 3.2+
#   - git
#   - vale
#   - awk
################################################################################

#===============================================================================
# BASH VERSION CHECK
#===============================================================================

if [ "${BASH_VERSINFO[0]}" -lt 3 ]; then
  echo "Error: This script requires bash 3.2 or higher." >&2
  echo "Current version: $BASH_VERSION" >&2
  exit 1
fi

# Exit on unset variables; don't exit on command failures (we handle errors)
set -u
set +e

#===============================================================================
# GLOBAL VARIABLES
#===============================================================================

# Vale command-line arguments (built dynamically based on flags)
VALE_ARGS=()

# Path to the repository's Vale configuration file
ORIGINAL_VALE_INI=".vale.ini"

# Array to track temporary files for cleanup
TEMP_FILES=()

# User-specified options (set during argument parsing)
USE_CQA=0                    # Whether to use CQA (AsciiDocDITA) mode
SINGLE_RULE=""               # Specific rule to check (e.g., "AsciiDocDITA.RelatedLinks")
STYLE_TO_ADD=""              # Custom style to enable (e.g., "RedHat")
ALERT_LEVEL="suggestion"     # Minimum alert level (error, warning, suggestion)
SCOPE=""                     # Scope of the check (pr, dir, assembly)
ARGS=()                      # Additional positional arguments

#===============================================================================
# CLEANUP AND ERROR HANDLING
#===============================================================================

# cleanup_temp_files - Removes all temporary files created during execution
#
# This function is called automatically on script exit (via trap). It removes
# any temporary .vale.ini files created when using --cqa, --style, or --rule.
cleanup_temp_files() {
  for temp_file in "${TEMP_FILES[@]}"; do
    [ -f "$temp_file" ] && rm -f "$temp_file"
  done
}

# Register cleanup function to run on script exit, interrupt, or termination
trap cleanup_temp_files EXIT INT TERM

#===============================================================================
# HELP AND DOCUMENTATION
#===============================================================================

# show_help - Displays usage information and examples
show_help() {
  echo "Usage: $0 <scope> [path] [flags]"
  echo ""
  echo "SCOPES:"
  echo "  pr          Checks all changed .adoc files on current branch"
  echo "  dir         Finds and checks assemblies in directory (grouped output)"
  echo "  assembly    Checks one assembly file and its modules"
  echo ""
  echo "FLAGS:"
  echo "  --cqa                 Use temporary config with AsciiDocDITA style enabled"
  echo "  --style <StyleName>   Enable a specific style package (e.g., AsciiDocDITA, RedHat)"
  echo "  --rule <Rule.Name>    Run only one specific Vale rule (e.g., AsciiDocDITA.RelatedLinks)"
  echo "  --level <level>       Filter output: 'error', 'warning', or 'all' (default: all)"
  echo "  --repo                Use repository .vale.ini config (default)"
  echo "  --help, -h            Show this help message"
  echo ""
  echo "EXAMPLES:"
  echo "  $0 pr"
  echo "  $0 pr --cqa"
  echo "  $0 pr --level error"
  echo "  $0 dir extensions/ --style RedHat"
  echo "  $0 assembly path/to/file.adoc --rule AsciiDocDITA.RelatedLinks"
  echo "  $0 pr --style AsciiDocDITA --level warning"
}

#===============================================================================
# CONFIGURATION SETUP
#===============================================================================

# setup_vale_config_and_rule - Configures Vale arguments based on user flags
#
# This function determines which Vale configuration to use and builds the
# VALE_ARGS array. It handles:
#   1. Adding styles to BasedOnStyles (via temp config file)
#   2. Filtering to a single rule (via --filter)
#
# Args:
#   $1 - use_cqa: 1 to enable AsciiDocDITA style, 0 otherwise
#   $2 - single_rule: Specific rule name to filter (empty if not specified)
#   $3 - custom_style: Custom style to enable (empty if not specified)
#
# Side effects:
#   - Modifies global VALE_ARGS array
#   - May create temporary .vale.ini file (tracked in TEMP_FILES)
setup_vale_config_and_rule() {
  local use_cqa=$1
  local single_rule=$2
  local custom_style=$3
  local base_ini="$ORIGINAL_VALE_INI"
  local style_to_add=""

  # Determine which style needs to be added (priority order matters)
  if [ "$use_cqa" -eq 1 ]; then
    # --cqa flag: Enable AsciiDocDITA
    style_to_add="AsciiDocDITA"
  elif [ -n "$custom_style" ]; then
    # --style flag: Enable user-specified style
    style_to_add="$custom_style"
  elif [ -n "$single_rule" ]; then
    # --rule flag: Extract and enable the style from the rule name
    # (e.g., "AsciiDocDITA.RelatedLinks" -> "AsciiDocDITA")
    style_to_add="${single_rule%%.*}"
  fi

  # Create a temporary config file if we need to add a style
  if [ -n "$style_to_add" ]; then
    # Check if the style is already in the base config
    if ! grep -q "BasedOnStyles.*$style_to_add" "$base_ini"; then
      # Style not present: create temp config with style added
      # Note: Created in repo root so Vale can find styles/ and config/ directories
      TEMP_VALE_INI=$(mktemp .vale.ini.temp.XXXXXX)
      TEMP_FILES+=("$TEMP_VALE_INI")

      # Use sed to append the style to the BasedOnStyles line
      sed "s/^\(BasedOnStyles = .*\)$/\1, $style_to_add/" "$base_ini" > "$TEMP_VALE_INI"
      VALE_ARGS=(--config "$TEMP_VALE_INI")
    else
      # Style already present: use default config
      VALE_ARGS=()
    fi
  else
    # No style to add: use default config
    VALE_ARGS=()
  fi

  # Add rule filter if a specific rule was requested
  if [ -n "$single_rule" ]; then
    # Vale's --filter uses jq-style queries to filter alerts
    VALE_ARGS+=(--filter=".Name=='$single_rule'")
  fi
}

#===============================================================================
# VALE EXECUTION HELPERS
#===============================================================================

# run_vale - Executes Vale with consistent arguments and output handling
#
# This is a wrapper function that runs Vale with the configured arguments
# (from VALE_ARGS) and the user-specified alert level (from ALERT_LEVEL).
#
# Args:
#   $@ - Files or paths to lint
#
# Returns:
#   Vale output (may be empty if no issues found)
run_vale() {
  vale --output CLI --minAlertLevel="$ALERT_LEVEL" "${VALE_ARGS[@]}" "$@" 2>/dev/null || true
}

# display_output - Shows Vale results with consistent formatting
#
# Args:
#   $1 - output: Vale output to display (may be empty)
#   $2 - context: Description of what was checked (e.g., "Assembly", "modules")
display_output() {
  local output="$1"
  local context="${2:-files}"

  if [ -z "$output" ]; then
    echo "✅ No issues found${context:+ in $context}."
  else
    echo "$output"
  fi
}

#===============================================================================
# MODULE EXTRACTION AND RESOLUTION
#===============================================================================

# extract_module_paths - Extracts module paths from an assembly file
#
# Parses an assembly file for include:: directives and extracts the module paths.
# Filters out partials (files/directories starting with underscore).
#
# Args:
#   $1 - assembly_file: Path to the assembly file
#
# Returns:
#   Newline-separated list of module paths (may be empty)
extract_module_paths() {
  local assembly_file="$1"

  # Use awk to parse include:: directives
  # Field separator handles: include::path/to/file.adoc[] or include::path[options]
  local modules
  modules=$(awk -F'::|\\[|]' '/^include::/ { print $2 }' "$assembly_file")

  # Filter out partials (paths containing /_  or starting with _)
  if [ -n "$modules" ]; then
    printf '%s\n' "$modules" | grep -v -E '(^|/)_' || true
  fi
}

# resolve_module_paths - Converts relative module paths to absolute paths
#
# Takes a list of relative module paths and converts them to absolute paths
# relative to the repository root. Separates existing files from missing files.
#
# Args:
#   $1 - filtered_modules: Newline-separated list of module paths
#
# Outputs:
#   Sets global arrays (via named references would be better, but bash 3.2 compatible):
#   - abs_modules: Array of absolute paths to existing files
#   - missing_files: Array of absolute paths to missing files
resolve_module_paths() {
  local filtered_modules="$1"
  local repo_root
  repo_root=$(git rev-parse --show-toplevel)

  # Reset arrays
  missing_files=()
  abs_modules=()

  # Process each module path
  while IFS= read -r module_path; do
    [ -z "$module_path" ] && continue

    # Remove leading ./ if present
    local clean_path="${module_path#./}"
    local full_path="$repo_root/$clean_path"

    # Separate existing vs missing files
    if [ ! -f "$full_path" ]; then
      missing_files+=("$full_path")
    else
      abs_modules+=("$full_path")
    fi
  done <<< "$filtered_modules"
}

#===============================================================================
# SCOPE EXECUTION FUNCTIONS
#===============================================================================

# run_vale_pr - Checks all changed .adoc files on the current branch
#
# This scope compares the current branch against its upstream and runs Vale
# on all changed .adoc files. Useful for PR/MR validation.
run_vale_pr() {
  echo "Checking changed files on this branch..."

  # Verify we're in a git repository
  if ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "Error: Not a git repo." >&2
    exit 1
  fi

  # Get the upstream branch for comparison
  local upstream
  upstream=$(git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}' 2>/dev/null)

  if [ -z "$upstream" ]; then
    echo "Error: No upstream set. Please set with git branch --set-upstream-to=<remote>/<branch>" >&2
    exit 1
  fi

  # Find the merge base (common ancestor) with upstream
  local base
  base=$(git merge-base HEAD "$upstream")
  if [ -z "$base" ]; then
    echo "Error: Could not find merge base with $upstream." >&2
    exit 1
  fi

  # Check if there are any changed files
  if git diff --quiet --diff-filter=d "$base" HEAD; then
    echo "No changed files found."
    exit 0
  fi

  echo "Running Vale..."

  # Get changed files (null-separated for safety with special characters)
  local changed_files
  changed_files=$(git diff -z --name-only --diff-filter=d "$base" HEAD)

  # Run Vale on changed files
  local output
  if [ -z "$changed_files" ]; then
    output=""
  else
    output=$(
      set -o pipefail
      printf '%s' "$changed_files" | xargs -0 run_vale --no-exit
    )
  fi

  display_output "$output"
}

# run_vale_assembly - Checks an assembly file and all its included modules
#
# This scope lints both the assembly file itself and all modules it includes.
# It provides separate output for the assembly and modules, and warns about
# missing module files.
#
# Args:
#   $1 - assembly_file: Path to the assembly file
run_vale_assembly() {
  local assembly_file="$1"

  # Validate assembly file exists
  if [ ! -f "$assembly_file" ]; then
    echo "Error: Assembly file not found: $assembly_file" >&2
    exit 1
  fi

  # --- Lint the assembly file itself ---
  echo "--- Linting Assembly: $assembly_file ---"
  local assembly_output
  assembly_output=$(run_vale "$assembly_file")
  display_output "$assembly_output"
  echo ""

  # --- Extract and lint included modules ---
  echo "--- Linting Modules from $assembly_file ---"

  # Extract module paths from include:: directives
  local filtered_modules
  filtered_modules=$(extract_module_paths "$assembly_file")

  if [ -z "$filtered_modules" ]; then
    echo "No modules found."
    return
  fi

  # Resolve module paths to absolute paths
  local missing_files abs_modules
  resolve_module_paths "$filtered_modules"

  # Warn about missing module files
  if [ ${#missing_files[@]} -gt 0 ]; then
    echo "Warning: The following included module files do not exist:" >&2
    for missing_file in "${missing_files[@]}"; do
      echo "  $missing_file" >&2
    done
    echo "Continuing linting, ignoring missing includes." >&2
  fi

  # Lint existing modules
  if [ ${#abs_modules[@]} -eq 0 ]; then
    echo "No existing modules found to lint."
    return
  fi

  local modules_output
  modules_output=$(run_vale "${abs_modules[@]}")
  display_output "$modules_output" "modules"
}

# run_vale_dir - Finds and checks all assemblies in a directory
#
# This scope recursively finds all assembly files in a directory and runs
# the assembly scope on each one. Assemblies are identified by the presence
# of "include::.*modules/" directives.
#
# Args:
#   $1 - scan_dir: Directory to scan for assemblies
run_vale_dir() {
  local scan_dir="$1"

  # Validate directory exists
  if [ ! -d "$scan_dir" ]; then
    echo "Error: Directory not found: $scan_dir" >&2
    exit 1
  fi

  echo "Scanning $scan_dir for assemblies..."

  # Find all .adoc files, excluding paths with underscore directories (partials)
  # Then filter for assemblies (files containing "include::.*modules/")
  local -a assemblies=()
  while IFS= read -r -d '' file; do
    if grep -q "^include::.*modules/" "$file" 2>/dev/null; then
      assemblies+=("$file")
    fi
  done < <(find "$scan_dir" -type f -name "*.adoc" ! -path "*/_*" -print0 2>/dev/null)

  # Check if any assemblies were found
  if [ ${#assemblies[@]} -eq 0 ]; then
    echo "No assembly files found."
    exit 0
  fi

  echo "Found ${#assemblies[@]} assemblies. Running grouped scans..."
  echo ""

  # Run assembly scope on each found assembly
  for assembly in "${assemblies[@]}"; do
    echo "====================================================================="
    echo "Checking Assembly and Modules: $assembly"
    echo "====================================================================="
    run_vale_assembly "$assembly"
    echo ""
  done
}

#===============================================================================
# DEPENDENCY VALIDATION
#===============================================================================

# Check for required command-line tools
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

# Validate .vale.ini exists in current directory
if [ ! -f "$ORIGINAL_VALE_INI" ]; then
  echo "Error: Configuration file '$ORIGINAL_VALE_INI' not found." >&2
  echo "Please run this script from the repository root." >&2
  exit 1
fi

#===============================================================================
# ARGUMENT PARSING
#===============================================================================

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --cqa)
      # Enable CQA mode (AsciiDocDITA style)
      USE_CQA=1
      shift
      ;;
    --repo)
      # Explicitly use repository config (default behavior)
      USE_CQA=0
      shift
      ;;
    --rule=*)
      # Parse --rule=RuleName format
      SINGLE_RULE="${1#*=}"
      shift
      ;;
    --rule)
      # Parse --rule RuleName format
      if [[ -n "$2" && "${2:0:1}" != "-" ]]; then
        SINGLE_RULE="$2"
        shift 2
      else
        echo "Error: --rule requires <Rule.Name>." >&2
        show_help
        exit 1
      fi
      ;;
    --style=*)
      # Parse --style=StyleName format
      STYLE_TO_ADD="${1#*=}"
      shift
      ;;
    --style)
      # Parse --style StyleName format
      if [[ -n "$2" && "${2:0:1}" != "-" ]]; then
        STYLE_TO_ADD="$2"
        shift 2
      else
        echo "Error: --style requires <StyleName>." >&2
        show_help
        exit 1
      fi
      ;;
    --level=*)
      # Parse --level=error format
      ALERT_LEVEL="${1#*=}"
      shift
      ;;
    --level)
      # Parse --level error format
      if [[ -n "$2" && "${2:0:1}" != "-" ]]; then
        ALERT_LEVEL="$2"
        shift 2
      else
        echo "Error: --level requires error|warning|all." >&2
        show_help
        exit 1
      fi
      ;;
    --help|-h)
      show_help
      exit 0
      ;;
    -*)
      # Unknown flag
      echo "Error: Unknown flag $1" >&2
      show_help
      exit 1
      ;;
    *)
      # Positional arguments: first is scope, rest are args
      if [ -z "$SCOPE" ]; then
        SCOPE="$1"
      else
        ARGS+=("$1")
      fi
      shift
      ;;
  esac
done

#===============================================================================
# VALIDATION AND SETUP
#===============================================================================

# Ensure a scope was provided
if [ -z "$SCOPE" ]; then
  echo "Error: No scope provided." >&2
  show_help
  exit 1
fi

# Validate and normalize alert level
# User specifies "all" but Vale uses "suggestion" for all levels
case "$ALERT_LEVEL" in
  error)
    ALERT_LEVEL="error"
    ;;
  warning)
    ALERT_LEVEL="warning"
    ;;
  all|suggestion)
    ALERT_LEVEL="suggestion"
    ;;
  *)
    echo "Error: --level must be 'error', 'warning', or 'all'." >&2
    exit 1
    ;;
esac

# Configure Vale arguments based on flags
setup_vale_config_and_rule "$USE_CQA" "$SINGLE_RULE" "$STYLE_TO_ADD"

#===============================================================================
# SCOPE EXECUTION
#===============================================================================

# Execute the appropriate scope function
case "$SCOPE" in
  pr)
    # PR scope: no additional arguments required
    if [ ${#ARGS[@]} -ne 0 ]; then
      echo "Error: 'pr' scope takes no args." >&2
      show_help
      exit 1
    fi
    run_vale_pr
    ;;
  dir)
    # Directory scope: requires one directory path
    if [ ${#ARGS[@]} -ne 1 ]; then
      echo "Error: 'dir' scope requires one directory arg." >&2
      show_help
      exit 1
    fi
    run_vale_dir "${ARGS[0]}"
    ;;
  assembly)
    # Assembly scope: requires one assembly file path
    if [ ${#ARGS[@]} -ne 1 ]; then
      echo "Error: 'assembly' scope requires one file arg." >&2
      show_help
      exit 1
    fi
    run_vale_assembly "${ARGS[0]}"
    ;;
  *)
    # Unknown scope
    echo "Error: Unknown scope '$SCOPE'." >&2
    show_help
    exit 1
    ;;
esac
