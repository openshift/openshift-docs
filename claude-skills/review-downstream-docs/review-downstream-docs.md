---
name: review-downstream-docs
description: "Review downstream (OpenShift/RHCL) documentation PRs for technical accuracy and style compliance"
argument-hint: "<PR-URL>"
---

# Downstream Documentation Review

Review a documentation PR for technical accuracy against the upstream codebase and compliance with IBM Style and the Red Hat supplementary style guide.

## Style authority

Priority order: IBM Style Guide (primary), then Red Hat Supplementary Style Guide (secondary, adds Red Hat-specific conventions on top of IBM). The substantive rules from both are baked into this skill below so that reviews do not require fetching external docs.

- IBM Style: https://www.ibm.com/docs/en/ibm-style
- Red Hat Supplementary Style Guide: https://redhat-documentation.github.io/supplementary-style-guide/

## Input

The user provides `$ARGUMENTS` which should be a GitHub PR URL (e.g. `https://github.com/openshift/openshift-docs/pull/109317`).

## Step 1: Fetch the PR

Requires `gh` CLI installed and authenticated (`gh auth status` to check).

Parse the PR URL to extract `<owner>/<repo>` and `<number>`, then run:

1. `gh pr view <number> --repo <owner>/<repo> --json title,body,files,additions,deletions` -- PR metadata and changed files
2. `gh pr diff <number> --repo <owner>/<repo>` -- full diff (this is the source of truth for all content)
3. `gh api repos/<owner>/<repo>/pulls/<number>/comments` -- existing review comments with threading
4. `gh api repos/<owner>/<repo>/pulls/<number>/reviews` -- review states (approved, changes requested)

Identify all changed `.adoc` files from the metadata. Focus the review on new and modified module files (`modules/con-*.adoc`, `modules/proc-*.adoc`, `modules/ref-*.adoc`) and assembly files.

## Step 2: Technical accuracy review

This is the most important step. Every technical claim in the documentation must be verified against the actual codebase.

### Verification methodology

For each technical claim in the docs, follow this process:

1. **Identify the claim type**: Is it about a header name, API field, component behaviour, architecture, configuration, or workflow?
2. **Locate the source of truth**: Find the code that implements the claimed behaviour. Use Grep/Read on the upstream repo.
3. **Verify precisely**: Don't assume -- check exact strings, field names, header values, config formats. A header called `x-mcp-tool` vs `x-mcp-toolname` is wrong even though it's close.
4. **Check scope claims**: Statements like "all traffic", "every request", "always" are frequently overstated. Verify the actual scope.
5. **Check component boundaries**: Which component does what? Don't let docs attribute behaviour to the wrong component.

### What to verify

- **Header names**: Grep for exact header string literals in the code. Header names in docs are frequently wrong or outdated.
- **Config types**: Is it a ConfigMap or Secret? Check the controller/operator code.
- **Component responsibilities**: Which component does what? Read the handler code.
- **API resource names**: CRD names, field names, status conditions. Check the API type definitions.
- **Architecture claims**: Data flow, what talks to what, what intercepts what. Check the actual wiring.
- **Feature claims**: Does the described feature actually exist? Is it implemented or just planned?
- **Default values**: Are claimed defaults correct? Check flag definitions and constants.
- **Shell commands**: Do grep patterns match actual log messages? Do deployment names match? Do protocol versions match current code?

### Upstream codebase location

The skill needs access to the upstream codebase to verify claims. To find it:

1. Check the current working directory -- it may already be the upstream repo.
2. Check sibling directories (e.g. `../project-name`).
3. If not found, ask the user for the path.

Once located, read the project's `CLAUDE.md` (if it exists) to understand the codebase structure, key files, architecture, and conventions. This replaces hardcoded file lists -- the CLAUDE.md is the source of truth for where to find things in the codebase.

## Step 3: Style review

Apply IBM Style (primary) and the Red Hat Supplementary Style Guide (secondary). Focus on obvious mistakes and issues that affect clarity, not pedantic nitpicks. The key rules from both guides are listed here for reference.

### Voice, tense, and person (IBM Style)

- **Active voice**: Use active voice. Passive is acceptable when the subject matters more than the actor.
- **Present tense**: Use present tense. Avoid future tense ("will") except when describing something that genuinely occurs later.
- **Second person**: Use "you" to address the reader. Avoid first person (I, we, our, us) in technical docs.
- **No anthropomorphism**: Systems do not "think", "want", "complain", "refuse", or "know".

