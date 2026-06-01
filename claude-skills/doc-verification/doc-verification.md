---
name: doc-verification
description: Verify project documentation accuracy and quality against the actual codebase. Use this skill when asked to "check documentation", "verify docs", "review documentation", or when you need to ensure documented information matches the current implementation. Also use when reviewing PRs that contain documentation changes (.md files) — invoke alongside the PR review skill to catch both code and documentation issues. Focuses on finding inaccuracies and quality problems in existing docs, not flagging missing documentation.
---

# Documentation Verification

Verify that existing project documentation accurately reflects the current codebase and serves users effectively.

## Philosophy: Accuracy and Quality

This skill checks two things:
1. **Accuracy**: What IS documented is correct against the codebase.
2. **Quality**: What IS documented is usable, well-structured, and serves the target audience.

It does NOT flag what ISN'T documented (completeness).

**Check (accuracy):**
- Documented make targets actually exist
- Documented constants match actual values
- YAML examples have valid fields and syntax
- Tool versions match actual requirements
- Documented file paths exist
- Default values match implementation
- Enum values match API types
- Code examples are syntactically correct

**Check (quality):**
- Document fits its type in the doc hierarchy (overview vs user guide vs reference)
- Information flows logically without requiring readers to jump back and forth
- Related information is grouped together (not split across distant sections)
- Claims are specific and match reality (absolute statements like "must be" are accurate)
- Users can act on the guidance (no dead ends, missing examples, or unexplained concepts)
- Cross-references connect docs into a navigable whole

**Do NOT check (completeness):**
- Whether all make targets are documented
- Whether all API fields have examples
- Whether new features are documented
- Whether all constants are in docs

**Rationale**: Completeness is subjective and context-dependent. Accuracy and quality are objective and actionable.

## Core Principles

1. **Zero assumptions** - Never conclude that a documented statement is correct or incorrect based on what you expect, infer, or "know" from training data. Every factual claim requires a verified source:
   - If the doc references a file or path, check that it exists.
   - If the doc contains a command, run it (or dry-run it) and compare the output to what the doc claims.
   - If the doc describes code behavior, read the actual implementation at the relevant file:line.
   - If the doc states a default value, constant, or version, find the source of truth in code or config and confirm it.
   - If you haven't read the file, run the command, or checked the source, you don't know — and must do so before forming any judgment.
2. **Code evidence is mandatory** - Every claim of inaccuracy must have specific file:line references from both docs and code. No guessing.
3. **Verify before reporting** - Research independently. Read the code, check official docs for syntax/conventions, trace execution. Only report issues you've confirmed.
4. **Quality over quantity** - 3 confirmed issues with evidence are worth more than 30 unverified claims. False positives damage trust.

## Step 1: Discover Documentation Files

Use Glob to find all `.md` files in the repository root and `doc/` or `docs/` directories:
- `CLAUDE.md` - Project documentation and AI context
- `README.md` - User-facing README
- `RELEASE.md` - Release procedures
- `CONTRIBUTING.md` - Contributor guide
- `doc/*.md` / `docs/*.md` - All documentation files

**Exclude**: `CHANGELOG.md` (historical archive, not current documentation).

## Step 2: Verify Each File Using These Patterns

For each discovered file, extract and verify factual claims:

### Pattern 1: Make Targets
- **Extract**: Any mention of `make <target>` or `` `make <target>` ``
- **Verify**: Test with `make -n <target>` to confirm it exists
- **Check**: Command examples show correct flag names and values
- **Check**: Documented defaults for Makefile variables match actual defaults
- **Detect typos**: If target doesn't exist, suggest similar names from Makefile

### Pattern 2: Constants and Default Values
- **Extract**: Documented constant names, default values, configuration values
- **Verify**: Cross-check against source code (API types, config files, main packages)
- **Check**: Referenced constants actually exist in the stated files
- **Sources**: Port numbers, default replicas, resource limits, enum values in type definitions

### Pattern 3: YAML/JSON Examples
- **Extract**: All YAML/JSON code blocks
- **Verify syntax**: Properly formatted, no stray markers
- **Verify fields**: All fields exist in the corresponding API/CRD spec
- **Verify types**: Field types match API (string vs int vs object)
- **Verify enums**: Enum fields use valid values from API type definitions

### Pattern 4: Tool Versions
- **Extract**: References to tool versions (e.g., "operator-sdk version 1.32.0")
- **Verify consistency**: Same tool versions across all documentation files
- **Verify accuracy**: Versions match Makefile, go.mod, or build configuration

### Pattern 5: File Paths and Directory References
- **Extract**: Any mention of file paths
- **Verify existence**: Use Glob or Bash to confirm paths exist
- **Verify links**: Internal markdown links point to existing files

### Pattern 6: Code References and Behavior
- **Extract**: Descriptions of how code works, function names, execution order
- **Verify**: Cross-reference with actual implementation
- **Check**: Function names, environment variables, reconciliation steps, behavior descriptions

## Step 3: Assess Documentation Quality

After verifying accuracy, evaluate the documentation quality using these patterns. Evidence is still required — cite specific sections, headings, or line ranges to support each finding.

### Pattern 7: Document Type Fit
- **Identify**: What type of document is this? (overview, user guide, reference, tutorial, design doc)
- **Check**: Does the level of detail match the type?
  - Overviews should explain concepts and help users make decisions, not provide step-by-step instructions
  - User guides should be actionable with working examples, not abstract explanations
  - References should document structure and fields, not use cases
