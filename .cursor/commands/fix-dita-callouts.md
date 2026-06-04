# fix-dita-callouts

Resolve **AsciiDocDITA.CalloutList** violations in one or more `.adoc` files by removing callout markers and replacing trailing callout lists with DITA-safe prose.

Use this command on its own, or when **`/fix-dita-vale`** reports **CalloutList** (that command defers callout work here).

**Formerly:** `/resolve-dita-callouts`

**Repository:** Run from the **openshift-docs** repository root.

## Primary reference

**Read and follow:** `.cursor/resources/dita-migration/callout-rewrite-ruleset.md`

That ruleset is derived from [openshift/openshift-docs#102276](https://github.com/openshift/openshift-docs/pull/102276) (*Callout rewrite examples*) in **before → after** format. It defines patterns A–F, term naming, **Specifies** wording, and anti-patterns.

Supplemental context only if a case is not covered: [PR #102276 files changed](https://github.com/openshift/openshift-docs/pull/102276/files).

## Invocation

The user supplies one or more `.adoc` file paths (required). If no path is given, ask which file(s) to process.

## Step 1: Find callouts

Scan each file for:

- Inline markers in code blocks: `# <1>`, `<1>` at end of lines, `#<6>`, and similar
- Trailing numbered callout lines after a code block: `<1>`, `<2>`, …

Optionally confirm with Vale:

```bash
vale --config=.vale.ini --output=line "<path>" | grep CalloutList
```

## Step 2: Strip markers

Remove every callout marker from `[source,...]` blocks. Do not leave `# <n>` comments that exist only as callouts.

## Step 3: Replace callouts (ruleset)

For each block, open **`.cursor/resources/dita-migration/callout-rewrite-ruleset.md`** and:

1. Count how many callouts applied to that example.
2. Pick **Pattern A, B, C, D, E, or F** from the ruleset decision table.
3. Apply the matching **before → after** structure. Do not leave numbered `<n>` lists.

### Preserve wording (required)

Read **Preserve source wording** and **Starting definitions with Specifies** in the ruleset first. This command is **not** an editorial rewrite.

- **Do:** remove markers; restructure into `where:`, a lead-in sentence, or bullets; set the `::` term (full path, placeholder, or flag).
- **Do:** for Pattern E, write a **grammatically correct**, **concise** sentence that starts with **Specifies**. The `::` term already names the field or section—state what it means or does; do not repeat **this specification**, **the \`strategy\` section**, **the \`runPolicy\` field**, or **this field** (for example, `This specification creates a new BuildConfig named …` → `Specifies a new \`BuildConfig\` named …`; `The \`strategy\` section describes the build strategy …` → `Specifies the build strategy …`). See ruleset *Avoid redundant framing*.
- **Do:** for **If this field is set to** callouts, reorder minimally (for example, `Specifies that {lvms} wipes… when set to \`true\`.`).
- **Do:** for callouts that began with **Optional:** (per [PR #102276](https://github.com/openshift/openshift-docs/pull/102276)), drop **Optional:**, rewrite with **Specifies** (multiple sentences OK). If **optional** does not appear in the new text, end with **This parameter is optional.** or **This field is optional.** / **This value is optional.** Do not add that sentence if **optional** is already in the description.
- **Do not:** paraphrase, shorten, improve, or replace the author’s explanation, examples, or links beyond that minimal fix.
- **Do not:** write **Specifies that you can specify**, **Specifies setting this field to**, or other redundant **Specifies** + **field** / **specify** combinations (see ruleset table).

Copy each original callout sentence, then apply only the minimum edits required for DITA structure and a natural **Specifies** opening.

### OpenShift rules (in addition to PR #102276)

- **Single callout:** Use Pattern **A, B, C, or D** only—`+` on its own line, then the lead-in sentence (for example `` `</path/to/example-ca.crt>` is the path to … `` or `Replace \`<secret>\` with …`). **Do not** use `where:` or `where::` for one callout ([PR #102276](https://github.com/openshift/openshift-docs/pull/102276) `customize-certificates-replace-default-router.adoc`).
- **`where:` / description list (Pattern E, 2+ callouts):** After the closing `----`, use `+`, then **`where:` on its own line** (not `where::`), then a blank line, then each `` `term`:: Specifies … `` on its own line—**no** leading `*`. Do **not** use `* \`term\`::`; `*` plus `::` breaks AsciiDoc list parsing and is not in [PR #102276](https://github.com/openshift/openshift-docs/pull/102276). Pattern **F** (output only) uses `*` bullets with plain sentences (for example `` * `my-lws-0` is the leader pod for the first group. ``), never `::`.
- **Terms (full notation):** Use the **full dotted path** for the left side of `::` (for example `` `spec.backupLocations.velero.provider` ``), built from the YAML in the example. Do **not** use a short key alone (`provider`, `bucket`).
- **Placeholders as terms:** Use `` `<bucket_name>` `` (or similar) as the term **only** when **every** callout in that example block documents user-defined placeholders and no real field paths are mixed in. Otherwise use the full path even when the value in YAML is `<bucket_name>`.
- **Procedure steps:** Connect replacements with `+` when they follow a procedure step (see ruleset *Connection to procedure steps*).
- **Conditionals:** Never add or remove `ifdef`, `ifndef`, `ifeval`, or other conditional directives. Keep every existing conditional block, its boundaries, and nesting exactly as in the source file; only change callout markers and callout replacement prose inside those blocks.

## Step 4: Re-run Vale and report

```bash
vale --config=.vale.ini --output=line "<path>" | grep CalloutList || true
```

Summarize:

- Files changed and which pattern(s) you used per block
- Remaining **CalloutList** hits
- Any ambiguous callouts that need a human choice

Do **not** commit unless the user asks.

## Execution notes

- Change only callout-related lines; do not rewrite unrelated procedure text.
- **Never make drastic language changes** to callout explanations; if unsure, keep the original sentence body and change only the opening (**Specify** → **Specifies**, or the smallest edit so **Specifies** starts a complete sentence) plus structure/term.
- Preserve attributes (`{product-title}`, `{oadp-short}`, etc.) and existing IDs.
- **Never add or remove conditionals** (`ifdef`, `ifndef`, `ifeval`, and similar). Restructure callout text only within the conditional blocks already present.
- Do **not** remove `.Procedure` or valid `.Example …` block titles; see `/fix-dita-vale` for those rules.