### Contractions (IBM Style + RH override)

IBM Style permits contractions in context. However, Red Hat product documentation avoids contractions except in content with a conversational tone. Flag contractions in formal procedure/reference docs: don't, can't, won't, it's, that's, you'll, isn't, aren't, doesn't, hasn't, haven't, shouldn't, couldn't, wouldn't.

### Conjunctions and clarity (IBM Style)

- Use *since* only for time, not as a synonym for *because*.
- Use *while* only for simultaneous actions, not as a synonym for *although*.
- Use *once* only for "one time", not as a synonym for *after* or *when*.
- Use *as* only for simultaneous actions, not as a synonym for *because*.
- Use *if* for conditions, *whether* for alternatives.
- Use *if...then*: avoid using *then* to introduce an independent clause after *if*.
- Use *that* (no comma) for restrictive clauses. Use *which* (with comma) for nonrestrictive clauses.
- Include *that* in subordinate clauses for translation clarity ("verify that the pod is running" not "verify the pod is running"). This is one of the most common issues in doc PRs; IBM is emphatic about it. Always include "that" after verbs like verify, ensure, confirm, specify, check, note.
- Place *only* immediately before the word or phrase it modifies ("the gateway processes only HTTP requests" not "the gateway only processes HTTP requests").

### Inclusive language (IBM Style + RH)

Flag these if found:
- blacklist/whitelist: use denylist/allowlist, blocklist/passlist
- master/slave: use primary/secondary, source/replica, controller/device
- Do not use "white" or "black" in contexts where white is good and black is bad
- Avoid gender-specific pronouns; use "you" or rephrase with plural nouns

### Banned words and filler (IBM Style + RH)

- **Filler**: simply, basically, essentially, actually, really, very, totally, obviously, just, easily
- **Vague/inflated verbs**: leverage (use "use"), utilize (use "use"), architect as verb (use "design"), performant
- **Informal**: gonna, admin (spell out on first use), info (spell out)
- **Politeness terms**: please, thank you (avoid in technical information; terms of politeness convey wrong tone)
- **Never state things are "easy" or "simple"**

### Preferred terms (IBM Style)

- "because" not "since/as" (for reason)
- "for example" not "e.g."
- "that is" not "i.e."
- "such as" not "like" (for examples)
- "whether" not "if" (for choices)
- "click" not "click on"
- "start" not "start up"
- "print" not "print out"
- "use" not "utilize/leverage"
- "ensure" not "make sure" (but note: "ensure" can imply a guarantee; in contexts with legal or SLA implications, consider "verify" or "confirm" instead)

### Possessives (IBM Style)

- Do not use possessive 's with inanimate objects ("the server labels" not "the server's labels")
- Do not use possessive 's with abbreviations or product names ("the layout of the GUI" not "the GUI's layout", "IBM Cloud solutions" not "IBM Cloud's solutions")

### Headings (IBM Style + RH override)

IBM Style says do not use question-style headings in concept/reference/procedure topics. Red Hat supplementary guide adds:

- Use **sentence-style capitalisation**, not headline-style
- Use **gerunds** for procedures: "Installing the CLI" not "Install the CLI"
- Use **nouns or noun phrases** for concept/reference topics
- Do not start with "Understanding", "Introducing"
- Keep between 3-11 words; no one-word titles
- Do not use Level 2 (H3) headings (`===`) or lower in any files
- No terminal periods (IBM Style); no file/command names in titles (IBM Style)

### Abbreviations (IBM Style)

- Spell out on first use, then abbreviation in parentheses, unless well known (HTML, API, HTTP, DNS, TCP/IP)
- Do not use abbreviations as verbs ("use the FTP command" not "FTP the files")
- Do not use possessive 's on abbreviations ("the properties of HTML" not "HTML's properties")
- Plural: add lowercase *s* (CRDs, APIs, LLMs)
- Do not use Latin abbreviations: use "for example" (not e.g.), "that is" (not i.e.), use "and so on" (not etc.)

### Punctuation (IBM Style)