- **Check**: Is content that belongs in another doc type leaking in? (e.g., a full tutorial inside a reference doc)

### Pattern 8: Structure and Flow
- **Check**: Does the document progress logically? (concept → decision → configuration → troubleshooting)
- **Check**: Can a reader follow the document top-to-bottom without needing to jump back to earlier sections?
- **Check**: Is related information grouped together? Flag cases where information needed to use a feature is split across distant sections (e.g., encoding requirements 100 lines away from the examples that need them)
- **Check**: Are there sections that describe a concept but leave the reader with no next step? (dead ends)

### Pattern 9: Audience and Accessibility
- **Check**: Is the assumed knowledge level consistent throughout? (don't explain Kubernetes basics then assume deep Envoy internals knowledge)
- **Check**: Are decision points clear? When users need to choose between options, is there enough guidance? (tables, "when to use" framing, trade-off comparisons)
- **Check**: Are examples realistic and self-contained? Can a user copy an example and adapt it without hunting for missing context?

### Pattern 10: Claim Specificity
- **Check**: Do absolute statements ("must be", "always", "only") match reality? Look for CRD fields or configuration options that provide alternatives the doc doesn't mention.
- **Check**: Are descriptions of fields or concepts consistent with their actual semantics? (e.g., a field described as "certificate serial number" that actually contains a Subject DN serial number)
- **Check**: Do examples use realistic values that won't mislead? (e.g., example values that look like a different concept than what the field actually contains)

### Pattern 11: Cross-Reference Integrity
- **Check**: Do related documents reference each other appropriately? (overview links to user guide, user guide links back to overview)
- **Check**: Is terminology consistent across related documents? (same concept shouldn't have different names in different docs)
- **Check**: When multiple docs cover related topics, is the division of responsibility clear? (no significant overlap that could diverge, no gaps between docs)

## Step 4: Avoiding False Positives

Before reporting any issue, verify it is NOT one of these common false positives:

**Accuracy false positives:**
- **Valid alternative syntax**: The doc uses a different but correct syntax. Check official docs first.
- **Intentionally out of scope**: The document type doesn't require this level of detail.
- **Standard conventions**: Industry-standard patterns don't need explicit documentation.
- **Architecture differences**: The code works differently than you assumed. Read more carefully.
- **Basic docs linking to detailed docs**: An overview doc referencing a detailed guide is not "incomplete."

**Quality false positives:**
- **Appropriate simplification**: An overview doc omitting advanced options is fine if it links to the reference. Not every field needs to be mentioned everywhere.
- **Audience-appropriate depth**: A user guide for beginners explaining basics isn't "too simple" — it's serving its audience.
- **Style preferences**: Don't flag writing style choices (active vs passive voice, heading conventions) unless they harm clarity. Focus on structural and informational issues.
- **Transitional content**: A section that describes a deprecated/fallback approach briefly without full examples may be intentional if the doc recommends users move to the preferred approach.

**When uncertain**: Research independently first. Check official docs, read related code, trace execution. Only ask the user about scope clarification, priority questions, or ambiguous requirements.

## Step 5: Generate Report

```markdown
## Documentation Verification Report

### Verified Accurate

List all checked documentation areas that are accurate:
- {file}: {section} - all values verified correct
- {file}: {section} - examples match API spec

### Inaccuracies Found

#### [{File name}] - [{Section}]
**Issue**: {Clear description}
**Location**: {File:line}
**Current docs say**: {Exact quote}
**Actual implementation**: {What the code actually says, with file:line}
**Suggested fix**: {Specific correction}

### Quality Issues Found

#### [{File name}] - [{Section}]
**Issue**: {Clear description}
**Location**: {File:line or section range}
**Pattern**: {Which quality pattern this violates: type fit, structure, audience, claim specificity, or cross-reference}
**Impact**: {How this affects users — what will they struggle with or misunderstand?}
**Suggested fix**: {Specific improvement}

### Summary

- Documentation files checked: {N}
- Inaccuracies found: {N}
- Quality issues found: {N}
- Severity breakdown:
  - Critical (wrong values/broken examples/misleading claims): {N}
  - Minor (typos/structure improvements/usability nits): {N}

### Assessment

If no issues: "Documentation is accurate and well-structured."
If issues found: "Found {N} inaccuracies and {N} quality issues."
```

## What to Flag vs What to Skip

**Flag these (inaccuracies):**
- "DefaultPort: 8080" but code says 8081
- "make verify-manifets" but Makefile has "verify-manifests"
- YAML example uses `spec.storage.redis.url` but API field is `configSecretRef`
- "version 1.32.0" in one doc but "1.30.0" in another
- Link to `doc/storage.yaml` but file doesn't exist

**Flag these (quality):**
- A field described as "certificate serial number" but the code returns the Subject DN serial number (misleading claim)
- Doc says "secrets must be in namespace X" but the API has an option to use all namespaces (absolute statement contradicted by reality)
- An option is described with "use EnvoyFilter resources" but no examples, no links, and no further guidance (dead end)
- Encoding requirements documented in a "requirements" section but not near the examples that need them (split information)
- An overview doc containing step-by-step kubectl commands that belong in a user guide (type mismatch)

**Skip these (completeness/opinions):**
- Make target exists but not documented
- New API field added but no example in docs
- Config directory exists but not listed
- Feature works but behavior not fully explained
- Writing style preferences that don't affect clarity
- An overview linking to a detailed guide instead of repeating the content