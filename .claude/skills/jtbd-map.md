---
name: jtbd-map
description: Populate JTBD navigation map files with actual include directives from category/job/topic names. Use when mapping content for a JTBD job, populating nav files, or connecting existing modules to the JTBD structure.
argument-hint: "[category/job/topic name]"
allowed-tools: Bash(git *) Read Grep Glob Edit Write
---

# JTBD Map: Populate navigation map files

## Purpose

This skill populates the JTBD (Jobs To Be Done) navigation map files under JTBD category directories (e.g., `discover/`, `plan/`, `integrate/`) with actual `include::` directives pointing to existing modules. It bridges the migration from the current modular docs structure (assemblies in `about/`, `configure/`, `operate/`, etc.) to the JTBD docs structure (MAP files organized by user jobs).

## Arguments

The skill accepts one or more of:
- A **category name** (e.g., `Discover`, `Install`, `Integrate`) — maps the entire category
- A **job or topic name** (e.g., `Integrate with IBM watsonx`, `Protect user privacy`) — maps a specific job

## Workflow

### Step 1: Identify scope and check file state

If the argument is a category/job/topic name:
1. Search the TOC mapping reference file at `.claude/skills/jtbd-map/jtbd-toc-mapping.tsv`
2. Find the matching entry in the hierarchy

Then, for each entry in scope:
3. Check whether the corresponding MAP file (nav file) and concept file exist in the target category directory (e.g., `discover/`, `integrate/`)
4. If the category directory does not exist, create it with the standard symlinks (see "Category directory setup" below)
5. If any MAP or concept file is missing, create it using the standard templates (see "MAP file structure" and "Concept file structure" below)
6. For existing MAP files, check whether they contain `// TODO:` comments (need population) or actual `include::` directives (already populated). Skip entries that are already fully populated.

### Step 2: Confirm scope with user

Before proceeding, show the user:
- The identified category, job, and topic hierarchy from the TSV
- The MAP files that will be populated, indicating which have TODOs vs. which are already done

Ask the user to confirm before making changes.

### Step 3: Find existing assemblies and modules

For each topic in the scope, find the corresponding assembly file first, then derive modules from it:

1. Search the current content directories (`about/`, `configure/`, `install/`, `operate/`, `troubleshoot/`) for matching assembly files by title (using `Glob` and `Grep`)
2. Read the found assembly's `include::` directives — these give the module file paths to use in the MAP file
3. Read the assembly's body content (abstract, paragraphs, admonitions, snippet includes, additional resources) — this content goes into the concept file

If no assembly is found for a topic, fall back to searching modules directly:
1. Search `modules/` for matching module files by filename or title heading

### Step 4: Populate MAP files

For each MAP file in scope:
1. Replace `// TODO:` comments with actual `include::` directives
2. Use the format without navtitle (default):
   ```
   include::modules/<module>.adoc[leveloffset=+1]
   ```
   Since this project has a flat `modules/` directory, includes always use `modules/<filename>.adoc`.
3. Add `navtitle` only when the TSV's Navtitle column (column 9) has an explicit value that differs from the module's internal `= Title` heading:
   ```
   include::modules/<module>.adoc[leveloffset=+1,navtitle="<nav title>"]
   ```
4. Keep any existing includes that are already populated
5. Use `leveloffset=+1` for top-level topics under the MAP, and `leveloffset=+2` for subtopics (H3 entries in the TSV)
6. For entries that reference other MAP files (sub-jobs with `Is a job? = TRUE` or entries with paths like `integrate/ols-integrate-*.adoc`), use:
   ```
   include::nav-<sub-job>.adoc[leveloffset=+1]
   ```
   or include the sub-MAP file directly if it lives in the same directory.

### Step 5: Populate concept files

The concept file (`con-*.adoc`) in the MAP structure contains the assembly's non-include content. For each concept file paired with a MAP file:

1. Read the corresponding assembly file to extract all non-include content
2. Replace the TODO placeholder with the following content, in this order:
   a. The `[role="_abstract"]` paragraph — always exactly one paragraph (the short description)
   b. Body content after the abstract — additional paragraphs, admonitions, notes, lists, maintaining the original order from the assembly
   c. Snippet includes — `include::` directives to `snippets/` files (such as unified perspective web console admonitions), placed where they appeared in the assembly body
   d. `[role="_additional-resources"]` section — always last, if present in the assembly
3. Do NOT include in the concept file:
   - Module includes (`ols-*.adoc` with leveloffset) — these go in the MAP file
   - Context save/restore (`ifdef::context[:parent-context:]`, `ifdef::parent-context[:context:]`)
   - `:context:` declarations — the MAP file owns the context
4. DO include the concept file's own `[id="con-<name>_{context}"]` before the title — the AsciiDoc DITA vale style requires an ID on every content file

### Step 6: Resolve xref dependencies

When the content you are migrating (modules or concept body text) contains `xref:` cross-references pointing to IDs that do not yet exist in the MAP structure, you must also migrate the referenced content as a dependency:

