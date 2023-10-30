// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-cluster-overcommit-about_{context}"]
= Understanding overcommitment

Requests and limits enable administrators to allow and manage the overcommitment of resources on a node. The scheduler uses requests for scheduling your container and providing a minimum service guarantee. Limits constrain the amount of compute resource that may be consumed on your node.

{product-title} administrators can control the level of overcommit and manage container density on nodes by configuring masters to override the ratio between request and limit set on developer containers. In conjunction with a per-project `LimitRange` object specifying limits and defaults, this adjusts the container limit and request to achieve the desired level of overcommit.

[NOTE]
====
That these overrides have no effect if no limits have been set on containers. Create a `LimitRange` object with default limits, per individual project, or in the project template, to ensure that the overrides apply.
====

After these overrides, the container limits and requests must still be validated by any `LimitRange` object in the project. It is possible, for example, for developers to specify a limit close to the minimum limit, and have the request then be overridden below the minimum limit, causing the pod to be forbidden. This unfortunate user experience should be addressed with future work, but for now, configure this capability and `LimitRange` objects with caution.


