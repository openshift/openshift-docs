#!/usr/bin/env bash
#
# Build a local, multi-page HTML preview from maps/<distro>/navigation.adoc.
#

set -euo pipefail

usage() {
  cat <<'EOF'
Usage: scripts/navmap/preview-map.sh [DISTRO...] [-o OUTPUT]
   or: scripts/navmap/preview-map.sh [-d DISTRO] [-o OUTPUT]

  DISTRO         Distro(s) under maps/ to preview (default: all distros)
  -d, --distro   Distro under maps/ to preview (repeatable)
  -o, --output   Output directory (default: _preview/map-preview)
  -h, --help     Show this help

Examples:
  scripts/navmap/preview-map.sh ocp
  scripts/navmap/preview-map.sh rosa-classic rosa-hcp
  scripts/navmap/preview-map.sh -d ocp -o /tmp/preview

Renders maps/<distro>/navigation.adoc with Asciidoctor multipage_html5,
adding a left navigation and a right-hand on-this-page navigation.
EOF
  exit "${1:-2}"
}

DISTROS=()
OUTPUT="_preview/map-preview"

while [[ $# -gt 0 ]]; do
  case "$1" in
    -d|--distro)
      if [[ -z "${2:-}" || "${2:-}" == -* ]]; then
        echo "Error: $1 requires a distro value." >&2
        usage 2
      fi
      DISTROS+=("$2")
      shift 2
      ;;
    -o|--output)
      if [[ -z "${2:-}" || "${2:-}" == -* ]]; then
        echo "Error: $1 requires an output directory." >&2
        usage 2
      fi
      OUTPUT="$2"
      shift 2
      ;;
    -h|--help)   usage 0 ;;
    -*)          echo "Unknown option: $1" >&2; usage 2 ;;
    *)           DISTROS+=("$1"); shift ;;
  esac
done

if [[ ! -d maps ]]; then
  echo "Error: run this command from the repository root." >&2
  exit 1
fi

if ! ruby -e "require 'asciidoctor-multipage'" 2>/dev/null; then
  echo "Error: asciidoctor-multipage is not installed." >&2
  echo "Install it with: gem install asciidoctor-multipage" >&2
  exit 1
fi

if [[ ${#DISTROS[@]} -eq 0 ]]; then
  for navigation in maps/*/navigation.adoc; do
    [[ -f "$navigation" ]] || continue
    DISTROS+=("$(basename "$(dirname "$navigation")")")
  done
fi

if [[ ${#DISTROS[@]} -eq 0 ]]; then
  echo "Error: no maps/<distro>/navigation.adoc files found." >&2
  exit 1
fi

for distro in "${DISTROS[@]}"; do
  if [[ ! -f "maps/$distro/navigation.adoc" ]]; then
    echo "Error: maps/$distro/navigation.adoc not found." >&2
    exit 1
  fi
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUDIT_SCRIPT="$SCRIPT_DIR/audit-map-includes.py"

preflight_dir="$(mktemp -d "${TMPDIR:-/tmp}/navmap-preflight.XXXXXX")"
trap 'rm -rf -- "$preflight_dir"' EXIT
declare -A preflight_failed_distros
any_preflight_failed=0
: > "$preflight_dir/all.txt"

if [[ -x "$AUDIT_SCRIPT" ]] || [[ -f "$AUDIT_SCRIPT" ]]; then
  for distro in "${DISTROS[@]}"; do
    navigation="maps/$distro/navigation.adoc"
    report="$preflight_dir/$distro.txt"
    if ! python3 "$AUDIT_SCRIPT" "$navigation" > "$report" 2>&1; then
      preflight_failed_distros[$distro]=1
      any_preflight_failed=1
      cat "$report" >> "$preflight_dir/all.txt"
    fi
    cat "$report"
  done

  if [[ "$any_preflight_failed" -eq 1 ]]; then
    echo "WARNING: building an incomplete preview; missing-content warnings will be added to the HTML." >&2
  fi
else
  echo "INFO: audit-map-includes.py not found; skipping include preflight audit." >&2
fi

if [[ -e "$OUTPUT" ]]; then
  if [[ -L "$OUTPUT" ]]; then
    echo "Error: refusing to remove a symlink output path: $OUTPUT" >&2
    exit 1
  fi
  if [[ ! -f "$OUTPUT/.navmap-preview-output" ]]; then
    echo "Error: refusing to remove an output directory without the preview marker: $OUTPUT" >&2
    echo "Choose a new output path or remove that directory manually." >&2
    exit 1
  fi
  rm -rf -- "$OUTPUT"
fi
mkdir -p "$OUTPUT"
touch "$OUTPUT/.navmap-preview-output"

for distro in "${DISTROS[@]}"; do
  navigation="maps/$distro/navigation.adoc"
  destination="$OUTPUT/$distro"
  mkdir -p "$destination"
  echo "Rendering $navigation -> $destination"
  asciidoctor -r asciidoctor-multipage -b multipage_html5 \
    "$navigation" \
    -D "$destination" \
    -a toc=left \
    -a doctype=book \
    -a toclevels=2 \
    -a docinfo=shared-footer \
    -a multipage-level=2

  python3 "$SCRIPT_DIR/right-toc.py" "$destination"
  python3 - "$destination" <<'PY'
import sys
from pathlib import Path

destination = Path(sys.argv[1])
(destination / "index.html").write_text(
    '<!doctype html><html><head><meta charset="utf-8">'
    '<meta http-equiv="refresh" content="0; url=navigation.html">'
    '<link rel="canonical" href="navigation.html">'
    '<title>Map preview</title></head><body>'
    '<p><a href="navigation.html">Open the navigation map</a></p>'
    '</body></html>\n',
    encoding="utf-8",
)
PY
  if [[ -n "${preflight_failed_distros[$distro]:-}" ]]; then
    python3 "$SCRIPT_DIR/preview-warning.py" "$destination" "$preflight_dir/$distro.txt"
  fi
done

python3 - "$OUTPUT" "${DISTROS[@]}" <<'PY'
import html, sys
from pathlib import Path

output = Path(sys.argv[1])
distros = sys.argv[2:]
links = "\n".join(
    f'<li><a href="{html.escape(d, quote=True)}/navigation.html">'
    f'{html.escape(d)}</a></li>'
    for d in distros
)
(output / "index.html").write_text(
    "<!doctype html><html><head><meta charset=\"utf-8\"><title>Map preview</title>"
    "<style>body{font-family:sans-serif;max-width:42em;margin:3em auto;padding:0 1em}"
    "li{line-height:2}</style></head><body><h1>Map preview</h1><ul>"
    + links + "</ul></body></html>\n",
    encoding="utf-8",
)
PY

if [[ "$any_preflight_failed" -eq 1 ]] && [[ -s "$preflight_dir/all.txt" ]]; then
  python3 "$SCRIPT_DIR/preview-warning.py" "$OUTPUT" "$preflight_dir/all.txt"
fi

echo "Preview written to $OUTPUT"
