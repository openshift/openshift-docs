# Navigation map scripts

Scripts for building, publishing, and auditing distribution-specific navigation maps from `maps/<distro>/navigation.adoc`.

## Quick start (wrapper scripts)

From the repository root:

```bash
# Audit job-to-category coverage
./audit-map ocp
./audit-map -M ocp          # jobs in multiple categories
./audit-map -D ocp          # duplicate job includes

# Audit module usage within categories
./audit-modules ocp
./audit-modules -t 5 ocp    # modules appearing 5+ times
./audit-modules -r ocp      # cross-job redundancy
```

## Scripts

| Script | Purpose |
|---|---|
| `preview-map.sh` | Build a local multi-page HTML preview |
| `publish-map.sh` | Build and publish to GitHub Pages |
| `audit-map-includes.py` | Check for missing `include::` targets |
| `audit-map-jobs.sh` | Report job-to-category coverage |
| `audit-module-duplicates.py` | Report module usage within categories (duplicates & cross-job redundancy) |
| `preview-warning.py` | Post-processor: adds warning banner when includes are missing |
| `conversion-prechecks.sh` | Run AsciiDoc pre-conversion validation (map completeness, Vale DITA, exploration) |
| `compare-ocp-prechecks.py` | Run an OCP category across branches and print a comparison snapshot |

## Requirements

```
gem install asciidoctor-multipage
```

Also requires `python3` and `asciidoctor`.

The shell scripts target Bash 3.2, which is the version macOS ships. Avoid
Bash 4 features (associative arrays, `mapfile`/`readarray`, `${var^^}`) so the
scripts keep running on both macOS and Linux without an upgraded Bash.

## Preview locally

Run from the repository root:

```bash
# Single distro
bash scripts/navmap/preview-map.sh -d ocp

# All distros
bash scripts/navmap/preview-map.sh

# Custom output directory
bash scripts/navmap/preview-map.sh -d rosa-hcp -o /tmp/rosa-preview
```

Output goes to `_preview/map-preview` by default. Serve it with:

```bash
python3 -m http.server 8000 --directory _preview/map-preview
```

Then open `http://localhost:8000`.

## Publish to GitHub Pages

```bash
bash scripts/navmap/publish-map.sh -d ocp
```

The preview is published under the current branch name:

```
https://<user>.github.io/openshift-docs/<branch>/ocp/navigation.html
```

Requires push access to `origin` and a remote `gh-pages` branch.

### Setting up the `gh-pages` branch on your fork

1. Log in to GitHub and go to your fork of the `openshift-docs` repo (for example, `https://github.com/<your_username>/openshift-docs`).
2. Go to `https://github.com/<your_username>/openshift-docs/branches` (or click the **Branches** button on the repo page), and then click **New branch**.
3. Fill out the branch creation form:
   - **New branch name:** `gh-pages`
   - **Source repository:** select `openshift/openshift-docs` from the first dropdown
   - **Source branch:** enter `gh-pages` in the second dropdown
4. Click **Create new branch**.
5. Go to your fork's **Settings** (from the menu across the top of the page), and then select **Pages** from the left-hand nav, or go directly to `https://github.com/<your_username>/openshift-docs/settings/pages`.
6. Under **Build and deployment**, ensure **Source** is set to **Deploy from a branch**.
7. Select the `gh-pages` branch from the **Branch** dropdown.
8. Click **Save** if these settings were not already correct.

## Audit missing includes

Checks that every `include::` directive in a map resolves to an existing file:

```bash
python3 scripts/navmap/audit-map-includes.py maps/ocp/navigation.adoc
```

This runs automatically as part of `preview-map.sh`. If missing includes are found, the preview still builds but a warning banner is added to every page.

## Audit job coverage

Reports which jobs from `maps/<distro>-jobs/` are mapped to categories under `maps/<distro>/`:

