#!/bin/bash
# Process AsciiDoc assembly files and update with :relfileprefix: changes

ASSEMBLIES=$(find . -type f -name '*.adoc' \
  ! -path './snippets/*' \
  ! -path './modules/*' \
  ! -path './_unused_topics/*' \
  ! -path './_preview/*' \
  ! -path './_attributes/*' \
  ! -path './microshift_rest_api/*' \
  ! -path './drupal-build/*' \
  ! -path './rest_api/*')

process_file() {
  local file="$1"
  echo "Processing $file"
  python scripts/update_for_relfileprefix.py "$file"
}

for file in $ASSEMBLIES; do
  if grep -q '^:_mod-docs-content-type: ASSEMBLY' "$file"; then
    process_file "$file"
  fi
done
