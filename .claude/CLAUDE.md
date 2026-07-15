# OCP Docs PR and Merge Review Checklist

Use this checklist when reviewing pull requests for OpenShift documentation.

## PR Requirements

### Mod Docs Templates Adherence
- Modules must follow one of the formats: concept, procedure, or reference
- All modules and assemblies must include one H1 and a short description
- All files include the type `:_mod-docs-content-type: <TYPE>`
- All procedure modules strictly follow the procedure module template:
  - No headings other than approved headings (Prerequisites, Procedure, etc.)
  - No lead-in or additional text throughout or after the procedure steps
  - There is only one procedure per module

### DITA Migration Requirements
- Must have an empty line between H1 heading and first paragraph
- Must be an empty line between include statements
- No level 3 headings (===) in any files
- Anchor ID values are not changed even if the titles are
- No additional text surrounding links in the additional resources sections
- No floating .Headings unless it's above an example, table, figure, or code block, or is an approved block title for procedure modules

### General Requirements
- Review the preview build, not just the diffs, to catch rendering issues
- Each .adoc file can contain no more than one H1 (=) heading
- Each assembly and module must contain a sentence or short introductory paragraph after the H1 heading (serves as the abstract)
- Each .adoc file must contain a content type attribute: `:_mod-docs-content-type: <TYPE>`
- All xrefs must include anchor IDs (and use .adoc, not .html)
- Heading anchors use the correct syntax: `[id="module-name_{context}"]`
- Check that `toc::[]` declarations in assemblies are preceded by a blank line
- Assembly-level `==Additional resources` and `==Next steps` titles must have unique IDs
- Each `.Additional resources` section must have a `[role="_additional-resources"]` tag before it
- Sentence case for headings
- Check for places where "OpenShift" should be "{product-title}"
- Check for places where "4.20" or similar should be "{product-version}"
- File name/literals in backticks (not any other markup)
- Source blocks should have the language specified (e.g. `[source,yaml]`)
- Terminal commands/output should have `[source,terminal]` specified
- Check file names and folder names: dashes for filenames, underscores for folders
- Check if xrefs use the complete path to the referencing doc
- Check capitalization - words shouldn't be unnecessarily capitalized
- For commands in source blocks:
  - Check that they are prepended with a suitable prompt
  - Consider whether overlong commands should be split with line breaks
- Check that lines aren't being hard wrapped at 80 characters
- Replaceable values should follow this format: `<ip_address>` (NOT italicized in OCP docs)
- Check that source files for auto-generated content (REST API docs, CLI reference) weren't updated

### Modules
- No xrefs in modules
  - Exceptions: Release notes modules and modules created from assembly content (as long as not reused)
- The "where used" list in the module contains the current list of assemblies
- Single-step procedure modules use an unordered bullet in the procedure section
- Only one heading per procedure module
- Every variable set within a module must be unset at the end of that module

### PR Formatting
- Verify that the PR title and first comment are in the right format (see PR template)
- Include link to the JIRA issue in the description
- Update PR description with deep link to Netlify preview
- PR must have only 1 commit

### Localization
- Avoids long sentences, opts for shorter ones with simple structure
- Avoids obscure descriptions that could lead to multiple interpretations
- Grammar, spelling, and punctuation follow best practices

### Accessibility
- Alternative text is present for all images
- Link text is descriptive
- Tables are properly formed and labeled
- Color is not used as the sole way of describing information
- Positional and sensory language are avoided
- Document sequences are ordered logically, heading levels are not skipped

## Merge Checklist

### Confirm Merge Review Readiness
- Verify PR has only 1 commit
- Verify PR specifies versions and milestones
- Verify PR has QE approval (if required)
  - Non-technical updates don't need QE review

### Check for Obvious Errors
- Scan the preview to ensure all elements (lists, code blocks) render properly
- Scan text for obvious typos or very poor wording
- Verify that all links work
- Check that there are no xrefs in modules (except allowed exceptions)
- Check that xrefs use proper syntax (.adoc extension, includes an anchor)
- Check that headings include only alphanumeric characters (attributes like `{my-attribute}` are fine)

### Merge
- Set version labels and milestone if necessary
- Merge the PR
- Use cherry-pick bot to apply changes to appropriate branches
- If cherry-pick fails, request manual cherry-picks from author
- Merge all cherry-pick PRs in a timely manner

## Content Ports
- Look for proper use of conditionals
- Do NOT suggest file name and ID changes (out of scope)
- Content changes for style improvements can be suggested but might not be made
- QE approval is essential

## Exceptions
- MicroShift and RHDE can use "offline" to describe use cases where there is no network connectivity
