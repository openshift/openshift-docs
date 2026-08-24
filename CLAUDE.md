## Skills

- `rhacs-patch-release-notes` — create patch (z-stream) release notes for RHACS from a Jira release version. Run with `/rhacs-patch-release-notes`. Defined in `.claude/skills/rhacs-patch-release-notes/SKILL.md`.

## Best practices when using Claude

### Use AsciiDoc templates

When creating new content, use the following AsciiDoc templates:

**Concept module template:**
```asciidoc
:_mod-docs-content-type: CONCEPT
[id="module-id_{context}"]
= Module title

[role="_abstract"]
Write a short introductory paragraph that provides an overview of the module.
The text that immediately follows the `[role="_abstract"]` tag is used for search metadata.

// Module content here
```

**Procedure module template:**
```asciidoc
:_mod-docs-content-type: PROCEDURE
[id="module-id_{context}"]
= Module title

[role="_abstract"]
Short introductory paragraph that provides an overview of the procedure.

.Prerequisites

* List procedure prerequisites one per bullet

.Procedure

. Start each step with an active verb.
. Use numbered steps for procedures.

.Verification

* Provide verification methods for the procedure.
```

**Reference module template:**
```asciidoc
:_mod-docs-content-type: REFERENCE
[id="module-id_{context}"]
= Module title

[role="_abstract"]
Short introductory paragraph that provides an overview of the reference content.

.Labeled list
Term 1:: Definition
Term 2:: Definition

.Table
[options="header"]
|====
|Column 1|Column 2|Column 3
|Row 1, column 1|Row 1, column 2|Row 1, column 3
|====
```

### Request code verification

Ask Claude to:
- Verify code examples against the actual product behavior
- Check that API signatures match the implementation
- Validate that configuration examples are current

## Documentation standards for this project

### Avoid parentheticals

Use alternatives to parentheses:

**For multiple items:** Use a colon.
- [CORRECT] You have at least 4 GPUs: 2 for prefill, 2 for decode recommended.
- [INCORRECT] You have at least 4 GPUs (2 for prefill, 2 for decode recommended).

**For single items or examples:** Incorporate naturally into the sentence.
- [CORRECT] You have a model such as Mixtral-8x7B or Mixtral-8x22B.
- [CORRECT] NVIDIA GPUs with GPUDirect RDMA support, Pascal architecture or later.
- [INCORRECT] You have a model (for example, Mixtral-8x7B).

**Exception:** Acronym definitions remain acceptable.
- [CORRECT] Large Language Model (LLM)

### Headings

Use imperatives (not gerunds) for the following content:

- Procedures
- Jobs when child topics contain any procedures, even if the job also contains concepts or references

**Important:**
- Do NOT use gerunds
- Do not mix imperatives and gerunds in headings or in sections
- If a job contains only conceptual or reference material, the headings should all be nouns or noun phrases

**For conceptual and reference information:** Use noun phrases for headings.

Examples of correct noun phrase headings:
- Platform and application integration
- Build strategies
- Failure domain requirements
- What to expect when you install an Operator

**Avoid generic terms:** Avoid using terms like "Introduction" and "About". Be more specific when you can be.

- [CORRECT] Models-as-a-Service overview
- [CORRECT] Prerequisites for installing MaaS
- [INCORRECT] Introduction to MaaS
- [INCORRECT] About MaaS

### Next steps sections

- No introductory sentence
- Jump straight to the bullet list

### Modular content

