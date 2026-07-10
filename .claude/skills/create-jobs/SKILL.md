---
name: create-jobs
description: Create L2 job topics and assembly from JTBD CSV with docs-writer agent
triggers: []
---

# create-jobs

Create L2 reference topics and assembly file from JTBD CSV mapping, using docs-writer agent for professional descriptions.

## Usage

When invoked, ask the user for:
1. **CSV file path** - Full path to JTBD mapping CSV (if not provided, search in ~/Downloads for "Builds JTBD*" or "Job Mapping*")
2. **Category** - Category name (e.g., "Configure", "Develop", "Secure", "Optimize")

Then automatically:
- Generate branch name: `builds-{category-lowercase}-l2-topics`
- Parse the CSV for the specified category
- Copy any required existing modules from the `builds-configure-l2-topics` branch
- Create all L2 modules and assembly file

## Workflow

### 1. Create git branch
Automatically generate branch name from category:
```bash
git checkout -b builds-{category-lowercase}-l2-topics main
```

### 2. Parse CSV
Read the CSV and extract for the given category:
- L1 job (assembly title)
- L2 sections (reference modules)
- Topics under each L2 (content includes)
- File paths

### 3. Create L2 reference modules

For each L2 section, create `modules/ob-{section-id}.adoc`:

```asciidoc
// This module is included in the following assembly:
//
// * {assembly-path}

:_mod-docs-content-type: REFERENCE
[id="ob-{section-id}_{context}"]
= {L2 Section Title}

[role="_abstract"]
{ABSTRACT - call docs-writer agent to generate}

This section covers the following topics:

* {Topic 1 navtitle}
* {Topic 2 navtitle}
* ...
```

**For the abstract**, call docs-writer agent:
```
Write a 2-3 sentence abstract for a REFERENCE module titled "{L2 title}".
This section covers: {comma-separated topic list}.
The abstract should explain what this section helps users accomplish.
Format: AsciiDoc. Keep it concise and user-focused.
```

### 4. Create assembly file

Create `{assembly-dir}/{assembly-file}.adoc`:

```asciidoc
:_mod-docs-content-type: ASSEMBLY
[id="{assembly-id}"]
= {L1 Job Title}

include::_attributes/common-attributes.adoc[]
:context: {assembly-id}

toc::[]

[role="_abstract"]
{ASSEMBLY ABSTRACT - call docs-writer agent to generate}

include::modules/ob-{l2-section-1-id}.adoc[leveloffset=+1]

include::modules/{topic-1-file}.adoc[leveloffset=+2]

include::modules/{topic-2-file}.adoc[leveloffset=+2]

...

include::modules/ob-{l2-section-2-id}.adoc[leveloffset=+1]

include::modules/{topic-1-file}.adoc[leveloffset=+2]

...

// [role="_additional-resources"]
// == Additional resources
```

**For assembly abstract**, call docs-writer agent:
```
Write a 2-3 sentence abstract for an ASSEMBLY titled "{L1 title}".
This assembly covers {number} main sections: {comma-separated L2 titles}.
The abstract should explain the overall purpose and scope.
Format: AsciiDoc. Keep it concise and user-focused.
```

### 5. Copy required existing modules

Check if the assembly references modules that exist on other branches (e.g., `builds-configure-l2-topics`):
```bash
git show origin/builds-configure-l2-topics:modules/ob-{module-name}.adoc > modules/ob-{module-name}.adoc
```

Copy all referenced modules that don't exist on the current branch to avoid "file not found" errors.

### 6. Report results

Show:
- Branch created (auto-generated name)
- Number of L2 modules created
- Number of existing modules copied
- Assembly file path
- All files verified and ready
- Next steps: review abstracts, verify files, commit changes

## Important Notes

- **Auto-detect CSV**: If file path not provided, search ~/Downloads for "Builds JTBD*" or "Job Mapping*" files
- **Auto-generate branch**: Use pattern `builds-{category-lowercase}-l2-topics`
- **Copy dependencies**: Automatically copy referenced modules from other branches to avoid build errors
- **Red markers in CSV**: Topics marked in red in the original Excel file indicate missing L2 titles (handle gracefully)
