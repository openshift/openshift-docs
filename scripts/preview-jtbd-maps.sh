#!/usr/bin/env bash
#
# Build a local, multi-page preview of a JTBD navigation map.
#
# This is deliberately local and read-only. It uses the same Asciidoctor
# multipage approach as preview-maps.sh, then adds a right-hand, page-local
# table of contents to each generated page.
#

set -euo pipefail

usage() {
  cat <<'EOF'
Usage: scripts/preview-jtbd-maps.sh [-d DISTRO] [-o OUTPUT]

  -d, --distro   Distro under maps/ to preview (default: all distros)
  -o, --output   Output directory (default: build/jtbd-preview)
  -h, --help     Show this help

The command renders maps/<distro>/navigation.adoc with Asciidoctor
multipage_html5, preserving the left navigation and adding a right-hand
on-this-page navigation to generated pages that contain headings.
EOF
  exit "${1:-0}"
}

DISTROS=()
OUTPUT="build/jtbd-preview"

while [[ $# -gt 0 ]]; do
  case "$1" in
    -d|--distro)
      [[ $# -ge 2 ]] || usage
      DISTROS+=("$2")
      shift 2
      ;;
    -o|--output)
      [[ $# -ge 2 ]] || usage
      OUTPUT="$2"
      shift 2
      ;;
    -h|--help)
      usage 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      ;;
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
  navigation="maps/$distro/navigation.adoc"
  if [[ ! -f "$navigation" ]]; then
    echo "Error: $navigation not found." >&2
    exit 1
  fi
done

preflight_dir="$(mktemp -d "${TMPDIR:-/tmp}/jtbd-preview-preflight.XXXXXX")"
trap 'rm -rf -- "$preflight_dir"' EXIT
preflight_failed=0
: > "$preflight_dir/all.txt"

for distro in "${DISTROS[@]}"; do
  navigation="maps/$distro/navigation.adoc"
  report="$preflight_dir/$distro.txt"
  if ! python3 scripts/audit-map-includes.py "$navigation" > "$report" 2>&1; then
    preflight_failed=1
  fi
  cat "$report"
  cat "$report" >> "$preflight_dir/all.txt"
done

if [[ "$preflight_failed" -eq 1 ]]; then
  echo "WARNING: building an incomplete preview; missing-content warnings will be added to the HTML." >&2
fi

if [[ -e "$OUTPUT" ]]; then
  if [[ -L "$OUTPUT" ]]; then
    echo "Error: refusing to remove a symlink output path: $OUTPUT" >&2
    exit 1
  fi
  if [[ ! -f "$OUTPUT/.jtbd-preview-output" ]]; then
    echo "Error: refusing to remove an output directory without the JTBD preview marker: $OUTPUT" >&2
    echo "Choose a new output path or remove that directory manually." >&2
    exit 1
  fi
  rm -rf -- "$OUTPUT"
fi
mkdir -p "$OUTPUT"
touch "$OUTPUT/.jtbd-preview-output"

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

  python3 scripts/preview-jtbd-right-toc.py "$destination"
  python3 - "$destination" <<'PY'
import sys
from pathlib import Path

destination = Path(sys.argv[1])
(destination / "index.html").write_text(
    '<!doctype html><html><head><meta charset="utf-8">'
    '<meta http-equiv="refresh" content="0; url=navigation.html">'
    '<link rel="canonical" href="navigation.html">'
    '<title>JTBD map preview</title></head><body>'
    '<p><a href="navigation.html">Open the JTBD navigation</a></p>'
    '</body></html>\n',
    encoding="utf-8",
)
PY
  if [[ "$preflight_failed" -eq 1 ]]; then
    python3 scripts/preview-jtbd-warning.py "$destination" "$preflight_dir/$distro.txt"
  fi
done

python3 - "$OUTPUT" "${DISTROS[@]}" <<'PY'
import html
import sys
from pathlib import Path

output = Path(sys.argv[1])
distros = sys.argv[2:]
links = "\n".join(
    f'<li><a href="{html.escape(distro, quote=True)}/navigation.html">'
    f'{html.escape(distro)}</a></li>'
    for distro in distros
)
(output / "index.html").write_text(
    "<!doctype html><html><head><meta charset=\"utf-8\"><title>JTBD map preview</title>"
    "<style>body{font-family:sans-serif;max-width:42em;margin:3em auto;padding:0 1em}"
    "li{line-height:2}</style></head><body><h1>JTBD map preview</h1><ul>"
    + links
    + "</ul></body></html>\n",
    encoding="utf-8",
)
PY

if [[ "$preflight_failed" -eq 1 ]]; then
  python3 scripts/preview-jtbd-warning.py "$OUTPUT" "$preflight_dir/all.txt"
fi

echo "Preview written to $OUTPUT"
