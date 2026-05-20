# fix-content-type

Verify that each file’s **`:_mod-docs-content-type:`** matches the actual content, and **fix only that attribute** when it is wrong.

Use on its own or as part of **`/prepare-dita`** (after **`/write-dita-abstract`** handles short descriptions).

**Formerly:** `/align-content-type-with-template`

**Repository:** openshift-docs repository root.

## Invocation

The user supplies one or more file paths (required), for example:

- `@modules/agent-service-failure.adoc`
- An assembly and its included modules

If no path is given, ask which file(s) to process.

## Templates (reference only)

Read the template for the **correct** type to decide what the content should be—not to rewrite the topic.

| Type | Template (repo-relative) |
| --- | --- |
| ASSEMBLY | `.cursor/resources/dita-migration/templates/TEMPLATE_ASSEMBLY_a-collection-of-modules.adoc` |
| CONCEPT | `.cursor/resources/dita-migration/templates/TEMPLATE_CONCEPT_concept-explanation.adoc` |
| PROCEDURE | `.cursor/resources/dita-migration/templates/TEMPLATE_PROCEDURE_doing-one-procedure.adoc` |
| REFERENCE | `.cursor/resources/dita-migration/templates/TEMPLATE_REFERENCE_reference-material.adoc` |

## What this command does

1. Read `:_mod-docs-content-type:` and the file body.
2. Decide the **correct** type from content signals (see table below).
3. If the declared type is wrong, change **only** `:_mod-docs-content-type:` to the correct value.
4. Report other template gaps **without fixing them** (see *Out of scope*).

## How to infer the correct type

| Type | Typical signals |
| --- | --- |
| **ASSEMBLY** | Level-1 assembly title; `toc::[]`; sequence of `include::` modules; little or no procedural body |
| **CONCEPT** | Explains *what* or *why*; no `.Procedure` / numbered install steps |
| **PROCEDURE** | `.Procedure` (or clear numbered steps); task-oriented “how to” |
| **REFERENCE** | Lookup material (parameters, fields, tables, YAML samples); not a step-by-step task |

When signals conflict (for example, reference YAML **and** `.Procedure`), prefer the type that matches how the assembly uses the module. Read the parent assembly comment at the top of the module if present.

## What to fix (only this)

```asciidoc
:_mod-docs-content-type: PROCEDURE
```

Change that line when it does not match the content. **Do not edit** titles, abstracts, steps, or examples in this command.

## Out of scope — do not fix here

| Item | Use instead |
| --- | --- |
| **`[role="_abstract"]` / short description text** | **`/write-dita-abstract`** only |
| Blank line after `=` title | **`/write-dita-abstract`** or **`/fix-dita-vale`** |
| Callouts, collapsibles, Vale/DITA rules | **`/fix-dita-vale`**, **`/fix-dita-callouts`** |
| IBM/RH/OCP style prose | **`/check-doc-style`** |
| `[id="…"]`, nested `===` sections, assembly include layout | Report for human review; fix only if the user asks |

If `[role="_abstract"]` is missing, note in the report: *Run `/write-dita-abstract` on this file* — **do not** add or rewrite the abstract in this pass.

## Report

Summarize:

- Files where **`:_mod-docs-content-type:` was corrected** (old → new, one-line reason)
- Files where the declared type **already matched** the content
- **Advisory only:** missing abstract, structural issues that need another command or human review

Do **not** commit unless the user asks.
