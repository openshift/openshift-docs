:_mod-docs-content-type: ASSEMBLY
[id="getting-started-with-openshift-gitops"]
= Installing {gitops-title}
include::_attributes/common-attributes.adoc[]
:context: installing-openshift-gitops

toc::[]

[role="_abstract"]
{gitops-title} uses Argo CD to manage specific cluster-scoped resources, including cluster Operators, optional Operator Lifecycle Manager (OLM) Operators, and user management.

[discrete]
== Prerequisites

* You have access to the {product-title} web console.
* You are logged in as a user with the `cluster-admin` role.
* You are logged in to the {product-title} cluster as an administrator.
* Your cluster has the xref:../../installing/cluster-capabilities.adoc#marketplace-operator_cluster-capabilities[Marketplace capability] enabled or the Red Hat Operator catalog source configured manually.

[WARNING]
====
If you have already installed the Community version of the Argo CD Operator, remove the Argo CD Community Operator before you install the {gitops-title} Operator.
====

This guide explains how to install the {gitops-title} Operator to an {product-title} cluster and log in to the Argo CD instance.

[IMPORTANT]
====
The `latest` channel enables installation of the most recent stable version of the {gitops-title} Operator. Currently, it is the default channel for installing the {gitops-title} Operator.

To install a specific version of the {gitops-title} Operator, cluster administrators can use the corresponding `gitops-<version>` channel. For example, to install the {gitops-title} Operator version 1.8.x, you can use the `gitops-1.8` channel.
====

include::modules/installing-gitops-operator-in-web-console.adoc[leveloffset=+1]

include::modules/installing-gitops-operator-using-cli.adoc[leveloffset=+1]

include::modules/logging-in-to-the-argo-cd-instance-by-using-the-argo-cd-admin-account.adoc[leveloffset=+1]