```bash
# Full report for OCP (using wrapper or direct script)
./audit-map ocp
# or
bash scripts/navmap/audit-map-jobs.sh ocp

# Summary table only
bash scripts/navmap/audit-map-jobs.sh -s ocp

# Jobs in multiple categories
bash scripts/navmap/audit-map-jobs.sh -M ocp

# Duplicate includes (same job twice in one category)
bash scripts/navmap/audit-map-jobs.sh -D ocp

# Unmapped jobs only
bash scripts/navmap/audit-map-jobs.sh -u ocp

# Filter to a specific category
bash scripts/navmap/audit-map-jobs.sh -m -c disconnected-environments ocp

# Multiple categories
bash scripts/navmap/audit-map-jobs.sh -m -c develop -c extend ocp

# All distros at once
bash scripts/navmap/audit-map-jobs.sh

# Combine flags
bash scripts/navmap/audit-map-jobs.sh -Mu ocp
```

### Flags

| Flag | Short | Description |
|---|---|---|
| `--mapped` | `-m` | Show mapped jobs and their categories |
| `--unmapped` | `-u` | Show unmapped (uncategorised) jobs |
| `--multi` | `-M` | Show jobs in multiple categories |
| `--duplicates` | `-D` | Show jobs included more than once in the same category |
| `--summary` | `-s` | Show only the summary table |
| `--category CAT` | `-c CAT` | Filter to a specific category (repeatable) |

No flags = full report. Flags combine: `-Mu` shows multi-category + unmapped.

## Audit module duplicates

Reports how many times each module appears within a category, tracking both:

- **Direct duplicates**: same module included multiple times in the same job (usually an error)
- **Cross-job redundancy**: same module appearing in multiple jobs within the same category (often valid, e.g., AWS prereqs in multiple AWS installation jobs)

This helps identify content redundancy and understand the reader experience when navigating through a category.

```bash
# Full report for troubleshoot category (using wrapper)
./audit-modules -c troubleshoot ocp

# Summary only
./audit-modules -s -c troubleshoot ocp

# Show only modules appearing 5+ times
./audit-modules -t 5 ocp

# Show only direct duplicates (same module 2+ times in one job)
./audit-modules -d ocp

# Show only cross-job redundancy (module in 2+ different jobs)
./audit-modules -r ocp

# All categories in OCP
./audit-modules ocp

# Multiple categories
./audit-modules -c install -c configure ocp

# All distros
./audit-modules

# Or call the script directly:
python3 scripts/navmap/audit-module-duplicates.py -c troubleshoot ocp
```

### Flags

| Flag | Short | Description |
|---|---|---|
| `--category CAT` | `-c CAT` | Filter to specific category file(s) (repeatable) |
| `--duplicates-only` | `-d` | Show only modules with duplicates in same job |
| `--redundant-only` | `-r` | Show only modules appearing in 2+ jobs |
| `--threshold N` | `-t N` | Show only modules appearing N+ times (default: 2) |
| `--summary` | `-s` | Show summary table only |

### Output markers

- `[DUP]` - Module appears multiple times in the same job
- `[CROSS]` - Module appears in multiple different jobs
- `[DUP+CROSS]` - Both duplicate and cross-job redundancy

## Pre-conversion validation

Run automated AsciiDoc validation checks before converting to DITA:

```bash
# From repository root (using wrapper)
./conversion-prechecks                    # Check OCP full navigation (default)
./conversion-prechecks install            # Check OCP install category only
./conversion-prechecks secure             # Check OCP secure category only
./conversion-prechecks rosa-hcp           # Check specific product
./conversion-prechecks --all              # Check all products

# Or call script directly
bash scripts/navmap/conversion-prechecks.sh install
```

This runs three validation checks:
1. **Map completeness** - Check for missing includes and AsciiDoctor errors
2. **Vale DITA validation** - Validate against AsciiDocDITA style rules
3. **Exploration** - Identify unknown issues and conversion blockers

Asciidoctor output is discarded to avoid generating HTML beside source maps. Vale styles sync once per run, and content files are discovered and deduplicated once per target for both Vale checks. Tool failures, failed style synchronization, and empty or failed content discovery return a non-zero exit status with diagnostics in the logs. Exploration suggestions are advisory; an exploration execution failure fails the run.

Results are logged to `logs/*.log` files:
- OCP navigation: `logs/asciidoctor.log`, `logs/vale.log`, `logs/exploration.log`
- OCP categories: `logs/install-asciidoctor.log`, `logs/secure-vale.log`, etc.
- Other products: `logs/rosa-hcp-asciidoctor.log`, etc.

