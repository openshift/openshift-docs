---
name: port-docs-to-downstream
description: Convert Kuadrant upstream documentation to Red Hat Connectivity Link (RHCL) downstream docs
argument-hint: "<upstream-doc-url-or-path> [scope-notes]"
---

# Port Documentation to Downstream

Convert Kuadrant upstream documentation into Red Hat Connectivity Link (RHCL) downstream documentation suitable for Red Hat product documentation.

## Scope and Philosophy

This skill transforms upstream Kuadrant docs (published at https://docs.kuadrant.io) into downstream RHCL docs following Red Hat documentation standards, OpenShift platform requirements, and IBM Style Guide conventions.

**Key transformation principle**: Not everything upstream belongs downstream. Filter, adapt, and contextualize based on what Red Hat supports and what downstream users need.

**CRITICAL: Procedural integrity**: Under no circumstance add or skip a procedural step (command-line instruction, configuration change, or any direct instruction to the reader) unless you are certain it will not break the procedure. When in doubt about whether a step is needed or can be safely omitted, ask the user for clarification. It is better to include a potentially redundant step than to create a broken procedure.

## Input

The user provides `$ARGUMENTS` which should be:
1. **Required**: Upstream documentation URL or file path (GitHub URL, local path, or docs.kuadrant.io URL)
2. **Optional**: Scope notes (features to include/exclude, specific use cases to cover, version information)

Example invocations:
```
/port-docs-to-downstream https://github.com/Kuadrant/kuadrant-operator/blob/main/doc/auth-x509.md "Only Tier 2 use case"
/port-docs-to-downstream docs/rate-limiting.md "OLM installation only, OSSM and CIO gateways"
```

## Prerequisites

- Access to upstream documentation (GitHub, local files, or docs.kuadrant.io)
- Understanding of downstream platform (OpenShift) and supported features
- Access to current downstream docs structure: https://github.com/openshift/openshift-docs/tree/rhcl-docs-main
- Knowledge of Red Hat documentation standards (IBM Style Guide + Red Hat Supplementary Style Guide)

## Step 1: Fetch and Analyze Upstream Content

1. **Retrieve the upstream doc**:
   - For GitHub URLs: Use Github MCP server (if configured) or alternatives such as `gh api` or WebFetch to get the raw content
   - For local paths: Use Read tool
   - For docs.kuadrant.io URLs: Use WebFetch

2. **Parse user scope notes** to identify:
   - Features/capabilities to include vs exclude
   - Specific use cases or tiers to document
   - Installation methods (assume OLM only unless specified)
   - Gateway providers (default to CIO; use OSSM only if mentioned in upstream or by user)
   - Version/release information

3. **Ask clarifying questions** if scope is ambiguous:
   - Which features from the upstream are supported downstream?
   - Are there specific use cases or tiers to focus on?
   - What should be excluded entirely?
   - Are there new constraints or requirements to apply?

## Step 2: Apply Downstream Transformation Rules

### Rule 1: Platform and Installation Differences

**Upstream → Downstream transformations:**

| Upstream | Downstream | Notes |
|----------|-----------|-------|
| Helm installation | OLM installation | Skip Helm procedures; assume operator installed via OLM |
| Kubernetes generic | OpenShift specific | Apply OpenShift security context constraints, use `oc` not `kubectl` |
| Istio, Envoy Gateway | CIO (primary), OSSM (secondary) | Prefer CIO unless upstream/user specifies OSSM |
| `kubectl` commands | `oc` commands | Convert all kubectl to oc |
| Kind, minikube, k3s | OpenShift clusters | Remove local dev cluster references |
| `make` targets | Inline procedures | Expand make targets into explicit steps |

**OpenShift-specific requirements:**
- All pod templates must include `securityContext` configuration
- Use OpenShift Routes for ingress (CIO) or OSSM ServiceEntry/VirtualService
- Reference OpenShift documentation for platform features
- Use OpenShift's RBAC and security model
- Apply namespace restrictions and project conventions

**Gateway provider priorities:**
- **Primary (default)**: OpenShift Cluster Ingress Operator (CIO)
  - Use `gatewayClassName: openshift-default` in Gateway objects
  - Assume CIO unless upstream doc or user specifically mentions OSSM
- **Secondary**: OpenShift Service Mesh (OSSM)
  - Use `gatewayClassName: istio` in Gateway objects
  - Only use when explicitly mentioned in upstream or by user

### Rule 2: Product Naming

**Find and replace (case-sensitive where appropriate):**
- "Kuadrant" → "Red Hat Connectivity Link (RHCL)" (first mention in each doc)
- "Kuadrant" → "Red Hat Connectivity Link" or "RHCL" (subsequent mentions)
- Keep "Kuadrant" only when explicitly referencing the upstream project as the basis (e.g., "based on the upstream Kuadrant project")

**Component naming:**
- Upstream component names remain the same (Authorino, Limitador, etc.) but context should indicate they're part of RHCL
- Use product attributes where possible: `{prodname}`, `{product-version}`

### Rule 3: Content Inclusion/Exclusion

**Exclude from downstream:**
- Helm installation procedures
- Unsupported gateway providers (vanilla Istio, Envoy Gateway)
- Development/testing tools (Kind, minikube)
- Upstream-only features not in the RHCL release
- GitHub-specific workflows (clone repos, use make targets)
- Alpha/experimental features
- Contributor-focused content

**Include in downstream:**
- User-facing procedures and use cases
- Supported API references and configurations
- Architecture and concepts (adapted for supported platforms)
- Prerequisites and verification steps
- Troubleshooting for supported scenarios

**Transform (don't exclude):**
- Installation steps: OLM-based installation
- Platform setup: OpenShift-specific configuration
- Examples: Real hostnames, production-like scenarios

**Procedural step preservation:**
- NEVER skip or add procedural steps unless certain it won't break the procedure
- Transform commands (kubectl → oc, etc.) but preserve the complete sequence
- If uncertain whether a step is necessary, ask the user before omitting it
- Expand abbreviated instructions (like make targets) into full steps, don't condense them

### Rule 4: YAML and Code Examples

**All referenced files must be inline:**
- No links to GitHub repositories for YAML files
- No instructions to "clone the repo and run..."
- Embed complete YAML examples directly in the doc
- Show full command sequences inline

**Example transformations:**

❌ Upstream:
```
See example-policy.yaml in the examples/ directory.
Run: make deploy-example
```

✅ Downstream:
```yaml
apiVersion: kuadrant.io/v1
kind: AuthPolicy
metadata:
  name: example-policy
  namespace: my-namespace
spec:
  # ... complete inline example
```

**Variables and placeholders:**
- Use clear placeholder syntax: `export HOSTNAME=<replace-with-gateway-hostname>`
- Avoid `localhost` and `nip.io` - use real hostname variables
- Prefer environment variables for values users must customize

**YAML ellipses:**
- Use commented ellipses: `# ...` (not bare `...` which means document end)

### Rule 5: Links and References

**Link policy:**
- **Avoid external links** where possible (GitHub, Wikipedia often not allowed)
- **Use internal cross-references** to other RHCL docs
- **Check current downstream structure**: https://github.com/openshift/openshift-docs/tree/rhcl-docs-main
- Replace upstream doc links with downstream equivalents
- Remove or inline content instead of linking to external sources

**When you must link:**
- Link to Red Hat documentation
- Link to OpenShift documentation
- Link to top-level pages, not deep links
- Never use bare URLs or URL shorteners

### Rule 6: DNS and Hostnames

**Hostname policy:**

❌ Upstream style:
```
curl http://localhost:8080/api
kubectl port-forward svc/api 8080:8080
export GATEWAY_URL=$(kubectl get svc -n istio-system -o jsonpath='{.status.loadBalancer.ingress[0].ip}').nip.io
```

✅ Downstream style:
```bash
# Get the gateway hostname
export GATEWAY_HOSTNAME=$(oc get route api-gateway -n gateway-namespace -o jsonpath='{.spec.host}')

# Test the endpoint
curl https://${GATEWAY_HOSTNAME}/api
```

**Principles:**
- Assume cloud or on-premises with real DNS
- Use variables and placeholders for hostnames
- Show how to retrieve actual hostnames from OpenShift resources
- Prefer production-like examples over localhost

### Rule 7: Avoid Repetition via Cross-References

**Reference existing procedures instead of duplicating:**
- Check current downstream structure for existing content
- Link to existing installation, configuration, or prerequisite docs
- Only duplicate if the existing doc is insufficient or wrong context

**Downstream doc structure** (release branch): https://github.com/openshift/openshift-docs/tree/rhcl-docs-main

Current published version: https://docs.redhat.com/en/documentation/red_hat_connectivity_link/latest/html/red_hat_connectivity_link/index

**Common cross-references:**
- Installation procedures
- Gateway setup
- Common prerequisites (oc login, project setup)
- Verification steps
- Troubleshooting sections

## Step 3: Apply IBM Style Guide and Red Hat Conventions

The downstream docs must follow IBM Style Guide (primary) and Red Hat Supplementary Style Guide (secondary). This skill inherits all style rules from the `review-downstream-docs` skill.

**Key rules to apply during conversion:**

### Voice and tense
- Active voice, present tense
- Second person ("you")
- No anthropomorphism

### Contractions
- Avoid in formal docs (don't → do not, can't → cannot)

### Clarity
- Include "that" in subordinate clauses: "Verify that the pod is running"
- Use "because" not "since" for causation
- Use "whether" not "if" for alternatives
- Place "only" immediately before what it modifies

### Headings
- Sentence-style capitalization (not headline-style)
- Gerunds for procedures: "Installing the operator" (not "Install the operator")
- Nouns for concepts: "Authentication overview"
- 3-11 words; no terminal periods
- Do not use Level 2 (H3) headings (`===`) or lower in any files

### Banned words
- Filler: simply, just, basically, easily, obviously
- Vague verbs: utilize, leverage, performant
- Politeness: please, thank you
- "Easy", "simple"
- Negative connotation: execute, kill – prefer "run", "stop"

### Word forms
- back end (n), back-end (adj)
- command line (n), command-line (adj)
- One word: cannot, download, email, hostname, upstream, downstream
- Verb/noun: log in (v), login (n); set up (v), setup (n)

### Red Hat specifics
- Short descriptions required: 50-300 chars, active voice, user intent
- Prerequisites as completed checks (not imperatives)
- One command per code block
- User-replaced values: `_<value_name>_` (italicized, angle brackets)
- Include `$` prompt sign for terminal commands, use `#` for root commands
- Use `sudo` not `su -`
- Product attributes: `{prodname}`, `{product-version}`
- No cost references, no future promises
- `{nbsp}` between "Red" and "Hat"

### OpenShift module conventions
- Module files: `con-` (concept), `proc-` (procedure), `ref-` (reference)
- Module IDs with context suffix: `[id="proc-install-operator_{context}"]`
- Files end with newline
- US English spelling

## Step 4: Generate Downstream Document

Create the downstream version with this structure:

### AsciiDoc format (standard for RHCL docs)

```asciidoc
[id="module-id-here_{context}"]
= Module title (sentence-style capitalization, use gerunds for procedures)

[role="_abstract"]
Short description here (50-300 chars, active voice, states what and why).

== Prerequisites

* Prerequisite as completed check
* Another prerequisite as completed check

== Procedure

. First step with inline YAML or command
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f - <<EOF
apiVersion: example.io/v1
kind: Example
metadata:
  name: example
  namespace: my-namespace
# ...
EOF
----

. Second step with verification
+
[source,terminal,subs="+quotes"]
----
$ oc get example -n my-namespace
----

. Final step

== Verification

. Check that the resource exists
+
[source,terminal,subs="+quotes"]
----
$ oc get example example -n my-namespace
----

. Verify the expected behavior

== Additional resources

* Link to related RHCL doc
* Link to OpenShift doc
```

### Content organization

1. **Module header**: ID with context variable, title
2. **Abstract**: Short description with role tag
3. **Prerequisites**: Completed checks, not imperatives
4. **Procedure/Content**: Step-by-step or concept explanation
5. **Verification**: How to confirm success (for procedures)
6. **Additional resources**: Internal cross-references

### YAML/Code examples
- One command per code block within procedure steps
- Separate input and output into different blocks
- Use `[source,yaml]` or `[source,terminal,subs="+quotes"]` tags – **never use `[source,bash]`**
- Quote substitution is **required** for all terminal blocks: `[source,terminal,subs="+quotes"]`
- Include prompt signs: `$` for regular user commands, `#` for root commands
- Comment ellipses: `# ...`
- No syntax highlighting for plain terminal output

### DITA compliance

Apply DITA 1.3 validation rules for OpenShift documentation:

- **Validation config**: https://raw.githubusercontent.com/openshift/openshift-docs/refs/heads/main/modules/.vale.ini
- **Accepted terms**: https://raw.githubusercontent.com/openshift/openshift-docs/refs/heads/main/.vale/styles/config/vocabularies/OpenShiftDocs/accept.txt (in addition to RHCL-specific terms such as Authorino, Limitador, Kuadrant, etc.)
- **Rejected terms**: https://raw.githubusercontent.com/openshift/openshift-docs/refs/heads/main/.vale/styles/config/vocabularies/OpenShiftDocs/reject.txt

If uncertain about a term or style choice, consult these vocabulary lists. Prefer accepted terms and avoid rejected terms entirely. RHCL-specific component names (Authorino, Limitador, DNS Operator, Cert-manager) are implicitly accepted even if not in the OpenShift vocabulary list.

## Step 5: Quality Checks

Before presenting the downstream doc, verify:

- [ ] No mentions of "Kuadrant" except when referencing upstream project
- [ ] No Helm installation procedures
- [ ] No unsupported gateway providers (vanilla Istio, Envoy Gateway)
- [ ] Gateway provider priority: CIO (default) with `gatewayClassName: openshift-default`, OSSM only if specified
- [ ] No `kubectl` commands (use `oc`)
- [ ] No `localhost` or `nip.io` hostnames (use variables)
- [ ] No links to GitHub files or repos
- [ ] All YAML examples are inline and complete
- [ ] All make targets expanded into explicit steps
- [ ] OpenShift security context constraints applied
- [ ] Product attributes used: `{prodname}`, `{product-version}`
- [ ] IBM Style compliance: active voice, present tense, "that" in clauses
- [ ] Red Hat conventions: short description, proper module ID, prerequisites
- [ ] Heading style: gerunds for procedures, nouns for concepts, L2 only (no L3+)
- [ ] Terminal commands: `$` prompt for user, `#` for root, `sudo` not `su -`
- [ ] Code blocks: `[source,terminal,subs="+quotes"]` for terminal output (not `bash`)
- [ ] Banned words avoided: execute/kill (use run/stop), simply, just, easily, etc.
- [ ] DITA 1.3 compliance: OpenShiftDocs vocabulary, no rejected terms
- [ ] Cross-references to existing downstream docs instead of duplication
- [ ] Real hostnames or clear placeholders (no trivial DNS tools)
- [ ] **All procedural steps preserved**: No steps added or removed without user confirmation
- [ ] Command sequences complete and in correct order

## Step 6: Output Format

Present the converted downstream documentation as:

1. **Summary of changes**: What was excluded, what was adapted, what was added
2. **Scope confirmation**: Features/use cases covered in this downstream version
3. **The downstream document**: Complete AsciiDoc module(s)
4. **Integration notes**: Where this fits in the current downstream structure, suggested cross-references
5. **Follow-up recommendations**: Suggest running `/review-downstream-docs` on the generated content

## Integration with Documentation Workflow

This skill is typically used in sequence:

1. `/jtbd-docs` - Frame the documentation around user jobs
2. `/doc-verification` - Verify upstream doc accuracy (optional, if working from existing upstream)
3. `/port-docs-to-downstream` - Convert to downstream format (this skill)
4. `/review-downstream-docs` - Review the downstream doc for technical accuracy and style compliance

## Common Scenarios

### Scenario 1: Feature guide with limited use cases
User: "Port the X.509 authentication doc but only Tier 2 use case"
- Read upstream doc
- Identify Tier 2 content
- Exclude Tier 1 and Tier 3 explanations and procedures
- Simplify branching logic
- Generate focused downstream procedure

### Scenario 2: API reference
User: "Port the RateLimitPolicy API reference"
- Read upstream API doc
- Filter out unsupported fields or options
- Convert examples to OpenShift context
- Replace Kubernetes-generic examples with OpenShift-specific ones
- Add RHCL context

### Scenario 3: Tutorial or walkthrough
User: "Port the getting started guide"
- Replace Helm with OLM installation (or skip, reference existing install doc)
- Convert kubectl to oc
- Replace Kind/local cluster with OpenShift cluster assumption
- Convert all hostnames to production-style variables
- Inline all YAML files referenced
- Remove make targets, show explicit commands

## Error Handling and Edge Cases

**If upstream doc not found:**
- Try alternate URLs (main vs specific branch)
- Ask user for correct path or URL

**If scope is ambiguous:**
- List features found in upstream
- Ask which to include/exclude
- Clarify use cases and tiers

**If downstream structure unclear:**
- Check current downstream docs: https://github.com/openshift/openshift-docs/tree/rhcl-docs-main
- Ask user where this should fit
- Suggest possible integration points

**If unsupported features referenced:**
- Flag them clearly in the summary
- Ask user whether to exclude or adapt
- Provide alternatives where possible

## Verification Before Finalizing

Run these checks on the generated downstream doc:

1. **Grep for upstream-only terms:**
   ```bash
   grep -i "kuadrant\|helm install\|kubectl\|kind create\|localhost\|nip\.io\|github\.com.*\.yaml" downstream-doc.adoc
   ```

2. **Check for inline YAML:**
   Ensure no "see example.yaml" or "clone the repo" instructions

3. **Verify OpenShift specifics:**
   ```bash
   grep -i "oc \|openshift\|securityContext\|route\|project" downstream-doc.adoc
   ```

4. **Style compliance:**
   ```bash
   grep -i "don't\|can't\|won't\|simply\|just\|easily\|please\|execute\|kill" downstream-doc.adoc
   ```

5. **Code block format:**
   ```bash
   grep "\[source,bash\]" downstream-doc.adoc
   ```
   Should return no results (use `[source,terminal,subs="+quotes"]` instead)

6. **Heading levels:**
   ```bash
   grep "^===" downstream-doc.adoc
   ```
   Should return no results (Level 2/H3 headings prohibited)

7. **Product attributes:**
   ```bash
   grep "{product-title}" downstream-doc.adoc
   ```
   Should return no results (use `{prodname}` instead)

Report any violations before presenting final output.

## Notes for Reviewers

When this skill completes:
- The generated downstream doc is a first draft requiring human review
- Technical accuracy must be verified against actual RHCL release capabilities
- Integration with existing downstream structure may need adjustment
- IBM Style and Red Hat conventions are applied but may need refinement
- Always run `/review-downstream-docs` as a follow-up quality check

## Related Skills

- **jtbd-docs**: Apply before this skill to ensure job-focused framing
- **doc-verification**: Verify upstream doc accuracy before conversion
- **review-downstream-docs**: Review generated downstream doc for quality and compliance