- **Serial comma**: Use a serial comma before a conjunction that precedes the final item in a series of three or more.
- **Em dashes**: Do not use em dashes in technical information. Use commas, parentheses, colons, or rewrite.
- **Exclamation points**: Never in docs.
- **Ellipses**: Avoid in technical information.
- **Slashes**: Do not use for "or". Write "enable or disable" not "enable/disable".
- **Parenthetical (s)**: Do not use. Write the plural form, or "one or more".

### Numbers (IBM Style)

- Use numerals to represent all numbers in most cases. For numbers below 10 in text, it is also acceptable to use words.
- Use commas to separate groups of three numerals, including 4-digit numbers (1,000 not 1000).
- Non-breaking space between value and unit (2 GB, 100 MHz).

### Lists (IBM Style)

- Lead-in must be a complete sentence (for translation clarity). Use complete sentences, not phrases, to introduce lists.
- Complete sentence items get periods. Fragment items get no punctuation.
- Items must be grammatically parallel.
- Do not break a sentence across a list.

### Word forms (IBM Style)

Two-word nouns, hyphenated adjectives:
- back end (n), back-end (adj) -- not "backend"
- front end (n), front-end (adj) -- not "frontend"
- command line (n), command-line (adj)
- real time (n), real-time (adj)
- on premise (adverb), on-premise (adj)

Two words always: bug fix, code base, data center, data source, data store, data type, file name, file system, file type, health check, home page, web page, web UI

One word always: cannot, download, downstream, email, hostname, lifecycle, offline, online, screenshot, troubleshoot, upstream, uptime, username

Verb/noun splits:
- backup (n/adj), back up (v)
- login (n/adj), log in (v), log in to (3 words, never "log into")
- setup (n/adj), set up (v)
- shut down (v), shutdown (only for the command)

Other:
- open source -- two words, lowercase, never hyphenated
- double-click -- hyphenated
- built-in (adj) -- hyphenated
- dialog box -- not "dialog" or "dialogue"

### Spelling (IBM Style)

US English spelling in all publications: labeled (not labelled), color (not colour), analyze (not analyse), center (not centre), license (not licence), program (not programme), canceled (not cancelled), gray (not grey), fulfill (not fulfil), recognize (not recognise).

### Red Hat supplementary conventions (RH overrides/additions)

These apply on top of IBM Style for Red Hat product docs:

**Admonitions**: Use NOTE, IMPORTANT, WARNING, TIP only. Use singular form (NOTE not NOTES). Keep brief; do not include procedures. Minimize use; avoid placing multiple admonitions near each other.

**Short descriptions (abstracts)**: Required for every module and assembly. Length: 50-300 characters. Use active voice, present tense, plain English. Include user intent (what and why). Avoid "This topic covers..." self-references. Tag: `[role="_abstract"]`.

**Prerequisites**: Write as checks that are true or completed before procedure. Use passive voice if needed. Do not use imperative formations.

**Single-step procedures**: Use an unnumbered bullet, not a numbered list.

**Code blocks**: One command per code block per procedure step. Separate command input and output into individual code blocks. Do not use `bash` for syntax highlighting of terminal commands (incorrectly interprets `#` as comment).

**User-replaced values**: Format as `_<value_name>_` (angle brackets, underscores for multi-word, lowercase, italicised). In XML, use `_${value_name}_`.

**Commands requiring root**: Use `sudo` for temporary elevation, not `su -`. When using `sudo`, display `$` prompt, not `#`.

**Product names and versions**: Use attributes (`{product-title}`, `{product-version}`) not hardcoded names.

**Date formats**: Preferred: _day Month year_ (3 October 2019).

**YAML ellipses**: Use `# ...` (commented) instead of bare `...` which indicates document end in YAML.

**IP addresses in examples**: Use documentation-reserved ranges: IPv4 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24. IPv6 2001:0DB8::/32.

**Developer Preview features**: Include the Developer Preview admonition template at the content beginning. Developer Preview is a distinct category from Technology Preview with its own required wording.

**Technology Preview features**: Include the Technology Preview admonition template at the content beginning. Technology Preview has its own distinct required wording, separate from Developer Preview. Do not conflate the two.

For both: avoid the word "support"; use "available", "provide", "capability".

**No cost references**: Avoid all references to product costs or charges.

**No future release promises**: Do not mention specific future release numbers or dates. Exception: deprecation/removal notices.

**CAUTION admonition banned**: Do not use CAUTION admonition type. It is not fully supported by the Red Hat Customer Portal.

