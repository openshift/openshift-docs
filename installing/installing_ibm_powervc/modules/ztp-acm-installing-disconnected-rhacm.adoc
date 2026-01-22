// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="installing-disconnected-rhacm_{context}"]
:_mod-docs-content-type: PROCEDURE
= Installing {ztp} in a disconnected environment

Use {rh-rhacm-first}, {gitops-title}, and {cgu-operator-first} on the hub cluster in the disconnected environment to manage the deployment of multiple managed clusters.

.Prerequisites

* You have installed the {product-title} CLI (`oc`).

* You have logged in as a user with `cluster-admin` privileges.

* You have configured a disconnected mirror registry for use in the cluster.
+
[NOTE]
====
The disconnected mirror registry that you create must contain a version of {cgu-operator} backup and pre-cache images that matches the version of {cgu-operator} running in the hub cluster. The spoke cluster must be able to resolve these images in the disconnected mirror registry.
====

.Procedure

* Install {rh-rhacm} in the hub cluster. See link:https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/{rh-rhacm-version}/html/install/installing#install-on-disconnected-networks[Installing {rh-rhacm} in a disconnected environment].

* Install {gitops-shortname} and {cgu-operator} in the hub cluster.
