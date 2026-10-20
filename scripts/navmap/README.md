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
| `tree-map.py` | Visualize hierarchical include structure as a tree |
| `preview-warning.py` | Post-processor: adds warning banner when includes are missing |
| `conversion-prechecks.sh` | Run AsciiDoc pre-conversion validation (map completeness, Vale DITA, exploration) |

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

## Visualize map structure

Displays the hierarchical include tree showing how categories, jobs, and modules are nested:

```bash
# From repository root (using wrapper)
./tree-map ocp                             # Full OCP navigation
./tree-map ocp observe                     # OCP Observe category
./tree-map rosa-hcp observe                # ROSA HCP Observe category
./tree-map --compare-jobs ocp               # Compare jobs within every OCP category
./tree-map --compare-jobs ocp observe optimize  # Review selected OCP categories
./tree-map --compare-jobs -c observe ocp    # Category flag, also repeatable

./tree-map maps/ocp/install.adoc              # Show install category structure
./tree-map maps/ocp-jobs/install-single-node-openshift.adoc  # Show specific job

# Show with line numbers where includes occur
./tree-map -l maps/ocp/install.adoc

# Show with leveloffset values
./tree-map -o maps/ocp/install.adoc

# Show both line numbers and leveloffset
./tree-map -l -o maps/ocp/install.adoc

# Validate leveloffset patterns (errors: ❌, warnings: ⚠️)
./tree-map --validate -o maps/ocp/install.adoc

# Limit depth to avoid overwhelming output
./tree-map -d 3 maps/ocp/navigation.adoc

# No colors (for piping to file)
./tree-map --no-color maps/ocp/install.adoc > install-tree.txt

# Or call script directly
python3 scripts/navmap/tree-map.py maps/ocp/install.adoc
```

Use `tree-map [FLAGS] DISTRO [CATEGORY ...]` to select a distro and optional
categories. With no categories, the distro's `navigation.adoc` is used. Categories
can also be selected with repeatable `-c`/`--category` flags, with or without the
`.adoc` suffix. Multiple categories are displayed separately, with comparison and
removal counts scoped to each category. Removal jobs are resolved across all
selected categories; categories that do not contain the selected jobs are
identified. An explicit map or job file path still selects that file directly.
Invalid names list the available distros or categories.

The output uses color-coded markers:
- **[CAT]** (blue) - Category files under `maps/ocp/`
- **[JOB]** (cyan) - Job files under `maps/ocp-jobs/` or `maps/hcm-jobs/`
- **[MOD]** (green) - Module files under `modules/`
- **[SNP]** (yellow) - Snippet files under `snippets/`
- **[MISSING]** (red) - Referenced files that don't exist

Example output showing nested job structure:
```
[CAT] install.adoc
├── [CAT] understand-openshift-installation-architecture.adoc
│   ├── [MOD] installation-overview.adoc
│   ├── [MOD] about-the-installation-program.adoc
│   └── [MOD] installation-process.adoc
├── [JOB] install-single-node-openshift.adoc
│   ├── [MOD] install-single-node-openshift-intro.adoc
│   ├── [JOB] prepare-to-install-single-node-openshift.adoc
│   │   ├── [MOD] install-sno-about-installing-on-a-single-node.adoc
│   │   └── [MOD] install-sno-requirements-for-installing-on-a-single-node.adoc
│   └── [MOD] install-sno-assisted-installer.adoc
```

### Flags

| Flag | Short | Description |
|---|---|---|
| `--category CATEGORY` | `-c` | Select a category within the specified distro (repeatable; also accepted positionally) |
| `--line-numbers` | `-l` | Show line numbers where includes occur |
| `--leveloffset` | `-o` | Show leveloffset values from include directives |
| `--max-depth N` | `-d N` | Limit tree depth to N levels |
| `--validate` | | Check include structure, heading levels, parent-child reuse, and identical direct job include target sets |
| `--check-redundancy` | | Check for modules repeated between ancestors and descendants |
| `--compare-jobs` | | Annotate jobs with shared and unique include coverage within each category |
| `--similarity PERCENT` | | Similarity cutoff for job annotations (1–100; default: 80); requires comparison or removal mode |
| `--removal-impact JOB` | | Simulate removing a reachable job; repeat to assess several removals together; implies `--compare-jobs` |
| `--no-color` | | Disable colored output (useful for piping to files) |

### Validation Mode

The `--validate` flag checks include structure, heading levels, parent-child module
reuse, and jobs with identical direct include target sets within each category:

```bash
./tree-map --validate -o maps/ocp/install.adoc
```

**Errors** (❌ red, must fix):
- Missing files referenced in include directives
- Circular include references
- Unreadable source files

