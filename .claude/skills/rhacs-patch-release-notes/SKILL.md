---
name: rhacs-patch-release-notes
description: Create patch (z-stream) release notes for Red Hat Advanced Cluster Security for Kubernetes (RHACS). Gathers the patch version, GA date, Jira board, supported branches, and doc ticket; syncs branches; classifies bug fixes and CVEs from Jira; writes the release note modules; lints with Vale; and pushes a topic branch.
argument-hint: "<patch-version> (e.g. 4.10.2)"
allowed-tools: Read, Write, Glob, Grep, Edit, Bash, Agent, AskUserQuestion
---

# RHACS Patch Release Notes

Generate patch (z-stream) release notes for Red{nbsp}Hat Advanced Cluster Security for Kubernetes (RHACS) in the `openshift/openshift-docs` repository.

## Input

Gather these inputs before proceeding. If any are missing, ask the user for them:

- **Patch release version** (e.g. `4.10.2`)
- **GA date** (e.g. `8 April 2026`)
- **Jira board link** (e.g. `https://redhat.atlassian.net/projects/ROX/versions/104472/tab/release-report-all-issues`)
- **Supported doc version branches** (e.g. `rhacs-docs-4.8`, `rhacs-docs-4.9`, `rhacs-docs-4.10`)
- **Doc ticket link** for the release (e.g. `https://redhat.atlassian.net/browse/ROX-33859`)

## Build and lint commands

- **Lint (Vale only):** `git diff --name-only --diff-filter=d HEAD | grep '\.adoc$' | xargs -r vale`
- Documentation is written in AsciiDoc (`.adoc`).

## Process

### Step 1: Base branch preparation and sync

- **Identify the base branch** from the patch version (e.g. `4.10.2` → `rhacs-docs-4.10`).
- **Check the current branch:** run `git branch --show-current`. If it is not the calculated base branch, run `git checkout <base-branch>`.
- **Sync with upstream:**

```
git fetch upstream <base-branch> && git rebase upstream/<base-branch> && git push origin <base-branch> -f
```

### Step 2: Intelligent branching

- **Calculate the topic branch name:** extract the Jira ID from the doc ticket (e.g. `ROX-34180` → `ROX34180`) and combine it with the base branch name → `ROX34180-rhacs-docs-4.10`.
- **Create the topic branch from the fresh upstream source:**

```
git checkout -b <topic-branch-name> upstream/<base-branch>
```

### Step 3: Style reference and multi-branch sync

For **each** branch in the "Supported doc version branches" input:

```
git checkout <branch-name>
git fetch upstream <branch-name>
git rebase upstream/<branch-name>
git push origin <branch-name> -f
```

Then scan existing release note files on that branch to analyze tone and structure.

**Check for related patch release PRs** in `openshift/openshift-docs` authored by `kcarmichael08` or `jlprevatt` or `agantony`:

```
gh pr list --repo openshift/openshift-docs --author kcarmichael08 --state open --search "RHACS" --json number,title,url
gh pr list --repo openshift/openshift-docs --author jlprevatt --state open --search "RHACS" --json number,title,url
gh pr list --repo openshift/openshift-docs --author agantony --state open --search "RHACS" --json number,title,url
```

- If related patch release PRs are found (e.g. 4.8.11, 4.9.5), report them to the user with links.
- **Check for matching ROX tickets:** for each PR, fetch the changed files and extract ROX ticket numbers:

  ```
  gh pr view <PR-NUMBER> --repo openshift/openshift-docs --json files --jq '.files[].patch'
  ```

  Look for `//ROX-XXXXX` comments and ticket references. Compare against the tickets in the current release and report any that appear in both, noting the PR number and version.
- **Ensure text consistency for matching tickets:** for any shared ROX ticket, reuse the **exact** text/description from the other PR's release notes. If your wording differs, tell the user and recommend matching it. Example: if `ROX-34121` (`CVE-2026-35469`) appears in both 4.8.11 and 4.10.2, the description must be identical in both.
- Review these PRs to understand formatting and structure; these authors may have drafted release notes for other versions that serve as current style references.

**Return to the topic branch** once all syncs are complete:

```
git checkout <topic-branch-name>
```

### Step 4: Analysis phase (persona: release engineer)

Use the **Atlassian MCP** to list issues for the version ID in the Jira board link, then classify each issue:

**A. Security vulnerabilities**
- Rule: issue type is "Vulnerability" **OR** summary starts with "CVE-".
- Action: document ALL unique security vulnerabilities (required per security policy). Avoid duplication.
- Status: include regardless of status (New, In Progress, Closed, etc.).

**B. Bug fixes** — everything that is NOT a security vulnerability. Apply this strict filter:

