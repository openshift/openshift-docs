// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-cluster-overcommit-reserving-memory_{context}"]
= Understanding compute resources and containers
The node-enforced behavior for compute resources is specific to the resource
type.

[id="understanding-container-CPU-requests_{context}"]
== Understanding container CPU requests

A container is guaranteed the amount of CPU it requests and is additionally able
to consume excess CPU available on the node, up to any limit specified by the
container. If multiple containers are attempting to use excess CPU, CPU time is
distributed based on the amount of CPU requested by each container.

For example, if one container requested 500m of CPU time and another container
requested 250m of CPU time, then any extra CPU time available on the node is
distributed among the containers in a 2:1 ratio. If a container specified a
limit, it will be throttled not to use more CPU than the specified limit.
CPU requests are enforced using the CFS shares support in the Linux kernel. By
default, CPU limits are enforced using the CFS quota support in the Linux kernel
over a 100ms measuring interval, though this can be disabled.

[id="understanding-memory-requests-container_{context}"]
== Understanding container memory requests

A container is guaranteed the amount of memory it requests. A container can use
more memory than requested, but once it exceeds its requested amount, it could
be terminated in a low memory situation on the node.
If a container uses less memory than requested, it will not be terminated unless
system tasks or daemons need more memory than was accounted for in the node's
resource reservation. If a container specifies a limit on memory, it is
immediately terminated if it exceeds the limit amount.

////
Not in 4.1
[id="containers-ephemeral_{context}"]
== Understanding containers and ephemeral storage

[NOTE]
====
The {product-title} cluster uses ephemeral storage to store information that does not have to persist after the cluster is destroyed.
====

A container is guaranteed the amount of ephemeral storage it requests. A
container can use more ephemeral storage than requested, but once it exceeds its
requested amount, it can be terminated if the available ephemeral disk space gets
too low.

If a container uses less ephemeral storage than requested, it will not be
terminated unless system tasks or daemons need more local ephemeral storage than
was accounted for in the node's resource reservation. If a container specifies a
limit on ephemeral storage, it is immediately terminated if it exceeds the limit
amount.
////