**Non-breaking space for "Red Hat"**: Use `{nbsp}` between "Red" and "Hat" to prevent line breaks splitting the company name.

**"enter" not "type"**: Use "enter" instead of "type" or "input" when instructing users to provide text in a GUI field.

**Short description before admonitions**: Never start a module or assembly with an admonition. Always provide a short description first.

**External links**: Avoid deep links into external sites (link to top-level pages). Do not use bare URLs or URL shorteners.

**MAC addresses in examples**: Use RFC 7042 documentation-reserved ranges: unicast 00:00:5E:00:53:00-FF, multicast 01:00:5E:90:10:00-FF.

### OpenShift/RHCL module conventions

- Module files: `con-` (concept), `proc-` (procedure), `ref-` (reference)
- Module IDs must include `_{context}` suffix: `[id="con-about-feature-name_{context}"]`
- Assembly files include modules with `include::modules/con-foo.adoc[leveloffset=+1]`
- Files must end with a newline
- US English spelling (labeled not labelled, color not colour, capitalize not capitalise)

## Step 3b: Run style checks (MANDATORY -- do not skip)

After completing the technical review, run these grep-based checks against the diff. Do not skip this step even if the technical review found many issues. Requires `gh` CLI installed and authenticated.

```bash
# Extract only added content lines (no diff metadata, no comments)
gh pr diff <number> --repo <owner>/<repo> | grep '^+' | grep -v '^+++' | grep -v '^+//' > /tmp/pr-content.txt

# 1. Banned words, filler, and contractions
grep -i -E "\bsimply\b|\bjust\b|\bbasically\b|\beasily\b|\beasy\b|\bsimple\b|\bobviously\b|\bplease\b|\bdon't\b|\bcan't\b|\bwon't\b|\bit's\b|\bthat's\b|\byou'll\b|\butilize\b|\bleverage\b|\bperformant\b|\band/or\b|\bgot\b|\bwish\b" /tmp/pr-content.txt

# 2. Ambiguous/incorrect terms
grep -i -E "\bshould\b|\bmay\b|\bonce\b|\bsince\b|\ballows\b|\bwhile\b|\bclick on\b|\blog into\b|\bnavigate to\b|\be\.g\.\b|\bi\.e\.\b" /tmp/pr-content.txt

# 3. Future tense and first person
grep -i -E "\bwill be\b|\bwill have\b|\bwill not\b|\bwe \b|\bour \b" /tmp/pr-content.txt

# 4. Exclusionary language
grep -i -E "\bblacklist\b|\bwhitelist\b|\bmaster\b|\bslave\b|\bsanity\b" /tmp/pr-content.txt

# 5. Vague heading verbs
gh pr diff <number> --repo <owner>/<repo> | grep '^+=' | grep -i -E "Understanding|Introducing"

# 6. Possessives on product names
grep -i -E "MCP gateway's|Envoy's|Kubernetes's|OpenShift's|Istio's|Authorino's" /tmp/pr-content.txt

# 7. Anthropomorphism
grep -i -E "\bthinks\b|\bwants\b|\bknows\b|\brefuses\b|\bcomplains\b|\btries to\b" /tmp/pr-content.txt

# 8. Common word form errors
grep -i -E "\bbackend\b|\bfrontend\b|\bopen-source\b|\bsetup\b.*verb-context|\blog into\b" /tmp/pr-content.txt

# 9. Em dashes (should not appear in technical docs per IBM Style)
grep -E "\xE2\x80\x94|--[^-]" /tmp/pr-content.txt

# 10. Latin abbreviations
grep -i -E "\be\.g\.|\bi\.e\.|\betc\." /tmp/pr-content.txt
```

Report only findings that affect clarity or violate IBM/RH rules. If the checks come back clean, state that explicitly -- don't manufacture issues. Context matters: "should" in a YAML comment is fine, "backend" as part of `backendRef` (a Kubernetes API field) is fine.

## Step 4: Check existing review comments

Use `gh` to fetch all review comments and their context:

```bash
# Get all review comments with reply threading
gh api repos/<owner>/<repo>/pulls/<number>/comments \
  --jq '.[] | {id, user: .user.login, path: .path, line: .line, body: .body, in_reply_to_id: .in_reply_to_id, created_at: .created_at}'

# Get review states (approved, changes requested, commented)
gh api repos/<owner>/<repo>/pulls/<number>/reviews \
  --jq '.[] | {user: .user.login, state: .state}'
```

