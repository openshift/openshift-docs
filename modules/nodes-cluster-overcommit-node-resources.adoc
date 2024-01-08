// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cluster-overcommit-node-resources_{context}"]

= Reserving resources for system processes

To provide more reliable scheduling and minimize node resource overcommitment,
each node can reserve a portion of its resources for use by system daemons
that are required to run on your node for your cluster to function.
In particular, it is recommended that you reserve resources for incompressible resources such as memory.

.Procedure

To explicitly reserve resources for non-pod processes, allocate node resources by specifying resources
available for scheduling.
For more details, see Allocating Resources for Nodes.
