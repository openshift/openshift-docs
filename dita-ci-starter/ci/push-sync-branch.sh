#!/usr/bin/env bash
# push-sync-branch.sh <normalized-dir> <sync-branch>
#
# Mirrors the normalized DITA output onto a dedicated sync/<branch> branch and
# pushes it. The Adobe Git Connector is configured to watch sync/* and imports
# only the delta (added/modified/deleted) into AEM, preserving GUIDs on re-sync.
#
# One-way by design: Git -> sync branch -> AEM. AEM never writes back.
set -euo pipefail

NORMALIZED_DIR="${1:?usage: push-sync-branch.sh <normalized-dir> <sync-branch>}"
SYNC_BRANCH="${2:?usage: push-sync-branch.sh <normalized-dir> <sync-branch>}"

git config user.name  "dita-sync-bot"
git config user.email "dita-sync@users.noreply.github.com"

tmp="$(mktemp -d)"
trap 'git worktree remove --force "$tmp" 2>/dev/null || true; rm -rf "$tmp"' EXIT

# Start the sync branch from its remote state if it exists, else fresh.
if git ls-remote --exit-code --heads origin "$SYNC_BRANCH" >/dev/null 2>&1; then
  git fetch origin "$SYNC_BRANCH"
  git worktree add --force -B "$SYNC_BRANCH" "$tmp" "origin/$SYNC_BRANCH"
else
  git worktree add --force -B "$SYNC_BRANCH" "$tmp"
  ( cd "$tmp" && git rm -rfq --ignore-unmatch . || true )
fi

# Replace sync-branch contents with the normalized output (delete removals too).
rsync -a --delete --exclude='.git' "$NORMALIZED_DIR"/ "$tmp"/

cd "$tmp"
git add -A
if git diff --cached --quiet; then
  echo "No changes to sync for ${SYNC_BRANCH}."
  exit 0
fi
git commit -m "Normalized sync from ${GIT_SHA:-local} (${GIT_REF_NAME:-local})"
git push origin "$SYNC_BRANCH"
echo "Synced normalized DITA to ${SYNC_BRANCH}."
