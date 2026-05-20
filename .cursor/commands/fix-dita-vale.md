# fix-dita-vale

Resolve **AsciiDocDITA Vale** errors and warnings on one or more `.adoc` files so content is ready for DITA migration. Use this command on its own or as part of **`/prepare-dita`**.

**Formerly:** `/asciidoctor-dita-vale-resolution`

**Repository:** Run from the **openshift-docs** repository root.

## Invocation

The user supplies one or more file paths (required), for example:

- `@modules/example.adoc`
- A directory of `.adoc` files

If no path is given, ask which file(s) to process.

## Prerequisites

1. `vale sync` at the repo root.
2. `.cursor/resources/` populated (`./scripts/sync-cursor-dita-resources.sh`).

## Step 1: Run Vale (AsciiDocDITA)

From the **repository root**, for each file:

```bash
vale --config=.vale.ini --output=line "<path>"
```

Record every **error** and **warning** with: file path, line, rule name (e.g. `AsciiDocDITA.ShortDescription`), and message.

## Step 2: Fix Vale issues (per rule)

Primary references:

- **OSDOCS PDF:** `.cursor/resources/dita-migration/OSDOCS-Content updates in preparation for migrating to DITA-190526-144719.pdf` (use `pdftotext` when you need rule-specific “Action to take” detail)
- **AsciiDocDITA rules:** https://github.com/jhradilek/asciidoctor-dita-vale?tab=readme-ov-file#available-rules

### Rule-specific handlers

| Vale rule | Action |
| --- | --- |
| **AsciiDocDITA.ShortDescription** | Run the full **`/write-dita-abstract`** workflow for that file—**do not** only add `[role="_abstract"]` to the existing first paragraph. Rewrite a proper short description (module: read the parent assembly first). Place `[role="_abstract"]` on its own line immediately after the `=` title, with a blank line before the abstract text; move any leftover intro to the body below the abstract. Validate with `python3 .cursor/resources/style-guide/check-ibm-style.py --no-spell` (stdin). |
| **AsciiDocDITA.CalloutList** | Run **`/fix-dita-callouts`** (see `callout-rewrite-ruleset.md` for full dotted path terms). Do not convert callouts here unless the user asks for a quick inline fix. |
| **AsciiDocDITA.AuthorLine** | Add a blank line between the `=` title and the following line. For assemblies, confirm TOC is not broken. |
| **AsciiDocDITA.BlockTitle** | **Never remove `.Procedure`.** It is required for DITA tasks and must stay in procedure modules. **`.Example output`** and similar example block titles (for example `.Example \`manifest.yaml\` file`) are allowed when the **next line is not a lone `+`**—remove only that stray `+`, not the block title. Remove other disallowed floating block titles per OSDOCS PDF (lead-in sentence or `==` heading). Image captions like `image:file.png[Caption]` are allowed. |
| **AsciiDocDITA.ExampleBlock** | Examples must not sit inside `[%collapsible]` / `====` wrappers or other blocks. Remove collapsible wrappers; keep the example block title and `[source,...]` block. Ensure no lone `+` sits between an example block title and `[source,...]`. |
| **AsciiDocDITA.NestedSection** | Split `===` (and deeper) sections into separate module files, or flatten to `==` only within a single topic. |
| **AsciiDocDITA.AssemblyContents** | Move prose between/after `include::` into a module; assembly may only have title, abstract, includes, and Additional resources. |
| **AsciiDocDITA.DocumentId** / **DocumentID** | Ensure `[id="..."]` immediately precedes the `=` title. |
| **AsciiDocDITA.ContentType** | Set `:_mod-docs-content-type:` to `ASSEMBLY`, `CONCEPT`, `PROCEDURE`, or `REFERENCE`. |
| **AsciiDocDITA.DiscreteHeading** | Replace `[discrete]` headings with description lists, `==` sections, or a new module. |
| **AsciiDocDITA.LineBreak** | Replace ` +` hard line breaks with separate paragraphs or the table `a` operator. **Also:** when **`.Example output`** (or another example block title) is immediately followed by a lone `+` on the next line, remove that `+` line only—do not remove the example block title. |
| **AsciiDocDITA.TaskContents** / **TaskTitle** / **TaskStep** / **TaskDuplicate** | Align procedure modules with `.cursor/resources/dita-migration/templates/TEMPLATE_PROCEDURE_doing-one-procedure.adoc`. |
| **AsciiDocDITA.AdmonitionTitle** | Remove titles on admonition blocks. |
| **AsciiDocDITA.ConceptLink** | Move in-body xrefs/links to `== Additional resources` where practical. |
| Other rules | Follow OSDOCS PDF “Action to take”; skip “no action required” or “tiger team” items unless the user asks. |

## Step 3: Re-run Vale and report

1. Re-run `vale --config=.vale.ini --output=line` on each file processed.
2. Summarize: files changed, remaining issues, skipped rules.
3. Do **not** commit unless the user asks.

## Execution notes

- Prefer minimal, correct diffs.
- Preserve `{product-title}` and existing IDs unless a rule requires a change.
- **ShortDescription:** Label-only fixes are insufficient. Always invoke **`/write-dita-abstract`** (see that command). **`/prepare-dita`** runs **`/write-dita-abstract`** on every topic in scope even when Vale no longer reports **ShortDescription**.
