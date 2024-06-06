//Duplicate this file and use it as a template to write your content.
//Look for TODO statements and angle brackets to identify content to add or replace.

// Basic document metadata
// TODO: replace anything in angle brackets in this metadata block
:_mod-docs-content-type: ASSEMBLY
[id=“cloud-experts-<topic>-tutorial”]
= Tutorial: <Topic>
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: cloud-experts-<topic>-tutorial

//This automatically adds a table of contents so readers can jump to a specific heading.
toc::[]

//TODO: The following block must remain commented out, but add your name to the authors list in whatever format you want to be publicly visible in the openshift-docs repo.
//Mobb content metadata
//Brought into ROSA product docs 2023-09-18
//---
//date: '2021-06-10'
//title: ROSA Prerequisites
//weight: 1
//tags: ["AWS", "ROSA", "Quickstarts"]
//authors:
//  - <author>
//---

// Docs will remove this support statement once this content has gone through regular QE validation.
// TODO: IF YOU UPDATED THIS DOCUMENT AND THIS STATEMENT IS COMMENTED OUT, make sure you uncomment it again so QE can review your updates.
include::snippets/mobb-support-statement.adoc[leveloffset=+1]

//TODO: Write a few sentences about what the people who use this doc want to accomplish and what that might let them do.
Introductory sentence or two about this whole file and why a customer might want to follow these steps.

//TODO: Write up the information you want to publish for customers.
//This documentation uses basic asciidoc syntax.

//TODO: replace anything in angle brackets and add your content below
[id='cloud-experts-<topic>-tutorial-<subsection1>']
== <Subsection 1>

Introductory sentence about the purpose of this section.

Steps or information that the customer should follow.

Check out the syntax guide below for examples of what you can add here.

//TODO: replace anything in angle brackets and add your content below
[id='cloud-experts-<topic>-tutorial-<subsection2>']
== <Subsection 2>

Introductory sentence about the purpose of this section.

Steps or information that a customer should follow.

Check out the syntax guide below for examples of what you can add here.

//TODO: Provide links to any next steps or additional information the user is likely to want at this point.
//TODO: If no other resources are likely to be needed, just delete this block.
[id='cloud-experts-<topic>-tutorial-additional-resources']
== Additional resources
* link:https://cloud.redhat.com/experts/rosa/verify-permissions[Verify required permissions for a ROSA STS deployment]
* link:https://cloud.redhat.com/experts/rosa/ecr[Configure a ROSA cluster to pull images from AWS Elastic Container Registry]

//TODO: When you are finished writing your tutorial, delete everything below this line.
// These are just some basic syntax examples so you can copy and paste easily.
== AsciiDoc Syntax Basics

For more information, refer to link:https://asciidoctor.org/docs/asciidoc-writers-guide/[AsciiDoc Writer's Guide]

=== Headings

To add a heading, use equals signs at the beginning of the line:

[source]
----
== Second level heading text
=== Third level heading text
----

Up to 5 levels of heading are available, but this usually won't be required.

.Block element heading
You can also add a small header to a block element by adding a full-stop at the start of the line. Do not add a space or this will become an ordered list item.

[source]
----
.Block element heading
----

=== Paragraphs, links, and inline elements

A paragraph is just a plain line of text like this.
A single line break will be rendered as part of the same paragraph.

A double line break will be rendered as a separate paragraph.

You can _emphasize_ or *strengthen* text in a paragraph, or add a link to a link:http://www.redhat.com[Red Hat website].

[source]
----
You can _emphasize_ or *strengthen* text in a paragraph, or add a link to a link:http://www.redhat.com[Red Hat website].
----

Link to non-Red Hat websites if necessary, but remember they won't necessarily open in a new tab, and might lead users away from your document.

=== Lists

Unordered lists use asterisks followed by a space:

.My unordered list
* First level list item
** Use multiple asterisks to indent second level list items
* Another first level list item

[source]
----
.My unordered list
* First level list item
** Use multiple asterisks to indent second level list items
* Another first level list item
----

Ordered lists use full stops followed by a space:

