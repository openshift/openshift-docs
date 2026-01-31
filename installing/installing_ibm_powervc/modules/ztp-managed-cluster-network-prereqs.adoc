// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-managed-cluster-network-prereqs_{context}"]
= Connectivity prerequisites for managed cluster networks

Before you can install and provision a managed cluster with the {ztp-first} pipeline, the managed cluster host must meet the following networking prerequisites:

* There must be bi-directional connectivity between the {ztp} container in the hub cluster and the Baseboard Management Controller (BMC) of the target bare-metal host.

* The managed cluster must be able to resolve and reach the API hostname of the hub hostname and `{asterisk}.apps` hostname. Here is an example of the API hostname of the hub and `{asterisk}.apps` hostname:

** `api.hub-cluster.internal.domain.com`
** `console-openshift-console.apps.hub-cluster.internal.domain.com`

* The hub cluster must be able to resolve and reach the API and `{asterisk}.apps` hostname of the managed cluster. Here is an example of the API hostname of the managed cluster and `{asterisk}.apps` hostname:

** `api.sno-managed-cluster-1.internal.domain.com`
** `console-openshift-console.apps.sno-managed-cluster-1.internal.domain.com`