1. For each `xref:<target-id>` found in migrated content, check whether `<target-id>` resolves to an existing `[id="..."]` in the JTBD include tree
2. If the target ID is missing, trace it back to the old assembly or module that defines it
3. Use the TOC mapping reference (`.claude/skills/jtbd-map/jtbd-toc-mapping.tsv`) to determine the correct JTBD category and job for the missing content
4. Create or populate the corresponding MAP file and concept file in the correct category directory, adding the module includes that provide the missing ID
5. When a module defines `[id="module-id_{context}"]` and existing xrefs use a hardcoded old context value (e.g., `xref:module-id_ols-configuring-openshift-lightspeed[...]`), set `:context:` to the old value before the module include and restore it after:
   ```asciidoc
   :context: ols-configuring-openshift-lightspeed
   include::modules/<module>.adoc[leveloffset=+1]
   :context: current-map-context
   ```
6. For assembly-level IDs (e.g., `xref:old-assembly-id_old-context[...]`), add a backward-compatible anchor before the concept include in the MAP file:
   ```asciidoc
   [id="old-assembly-id_old-context"]
   ```
7. Repeat until all xref targets in the migrated scope are resolvable

### Step 7: Ensure required attributes

For each modified MAP file, verify:

1. **Mandatory attributes** are present:
   - `:_mod-docs-content-type: MAP` before the ID
   - `[id="<context-value>_{context}"]` before the title
   - `:context: <context-value>` after the title
   - `include::_attributes/common-attributes.adoc[]` after the assembly header
2. **Context uniqueness**: Context values must be unique across all MAP files

### Step 8: Update topic map navigation

After creating or populating MAP files, update `_topic_maps/_topic_map.yml` to reflect the new JTBD navigation structure:

1. Add new category sections with `Distros: openshift-lightspeed`
2. Add topic entries for each MAP file in the category
3. Use the JTBD category names as section `Name` values
4. Use the job navtitle from the TSV as topic `Name` values

### Step 9: Validate

1. Verify that all referenced module files exist: `ls modules/<filename>.adoc`
2. Check for broken xrefs by searching for `xref:` patterns and verifying target IDs exist
3. If available, run the AsciiBinder build: `asciibinder build`
4. Report any errors and suggest fixes

## Architecture reference

### Current structure (modular docs with assemblies)
```
about/
  _attributes -> ../_attributes
  images -> ../images
  modules -> ../modules
  snippets -> ../snippets
  docinfo.xml
  ols-about-openshift-lightspeed.adoc       # Assembly: overview + data privacy
configure/
  ols-configuring-openshift-lightspeed.adoc  # Assembly: LLM config + RBAC + features
  olsconfigure-api.adoc                     # Assembly: API reference
  olsconfigure-rest-api-authentication-configuration.adoc
  ols-configuring-integrating-google-vertex-ai.adoc
install/
  ols-installing-openshift-lightspeed.adoc   # Assembly: Operator installation
operate/
  ols-using-openshift-lightspeed.adoc        # Assembly: using the AI assistant
  ols-interacting-with-the-api.adoc          # Assembly: API interaction
  ols-interact-with-openshift-lightspeed-rest-api.adoc
troubleshoot/
  ols-troubleshooting-openshift-lightspeed.adoc  # Assembly: all troubleshooting
modules/
  ols-*.adoc                                 # All modules (flat, ~136 files)
snippets/
  ols-*.adoc                                 # Snippet includes (~6 files)
_topic_maps/
  _topic_map.yml                             # Navigation structure
```

