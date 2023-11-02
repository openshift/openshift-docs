// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cluster-overcommit-node-disable_{context}"]
= Disabling overcommitment for a node

When enabled, overcommitment can be disabled on each node.

.Procedure

To disable overcommitment in a node run the following command on that node:

[source,terminal]
----
$ sysctl -w vm.overcommit_memory=0
----
