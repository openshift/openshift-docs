# Style Guide for Technical Documentation

When helping draft or edit documentation, follow these rules. **Red Hat Supplementary Style Guide rules take precedence when they conflict with IBM.**

## IBM Style Guide rules

### Grammar

- **"since"** = time only, not a synonym for "because". Use "because".
- **"while"** = time only, not a synonym for "although". Use "although".
- **"once"** = one time. Not a synonym for "after" or "when".
- **"can"** for ability/permission, **"might"** for possibility, **"must"** for requirements. Do not use "should" for requirements.
- **"verify"** not "make sure". **"examine"** not "look at". **"omit"** not "leave out".
- **"by using"** not "using" to avoid ambiguity: "Unload the file by using the utility."
- Avoid phrasal verbs when the verb alone works: "click" not "click on", "start" not "start up", "print" not "print out".
- Avoid Latin abbreviations: "for example" not "e.g.", "that is" not "i.e.", "and so on" not "etc."
- Avoid anthropomorphism: do not give human characteristics to inanimate objects. Focus on users and their actions, not on a product and its actions. Common anthropomorphic verbs to watch for: "allow", "let", "permit", "enable". Rewrite in a user-oriented style.
  - "The system determines..." not "The system thinks..."
  - "The server rejects..." not "The server refuses..."
  - "The speech recognition engine accepts only the following words." not "The speech recognition engine is interested only in the following words."
  - "You can use the Placement service to provide tenant isolation..." not "The Placement service allows you to provide tenant isolation..."
- Avoid noun stacks (more than 3 nouns in a row). Restructure with prepositions.
- Do not use verbs as nouns: "after the installation" not "after the install"; "during the compilation" not "during the compile".

### Punctuation

- **No em dashes.** Rewrite using commas, parentheses, semicolons, or colons. (Red Hat Vale linter flags these.)
- **En dash** for ranges, no spaces: "pages 100--107", "September--December".
- **Hyphens:** Hyphenate compound adjectives before a noun ("data-driven businesses", "command-line tool"). Do not hyphenate after -ly adverbs ("fully qualified path"). After the noun, hyphens are often optional.
- **Colons:** Use after a complete sentence to introduce a list. Lowercase after colon mid-sentence; uppercase for vertical lists, notes, labels.
- **Parentheses:** avoid in general text; rewrite if possible.
- **Semicolons:** "then" is not a coordinating conjunction. Use "and then" or a semicolon: "Click Start, and then select a program."
- Do not use symbols instead of words in text: "&" -> "and", "#" -> "number".

### Formatting

- Do not use italic for emphasis; restructure the sentence instead.
- Use "select" for general UI interaction; "click" only for mouse-specific actions (Red Hat convention).
- Refer readers forward with "see": "For more information, see the Installation Guide." (Not "refer to".)

### Capitalization

- Do not capitalize common tech terms: "internet", "web", "cloud", "kernel", "hypervisor" (unless part of a product name).
- **Kubernetes Operators** are always capitalized ("the Operator", "Cluster Version Operator") to distinguish from mathematical/human operators.
- API objects: capitalize as they appear in code and use monospace (`Pod`, `Deployment`, `Service`). Use lowercase in general prose ("a pod", "a deployment") when not referring to the specific API object.
- "open source" -- lowercase, two words, no hyphen.

### Abbreviations

- Spell out on first use with abbreviation in parentheses, then use the abbreviation afterward.
- **Exceptions (do not spell out):** DNS, LDAP, LDAPS, TLS, IP, TCP, UDP, FQDN, HTML, URL, API, SSH, NIC, RPM. These are standard enough.
- Use "SSL/TLS" in headings for context; "TLS" in body text.
- No periods in abbreviations: "US" not "U.S."
- Plural abbreviations: add lowercase "s", no apostrophe: "APIs", "VMs", "URLs".
- Never start a sentence with an abbreviation unless it is the official product name.
- "an FAQ" (read as "an F-A-Q"), "an SQL" (read as "ess-queue-ell"), "a RHEL system" (read as "rell").

