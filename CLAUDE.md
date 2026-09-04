# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## About this repository

AsciiDoc documentation for **OpenShift Container Platform** and related distributions (OKD, OpenShift Online, OpenShift DPU, OpenShift Telco). Upstream repository: `openshift/openshift-docs` on GitHub.

## Build and validation commands

```bash
# Build docs locally with AsciiBinder (generates _preview/)
asciibinder build

# Update REST API documentation
make

# Lint with Vale (requires vale CLI + sync first)
vale sync
vale <file.adoc>
```

## Architecture

### Topic map and distros

`_topic_maps/_topic_map.yml` defines the site structure — topic groups, directories, and which distros include each topic. Each entry maps a display name to a directory and file, with optional `Distros:` filtering.

`_distro_map.yml` defines the available distributions and their product names/versions per branch.

### Assembly and module pattern

Each top-level directory (e.g., `networking/`, `security/`, `backup_and_restore/`) contains AsciiDoc assembly files that pull in modules via `include::modules/<name>.adoc[leveloffset=+1]`. The `modules/` directory at the repo root holds all reusable content — assemblies should not contain prose directly outside of `include` directives and introductory context.

### Attributes

`_attributes/common-attributes.adoc` defines all product names, versions, and common substitutions. Every assembly includes this file. Always use attribute references (`{product-title}`, `{product-version}`, `{op-system}`, etc.) — never hardcode product names or versions.

### Build system

- **AsciiBinder**: Ruby-based build tool that reads `_distro_map.yml` and `_topic_maps/` to generate HTML per distro
- **`build.py` / `build_for_portal.py`**: Python scripts for portal builds
- **`_update_rest_api.py`**: Generates REST API reference docs (invoked via `make`)

## Documentation standards

- **Ventilated prose**: one sentence per line, blank line between paragraphs
- **Sentence case headings** with a single heading per module
- **Module content types**: every module requires `:_mod-docs-content-type:` set to `ASSEMBLY`, `CONCEPT`, `PROCEDURE`, `REFERENCE`, or `SNIPPET`
- **No AsciiDoc callouts** (`<1>`, `<2>`) — use bullet lists or definition lists instead
- **No parenthetical content** — rewrite into natural sentence structure
- **No file prefixes** — don't use `con-`, `proc-`, `ref-` prefixes on filenames
- **Attributes over hardcoding** — use `{product-title}`, `{product-version}`, and other attributes from `_attributes/common-attributes.adoc`
- Follow the [Red Hat Supplementary Style Guide](https://redhat-documentation.github.io/supplementary-style-guide/)

## Git workflow

- Upstream: `git@github.com:openshift/openshift-docs.git` (remote: `upstream`)
- Personal fork: `git@github.com:kquinn1204/openshift-docs.git` (remote: `origin`)
- Always rebase from `upstream/main` before pushing
- Force push to personal fork is standard practice
- Branch names typically match JIRA ticket IDs
- Pull requests target the upstream repository

## Workflow

When starting a documentation task:
1. Read relevant existing modules and assemblies to understand current patterns
2. Use attributes from `_attributes/common-attributes.adoc` for all product names and versions
3. Check `_topic_maps/_topic_map.yml` if adding new topics or understanding site structure
4. Run `vale <file.adoc>` on changed files before committing