**Warnings** (⚠️ yellow, review recommended):
- An include starts more than one heading level below the preceding heading, skipping an intermediate parent
- An offset moves a module heading above its containing map or job
- Different jobs in the same category have identical nonempty direct include
  target sets. The warning names both jobs and reminds reviewers to check
  conditional includes and include attributes before removing either job.

Matching jobs are marked `[IDENTICAL G1]`, `[IDENTICAL G2]`, and so on beside their
names in the tree. Jobs with the same group marker share a direct include target
set, and their warnings carry that marker too. A group can contain more than two
jobs. Markers are yellow in colored output and remain readable with `--no-color`.
Group numbers are local to each displayed map and do not imply that jobs are safe
to remove.

**Ignored** (intentional patterns):
- A title or introductory module at `+0`, regardless of its filename
- Subsections at `+2` following a section at `+1`
- Deep nesting such as `+3` followed by `+4`, and returns to shallower sections
- Missing or negative offsets that preserve the heading hierarchy

Validation uses heading order and the included modules' literal heading levels, including their internal subsections. It does not compare offsets against a majority pattern. For example, `+1` followed by `+2` is valid; `+1` followed by `+3` warns if the preceding module does not provide an intermediate heading.

```text
leveloffset=+3 skips a parent heading (section level 1 to 3)
```

Section levels use AsciiDoc numbering: `= Title` is level 0, `== Section` is level 1, and so on. A warning identifies the include directive to review; it does not automatically change its offset.

Validation summary appears at the end with file references and line numbers where
applicable. Exit code is non-zero if errors are found (useful for CI/CD).

Validation states how many traversed jobs were compared. Identical-job matches
are review warnings, not errors or proof that rendered content is equivalent.
The comparison ignores include order, repetitions, and attributes, and resolves
file path aliases. It compares each job's direct include targets; use
`--compare-jobs` for expanded nested coverage. Only jobs read within the traversal
depth are compared. A clean result refers to the checks performed in that scope,
not a complete content or rendered-output review.

This is a conservative static check. It skips heading comparisons that depend on conditional headings, included files that themselves contain includes, partial includes (`tags` or `lines`), absolute offsets, or attribute-driven offsets. It cannot determine whether a structurally valid subsection belongs under the intended topic. The tree stops at modules by default, but validation reads their headings; `--max-depth` enables traversal into modules and limits the scope of all checks to that depth. Use the Asciidoctor pre-conversion check below to validate rendered content.

### Parent-Child Redundancy Checking

The `--check-redundancy` flag (or included in `--validate`) detects when a module is included in both a parent job and a nested child job:

```bash
# Redundancy checking only
./tree-map --check-redundancy -o maps/ocp/install.adoc

# Validation includes redundancy checking
./tree-map --validate -o maps/ocp/install.adoc
```

**What it detects** (🔁 marker, full ancestor chain):
- Modules included in parent job AND in nested child job
- Modules included at any ancestor level (grandparent, etc.)
- This creates content duplication in the rendered output

**Example output:**
```
[JOB] install-on-platform.adoc
├── [MOD] virt-planning.adoc (leveloffset=+1)
├── [JOB] prepare-to-install.adoc (leveloffset=+1)
│   ├── [MOD] virt-planning.adoc (leveloffset=+1) 🔁  ← Already in parent!
```

**Redundancy summary:**
```
PARENT-CHILD REDUNDANCY (review for duplication):
  🔁 virt-planning.adoc
     In child:  prepare-to-install.adoc:line 7
     In parent: install-on-platform.adoc:line 4
```

**Note:** This is different from sibling redundancy (same module in parallel jobs), which is detected by `audit-module-duplicates.py`.
`--check-redundancy` does not run offset validation. Missing files, unreadable files, and circular includes still fail the check because the tree is incomplete.

### Job comparison and removal impact

Show which jobs add include targets and which are covered by another job:

```bash
./tree-map --compare-jobs --no-color ocp observe
```

For example, the inventory job is annotated with `0 unique include targets; all
also in maps/ocp-jobs/view-cluster-resource-utilization.adoc`. Similar jobs also
show a similarity percentage and the other job's path. Similarity uses shared
targets divided by the distinct targets across both jobs, with an 80% default
cutoff. Complete containment is reported regardless of that cutoff.

Assess a particular removal, showing include locations to edit, targets lost or
retained, the covering jobs to keep, and retained include locations:

```bash
./tree-map --removal-impact view-cluster-resource-inventory.adoc ocp observe

# Evaluate both removals together, retaining the utilization job
./tree-map --max-depth 1 --no-color \
  --removal-impact view-cluster-resource-inventory.adoc \
  --removal-impact view-cluster-information-on-the-dashboard.adoc \
  ocp observe
```

Use a repository-relative job path when its filename is ambiguous. The simulation
removes all include occurrences of the selected jobs from the selected map's
reachable graph. It does not edit files. Several individually redundant jobs may
collectively contain unique content: repeat `--removal-impact` to check the whole
proposed removal together. Do not remove all matching jobs just because each has
zero unique targets.