### Available OCP categories

You can check individual categories: `administer`, `configure`, `deploy`, `develop`, `disconnected-environments`, `discover`, `extend`, `get-started`, `install`, `integrate`, `migrate`, `networking`, `observe`, `optimize`, `plan`, `reference`, `secure`, `storage`, `troubleshoot`.

### Prerequisites

The script checks for these required tools (install instructions shown in error message):

- `asciidoctor` - Already required for preview
- `list-content` - `gem install asciidoctor-list-content`
- `vale` - https://docs.vale.sh/topics/installation
- `~/.dita.ini` - AsciiDocDITA Vale configuration (required for DITA validation)

Set `DITA_CONFIG` to use another Vale configuration file, for example:

```bash
DITA_CONFIG=/path/to/dita.ini ./conversion-prechecks install
```

### Compare a category across branches

Run from a checkout containing the precheck scripts:

```bash
./compare-ocp-prechecks integrate \
  enterprise-4.20 enterprise-4.21 enterprise-4.22 enterprise-5.0
```

This runs fresh category checks in temporary Git worktrees using the same checker
for every branch. It prints a table with Branch, AsciiDoctor, Vale, Exploration,
ConditionalCode, and AttributeDefinition counts. By default, the command fetches
`upstream` and rebases each selected local branch before checking it, so checks
include the latest upstream content. `--rebase-upstream` remains accepted but is
no longer required.

Use local branch names and launch from a different branch, such as
`compare-ocp-prechecks`. Selected branches must not be checked out in another
worktree. The command fetches matching upstream branches once, rebases each local
branch onto its matching upstream commit, and checks the rebased content. Local
commits are replayed on upstream, and successful rebases update the local branches.
It does not push. The launch checkout and its uncommitted content are preserved.
If a rebase conflicts, the temporary rebase is aborted, that local branch remains
unchanged, its counts are shown as `N/A`, and the other branches are still checked.
If fetching fails, the command stops without running checks or replacing the
previous comparison.

To deliberately check existing local snapshots without fetching or updating
branches, use `--no-rebase-upstream`. This also accepts other commit references,
including remote tracking references such as `upstream/enterprise-4.20`, which
may be stale:

```bash
./compare-ocp-prechecks --no-rebase-upstream integrate \
  enterprise-4.20 enterprise-4.21 enterprise-4.22 enterprise-5.0
```

Each category retains only its latest Markdown snapshot and branch logs under
`logs/category-comparisons/<category>/latest/`. The snapshot is named
`<category>-comparison.md`. Branch directories such as `01-enterprise-4.20/logs/`
contain the three category logs; `run.log` contains the console output. Commit IDs,
upstream commit IDs when rebasing, and execution details are recorded in
`run-metadata.json`. Older completed output is replaced after the comparison
finishes. Concurrent runs for the same output directory are rejected.

Counts include zero findings. ConditionalCode and AttributeDefinition are included
in the Exploration total. Tool failures, missing categories, and unexpected log
output produce `N/A` with details on standard error. Rows are sorted by
ConditionalCode count and branch name, with incomplete checks last. The command
returns `0` when all counts were obtained, including runs with conversion findings,
or `1` when a branch cannot be checked.

The command requires Git, Python 3.8 or later, and the prerequisites above on Linux
or macOS. It reads logs directly using the Python standard library. Use `--repo`
to select another checkout or `--output-dir` to select a category output directory.
The `DITA_CONFIG` setting is passed through to the checker.

### Regression checks

The tests use isolated fixtures and tool doubles; they do not sync styles or modify source maps:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts/navmap/tests -v
bash -n conversion-prechecks compare-ocp-prechecks scripts/navmap/conversion-prechecks.sh
```

## Supported distros

| Distro | Map directory | Job pool |
|---|---|---|
| `ocp` | `maps/ocp/` | `ocp-jobs` |
| `rosa-hcp` | `maps/rosa-hcp/` | `hcm-jobs` |
| `rosa-classic` | `maps/rosa-classic/` | `hcm-jobs` |
| `osd` | `maps/osd/` | `hcm-jobs` |
| `microshift` | `maps/microshift/` | — |