### Numbers and Measurements

- Spell out zero through nine; use numerals for 10 and above.
- Always use numerals with units: "2 GB", "5 seconds", "100 Mbps".
- Put a space between value and unit: "2 GB" not "2GB".
- Unit abbreviations are both singular and plural: "1 mm", "10 mm".
- Spell out fractions: "three-fourths". Use hyphens: "twenty-four".
- Use US English plurals: "matrixes" not "matrices".

## Red Hat Supplementary Style Guide Rules

These recommendations might override existing guidance in the [_IBM Style_](https://www.ibm.com/docs/en/ibm-style) guide, or might provide guidance for items not covered in the _IBM Style_ guide.

> **NOTE:**

If applicable, these guidelines provide example formatting in AsciiDoc, which is the markup language that Red Hat Customer Content Services currently uses. However, the guidelines can be applied to any language.


### Grammar and language

#### Contractions

Avoid contractions.

#### Minimalism
Minimalism is a methodology for creating targeted documentation focused on your readers' needs. If you understand your customers' needs, you can write shorter and simpler documentation specific to what customers want to do.

Minimalism has five principles:

##### Principle 1: Customer focus and action orientation
Know what your users do, what their goals are, and why they perform these actions. Minimize how much content customers must wade through to get to something they recognize as real work. Separate conceptual and background information from procedural tasks.

##### Principle 2: Findability
Findability covers two areas:

* Ensure your content is findable through Google search and access.redhat.com site searches.
* Ensure your content is scannable. Use short paragraphs and sentences and bulleted lists where appropriate.

##### Principle 3: Titles and headings
Use clear titles with familiar keywords for customers. Keep titles and headings between 3 to 11 words. Headings that are too short lack clarity and don’t help customers know what’s in a section. Headings that are too long are less visible in Google searches and harder for customers to understand.

##### Principle 4: Elimination of fluff
Avoid long introductions and unnecessary context. Shorten unnecessarily long sentences.

##### Principle 5: Error recovery, verification, and troubleshooting
Recognize that people make mistakes and need to verify that they have completed a task. Be sure to include troubleshooting, error recovery, and verification steps.

#### Users
In most cases, the word "user" refers to a person or a person’s user account, and therefore would be considered animate. In these cases, use animate personal pronouns such as "who".

In certain technical cases, these users are not persons but instead system accounts or more abstract concepts (inanimate). For example, Linux `root` and `guest` users do not relate to any person. Applications and services might run as specific Linux users with no person controlling them. SELinux users such as `user_u` or `sysadm_u` are identifiers of one or multiple Linux users for access control purposes. In these specific cases, refer to these inanimate users with inanimate personal pronouns such as "that".

In these specific cases, and only if you cannot write around it, you can refer to these inanimate users with inanimate personal pronouns such as "that".

### Formatting

#### Commands in code blocks

Use a single command per code block for each procedure step. Separate a command and its related example output into individual code blocks. This approach helps with readability and makes it possible for the copy button in code blocks to work correctly.

#### Explanation of commands and variables used in code blocks

To explain commands, lines of code, or user-replaced values in a code block, do not use callouts.

Instead, follow the code block with the relevant explanation or description of the elements, using the following guidelines:

* Use a simple sentence to explain or describe a single line of command, variable, option, or parameter.

```terminal
$ hcp create cluster <platform> --help
```
+
Use the `hcp create cluster` command to create and manage hosted clusters. The supported platforms are `aws`, `agent`, and `kubevirt`.

* Use a definition list to explain multiple options, parameters, user-replaced values, placeholders, or UI elements.
  * List the parameters or variables in the order in which they appear in the code block.
  * Introduce definition lists with "where:" and begin each variable description with "Specifies".

```yaml
$ cat <<EOF | oc -n <my_product_namespace> create -f -
apiVersion: v1
kind: Secret
metadata:
 name: <my_product_database_certificates_secrets>
type: Opaque
stringData:
 postgres-ca.pem: |-
  -----BEGIN CERTIFICATE-----
  <ca_certificate_key>
 postgres-key.key: |-
  -----BEGIN CERTIFICATE-----
  <tls_private_key>
 postgres-crt.pem: |-
  -----BEGIN CERTIFICATE-----
  <tls_certificate_key>
  # ...
EOF
```
+
where:

* **`<my_product_database_certificates_secrets>`**\
Specifies the name of the certificate secret.
* **`<ca_certificate_key>`**\
Specifies the CA certificate key.
* **`<tls_private_key>`**\
Specifies the TLS private key.
* **`<tls_certificate_key>`**\
Specifies the TLS certificate key.
  * Use a bulleted list to describe the structure of a sample YAML file or explain multiple lines of code in a code block.
    * List the explanations in the order in which they appear in the code block.
    * Use the bullet format that makes the most sense for your explanations. You do not have to follow the exact wording in the following example.

```yaml
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: build-and-deploy
spec:
  workspaces:
  - name: shared-workspace
  params:
...
  tasks:
  - name: build-image
    taskRef:
      resolver: cluster
      params:
      - name: kind
        value: task
      - name: name
        value: buildah
      - name: namespace
        value: openshift-pipelines
    workspaces:
    - name: source
      workspace: shared-workspace
    params:
    - name: TLSVERIFY
      value: "false"
    - name: IMAGE
      value: $(params.IMAGE)
    runAfter:
    - fetch-repository
  - name: apply-manifests
    taskRef:
      name: apply-manifests
    workspaces:
    - name: source
      workspace: shared-workspace
    runAfter:
      - build-image
...
```
+
***** `spec.workspaces` defines the list of pipeline workspaces shared between the tasks defined in the pipeline. A pipeline can define as many workspaces as required. In this example, only one workspace named `shared-workspace` is declared.
***** `spec.tasks` defines the tasks used in the pipeline. This snippet defines two tasks, `build-image` and `apply-manifests`.
***** `spec.tasks.workspaces` defines the list of task workspaces used in the `build-image` and `apply-manifests` tasks. A task definition can include as many workspaces as it requires. However, it is recommended that a task uses at most one writable workspace. In this example, both the tasks share a common task workspace named `source`, which in turn could share the pipeline workspace named `shared-workspace`.

#### Non-breaking spaces

Use a _non-breaking space_ (`{nbsp}`) between the words "Red" and "Hat". The non-breaking space prevents an automatic line break from separating the two words onto two lines.
A _non-breaking space_ prevents the company name from splitting across a line break.

#### Titles and headings

Use the following guidelines when writing titles and headings:

* Write all titles and headings, including the titles of product documentation guides and Knowledgebase articles, in sentence-style capitalization. Do not use headline-style capitalization.
* Focus your headings on user jobs and outcomes. Begin with user intent and then explain how the product fulfills the intended purpose.
* Use imperative verbs for procedural and task-based content. Do not use gerunds (-ing forms). Imperatives are more direct, translate more consistently, and better map to task sequences. Do not mix imperatives and gerunds.
* For concept and reference topics, use nouns or noun phrases. Do not use "Understanding" or "Understand" to begin a concept or reference topic.
* Avoid generic titles such as "Introduction," "About," or "Overview." Instead, use descriptive keywords that clearly define the specific task or subject.
* Keep headings between 3 and 11 words (approximately 60-75 characters) to ensure scannability and findability. Titles that exceed 60-75 characters are often truncated in search engine results.

#### User-replaced values

A _user-replaced value_, also known as a replaceable or variable value, is a placeholder that the user replaces with a value that is relevant for their situation. User-replaced values are often found in places such as code blocks, file paths, and commands.

Use descriptive names for user-replaced values and follow this general format: _&lt;value_name>_.

> **NOTE:**

Ensure that user-replaced values have the following characteristics:

* Surrounded by angle brackets (`< >`)
* Separated by underscores (`_`) for multi-word values
* Lowercase, unless the rest of the related text is uppercase or another capitalization scheme
* If the user-replaced value is referencing a value in code or in a command that is normally monospace, also use monospace for the user-replaced value
* If you want to use a user-replaced value in example output, format the replaceable value with italics and in angle brackets. Alternatively, if you choose to use an example value instead, do not italicize the example value and do not place it in angle brackets.

```
Create an Ansible inventory file that is named `/_<path>_/inventory/hosts`.
```

This example renders as follows in HTML:

Create an Ansible inventory file that is named `/_<path>_/inventory/hosts`.

To explain user-replaced values used in a code block, you must use a definition list following the code block. See [Explanation of commands and variables used in code blocks](#explanation-of-commands-and-variables-used-in-code-blocks) for details.

### Structure

#### Admonitions

Admonitions should draw the reader’s attention to certain information. Keep admonitions to a minimum, and avoid placing multiple admonitions close to one another. If multiple admonitions are necessary, restructure the information by moving the less-important statements into the flow of the main content.

Valid admonition types:

* **NOTE**\
Additional guidance or advice that improves product configuration, performance, or supportability.
* **IMPORTANT**\
Advisory information essential to the completion of a task. Users must not disregard this information.
* **WARNING**\
Information about potential system damage, data loss, or a support-related issue if the user disregards this admonition. Explain the problem, cause, and offer a solution that works. If available, offer information to avoid the problem in the future or state where to find more information.
* **TIP**\
Alternative methods that might not be obvious. Makes applying the techniques and procedures described in the text easier or targets specific needs. Helps users understand the benefits and capabilities of the product. Not essential to using the product.

> **IMPORTANT:**

CAUTION, which is another type of AsciiDoc admonition, is not fully supported by the Red Hat Customer Portal. Do not use this admonition type.


Admonitions should be short and concise. Do not include procedures in an admonition.

Only individual admonitions are allowed, for example, you cannot have a plural **NOTES** heading.

**Example AsciiDoc**

```
[NOTE]
====
Text for note.
====
```

#### Lead-in sentences

A lead-in sentence in this context is the text that directly follows a `Prerequisites` or `Procedure` heading in a task-based module. It is distinct from the module abstract, which describes the goals of the user for the module.

Do not use a lead-in sentence in the `Prerequisites` or `Procedure` sections of a module unless it is necessary to aid navigation or add clarity.

The following examples demonstrate when a lead-in sentence might add value.

* Your module has a long list of prerequisites, and you want to group the prerequisites in sections to make it easier for users to understand what tasks must be performed to complete a procedure.
* Your module has a complex procedure or set of prerequisites, and you want to emphasize that all steps or prerequisites must be completed.

Use a complete sentence for the lead-in sentence to reduce ambiguity and support translation.

#### Prerequisites

When writing prerequisites, be as clear and concise as possible. You can use the passive voice, _if necessary_, to achieve that end.

Write prerequisites as checks that are true or that the user must have completed before they begin a procedure. They can be actions that the user, another person, or piece of technology has completed. Prerequisites can also include items that the user must have ready before beginning the procedure.

* The passive voice might be appropriate for a prerequisite that is not completed by the current user. For example, having a configuration enabled by a system admin.
* Avoid using imperative formations.
* Use parallel language when you write prerequisites. For example, if one bullet is a complete sentence, write the other bullets as complete sentences. But one bullet can be passive voice and another active voice.

* JDK 11 or later is installed.

  Passive voice: the agent is unknown or unimportant.
* A running Kafka instance in {product}.

  Not a complete sentence: This prerequisite is acceptable if all the other prerequisites in your list are also not complete sentences.
* You are logged in to the Administration Portal.
* You have validated Thing 1.

* [_Procedure Prerequisites_ in the _Modular Documentation Reference Guide_](https://redhat-documentation.github.io/modular-docs/#creating-procedure-modules)

#### Short descriptions

Every module and assembly must include a _short description_, formerly called an _abstract_. A short description provides a high-quality summary for both readers and AI-powered search tools.

* Short descriptions ***must*** be at least 50 characters and no more than 300 characters long.
* Place any information that exceeds 300 characters in a new paragraph or paragraphs. It cannot be part of the short description.

The short description must have the correct formatting and tagging:

* In AsciiDoc, label the short description with `[role="_abstract"]`.
* In DITA, tag the short description with `<shortdesc>`.

> **IMPORTANT:**

Do not start a module or assembly with an admonition, even when adding the Technology Preview admonition. Always provide a short description first.


##### Placement of the short description in procedures

In procedures, the short description is displayed between the module title and the prerequisites section. Put additional information in a new paragraph or paragraphs.

In AsciiDoc, additional information is displayed ***before*** the prerequisites. The following image illustrates how to place this information:

##### Core principles for writing a helpful short description ===

Short descriptions help readers find the information that they need and confirm that they are in the right place. The following principles ensure that you are writing the best short description that you can:

* Include user intent. Explain **what** the user must do and **why** they must complete that action. Build upon the title--do not repeat it.
* Write for AI and search. High-quality short descriptions are a primary source of metadata for large language models (LLMs) and search engine link previews. A high quality, human-verified summary reduces the risk of AI misinterpretation and saves processing time.
* Do not use DITA-incompatible structures, such as bulleted lists or multiple paragraphs.

### Technical examples

#### Ellipses in YAML code blocks

Use the number sign (`#`) to comment out an ellipsis in YAML code blocks.
YAML reserves `...` to indicate the end of a document without starting a new document.

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
metadata:
  name: cluster
# ...
```

### Links

#### Cross-references

Follow these guidelines when adding cross-references within your documentation:

* Include cross-references only when necessary.
* If the information is critical, consider including it instead of cross-referencing.

**Example AsciiDoc: Cross-reference**

```
For more information about <topic>, see xref:<link>[<link_text>].
```

#### External links

Follow these guidelines when linking externally:

* Avoid unnecessary links to external sites not owned and operated by Red Hat or IBM.
Links to external sites can change or be unreliable.
In addition, customers might infer that Red Hat endorses or supports the linked content, even if that is not the intent.

  > **NOTE:**

  Links to upstream sites, such as GitHub, are considered to be external links.
  

* When possible, link to a top-level page and avoid deep links to a specific page or image.
Deep links can break more frequently and can inadvertently bypass a site’s legal notices.
* Do not use bare URLs for links.
Bare URLs are unhelpful because they do not provide adequate context about the link target.
* Do not use URL shorteners to replace full URLs.
* Always include meaningful link text.
Meaningful link text describes to users what content they will see if they click the link.
* Use hyperlinks unless the URL is an example URL or is otherwise inaccessible to users.
* By default, links are followable and crawlable. Do not use the `nofollow` link option unless absolutely necessary.

For information about links and web addresses, including using URLs in examples, see the _IBM Style_ guide.

**Example AsciiDoc: External link**

```
For more information about <topic>, see link:<link>[<link_text>].
```

#### Links to Red Hat documentation

* Use `latest` in the URL so that the link resolves to the last published version.

**Example AsciiDoc: Latest version**

```
For more information, see link:https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/disconnected_environments/oc-mirror-migration-v1-to-v2[Migrating from oc-mirror plugin v1 to v2].
```

## Other style rules

Use attributes located in /home/sslocket/repos/openshift-docs/_attributes/common-attributes.adoc instead of hard coded product names.