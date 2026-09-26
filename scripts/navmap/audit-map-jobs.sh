#!/usr/bin/env bash
#
# Report job-to-category coverage for map distros.
#
# Usage:
#   scripts/navmap/audit-map-jobs.sh [FLAGS] [DISTRO ...]
#
# Flags (filter output — default shows all sections):
#   -m, --mapped           Show mapped jobs and their categories
#   -u, --unmapped         Show unmapped (uncategorised) jobs
#   -M, --multi            Show jobs that appear in multiple categories
#   -D, --duplicates       Show jobs included more than once in the same category
#   -s, --summary          Show only the summary table
#   -c, --category CAT     Filter to a specific category (repeatable)
#   -h, --help             Show this help
#
# Flags combine:  -Mu  shows multi-category + unmapped jobs.
# If no flags are given, all sections are shown.
#
# Examples:
#   scripts/navmap/audit-map-jobs.sh                                # all distros, full report
#   scripts/navmap/audit-map-jobs.sh ocp                            # OCP full report
#   scripts/navmap/audit-map-jobs.sh -M ocp                         # OCP multi-category only
#   scripts/navmap/audit-map-jobs.sh -D rosa-hcp osd                # duplicates across distros
#   scripts/navmap/audit-map-jobs.sh -u ocp                         # OCP unmapped jobs only
#   scripts/navmap/audit-map-jobs.sh -s                              # summary tables only
#   scripts/navmap/audit-map-jobs.sh -c disconnected-environments ocp  # single category
#   scripts/navmap/audit-map-jobs.sh -c develop -c extend ocp         # multiple categories

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUDIT_SCRIPT="$SCRIPT_DIR/audit-map-jobs.py"

if [[ ! -f "$AUDIT_SCRIPT" ]]; then
  echo "Error: audit-map-jobs.py not found in $SCRIPT_DIR." >&2
  exit 1
fi

if [[ ! -d maps ]]; then
  echo "Error: run this command from the repository root." >&2
  exit 1
fi

if ! command -v python3 &>/dev/null; then
  echo "Error: python3 is required but not found." >&2
  exit 1
fi

exec python3 "$AUDIT_SCRIPT" "$@"
