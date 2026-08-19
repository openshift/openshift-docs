---
name: jtbd-create-jobs
description: >
  Create JTBD job map files in maps/jobs/ and wire them into a distro category
  map, using a coverage map CSV and existing repo modules. Use after
  /jtbd-coverage-map has been run and the coverage map has been reviewed.
disable-model-invocation: true
---

# JTBD Create Jobs

Create AsciiDoc job map files and wire them into category maps based on a
reviewed JTBD coverage map.

## Inputs

You need three things from the user before proceeding:

1. **Coverage map CSV** -- the reviewed output from `/jtbd-coverage-map`
   (or a manually prepared equivalent) that lists modules per job
2. **Distro name** -- which distro this is for (e.g., `ocp`, `rosa`,
   `microshift`). This determines the category map directory under `maps/`.
3. **Category name** -- which category these jobs belong to (e.g., `install`,
   `configure`, `upgrade`). This is the category map file the jobs will be
   included in.

If the user invoked this skill without providing all three, ask for them.

## Reference: existing structure

The maps directory structure is:

```
maps/
  jobs/                          # shared job maps (all distros)
    modules/                     # shared modules used by job maps
    prepare-your-environment-mirroring.adoc   # example job map
  microshift/                    # distro-specific category maps
    navigation.adoc              # top-level nav
    install.adoc                 # category map that includes job maps
```

Here is a real example of each file type:

### Job map file (`maps/jobs/prepare-your-environment-mirroring.adoc`):

@maps/jobs/prepare-your-environment-mirroring.adoc

### Category map with job includes (`maps/microshift/install.adoc` from the JTBD branch):

```asciidoc
:_mod-docs-content-type: MAP

= Install

include::jobs/prepare-your-environment-mirroring.adoc[leveloffset=+1,chunk="to-content",navtitle="Prepare your environment (mirroring)"]

include::jobs/install-with-image-mode-rhel.adoc[leveloffset=+1,navtitle="Install with image mode for RHEL"]
```

### Intro concept module (`maps/jobs/modules/microshift-mirror-container-images.adoc`):

@maps/jobs/modules/microshift-mirror-container-images.adoc

## Procedure: do one first, then replicate

**Do NOT create all jobs at once.** Follow this iterative approach:

### Step 1: Create the first job

Pick the first non-hidden job from the coverage map and create it:

1. Create a new job map file in `maps/jobs/` named after the job
   (kebab-case, e.g., `prepare-your-environment-mirroring.adoc`)

2. The job map file must:
   - Start with `:_mod-docs-content-type: MAP`
   - Include modules from the coverage map using relative paths to
     `modules/` (for modules in `maps/jobs/modules/`) or absolute paths
     from repo root for modules elsewhere
   - Use `leveloffset=+0` for the first module and `leveloffset=+1` for
     subsequent modules
   - Use `toc="no"` on all include statements

3. **Intro concept module**: every job needs one as its first include.
   - If a suitable existing concept module exists, use it as the first
     include with `leveloffset=+0,toc="no"`
   - If no suitable intro exists, create a new concept module in
     `maps/jobs/modules/` with:
     - Content type: CONCEPT
     - A concise 1-2 sentence short description based on the Job Statement
     - The `[role="_abstract"]` attribute
   - The first module in the job map gets `chunk="to-content"` when
     included in the **category map** (not in the job map itself)

4. Add the job to the category map at
   `maps/<distro>/<category>.adoc`:
   ```asciidoc
   include::jobs/<job-name>.adoc[leveloffset=+1,chunk="to-content",navtitle="<Job display name>"]
   ```

### Step 2: Show and confirm

Present the created job map and category map entry to the user. Explain
what modules were included and why. Wait for the user to review and
confirm before continuing.

### Step 3: Replicate for remaining jobs

Only after the user confirms the first job looks good, create the remaining
jobs following the same pattern. For each job:

1. Create the job map file in `maps/jobs/`
2. Create an intro concept module if needed
3. Add the include to the category map

Create the distro directory under `maps/` if it doesn't already exist
(e.g., `maps/ocp/`).

### Step 4: Summary

After all jobs are created, provide a summary:
- List of job map files created
- List of new intro concept modules created
- The updated category map content
- Any jobs from the coverage map that were skipped and why

## Important conventions

- Job map filenames use kebab-case matching the job name
- All modules in job maps use `toc="no"` in their include attributes
- The `chunk="to-content"` attribute goes on the job include in the
  **category map**, not on individual module includes within the job map
- `navtitle` in the category map should match the human-readable job name
- If the coverage map flags a job as having gaps (missing modules), note
  this to the user rather than silently skipping content