**INCLUDE if the ticket meets ANY of these:**
- User-visible UI changes or fixes (buttons, forms, dashboards, displays)
- User-reported bugs (check Jira comments/description for customer references)
- Noticeable performance improvements users would experience ("search is faster", "page loads quicker")
- CLI/API behavior changes that users interact with directly
- Operator behavior changes that affect user deployments
- Documentation fixes that clarify user confusion
- Bug fixes that prevent user-visible errors or failures
- Features that were broken and now work (from the user perspective)

**EXCLUDE if the ticket meets ANY of these:**
- Internal code refactoring or optimization users won't notice
- Memory management improvements without user-visible impact
- Database query optimizations (N+1 patterns, query efficiency) unless causing noticeable slowness
- Internal architecture changes (reconciliation logic, controller internals)
- Dependency updates ("Update rpms", library bumps)
- Internal tooling or build system changes
- Code cleanup or technical debt reduction
- Internal pruning/garbage collection optimizations
- Changes that expose internal system architecture if documented in detail
- Performance fixes with improvements too small for users to notice
- Fixes that lack "Release Note" content in the Jira ticket (engineering doesn't think it needs documentation)

**When in doubt:** present the ticket to the user and ask whether to document it, explaining the uncertainty.

**Output and review:** present a categorized analysis table showing the category breakdown, issue counts, the specific lists of issues to document/skip, and the summary: `Total issues to document: X out of Y`.

**Jira action:** after the user confirms the table, post the analysis findings (summary + categorized list) as a comment on the **doc ticket** in Atlassian Cloud using the **Atlassian MCP** (`mcp__atlassian__addCommentToJiraIssue` with `cloudId` for `redhat.atlassian.net` and the doc ticket's issue key).

### Step 5: Execution phase (writing and attributes)

- **Version formatting:** create a "clean" version string by removing dots (e.g. `4.10.2` → `4102`).
- **Update attributes** in `modules/common-attributes.adoc`:
  - Add/update `:ga-date-<clean-version>: <GA Date>`
  - Add/update `:rhacs-version: <patch release version>`

**For version 4.10 and above:**

1. Create or update `modules/bug-fixes-in-version-<clean-version>.adoc` with the bug fixes and security vulnerabilities, following the writing style below.
2. Update the release dates table in `modules/release-dates-<major-minor>.adoc` (e.g. `modules/release-dates-410.adoc`):
   - Add a new row for the patch version in version order, before the closing `|====`, using the format:
     `` |`<patch version>`| {ga-date-<clean-version>} ``
   - Example: `` |`4.10.2`| {ga-date-4102} ``
3. Add the include directive to the release notes assembly (e.g. `release_notes/410-release-notes.adoc`):
   - `include::modules/bug-fixes-in-version-<clean-version>.adoc[leveloffset=+1]`
   - Example: `include::modules/bug-fixes-in-version-4102.adoc[leveloffset=+1]`

**For versions below 4.10:** append/update content in the legacy file structure, following the historical pattern for that branch, still applying the writing style below.

#### Bug fix writing style (CRITICAL — follow strictly)

**DO:**
- Be extremely concise — prefer 1-2 sentences over paragraphs.
- Use the three-part structure Problem → Solution → Result:
  - "Before this update, [user-visible symptom]. With this release, Red{nbsp}Hat [what was fixed]. As a result, [user benefit]."
  - OR the simplified form: "With this release, Red{nbsp}Hat [what changed/improved]. As a result, [user benefit]."
- Focus on user-visible symptoms and impacts only.
- Use simple, clear language a non-technical user can understand.
- Remove ALL implementation details before presenting.
- State improvements in terms of user experience ("performance has improved", "memory usage is reduced", "searches work correctly").

**DO NOT:**
- **NEVER expose internal system architecture** (N+1 queries, query patterns, database operations, reconciliation logic, controller internals).
- **NEVER include specific technical numbers** that reveal internals (GB of memory, number of queries, component counts, specific performance metrics).
- **NEVER explain HOW the fix was implemented** (code changes, algorithms, data structures, deserialization methods).
- **NEVER mention internal technical concepts** (zero-copy deserialization, protobuf, in-memory maps, status controllers, predicates).
- **NEVER use overly technical jargon** — replace with user-friendly terms.
- **NEVER write long explanations** — if it can't be concise, it probably shouldn't be documented.
- **NEVER include details that could raise customer questions** about internal system workings.

**Examples (BAD vs GOOD):**

❌ BAD (too technical, exposes internals):
> "Before this update, the image store used an inefficient N+1 query pattern when fetching CVE data, issuing a separate database query for each component in an image. For images with 100 components, this resulted in 101 queries to load a single image, significantly impacting performance for batch operations, GraphQL queries, image search, and enrichment processes."

✅ GOOD (user-focused, concise):
> "With this release, Red{nbsp}Hat introduced performance optimizations with CVE fetching. As a result, image retrieval performance has improved."

❌ BAD (exposes memory management internals):
> "Before this update, the image component ranker initialization process walked the entire image components table and deserialized full protobuf data just to extract ID and risk score fields. This caused excessive memory usage because zero-copy deserialization pinned entire row buffers in memory. In large deployments with about 15 million image components, this resulted in about 6.7 GB of retained heap memory."

✅ GOOD (user-focused outcome):
> "Before this update, the image component initialization process caused excessive memory usage in large deployments. With this release, Red{nbsp}Hat has optimized the initialization process. As a result, memory usage has decreased and out-of-memory risks are reduced."

❌ BAD (too much internal detail about reconciliation):
> "Before this update, the RHACS Operator performed unnecessary reconciliations due to two issues. The status controller reconciler triggered on deployment spec changes in addition to status changes, and the helm-reconciler predicate did not correctly filter out updates from the status controller when working with unstructured objects."

✅ GOOD (simple, user-benefit focused):
> "With this release, Red{nbsp}Hat made changes to the Operator reconciliation to improve performance and reduce resource usage."

#### CVE documentation format (inline style)

- Do NOT create a separate `== Security Vulnerabilities` heading.
- After all bug fix entries, add: `This release also addresses the following security vulnerabilities:`
- **Add Jira ticket references:** above each CVE entry, add a commented line with the associated Jira ticket number(s) for future reference — `//ROX-XXXXX` (or `//ROX-XXXXX, ROX-YYYYY` for multiple tickets).
- List each CVE with the description followed by the CVE link in parentheses:
  - Format: `* <Description> (link:https://access.redhat.com/security/cve/<CVE-ID>[<CVE-ID>])`
  - Example:

    ```
    //ROX-34121
    * Kubelet, CRI-O, kube-apiserver: Denial of service via SPDY streaming code (link:https://access.redhat.com/security/cve/CVE-2026-35469[CVE-2026-35469])
    ```
- For CVEs with special characters (e.g. underscores in function names), use `+++` passthrough escaping: `+++_.unset+++` instead of `_.unset`. Example: `lodash: Prototype pollution in +++_.unset+++ and +++_.omit+++ functions`.
- Combine duplicate vendor entries (same component, multiple CVEs) into one entry with comma-separated CVE links.

Follow established RHACS AsciiDoc formatting for all content.

### Step 6: Validation phase (interactive)

- **Pre-flight:** run `vale sync` to synchronize styles.
- **Staging:** run `git add .` to stage the new and modified files.
- **Lint** the modified `.adoc` files:
  - Staged changes: `git diff --name-only --diff-filter=d HEAD | grep '\.adoc$' | xargs -r vale`
  - Specific file: `vale modules/bug-fixes-in-version-<clean-version>.adoc`
- **Vale results handling** — present errors, warnings, AND suggestions to the user and ask whether to fix or ignore each:
  - **Passive voice:** always fix by rewriting in active voice.
  - **Simple language:** replace complex words (e.g. "approximately" → "about").
  - **Readability:** simplify sentences where possible without losing technical accuracy.
  - **Known potentially acceptable issues (require user approval to ignore):**
    - "FATAL ERROR" terminology: only acceptable when quoting an exact error message.
    - Case sensitivity (e.g. "Kubelet" vs "kubelet"): only acceptable for proper names or component names.
    - Readability scores above grade 9: may be acceptable for technical documentation.
    - Acronym definitions (RHACS, SPDY, JOSE): may be acceptable if widely known in context.
    - AsciiDoc attribute references (e.g. `{context}`): standard syntax, acceptable.
- **Review:** present the complete Vale summary and **ask permission** before applying any fixes or ignoring any issues. Document all intentionally ignored items.
- **Confirmation:** after approval or fixes, rerun Vale to confirm the final state and record which issues remain unaddressed by user choice.

### Step 7: Deployment phase

Add, commit, and push the topic branch:

```
git push -u origin <topic-branch-name>
```

## Important notes

- Repository is `openshift/openshift-docs`; `upstream` is the openshift org remote and `origin` is your fork.
- Base and doc-version branches follow the `rhacs-docs-<major.minor>` naming; the topic branch is `<ROXID>-rhacs-docs-<major.minor>`.
- Document **all** unique security vulnerabilities regardless of status; apply the strict INCLUDE/EXCLUDE filter to bug fixes.
- Reuse identical wording for ROX tickets shared across concurrent patch releases.
- Version 4.10 and above uses per-patch `modules/bug-fixes-in-version-<clean-version>.adoc` files; earlier versions use the legacy file structure on their branch.
- All Jira interactions (listing release issues, posting the analysis comment) go through the **Atlassian MCP** against Atlassian Cloud (`redhat.atlassian.net`) — not a local `jira` CLI.
- Always confirm the analysis table with the user before posting the comment to Atlassian Cloud, and confirm Vale results before applying fixes.

## Dry run

To dry-run this workflow, the user can request: perform a DRY RUN of the patch release notes workflow — follow the steps but do not execute any `git push` or `git rebase` commands (just list them), do not post the comment to the Atlassian Cloud doc ticket (just show the text), and show the generated file content before saving it.