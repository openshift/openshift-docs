:_mod-docs-content-type: ASSEMBLY
[id="cloud-experts-getting-started-simple-cli-guide"]
= Tutorial: Simple CLI guide
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: cloud-experts-getting-started-simple-cli-guide

toc::[]

//rosaworkshop.io content metadata
//Brought into ROSA product docs 2023-11-16

This page outlines the minimum list of commands to deploy a {product-title} (ROSA) cluster using the command line interface (CLI). 

[NOTE]
====
While this simple deployment works well for a workshop setting, clusters used in production should be deployed with a more detailed method.
====

== Prerequisites

* You have completed the prerequisites in the xref:../../../cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-setup.adoc#cloud-experts-getting-started-setup[Setup] tutorial.

== Creating account roles
Run the following command _once_ for each AWS account and y-stream OpenShift version:

[source,terminal]
----
rosa create account-roles --mode auto --yes
----

== Deploying the cluster

. Create the cluster with the default configuration by running the following command substituting your own cluster name:
+
[source,terminal]
----
rosa create cluster --cluster-name <cluster-name> --sts --mode auto --yes
----

. Check the status of your cluster by running the following command:
+
[source,terminal]
----
rosa list clusters
----