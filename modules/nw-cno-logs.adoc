// Module included in the following assemblies:
//
// * networking/cluster-network-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-cno-logs_{context}"]
= Viewing Cluster Network Operator logs

You can view Cluster Network Operator logs by using the `oc logs` command.

.Procedure

* Run the following command to view the logs of the Cluster Network Operator:
+
[source,terminal]
----
$ oc logs --namespace=openshift-network-operator deployment/network-operator
----
