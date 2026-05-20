# prepare-dita

**Master command:** prepare **one assembly (and its includes)** or **one standalone module** for DITA migration by running sub-commands in order, then reporting final Vale status.

**Formerly:** `/fix-dita-assembly`

**Repository:** Run from the **openshift-docs** repository root (where `.vale.ini` lives).

## Invocation

The user supplies one `.adoc` path (required), for example:

- **Assembly:** `installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc`
- **Single module:** `modules/installation-azure-stack-hub-config-yaml.adoc`
- `@modules/installation-azure-stack-hub-config-yaml.adoc`

If no path is given, ask which file to process.

## Prerequisites

1. `vale sync` has been run at the repo root (see `.cursor/README.md`).
2. `.cursor/resources/` is populated (`./scripts/sync-cursor-dita-resources.sh`).

## Scope: which files to process

Determine scope from the path and file content:

| Mode | When | Files in scope |
| --- | --- | --- |
| **Single module** | Path is under a `modules/` directory (for example `modules/…`, `cloud_experts_osd_tutorials/modules/…`), **or** the file has no active (non-commented) `include::` lines | **Only** the supplied file |
| **Assembly** | Any other path **and** the file has at least one active `include::path.adoc[…]` | The assembly **plus** each included module (see below) |

**Assembly include discovery** (assembly mode only):

1. Read the assembly `.adoc` file.
2. Collect every file to process:
   - The assembly itself
   - Each active `include::path.adoc[…]` (resolve relative paths from the assembly’s directory)
   - Ignore commented includes (`//include::`)
3. Process in order: **assembly first**, then included modules **top to bottom** as they appear in the assembly.

**Single module mode:** Do **not** follow `include::` in the module—even if the module includes other files. Fix only the file the user named.

Pass the file list to each sub-command below.

## Workflow (run in order)

### 1. `/fix-dita-vale`

Run **`/fix-dita-vale`** on every file in scope.

When any file reports **AsciiDocDITA.CalloutList**, run **`/fix-dita-callouts`** on those files before continuing (or re-run step 1 after callouts are fixed).

### 2. `/write-dita-abstract` (required for topics)

Run **`/write-dita-abstract`** on **every** assembly and module in scope that has a level-1 title (`ASSEMBLY`, `CONCEPT`, `PROCEDURE`, or `REFERENCE` per `:_mod-docs-content-type:`).

**Do not** only add `[role="_abstract"]` to the existing first paragraph. **Rewrite** the short description using the `/write-dita-abstract` command (read the parent assembly for modules). Vale may stop reporting **ShortDescription** once the role is present even when the prose is still a weak or mis-placed intro—this step fixes that.

- Place `[role="_abstract"]` on its own line immediately after the `=` title (blank line before the abstract paragraph).
- Keep any necessary introductory prose **after** the abstract, not inside it.
- Validate with `python3 .cursor/resources/style-guide/check-ibm-style.py --no-spell` (stdin) before saving.

Skip only snippet files or other paths with no `:_mod-docs-content-type:` topic marker.

### 3. `/fix-content-type`

Run **`/fix-content-type`** on every file in scope. This step **only** verifies and corrects **`:_mod-docs-content-type:`** when it does not match the content. It does **not** write or rewrite abstracts (step 2 owns that).

### 4. `/check-doc-style`

Run **`/check-doc-style`** on every file in scope. Follow that command’s guidance. Re-run until each file is clean or only acceptable false positives remain (document any you skip).

## Final step: re-run Vale and report

1. From the **repository root**, re-run Vale on each file in scope:

   ```bash
   vale --config=.vale.ini --output=line "<path>"
   ```

2. Summarize for the user:
   - **Mode used** (single module vs assembly + N includes)
   - Files changed across all steps (with brief note per file)
   - Remaining Vale errors/warnings that need human review
   - Remaining style-guide issues (if any)
   - Any rules skipped per OSDOCS “wait for instruction”
3. Do **not** commit unless the user asks.

## Execution notes

- Work through all files in scope in one session when possible.
- Prefer minimal, correct diffs; do not rewrite unrelated prose.
- Preserve attribute names (`{product-title}`, `{productname}`, etc.) and existing IDs unless a rule requires a change.
- For large assemblies, you may process in batches but must report overall status when done.

## Example: discover includes (assembly mode only)

```bash
grep -E '^(//)?include::' installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
```

## Sub-commands (also usable standalone)

| Command | Purpose |
| --- | --- |
| `/fix-dita-vale` | Run Vale and fix AsciiDocDITA rule violations |
| `/fix-dita-callouts` | Apply `callout-rewrite-ruleset.md`; preserve callout wording and all conditionals; Pattern E opens with **Specifies** (minimal opening edit when needed) |
| `/fix-content-type` | Correct **`:_mod-docs-content-type:`** only when it mismatches content (no abstract writing) |
| `/check-doc-style` | IBM/RH supplementary and OCP structural checks |
| `/write-dita-abstract` | **Required in step 2**—rewrite short descriptions (not label-only); also used when Vale reports **ShortDescription** |
