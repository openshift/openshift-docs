#!/usr/bin/env bash
#
# Build and publish the JTBD map preview to GitHub Pages.
#
# This uses preview-jtbd-maps.sh for the build, so the published output keeps
# the recursive include audit, missing-content warning, left navigation, and
# right-hand on-this-page navigation.
#

set -euo pipefail

usage() {
  cat <<'EOF'
Usage: scripts/publish-jtbd-maps.sh [-b BRANCH] [-d DISTRO]

  -b, --branch   Branch-name path under gh-pages (default: current branch)
  -d, --distro   Distro under maps/ (repeatable; default: all distros)
  -h, --help     Show this help

The command builds the JTBD preview and publishes it to the gh-pages branch.
It requires push access to the configured origin and a remote gh-pages branch.
EOF
  exit "${1:-0}"
}

BRANCH=""
DISTRO_ARGS=()

html_escape() {
  printf '%s' "$1" | sed \
    -e 's/&/\&amp;/g' \
    -e 's/</\&lt;/g' \
    -e 's/>/\&gt;/g' \
    -e 's/"/\&quot;/g'
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -b|--branch)
      [[ $# -ge 2 ]] || usage 2
      BRANCH="$2"
      shift 2
      ;;
    -d|--distro)
      [[ $# -ge 2 ]] || usage 2
      DISTRO_ARGS+=("-d" "$2")
      shift 2
      ;;
    -h|--help)
      usage 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage 2
      ;;
  esac
done

if [[ -z "$BRANCH" ]]; then
  BRANCH="$(git rev-parse --abbrev-ref HEAD)"
  if [[ "$BRANCH" == "HEAD" ]]; then
    echo "Error: detached HEAD state. Use --branch to specify a Pages path." >&2
    exit 1
  fi
fi

case "$BRANCH" in
  ""|/*|.|..|../*|*/../*|*/..)
    echo "Error: unsafe branch path: $BRANCH" >&2
    exit 1
    ;;
esac

if [[ ! -f scripts/preview-jtbd-maps.sh ]]; then
  echo "Error: run this command from the repository root." >&2
  exit 1
fi

if ! ruby -e "require 'asciidoctor-multipage'" 2>/dev/null; then
  echo "Error: asciidoctor-multipage is not installed." >&2
  echo "Install it with: gem install asciidoctor-multipage" >&2
  exit 1
fi

if ! git ls-remote --exit-code --heads origin gh-pages >/dev/null 2>&1; then
  echo "Error: origin does not have a gh-pages branch." >&2
  exit 1
fi

REMOTE_URL="$(git remote get-url origin)"
GH_USERNAME="$(echo "$REMOTE_URL" | sed -E 's|.*[:/]([^/]+)/[^/]+$|\1|' | sed 's/\.git$//')"
GH_REPO="$(echo "$REMOTE_URL" | sed -E 's|.*[:/][^/]+/([^/]+)$|\1|' | sed 's/\.git$//')"

BUILD_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/jtbd-pages-build.XXXXXX")"
WORKTREE="/tmp/gh-pages-jtbd-$$"
cleanup() {
  if [[ -d "$WORKTREE" ]]; then
    git worktree remove "$WORKTREE" --force 2>/dev/null || true
  fi
  rm -rf -- "$BUILD_ROOT"
}
trap cleanup EXIT

BUILD_OUTPUT="$BUILD_ROOT/preview"
echo "Building JTBD preview for branch: $BRANCH"
bash scripts/preview-jtbd-maps.sh "${DISTRO_ARGS[@]}" -o "$BUILD_OUTPUT"

echo "Fetching gh-pages..."
git fetch origin gh-pages
git worktree add --detach "$WORKTREE" origin/gh-pages

TARGET="$WORKTREE/$BRANCH"
rm -rf -- "$TARGET"
mkdir -p "$TARGET"
cp -R "$BUILD_OUTPUT"/. "$TARGET/"

{
  echo '<!doctype html>'
  echo '<html><head><meta charset="utf-8">'
  echo "<title>Preview: $(html_escape "$BRANCH")</title>"
  echo '<style>body{font-family:sans-serif;max-width:42em;margin:3em auto;padding:0 1em}li{line-height:2}</style>'
  echo '</head><body>'
  echo "<h1>$(html_escape "$BRANCH") JTBD preview</h1><ul>"
  for dir in "$TARGET"/*/; do
    [[ -d "$dir" ]] || continue
    distro_name="$(basename "$dir")"
    echo "<li><a href=\"$(html_escape "$distro_name")/navigation.html\">$(html_escape "$distro_name")</a></li>"
  done
  echo '</ul></body></html>'
} > "$TARGET/index.html"

{
  echo '<!doctype html>'
  echo '<html><head><meta charset="utf-8"><title>JTBD branch previews</title>'
  echo '<style>body{font-family:sans-serif;max-width:42em;margin:3em auto;padding:0 1em}li{line-height:2}</style>'
  echo '</head><body><h1>JTBD branch previews</h1><ul>'
  for dir in "$WORKTREE"/*/; do
    [[ -d "$dir" ]] || continue
    branch_name="$(basename "$dir")"
    echo "<li><a href=\"$(html_escape "$branch_name")/index.html\">$(html_escape "$branch_name")</a></li>"
  done
  echo '</ul></body></html>'
} > "$WORKTREE/index.html"

touch "$WORKTREE/.nojekyll"
git -C "$WORKTREE" add "$BRANCH" index.html .nojekyll

if git -C "$WORKTREE" diff --cached --quiet; then
  echo "No changes to publish."
else
  git -C "$WORKTREE" commit -m "Preview JTBD maps for $BRANCH"
  git -C "$WORKTREE" push origin HEAD:gh-pages
fi

echo "Preview: https://${GH_USERNAME}.github.io/${GH_REPO}/${BRANCH}/rhcl/navigation.html"