.My ordered list
. Step one
.. Step 1.a.
. Step two

[source]
----
.My ordered list
. Step one
.. Step 1.a.
. Step two
----

You can also use two colons to get a term and definition list:

.Important definitions
term:: definition goes here
cat:: A cute and cuddly carnivorous companion animal with hidden foot knives.
dog:: A cute and cuddly omnivorous companion animal with clearly visible foot knives.

[source]
----
.Important definitions
term:: definition goes here
cat:: A cute and cuddly carnivorous companion animal with hidden foot knives.
dog:: A cute and cuddly omnivorous companion animal with clearly visible foot knives.
----

=== Code

You can use `backticks` to indicate a literal value inline, but for commands, code, and terminal output you want a code block:

[source,terminal]
----
$ rosa version
1.2.23
I: There is a newer release version '1.2.26', please consider updating: https://mirror.openshift.com/pub/openshift-v4/clients/rosa/latest/
----

[source]
------
[source,terminal]
----
$ rosa version
1.2.23
I: There is a newer release version '1.2.26', please consider updating: https://mirror.openshift.com/pub/openshift-v4/clients/rosa/latest/
----
------

The `[source]` part ahead of the code block specifies the kind of code in the block, and enables syntax highlighting based on the language provided after the comma.


=== Tables

Tables use a combination of pipes and equals signs for their basic structure. If you want to include more complex content, you can add an `a` before the pipe indicating the start of the complex cell, and use other kinds of asciidoc syntax in that cell as required.

.Tables need a title
|===
|Left column |Right column

| Row 1 left column cell
| Row 1 right column cell

a| Row 2 left column cell

[NOTE]
====
With a note!
====

| Row 2 right column cell

|===

[source]
------
.Tables need a title
|===
|Left column |Right column

| Row 1 left column cell
| Row 1 right column cell

a| Row 2 left column cell

[NOTE]
=====
With a note!
====

| Row 2 right column cell

|===
------

=== Images

Place the image you want to use in the `cloud_experts_tutorials/images` sub-directory, and use only the file name in the `image::` block (not the relative path). For accessibility support, add a title for the image and describe the contents of the image. We recommend using PNG and SVG image formats.

.The perspectives menu in OpenShift Web Console
image::web_console_perspectives.png[The perspectives menu in OpenShift Web Console showing the Developer and Administrator persoectives]

[source]
----
.The perspectives menu in OpenShift Web Console
image::web_console_perspectives.png[The perspectives menu in OpenShift Web Console showing the Developer and Administrator persoectives]
----

=== Warnings and admonition blocks

If you want to highlight some information you can place it in a callout block.
Only do this for important things a user might miss, or our users will start ignoring them.

[NOTE]
====
You can use other elements inside an admonition, but don't go overboard.
We typically use three kinds:

* NOTE is for information that is useful, and can often be just a regular sentence instead.
* IMPORTANT is for information that a customer should be aware of but won't cause serious problems if it's ignored.
* WARNING is for information that a customer needs to obey to avoid data loss or other critical failures.
====

[source]
----

[NOTE]
====
You can use other elements inside an admonition, but don't go overboard.
We typically use three kinds:

* NOTE is for information that is useful to know, and can often be just a regular sentence instead.
* IMPORTANT is for information that a customer should be aware of but won't cause serious problems if it's ignored.
* WARNING is for information that a customer needs to obey to avoid data loss or other critical failures.
====
----

=== Combining block level elements

You can chain multiple block-level asciidoc elements together with the plus sign. You'll most often do this with steps and code blocks, so that the code block stays at the same indent level as the instruction text, for example:

. Open a terminal and log in to the ROSA CLI using your personal token:
+
[source,terminal]
----
$ rosa login --token=<your_token>
----

. Check your ROSA CLI version:
+
[source,terminal]
----
$ rosa version
----

[source]
------

. Open a terminal and log in to the ROSA CLI using your personal token:
+
[source,terminal]
----
$ rosa login --token=<your_token>
----
. Check your ROSA CLI version:
+
[source,terminal]
----
$ rosa version
----
------