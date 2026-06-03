#!/bin/bash
# Upload *_MODULES.txt attachments to OSDOCS-17175.
# Requires: JIRA_EMAIL, JIRA_API_TOKEN (or JIRA_AUTH_TOKEN)

set -euo pipefail

ISSUE="${1:-OSDOCS-17175}"
JIRA_URL="${JIRA_URL:-https://redhat.atlassian.net}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

: "${JIRA_API_TOKEN:=${JIRA_AUTH_TOKEN:-}}"
if [[ -z "${JIRA_API_TOKEN:-}" || -z "${JIRA_EMAIL:-}" ]]; then
    echo "Error: set JIRA_EMAIL and JIRA_API_TOKEN, then re-run." >&2
    exit 1
fi

for file in "$SCRIPT_DIR"/*_MODULES.txt; do
    [[ -f "$file" ]] || continue
    echo "Uploading $(basename "$file")..."
    http_code=$(curl -s -o /dev/null -w "%{http_code}" -X POST \
        -u "${JIRA_EMAIL}:${JIRA_API_TOKEN}" \
        -H "X-Atlassian-Token: no-check" \
        -F "file=@${file}" \
        "${JIRA_URL}/rest/api/2/issue/${ISSUE}/attachments")
    if [[ "$http_code" -lt 200 || "$http_code" -ge 300 ]]; then
        echo "Failed: $(basename "$file") (HTTP ${http_code})" >&2
        exit 1
    fi
done

echo "Uploaded attachments to ${JIRA_URL}/browse/${ISSUE}"
