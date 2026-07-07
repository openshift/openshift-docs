#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 [-b branch]"
  echo ""
  echo "  -b  Branch name (default: current git branch)"
  exit 1
}

BRANCH=""

while getopts "b:h" opt; do
  case $opt in
    b) BRANCH="$OPTARG" ;;
    h) usage ;;
    *) usage ;;
  esac
done

# Validate we're in the openshift-docs repo root
if [ ! -f "maps/navigation.adoc" ]; then
  echo "Error: maps/navigation.adoc not found. Run this script from the openshift-docs repo root."
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

# Derive GitHub username and repo name from origin remote
GH_REMOTE=$(git remote get-url origin)
GH_USERNAME=$(echo "$GH_REMOTE" | sed -E 's|.*[:/]([^/]+)/[^/]+$|\1|' | sed 's/\.git$//')
GH_REPO=$(echo "$GH_REMOTE" | sed -E 's|.*[:/][^/]+/([^/]+)$|\1|' | sed 's/\.git$//')

WORKTREE="/tmp/gh-pages-$$"

echo "Branch:  $BRANCH"
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
git worktree add "$WORKTREE" gh-pages

cleanup() {
  git worktree remove "$WORKTREE" --force 2>/dev/null || true
}
trap cleanup EXIT

# Clear and recreate branch directory in worktree
rm -rf "${WORKTREE:?}/$BRANCH"
mkdir -p "$WORKTREE/$BRANCH"

# Build HTML directly into the worktree branch directory
echo "Building HTML..."
asciidoctor maps/navigation.adoc \
  -D "$WORKTREE/$BRANCH" \
  -a toc=left \
  -a doctype=book \
  -a docinfo=shared-footer

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
    echo "    <li><a href=\"${branch_name}/navigation.html\">${branch_name}</a></li>"
  done
  echo '  </ul>'
  echo '</body>'
  echo '</html>'
} > "$WORKTREE/index.html"

# Commit and push
echo "Pushing to gh-pages..."
git -C "$WORKTREE" add "$BRANCH" index.html

if git -C "$WORKTREE" diff --cached --quiet; then
  echo "No changes to commit."
else
  git -C "$WORKTREE" commit -m "Preview: $GH_REPO/$BRANCH"
  git -C "$WORKTREE" push origin gh-pages
fi

PREVIEW_URL="https://${GH_USERNAME}.github.io/${GH_REPO}/${BRANCH}/navigation.html"
STATUS_URL="https://github.com/${GH_USERNAME}/${GH_REPO}/deployments"

echo ""
echo "Preview:  $PREVIEW_URL"
echo "Status:   $STATUS_URL"
