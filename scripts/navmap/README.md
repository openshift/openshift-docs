# Navigation map scripts

Scripts for building, publishing, and auditing distribution-specific navigation maps from `maps/<distro>/navigation.adoc`.

## Scripts

| Script | Purpose |
|---|---|
| `preview-map.sh` | Build a local multi-page HTML preview |
| `publish-map.sh` | Build and publish to GitHub Pages |
| `audit-map-includes.py` | Check for missing `include::` targets |
| `audit-map-jobs.sh` | Report job-to-category coverage |
| `preview-warning.py` | Post-processor: adds warning banner when includes are missing |

## Requirements

```
gem install asciidoctor-multipage
```

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

## Audit missing includes

Checks that every `include::` directive in a map resolves to an existing file:

```bash
python3 scripts/navmap/audit-map-includes.py maps/ocp/navigation.adoc
```

This runs automatically as part of `preview-map.sh`. If missing includes are found, the preview still builds but a warning banner is added to every page.

## Audit job coverage

Reports which jobs from `maps/<distro>-jobs/` are mapped to categories under `maps/<distro>/`:

```bash
# Full report for OCP
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

## Supported distros

| Distro | Map directory | Job pool |
|---|---|---|
| `ocp` | `maps/ocp/` | `ocp-jobs` |
| `rosa-hcp` | `maps/rosa-hcp/` | `hcm-jobs` |
| `rosa-classic` | `maps/rosa-classic/` | `hcm-jobs` |
| `osd` | `maps/osd/` | `hcm-jobs` |
| `microshift` | `maps/microshift/` | — |
