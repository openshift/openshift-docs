// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

:_mod-docs-content-type: CONCEPT
[id="cli-about-cli_{context}"]
= About the OpenShift CLI

With the {oc-first}, you can create applications and manage {product-title}
ifdef::openshift-rosa[]
(ROSA)
endif::openshift-rosa[]
projects from a terminal. The OpenShift CLI is ideal in the following situations:

* Working directly with project source code
* Scripting
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
operations
ifndef::microshift[]
* Managing projects while restricted by bandwidth resources and the web console is unavailable
endif::microshift[]
ifdef::microshift[]
* Managing projects while restricted by bandwidth resources
endif::microshift[]
