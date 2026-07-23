# OCP docs core PR and merge review checklist

[For writers](#for-writers)

[PR requirements](#pr-requirements)

[Mod docs templates adherence](#mod-docs-templates-adherence)

[DITA migration requirements](#dita-migration-requirements)

[General](#general)

[Modules](#modules)

[PR](#pr)

[Content Ports](#content-ports)

[Localization](#localization)

[Accessibility](#accessibility)

[Exceptions](#exceptions)

[Merge checklist](#merge-checklist)

[Confirm merge review readiness](#confirm-merge-review-readiness)

[Check for obvious errors](#check-for-obvious-errors)

[Merge](#merge)

## For writers {#for-writers}

*Before you add content to the OpenShift docs, please ensure the following steps have been completed BEFORE requesting merge:*

* Content is modularized and adheres to the [modular docs guidelines](https://redhat-documentation.github.io/modular-docs/).   
* Content adheres to style guidelines ([Red Hat supplementary style guide](https://redhat-documentation.github.io/supplementary-style-guide/) and [IBM style guide](https://www.ibm.com/docs/en/ibm-style)).  
  * Also review tips for [simplifying complex procedures](https://spaces.redhat.com/display/DOCS/Complex+procedures).  
* When you use AI tools to generate or edit content, you **must** thoroughly review the output before seeking any other reviews.  
* If you are a newer contributor, reach out to your onboarding buddy or another senior team member to provide an initial editorial review on your first few large assignments.  
* Get SME and QE approval before requesting a merge review of your PR. QE approval is required before merging a PR.  
  * Exception: non-technical updates, such as fixing broken links, basic typos, or formatting issues do not require QE review. See the [contribution guide](https://github.com/openshift/openshift-docs/blob/main/contributing_to_docs/doc_guidelines.adoc#verification-of-your-content).

## PR requirements {#pr-requirements}

*Since your self review replaces peer review, review and comply with the [Red Hat peer review guide for technical documentation](https://ccs-internal-documentation.pages.redhat.com/peer-review/).*

### Mod docs templates adherence {#mod-docs-templates-adherence}

Check that all files strictly adhere to the [mod docs templates](https://github.com/redhat-documentation/modular-docs/tree/main/modular-docs-manual/files), especially the following:

- [ ] Modules must follow one of the formats of concept, procedure, or reference.   
- [ ] All modules and assemblies must include one H1 and a short description  
- [ ] All files follow the [mod docs templates](https://github.com/redhat-documentation/modular-docs/tree/main/modular-docs-manual/files). For example:  
      * All files include one H1, and a short description  
      * All files include the type :\_mod-docs-content-type: \<TYPE\>  
- [ ] All procedure modules strictly follow the [procedure module template](https://github.com/redhat-documentation/modular-docs/blob/main/modular-docs-manual/files/TEMPLATE_PROCEDURE_doing-one-procedure.adoc). For example:  
      * No headings other than approved headings (Prerequisites, Procedure, etc.)  
      * No lead-in or additional text throughout or after the procedure steps  
      * There is only one procedure per module

### DITA migration requirements {#dita-migration-requirements}

- [ ] Must have an empty line between H1 heading and first paragraph  
- [ ] Must be an empty line between include statements  
- [ ] No level 3 headings (===) in any files  
- [ ] Anchor id values are not changed even if the titles are  
- [ ] No additional text surrounding links in the additional resources sections  
- [ ] No floating .Headings unless it’s above an example, table, figure, or code block, or is an [approved block title for procedure modules](https://github.com/redhat-documentation/modular-docs/blob/main/modular-docs-manual/files/TEMPLATE_PROCEDURE_doing-one-procedure.adoc?plain=1#L45), such as .Procedure or .Prerequisites.

### General {#general}

* Review the preview build, not just the diffs, to catch rendering issues  
* Confirm that change management either isn’t necessary or has been completed. Change management is necessary with major changes to published content, such as support status changes, content removal, or major content reorganization.  
* Each .adoc file can contain no more than one H1 (=) heading.  
* Each assembly and module must contain a sentence or short introductory paragraph after the H1 heading. This serves as the *abstract* for the file.  
* Each .adoc file must contain a content type attribute in the metadata: :\_mod-docs-content-type: \<TYPE\>  
* All xrefs must include anchor IDs (and use .adoc, not .html)  
* Heading anchors use the correct syntax: \[id="module-name\_{context}"\]  
* Check that toc::\[\] declarations in assemblies are preceded by a blank line and that the TOCs are rendered in the preview build  
* Assembly-level \`==Additional resources\` and \`==Next steps\` titles must have unique IDs.  
* Each .Additional resources and \== Additional resources section must have a \[role="\_additional-resources"\] tag before it. These sections can contain only an unordered list of links and/or xrefs.  
* Sentence case for headings  
* No new attribute files are allowed \- if a PR adds one, check with Kathryn before you approve it.  
* Check for places where “OpenShift” should be “{product-title}”  
* Check for places where "4.20" or similar should be "{product-version}"  
* File name/literals in backticks (not any other markup)  
* Source blocks should have the language specified when appropriate (e.g. \[source,yaml\]). Terminal commands/output should have \[source,terminal\] specified.  
* Avoid linking to GitHub. Instead, try to incorporate the required information directly into our documentation so that it goes through the same QE verification process as the rest of the content. Exceptions to this rule must be okayed by the relevant Product Experience team rep (for OpenShift, that would be Chris Fields).   
* Check if file names and folder names correspond to our guidelines, such as dashes for filenames, underscores for folders.  
* Check if xrefs use the complete path to the referencing doc.  
* Check capitalization, that words aren’t unnecessarily capitalized. (Current exceptions are [API objects](https://github.com/openshift/openshift-docs/blob/master/contributing_to_docs/doc_guidelines.adoc#api-object-formatting), as you can see in the [glossary](https://github.com/openshift/openshift-docs/blob/master/contributing_to_docs/term_glossary.adoc).)  
* For [commands in source blocks](https://github.com/openshift/openshift-docs/blob/master/contributing_to_docs/doc_guidelines.adoc#code-blocks):  
  * Check that they are prepended with a suitable prompt.  
  * Consider whether an overlong command should be split up with line breaks for readability.  
* Conformance to [assembly](https://github.com/openshift/openshift-docs/blob/master/contributing_to_docs/doc_guidelines.adoc#assembly-file-metadata) and [module](https://github.com/openshift/openshift-docs/blob/master/contributing_to_docs/doc_guidelines.adoc#module-file-metadata) metadata as defined in the guidelines. (Note that the assembly heading must contain a blank line before the line that contains toc::\[\].)  
* Check if an include file is referencing an external source, it is referencing a valid URL, and that the inclusion of that URL has been acked by QE, Engineering and Docs. The external source **must not** be an AsciiDoc file and should be restricted to the OpenShift organization on GitHub (The URLs must start with [https://raw.githubusercontent.com/openshift](https://raw.githubusercontent.com/openshift)).  
* Check that lines aren’t being hard wrapped at 80 characters (or any other length).  
* Check that customer-facing names are used for products and the product appears in the [Official Red Hat product and solutions names list](%20https://docs.google.com/spreadsheets/u/1/d/1DLS_lS3VKidgZIvcLmLp9BoiqptkvqHWfe1D5FD2kfk/pubhtml?gid=1259317633&single=true).  
* Check terminology with the [glossary](https://github.com/openshift/openshift-docs/blob/master/contributing_to_docs/term_glossary.adoc) in the doc guidelines.  
* Check [conscious language terminology](https://github.com/openshift/openshift-docs/blob/main/contributing_to_docs/doc_guidelines.adoc#using-conscious-language) in the doc guidelines.  
  * Be sure that \`master\` is used appropriately.  
* Replaceable values should follow this format: \<ip\_address\>. Note that OCP docs do NOT yet italicize replaceable values (like the CCS supplementary style guide [recommends](https://redhat-documentation.github.io/supplementary-style-guide/#user-replaced-values)).  
* Check that source files for auto-generated content, such as the REST API docs (in the rest\_api/ folder) and the CLI reference docs (oc-by-example-content.adoc and oc-adm-by-example-content.adoc) weren’t updated.  
* If the PR reverts another PR, it still needs review. Additionally, confirm that all the changes from the original PR have been reverted.

### Modules {#modules}

* No xrefs in modules.  
  * Exceptions: Release notes modules and modules created from assembly content may contain xrefs as long as these modules are not reused in another assembly.  
* The “where used” list in the module contains the current list of assemblies.  
* Single-step procedure modules use an unordered bullet in the procedure section  
* Only one heading per procedure module.  
* Modules must follow one of the formats of concept, procedure, or reference. For example, one module shouldn’t contain several procedures or a mix of procedure and reference.  
* Every time you set a variable within a module, you must unset it at the end of that module. This is typically done in ifeval statements at the start of a module. 

### PR {#pr}

* Verify that the PR title and first comment are in the right format. This format is described in the PR template, and a correctly formatted PR title and comment looks like this: [https://github.com/openshift/openshift-docs/pull/51056](https://github.com/openshift/openshift-docs/pull/51056)   
* Include link to the JIRA issue in the description of the PR.  
* Update PR’s description with a deep link to the Netlify preview where the PR’s changes can be seen (e.g., the specific module or assembly section).  
* PR must have only 1 commit  
* While QE verification is required for most PRs, no QE or SME is required for core OCP z-stream release note PRs or core OCP y-stream release note bug fixes.

### Content Ports {#content-ports}

Content ports are conducted from one doc set to another and involve reusing content, sometimes in a different context or doc structure. Some things to note when reviewing content ports:

- [ ] Look for the proper use of conditionals in the ported content, and if possible, look at previews for both the destination and source content (usually the OCP docs) to ensure nothing was bumped out of the source.  
- [ ] Do not suggest file name and ID changes. These are out of scope with content ports and potentially disastrous for the many cross references to the borrowed content.  
- [ ] Content changes for style improvements can be suggested, but are out of scope and might not be made.  
- [ ] Asking technical questions is not recommended, as the context of the destination might be different than the source. QE approval, on the other hand, is essential here.

### [Localization](https://www.patternfly.org/v4/ux-writing/writing-for-all-audiences/) {#localization}

* Avoids long sentences, opting for shorter ones with simple structure, minimalism principles are applied.  
* Avoids obscure descriptions that could lead to multiple or wrong interpretations that could result in machine translation applying an incorrect interpretation.  
* Grammar, spelling, and punctuation follow best practices, to help facilitate machine translation.  
* Eliminate redundancies.

### Accessibility {#accessibility}

* Content conforms to [CCS a11y guidance](https://docs.google.com/document/u/1/d/e/2PACX-1vSfEv9uCP-75b9vn3yrv3NOaDhLq-VaqVtUW4CXQDYXJjpNztIaI3JC8uHh1Z-cDCqNW1JZAjAvrLtS/pub). This guidance includes:  
  * Alternative text is present for all images.  
  * Link text is descriptive.  
  * Tables are properly formed and labeled.  
  * Color is not used as the sole way of describing information.  
  * Positional and sensory language are avoided.  
  * Document sequences are ordered logically, and heading levels are not skipped.

### Exceptions {#exceptions}

Catalog product-specific exceptions to the IBM style guide and other guidelines.

- [ ] MicroShift and RHDE can use “offline” to describe use cases where there is no network connectivity. This is a temporary exemption that will be added to the SSG.

## Merge checklist {#merge-checklist}

*Before you merge, do a final check of the PR.*

### Confirm merge review readiness {#confirm-merge-review-readiness}

*If the PR does not meet these criteria, immediately send it back to the author to correct.*

- [ ] Verify PR has only 1 commit  
- [ ] Verify PR specifies versions and milestones   
- [ ] Verify PR has QE approval, if required  
      * Non-technical updates, such as fixing broken links, basic typos, or formatting issues do not need QE review

### Confirm the DITA migration requirements

- [ ] Must have an empty line between H1 heading and first paragraph  
- [ ] No H3 headings (===) in any files  
- [ ] Anchor id values are not changed even if the titles are.  
- [ ] No additional text surrounding links in the additional resources sections  
- [ ] No floating .Headings unless it’s above an example, table, figure, or code block, or is an [approved block title for procedure modules](https://github.com/redhat-documentation/modular-docs/blob/main/modular-docs-manual/files/TEMPLATE_PROCEDURE_doing-one-procedure.adoc?plain=1#L45), such as .Procedure or .Prerequisites.  
- [ ] Modules must follow one of the formats of concept, procedure, or reference  
- [ ] All modules and assemblies must include one H1 and a short description  
- [ ] All files follow the [mod docs templates](https://github.com/redhat-documentation/modular-docs/tree/main/modular-docs-manual/files). For example:  
      - [ ] All files include one H1, and a short description  
      - [ ] All files include the type :\_mod-docs-content-type: \<TYPE\>  
- [ ] All procedure modules strictly follow the [procedure module template](https://github.com/redhat-documentation/modular-docs/blob/main/modular-docs-manual/files/TEMPLATE_PROCEDURE_doing-one-procedure.adoc). For example:  
      - [ ] No headings other than approved headings (Prerequisites, Procedure, etc.)  
      - [ ] No lead-in or additional text throughout or after the procedure steps  
      - [ ] There is only one procedure per module  
- [ ] No preexisting IDs have been changed.

### Check for obvious errors {#check-for-obvious-errors}

*Remember to stop reviewing PRs with many issues. Remove the merge labels and send it back to the author. For very troubled PRs, use the* [OCP docs PR feedback form](https://docs.google.com/forms/d/e/1FAIpQLSdsX3_KOnTRYzCQhmLyu5jCyq-Sp1Qnc_xFWh5uqpJk13iOVw/viewform?usp=header) *according to the details in the docs manual.*

- [ ] Scan the preview to ensure that all elements (lists, code blocks) are rendering properly  
- [ ] Scan text for obvious typos or very poor wording  
- [ ] Verify that all links work  
- [ ] Check that there are no xrefs in modules. A few exceptions exist for migration, such as for release note modules that are not reused in another assembly and index.adoc files. Check the [contrib guide](https://github.com/openshift/openshift-docs/blob/main/contributing_to_docs/doc_guidelines.adoc#writing-procedures) if you’re unsure.  
- [ ] Check that xrefs use proper syntax (.adoc extension, includes an anchor)  
- [ ] Check that headings include only alphanumeric characters  
      - [ ] Attributes ({my-attribute}) that will be replaced are also fine

### Merge {#merge}

- [ ] If necessary, set the version labels and milestone.  
- [ ] Merge the PR.  
- [ ] Use the cherry-pick bot to apply changes to the [appropriate branches](https://docs.google.com/document/u/2/d/e/2PACX-1vRLKWEMHQ3DZroxZKfTu3XcrSdREr6D3oSSayBanEprXhkA2Ciyr2SQuDTYI4aIKUiOPPIQMHgjHeh8/pub#h.x2d4tdt5adta).  
      - [ ] If the cherry-pick bot fails to open the PR automatically for a published branch, request that the PR author create manual cherry-picks.  
            - [ ] When reviewing a manual cherry pick, always check the diff and preview to make sure the changes match the original PR (or close enough as expected).  
      - [ ] If the cherry-pick bot fails to open a PR automatically for the latest version branch, there’s probably a larger issue with the PR. Attempt to investigate it, and ask Andrea if you cannot locate the issue.  
      - [ ] 4.13 is EOL, but we are following engineering’s lead on backports. No change can originate in 4.13, but changes that apply to 4.12 must also be applied to 4.13.  
- [ ] Merge all the cherry-pick PRs in a timely manner.