### New structure (JTBD with MAP files)
```
discover/
  _attributes -> ../_attributes
  images -> ../images
  modules -> ../modules
  snippets -> ../snippets
  docinfo.xml
  ols-evaluate-openshift-lightspeed-capabilities.adoc  # Job MAP
  con-evaluate-openshift-lightspeed-capabilities.adoc  # Job concept
  ols-evaluate-data-privacy-compliance.adoc            # Job MAP
  con-evaluate-data-privacy-compliance.adoc            # Job concept
plan/
  ols-plan-deployment-architecture.adoc                # Job MAP
  con-plan-deployment-architecture.adoc                # Job concept
install/
  ols-installing-openshift-lightspeed.adoc             # Job MAP
  con-installing-openshift-lightspeed.adoc             # Job concept
integrate/
  ols-integrate-with-llms.adoc                         # Job MAP (parent)
  con-integrate-with-llms.adoc                         # Job concept
  ols-integrate-ibm-watsonx.adoc                       # Sub-job MAP
  con-integrate-ibm-watsonx.adoc                       # Sub-job concept
  ols-integrate-openai.adoc                            # Sub-job MAP
  ...                                                  # (one pair per LLM provider)
  ols-extend-ai-with-cluster-data.adoc                 # Job MAP
  con-extend-ai-with-cluster-data.adoc                 # Job concept
  ols-govern-ai-operations.adoc                        # Job MAP
  con-govern-ai-operations.adoc                        # Job concept
get_started/
  ols-interact-with-ai-assistant.adoc                  # Job MAP
  con-interact-with-ai-assistant.adoc                  # Job concept
  ols-improve-ai-accuracy-with-feedback.adoc           # Job MAP
  con-improve-ai-accuracy-with-feedback.adoc           # Job concept
  ols-troubleshoot-cluster-issues.adoc                 # Job MAP
  con-troubleshoot-cluster-issues.adoc                 # Job concept
configure/
  ols-expose-lightspeed-service.adoc                   # Job MAP
  con-expose-lightspeed-service.adoc                   # Job concept
  ols-configure-persistent-cache-storage.adoc          # Job MAP
  ...
secure/
  ols-protect-user-privacy.adoc                        # Job MAP
  con-protect-user-privacy.adoc                        # Job concept
  ols-configure-authentication-access-control.adoc     # Job MAP
  con-configure-authentication-access-control.adoc     # Job concept
develop/
  ols-build-api-integrations.adoc                      # Job MAP
  con-build-api-integrations.adoc                      # Job concept
  ols-look-up-api-specifications.adoc                  # Job MAP
  con-look-up-api-specifications.adoc                  # Job concept
troubleshoot/
  ols-troubleshoot-installation-access.adoc            # Job MAP
  con-troubleshoot-installation-access.adoc            # Job concept
  ols-troubleshoot-model-responses.adoc                # Job MAP
  con-troubleshoot-model-responses.adoc                # Job concept
modules/
  ols-*.adoc                                           # Unchanged — all shared modules
snippets/
  ols-*.adoc                                           # Unchanged — snippet includes
_topic_maps/
  _topic_map.yml                                       # Updated navigation
```

### Category directory setup

When creating a new JTBD category directory, set up:
1. Create the directory: `mkdir <category>/`
2. Create symlinks:
   ```bash
   cd <category>/
   ln -s ../_attributes _attributes
   ln -s ../images images
   ln -s ../modules modules
   ln -s ../snippets snippets
   ```
3. Create `docinfo.xml` with the appropriate title and abstract for the category

### MAP file structure
```asciidoc
:_mod-docs-content-type: MAP
[id="<context-value>_{context}"]
= <Title>
include::_attributes/common-attributes.adoc[]
:context: <context-value>

toc::[]

include::con-<matching-concept>.adoc[leveloffset=+1]

include::modules/<module>.adoc[leveloffset=+1]
include::modules/<sub-module>.adoc[leveloffset=+2]
```

**Mandatory attributes:**
- `:_mod-docs-content-type: MAP`
- `[id="<context-value>_{context}"]`
- `include::_attributes/common-attributes.adoc[]`
- `:context: <context-value>`
- `toc::[]`

**Also allowed:**
- Comments (`// ...`) and blank lines
- `// TODO: include <Topic title>` for topics not yet populated
- Sub-MAP includes for sub-jobs

### Concept file structure
```asciidoc
:_mod-docs-content-type: CONCEPT
[id="con-<name>_{context}"]
= <Title>

[role="_abstract"]
<Short description paragraph.>
```

**Rules:**
- `[id="con-<name>_{context}"]` is required — the ID is derived from the concept filename without the `.adoc` extension (e.g., `con-evaluate-openshift-lightspeed-capabilities.adoc` gets `[id="con-evaluate-openshift-lightspeed-capabilities_{context}"]`). The AsciiDoc DITA vale style requires an ID on every content file.
- No `:context:` declaration — the MAP file owns the context
- Title matches the corresponding MAP file section title

### Key rules
- First include in a MAP (after `toc::[]`) must be a `con-` concept file
- MAP files contain only the mandatory attributes listed above, `include::` directives, comments, and blank lines
- `navtitle` is only added when the module's internal title does not match the desired navigation title (check the TSV Navtitle column vs. the module heading)
- Context values must be unique across all MAP files (IDs derive from context)
- Modules are always referenced from the flat `modules/` directory (no subdirectories)
- When the same module is included in multiple MAP files (e.g., `ols-creating-the-credentials-secret-using-web-console.adoc` in each LLM provider sub-job), each MAP file gets its own include with the appropriate `navtitle` for that provider context

## TOC mapping reference

The complete TOC mapping is available at `.claude/skills/jtbd-map/jtbd-toc-mapping.tsv`. This file maps:
- Categories (L1) to their directory names
- Jobs (L2) and sub-jobs (L3/L4) to their MAP file paths
- Topics to their H2/H3 headings and module `.adoc` file paths
- Navtitles for navigation display

Each level in the TSV hierarchy can correspond to either a MAP file (job with `Is a job? = TRUE`) or a leaf module include (`Is a job? = FALSE`). The skill determines which from the TSV and the actual file structure on disk.

## Categories (9)

Discover, Plan, Install, Integrate, Get Started, Configure, Secure, Develop, Troubleshoot