For each comment from a human reviewer (ignore bots unless they flag real errors):

1. **Check if addressed**: A comment is considered addressed if ANY of:
   - The suggested change appears in the current diff (compare suggestion text against current file content)
   - A reply exists from the author acknowledging it
   - The comment has emoji reactions (the API doesn't always show these -- note this limitation)
   - The `in_reply_to_id` field shows a thread with resolution

2. **Check if technically correct**: Reviewer suggestions can be wrong. Verify every `suggestion` block against the codebase before endorsing it. If a reviewer suggests wrong header names, flag that too.

3. **Check if still relevant**: The file or section may have been rewritten since the comment was posted. Compare the comment's `path` and `line` against the current diff.

4. **Author `//Q:` comments**: These are inline questions from the doc author asking for technical input. Answer each one based on the codebase. Use `gh pr diff` to find them:
   ```bash
   gh pr diff <number> --repo <owner>/<repo> | grep -n '//Q:'
   ```
   Then get the correct file line number using the per-file extraction method.

Only flag unaddressed comments that contain valid technical corrections or unanswered questions. Do not flag resolved threads or style-only suggestions from bots.

## Step 5: Output format

The output is a single numbered list of comments to post on the PR. Every finding (technical accuracy, style, author questions, unaddressed reviewer comments) becomes a comment in this list. Do not split findings into separate sections -- the user needs one consolidated list of actions.

Structure each comment as:

```
**N. `file path`, line NN**

Comment text explaining the issue. Include ```suggestion blocks where appropriate.
```

Group related issues on the same file/line into a single comment where it makes sense (e.g. a typo and a technical error on the same line).

For author `//Q:` comments, the comment should answer the question based on the codebase. Frame it as a helpful response, not a finding.

### Priority ordering

Order comments by priority within the list:

1. Technical inaccuracies (wrong header names, wrong component, wrong config type) -- always include
2. Misleading scope claims ("all traffic", "every request") -- always include
3. Unaddressed reviewer comments with valid corrections -- always include
4. Author `//Q:` questions -- always answer
5. Grammar errors that change meaning -- include
6. Style violations -- include only if egregious or frequent
7. Minor style nits -- skip entirely

### No nitpicking

Do not include:
- Minor style preferences that don't affect clarity (serial comma placement, minor word choice)
- Formatting inconsistencies that don't affect rendering
- AsciiDoc conventions that are clearly just the author's style
- Anything you'd label "minor" or "nit" -- skip it entirely

Only include issues that would cause user confusion, technical errors, or broken workflows.

### Verification before reporting (MANDATORY)

Every finding must be triple-checked before inclusion. False positives destroy reviewer credibility.

For each finding, complete ALL of these steps:

1. **Re-read the exact text in the PR diff** -- not a paraphrase, not from memory. Run `gh pr diff` and grep for the exact string.
2. **Re-verify against the code** -- grep for exact string literals (header names, log messages, config types, field names). If you claim something "doesn't exist in the codebase", prove it with a zero-match grep.
3. **Confirm the line number** -- GitHub PR reviews use file line numbers (right-side in the diff view), NOT diff output line numbers. To get the correct line number for a finding in a new file, extract just the file content from the diff and number it:
   ```
   gh pr diff <number> --repo <owner>/<repo> | sed -n '/^+++ b\/path\/to\/file/,/^diff --git/p' | grep '^+' | grep -v '^+++' | cat -n | grep 'search term'
   ```
   This strips the diff metadata and gives you the true file line numbers. NEVER use raw `gh pr diff | cat -n` line numbers -- they include diff headers, hunk markers, and context lines that throw off the count. NEVER estimate line numbers from memory.
4. **Verify reviewer suggestions** -- if a finding is about another reviewer's suggestion, check that the suggestion itself is correct. Reviewers can be wrong too.
5. **Check for stale upstream docs** -- API type comments, CLAUDE.md, AGENTS.md can contain stale information. If the doc repeats a claim from an API comment, verify the claim matches the actual implementation, not just the comment.
6. **Test commands** -- if the doc includes shell commands (grep patterns, curl commands, oc commands), verify: (a) the exact string/pattern would produce results, (b) deployment names and namespaces match the actual deployment, (c) protocol versions and API paths are current.