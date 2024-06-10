[[contributing-user-stories]]
= Contribute user stories to OpenShift documentation
:icons:
:toc: macro
:toc-title:
:toclevels: 1
:description: Basic information about how to create user stories for OpenShift GitHub repository

toc::[]

== Modularization backstory
OpenShift docs are modularized, starting from OpenShift 4.1.
All existing content has been replaced with content that is based on user stories and
complies with the modularization guidelines. All future content must both
support a user story and be modular.

== How do I contribute modularized content?
To contribute modularized content, you need to write a user story, create
documentation modules to support the user story, and create an assembly for the
story.

== What if I don't want to write in modules?
If you don't want to write the modules yourself but have a content change,
write a user story, provide details to support the story, and reach out to the
OpenShift docs team.

== How do I write a user story? Is there a template?
Instead of a template, we have a series of questions for you to answer to
create the user story. Follow the same steps if you are writing the modules
yourself or if you plan to work with the docs team.

The basic format of a user story is:

----
As a <type of user>, I want to <goal state> because <reason behind the goal>.
----

For example, "As a cluster administrator, I want to enable an Auto Scaling group to manage my OpenShift Enterprise
cluster deployed on AWS because I want my node count to scale based on application demand."

Use the following questions to guide you in providing the context for your user story and the necessary technical details to start a draft.
You don't have to answer all of these questions, only the ones that make sense to your particular user story.

=== Feature info
* What is the feature being developed? What does it do?
* How does it work?
* Are there any configuration files/settings/parameters being added or modified? Are any new commands being added or modified?
* What tools or software does the docs team need to test how this feature works? Does the docs team need to update any installed software?
* Are there any existing blogs, Wiki posts, Kbase articles, or Bzs involving this feature? Or any other existing information that may help to understand this feature?

=== Customer impact
* Who is the intended audience for this feature? If it's for Enterprise, does it apply to developers, admins, or both?
* Why is it important for our users? Why would they want to use this feature? How does it benefit them?
* How will the customer use it? Is there a use case?
* How will the customer interact with this feature? Client tools? Web console? REST API?

=== Product info
* Is this feature being developed for Online? Enterprise? Dedicated? OKD? All?
* Will this feature be rolled back to previous versions?
* If it's for Online, what type of plan do users need to use this feature?
* Is it user-facing, or more behind-the-scenes admin stuff?
* What tools or software does the docs team need to test how this feature works?

== How do I write in modules?
The full guidelines for writing modules are in the Customer Content Services (CCS)
link:https://redhat-documentation.github.io/modular-docs/[modularization guide].

The main concepts of writing in modules are:

* Each assembly contains the information required for a user to achieve a single
goal.
* Assemblies contain primarily `include` statements, which are references to
smaller, targeted module files.
* Modules can contain conceptual information, reference information, or steps,
but not a combination of the types.

For example, a simple assembly might contain the following three modules:

* A concept module that contains background information about the feature
that the user will configure
* A reference module that contains an annotated sample yaml file that the user
needs to modify
* A procedure module that contains the prerequisites that the user needs to
complete before they start configuring and steps that the user takes to
complete the configuration.

The `enterprise-4.1` branch contains sample assemblies that explain how to
get started with modular documentation for OpenShift and that serve as
references for including modules in assemblies. The
link:https://raw.githubusercontent.com/openshift/openshift-docs/enterprise-4.1/mod_docs_guide/mod-docs-conventions-ocp.adoc[Modular Docs OpenShift conventions]
assembly contains the
link:https://raw.githubusercontent.com/openshift/openshift-docs/enterprise-4.1/modules/mod-docs-ocp-conventions.adoc[Modular docs OpenShift conventions]
reference module, and the
link:https://github.com/openshift/openshift-docs/blob/enterprise-4.1/mod_docs_guide/getting-started-modular-docs-ocp.adoc[Getting started with modular docs on OpenShift]
assembly contains the
link:https://raw.githubusercontent.com/openshift/openshift-docs/enterprise-4.1/modules/creating-your-first-content.adoc[Creating your first content]
procedure module.
