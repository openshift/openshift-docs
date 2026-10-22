#!/usr/bin/env bash
# linkcheck.sh [root-dir]
#
# Fails if any on-disk href/conref target does not exist. Run against the
# RESOLVED output (.validate-out / out/normalized), not raw source, so that
# keyref/conkeyref are already resolved to real files and don't need checking.
#
# External links (http/https/mailto) and same-file fragments (#id) are skipped
# here on purpose — external liveness is flaky in a merge gate; run it on a
# schedule instead (see README).
set -euo pipefail

ROOT="${1:-.}"
broken="$(mktemp)"
trap 'rm -f "$broken"' EXIT

while IFS= read -r -d '' file; do
  dir="$(dirname "$file")"
  # Only href/conref carry file paths. keyref/conkeyref use keys (already
  # resolved in normalized output), so we don't path-check them.
  # `|| true`: a file with no matches makes grep exit 1, which under
  # `set -o pipefail` would otherwise abort the whole run.
  { grep -oE '(href|conref)="[^"]+"' "$file" 2>/dev/null || true; } \
    | sed -E 's/.*="([^"]+)".*/\1/' \
    | while IFS= read -r ref; do
        case "$ref" in
          http://*|https://*|mailto:*|'#'*|'') continue ;;
        esac
        path="${ref%%#*}"            # strip fragment
        [ -z "$path" ] && continue
        [ -e "$dir/$path" ] || echo "BROKEN: $file -> $ref" >> "$broken"
      done
done < <(find "$ROOT" \( -name '*.dita' -o -name '*.ditamap' \) -print0)

if [ -s "$broken" ]; then
  echo "Broken references found:"
  sort -u "$broken"
  exit 1
fi
echo "Link check passed."