- Follow the [Red Hat modular documentation reference guide](https://redhat-documentation.github.io/modular-docs/)
- Follow the [Red Hat supplementary style guide](https://redhat-documentation.github.io/supplementary-style-guide/)
- Extract reusable sections into standalone modules
- Prefer modular structure over monolithic assemblies for maintainability and reuse

### AsciiDoc conventions

- Use sentence case for headings
- Use a single heading per module
- Include `id` attributes for all major sections with `_{context}` suffix
- Use `source` blocks with appropriate language highlighting
- Include `include::` statements for reusable content
- Add `xref:` links between related documentation
- Follow the Red Hat Style supplementary guide when drafting content
- Do not use file prefixes to denote topic type (avoid `con-`, `proc-`, `ref-` prefixes)
- When creating new files, ensure that one of the following attributes is applied at the top of the file:
    - `:_mod-docs-content-type: ASSEMBLY`
    - `:_mod-docs-content-type: PROCEDURE`
    - `:_mod-docs-content-type: CONCEPT`
    - `:_mod-docs-content-type: REFERENCE`
    - `:_mod-docs-content-type: SNIPPET`
- Use AsciiDoc description lists for discrete paragraphs focused on a single idea
- Use AsciiDoc NOTE and IMPORTANT admonitions where appropriate:

```asciidoc
[NOTE]
====
Add note content here.
====
```

```asciidoc
[IMPORTANT]
====
Add important note content here.
====
```

#### Links and additional resources

**In sentences:** No colons, link at end, period after link, commas are OK.
- [CORRECT] For more information, see link:...[Link Text].
- [INCORRECT] For more information: link:...[Link Text].

**In bullet lists for references or next steps:** Entire bullet is the link, no period at end.
- [CORRECT] * link:...[Link Text]
- [INCORRECT] * Descriptive text: link:...[Link Text]
- [INCORRECT] * link:...[Link Text].

**Additional resources:** Single flat list, no category subdivisions.
- [CORRECT] Single flat list of all links
- [INCORRECT] Category:: with nested lists

#### Header levels

- Maximum 2 levels: = (level 1) and == (level 2) only
- No deeper nesting (=== or beyond)
- For granular sections: Use introductory sentences instead of level 3+
headers

#### Flattening nested procedures

- Keep to 2 levels maximum (`.` and `..`)
- Flatten any triple nesting (`...`), incorporate into double-nested or convert
to separate steps

### Code examples

All code examples should be tested and current. Include both minimal and complete examples where appropriate.

#### Explaining code elements

Do not use AsciiDoc callouts. Instead, use one of these approaches:

**For single elements**
Use a simple sentence after the code block:

Example AsciiDoc:

```asciidoc
[source,terminal]
----
$ hcp create cluster <platform> --help
----
+
Use the `hcp create cluster` command to create and manage hosted clusters. The supported platforms are `aws`, `agent`, and `kubevirt`.
```

**For multiple parameters/variables**
- Use a definition list to explain multiple options, parameters, user-replaced values, placeholders, or UI elements.
    - List the parameters or variables in the order in which they appear in the code block.
    - Introduce definition lists with "where:" and begin each variable description with "Specifies".

Example AsciiDoc:

```asciidoc
[source,yaml,subs="+attributes,+quotes"]
----
$ cat <<EOF | oc -n product create -f -
apiVersion: v1
kind: Secret
metadata:
 name: <my_product_database_certificates_secrets>
  # ...
EOF
----
+
where:

`<my_product_database_certificates_secrets>`:: Specifies the name of the certificate secret.
```

**For YAML files or multiple lines of code**
* Use a bulleted list to describe the structure of a sample YAML file or explain multiple lines of code in a code block.
**  List the explanations in the order in which they appear in the code block.
** Use the bullet format that makes the most sense for your explanations.

Example AsciiDoc:

```asciidoc
[source,yaml]
----
apiVersion: tekton.dev/v1
# ...
spec:
  workspaces:
  - name: shared-workspace
  params:
# ...
  tasks:
    # ...
    workspaces:
    - name: source
      workspace: shared-workspace
# ...
----
+
* `spec.workspaces` defines the list of pipeline workspaces shared between the tasks defined in the pipeline.
* `spec.tasks.workspaces` defines the list of task workspaces used in the `build-image` and `apply-manifests` tasks.
```

### Product attributes

Always use product attributes from `modules/common-attributes.adoc`:

## Review checklist

When Claude helps generate or improve documentation:

- [ ] Technical accuracy verified against current product behavior
- [ ] AsciiDoc formatting follows project conventions
- [ ] Cross-references and includes work correctly
- [ ] Code examples are complete and tested
- [ ] Content matches the intended audience level
- [ ] Product attributes used instead of hardcoded names
