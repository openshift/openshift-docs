---
name: jtbd-coverage-map
description: >
  Cross-reference a JTBD mapping CSV with existing documentation to produce a
  coverage map showing which modules belong to each job. Use when starting JTBD
  implementation for a new feature area or distro.
disable-model-invocation: true
---

# JTBD Coverage Map

Generate a coverage analysis that maps existing documentation modules to the
jobs defined in a JTBD mapping spreadsheet.

## Inputs

You need two things from the user before proceeding:

1. **JTBD CSV file path** -- a CSV export of the JTBD mapping spreadsheet
   (e.g., `~/Downloads/JTBD-Install.csv`)
2. **Documentation directory** -- the path to the relevant docs directory in
   the repo (e.g., the assembly/module directories that cover this feature area)

If the user invoked this skill without providing both, ask for them.

## What to produce

Create a CSV file (saved to the user's working directory) with the following
structure. Use a tab named "Modules per Job" as the conceptual grouping:

### Per job (one section per job from the CSV):

- **Job name** -- from the CSV
- **Job statement** -- from the CSV
- **Modules** -- list of existing modules (by filename) that should be included
  in this job, determined by cross-referencing the job's scope with the content
  of existing assemblies and modules
- **Coverage status** for each module:
  - `full` -- module content fully addresses the job step
  - `partial` -- module is relevant but doesn't fully cover the job step
  - `gap` -- no existing module covers this aspect of the job

### Summary section:

- **Journey gaps** -- jobs or job steps with no corresponding modules at all
- **Duplicate jobs** -- jobs that substantially overlap in module coverage
- **Unmapped assemblies** -- existing assemblies whose modules don't map to any job

## How to analyze

1. Read the CSV to extract all jobs and their job statements
2. Read the existing assemblies in the documentation directory to build a list
   of all modules and their content summaries
3. For each job, identify which existing modules are relevant based on:
   - Topic alignment between the job statement and module content
   - Procedural steps that match the job's intent
   - Prerequisite or context modules that support the job
4. Flag gaps where a job has no suitable modules
5. Flag assemblies whose modules don't map to any job

## Output format

Save the result as a CSV file. Tell the user the output path and summarize:
- Total jobs found
- Jobs with full coverage
- Jobs with gaps
- Number of unmapped assemblies

The user will review and adjust this coverage map before proceeding to
`/jtbd-create-jobs` to generate the actual map files.
