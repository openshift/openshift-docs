#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 [-b branch] [-d distro] [-d distro] ..."
  echo ""
  echo "  -b, --branch   Branch name (default: current git branch)"
  echo "  -d, --distro   Distro to build (default: all distros under maps/)"
  echo ""
  echo "Examples:"
  echo "  $0                                  # all distros, current branch"
  echo "  $0 -d openshift-enterprise          # one distro"
  echo "  $0 -d openshift-enterprise -d rosa  # two distros"
  exit 1
}

BRANCH=""
DISTROS=()

while [[ $# -gt 0 ]]; do
  case $1 in
    -b|--branch) BRANCH="$2"; shift 2 ;;
    -d|--distro) DISTROS+=("$2"); shift 2 ;;
    -h|--help)   usage ;;
    *)           echo "Unknown option: $1"; usage ;;
  esac
done

# Check that asciidoctor-multipage is installed
if ! ruby -e "require 'asciidoctor-multipage'" 2>/dev/null; then
  echo "Error: asciidoctor-multipage gem not found. Install it with:"
  echo "  gem install asciidoctor-multipage"
  exit 1
fi

# Auto-detect branch
if [ -z "$BRANCH" ]; then
  BRANCH=$(git rev-parse --abbrev-ref HEAD)
  if [ "$BRANCH" = "HEAD" ]; then
    echo "Error: detached HEAD state. Use -b to specify a branch name."
    exit 1
  fi
fi

# Auto-discover distros if none specified
if [ ${#DISTROS[@]} -eq 0 ]; then
  for nav in maps/*/navigation.adoc; do
    if [ -f "$nav" ]; then
      DISTROS+=("$(basename "$(dirname "$nav")")")
    fi
  done
  if [ ${#DISTROS[@]} -eq 0 ]; then
    echo "Error: no distros found. Expected maps/<distro>/navigation.adoc"
    exit 1
  fi
fi

# Validate requested distros
for distro in "${DISTROS[@]}"; do
  if [ ! -f "maps/$distro/navigation.adoc" ]; then
    echo "Error: maps/$distro/navigation.adoc not found."
    exit 1
  fi
done

# Derive GitHub username and repo name from origin remote
GH_REMOTE=$(git remote get-url origin)
GH_USERNAME=$(echo "$GH_REMOTE" | sed -E 's|.*[:/]([^/]+)/[^/]+$|\1|' | sed 's/\.git$//')
GH_REPO=$(echo "$GH_REMOTE" | sed -E 's|.*[:/][^/]+/([^/]+)$|\1|' | sed 's/\.git$//')

WORKTREE="/tmp/gh-pages-$$"

echo "Branch:  $BRANCH"
echo "Distros: ${DISTROS[*]}"
echo "Remote:  $GH_USERNAME/$GH_REPO"
echo ""

# Check gh-pages branch exists on origin
if ! git ls-remote --exit-code --heads origin gh-pages > /dev/null 2>&1; then
  echo "Error: No gh-pages branch found on origin. Create one first:"
  echo "  git checkout --orphan gh-pages && git reset --hard && git push origin gh-pages"
  exit 1
fi

# Check out gh-pages into a temp worktree
git fetch origin gh-pages
git worktree add --detach "$WORKTREE" origin/gh-pages

cleanup() {
  git worktree remove "$WORKTREE" --force 2>/dev/null || true
}
trap cleanup EXIT

# Clear and recreate branch directory in worktree
rm -rf "${WORKTREE:?}/$BRANCH"
mkdir -p "$WORKTREE/$BRANCH"

# Build each distro
for distro in "${DISTROS[@]}"; do
  echo "Building $distro..."
  mkdir -p "$WORKTREE/$BRANCH/$distro"

  asciidoctor -r asciidoctor-multipage -b multipage_html5 \
    "maps/$distro/navigation.adoc" \
    -D "$WORKTREE/$BRANCH/$distro" \
    -a toc=left \
    -a doctype=book \
    -a docinfo=shared-footer \
    -a multipage-level=1
done

# Generate per-branch index listing distros
{
  echo '<!DOCTYPE html>'
  echo '<html>'
  echo '<head>'
  echo "  <title>Preview: ${BRANCH}</title>"
  echo '  <style>'
  echo '    body { font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; }'
  echo '    h1 { font-size: 1.4em; }'
  echo '    ul { line-height: 2; }'
  echo '  </style>'
  echo '</head>'
  echo '<body>'
  echo "  <h1>${BRANCH}</h1>"
  echo '  <ul>'
  for dir in "$WORKTREE/$BRANCH"/*/; do
    distro_name=$(basename "$dir")
    echo "    <li><a href=\"${distro_name}/navigation.html\">${distro_name}</a></li>"
  done
  echo '  </ul>'
  echo '</body>'
  echo '</html>'
} > "$WORKTREE/$BRANCH/index.html"

# Regenerate root index listing all branch directories
{
  echo '<!DOCTYPE html>'
  echo '<html>'
  echo '<head>'
  echo '  <title>Branch Previews</title>'
  echo '  <style>'
  echo '    body { font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; }'
  echo '    h1 { font-size: 1.4em; }'
  echo '    ul { line-height: 2; }'
  echo '  </style>'
  echo '</head>'
  echo '<body>'
  echo '  <h1>Branch Previews</h1>'
  echo '  <ul>'
  for dir in "$WORKTREE"/*/; do
    branch_name=$(basename "$dir")
    echo "    <li><a href=\"${branch_name}/index.html\">${branch_name}</a></li>"
  done
  echo '  </ul>'
  echo '</body>'
  echo '</html>'
} > "$WORKTREE/index.html"

# Commit and push
echo ""
echo "Pushing to gh-pages..."
git -C "$WORKTREE" add "$BRANCH" index.html

if git -C "$WORKTREE" diff --cached --quiet; then
  echo "No changes to commit."
else
  git -C "$WORKTREE" commit -m "Preview: $GH_REPO/$BRANCH"
  git -C "$WORKTREE" push origin HEAD:gh-pages
fi

echo ""
if [ ${#DISTROS[@]} -eq 1 ]; then
  PREVIEW_URL="https://${GH_USERNAME}.github.io/${GH_REPO}/${BRANCH}/${DISTROS[0]}/navigation.html"
else
  PREVIEW_URL="https://${GH_USERNAME}.github.io/${GH_REPO}/${BRANCH}/index.html"
fi
STATUS_URL="https://github.com/${GH_USERNAME}/${GH_REPO}/actions"

echo "Preview:  $PREVIEW_URL"
echo "Preview may take 5-10 minutes to go live. Check the status link below for the status of the build."
echo "Status:   $STATUS_URL"
