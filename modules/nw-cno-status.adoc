// Module included in the following assemblies:
//
// * networking/cluster-network-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-cno-status_{context}"]
= Viewing Cluster Network Operator status

You can inspect the status and view the details of the Cluster Network Operator
using the `oc describe` command.

.Procedure

* Run the following command to view the status of the Cluster Network Operator:
+
[source,terminal]
----
$ oc describe clusteroperators/network
----
