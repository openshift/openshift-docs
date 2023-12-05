// Module included in the following assemblies:
//
// * networking/network-verification.adoc

:_mod-docs-content-type: PROCEDURE
ifdef::openshift-dedicated[]
[id="running-network-verification-manually-ocm_{context}"]
= Running the network verification manually
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
[discrete]
[id="running-network-verification-manually-ocm_{context}"]
= Running the network verification manually using {cluster-manager}
endif::openshift-rosa[]

You can manually run the network verification checks for an existing
ifdef::openshift-dedicated[]
{product-title}
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
{product-title} (ROSA)
endif::openshift-rosa[]
cluster by using {cluster-manager-first}.

.Prerequisites

* You have an existing
ifdef::openshift-dedicated[]
{product-title}
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
cluster.
* You are the cluster owner or you have the cluster editor role.

.Procedure

. Navigate to {cluster-manager-url} and select your cluster.

. Select *Verify networking* from the *Actions* drop-down menu.