This analysis resolves file paths and symlink aliases and expands nested jobs,
modules, and snippets. It runs over the full selected map even when `--max-depth`
limits the displayed tree. Comparisons stay within each category. Unlike the
direct-target comparison in `audit-modules -j`, different content selection
attributes (such as `tags` and `lines`) are treated as different targets. Selected
fragments are not expanded and require render review. Repeated targets and level
offsets do not affect coverage counts; order and heading effects need review.

The report also lists text and anchors in jobs that would leave the map, context
changes, TODO notes to preserve, and literal references or include users found in
repository `.adoc` files. Users of edited parent jobs are included because those
parents might also appear in other maps. The impact counts cover only the selected
map, not the effect of deleting a file from the repository. Reference scanning
does not follow directory symlinks or prove generated/dynamic links remain valid.

Conditional prose is marked separately as `distro-specific or conditional text
needs review`, with file and line references. It does not make the include
comparison incomplete by itself. Conditional includes can change which files
appear, so those still make the comparison incomplete. Dynamic include paths,
local attributes, and selected fragments are also marked for review.
Remote includes are tracked by URL without
fetching or expanding their contents, and are marked for external content review.
Missing local files, unreadable sources, circular
includes, and failed reference scans produce a nonzero exit status. Comparison
findings and other review notes are advisory. A zero-loss count describes included
file/selection coverage, not equivalent rendered output or permission to delete a
job file. Review contexts, references, local text, and a rendered preview before
making the corresponding edit.

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

# Compare complete include sets between jobs in a category
./audit-modules --compare-jobs -c observe ocp

# Compare jobs in all OCP categories, with a lower similarity cutoff
./audit-modules -j --similarity 70 ocp

# Show only jobs with identical direct include target sets
./audit-modules -j --identical-only ocp

# Count matching job pairs per category
./audit-modules -js ocp

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
| `--compare-jobs` | `-j` | Compare jobs' complete direct include target sets within each category |
| `--identical-only` | | Show only identical job pairs; requires `-j`; works with `-c` and `-s` |
| `--similarity N` | | Minimum shared/combined target percentage for similar pairs (1–100; default: 80); requires `-j` |
| `--summary` | `-s` | Show summary table only |

### Output markers

- `[DUP]` - Module appears multiple times in the same job
- `[CROSS]` - Module appears in multiple different jobs
- `[DUP+CROSS]` - Both duplicate and cross-job redundancy

### Compare jobs

`--compare-jobs` switches from the module usage report to a comparison of job
pairs within each selected category. It reports:

- `[IDENTICAL]`: both jobs have the same nonempty include target set.
- `[CONTAINED]`: all targets in job A also appear in job B; B has additional targets.
- `[SIMILAR]`: neither job contains the other, but their similarity meets the cutoff.

Similarity is the number of shared targets divided by the number of distinct
targets across both jobs. For example, jobs including `{a, b, c}` and `{a, b, d}`
share two of four distinct targets, giving 50% similarity. By default, identical
and fully contained pairs are shown regardless of the similarity cutoff. This
catches single-module jobs that contribute no additional includes alongside a
much larger job.

Use `--identical-only` with `-j` to exclude contained and similar pairs. This also
filters summary counts when combined with `-s`.

The detailed report lists shared targets and targets unique to each job. `-s`
shows pair counts per category instead. Category and distro selection work as in
the module report; `-d`, `-r`, and `-t` cannot be combined with this mode.

Comparison uses literal direct include target sets, including nested job and
snippet targets. It ignores include order, repeated targets, include attributes
(including tags, line ranges, and level offsets), and commented-out includes.
Nested jobs are not expanded, paths are not resolved, and AsciiDoc conditionals
are not evaluated. Empty jobs are excluded, and unreadable or missing job files
are warned about and skipped. Matches identify candidates for review; they do not
establish equivalent rendered content or compare job prose and TODOs.
The report reminds reviewers to check conditional includes before removing either
job, including when the pair is marked `[IDENTICAL]`.

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

### Regression checks

The tests use isolated fixtures and tool doubles; they do not sync styles or modify source maps:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts/navmap/tests -v
bash -n conversion-prechecks scripts/navmap/conversion-prechecks.sh
```

## Supported distros

| Distro | Map directory | Job pool |
|---|---|---|
| `ocp` | `maps/ocp/` | `ocp-jobs` |
| `rosa-hcp` | `maps/rosa-hcp/` | `hcm-jobs` |
| `rosa-classic` | `maps/rosa-classic/` | `hcm-jobs` |
| `osd` | `maps/osd/` | `hcm-jobs` |
| `microshift` | `maps/microshift/` | — |
