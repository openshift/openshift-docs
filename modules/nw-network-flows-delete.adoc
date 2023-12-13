// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/tracking-network-flows.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-network-flows-delete_{context}"]
= Deleting all destinations for network flows collectors

As a cluster administrator, you can configure the Cluster Network Operator (CNO) to stop sending network flows metadata to a network flows collector.

.Prerequisites

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.

.Procedure

. Remove all network flows collectors:
+
[source,terminal]
----
$ oc patch network.operator cluster --type='json' \
    -p='[{"op":"remove", "path":"/spec/exportNetworkFlows"}]'
----
+
.Example output
[source,terminal]
----
network.operator.openshift.io/cluster patched
----
