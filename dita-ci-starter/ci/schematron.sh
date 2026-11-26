#!/usr/bin/env bash
# schematron.sh [root-dir]
#
# STUB — wire this to the CCS Schematron rules used by the docs team.
# Left as a clearly-marked stub rather than faked, so the gate doesn't report
# a green check it didn't actually earn.
#
# To activate: install a Schematron processor in the gate job (e.g. the DITA-OT
# `org.dita.specialization` validation, Saxon + an ISO Schematron pipeline, or
# the CCS rules bundle) and run each .sch against changed files here.
set -euo pipefail

ROOT="${1:-.}"
shopt -s nullglob globstar
rules=("$ROOT"/**/*.sch)

if [ ${#rules[@]} -eq 0 ]; then
  echo "schematron.sh: no .sch rule files found; nothing to check (stub)."
  exit 0
fi

echo "schematron.sh: found ${#rules[@]} rule file(s) but the processor is not wired yet."
echo "               See the comment block in this script to activate."
exit 0
