// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc
// * post_installation_configuration/node-tasks.adoc

[id="nodes-cluster-overcommit-resource-requests_{context}"]
= Resource requests and overcommitment

For each compute resource, a container may specify a resource request and limit.
Scheduling decisions are made based on the request to ensure that a node has
enough capacity available to meet the requested value. If a container specifies
limits, but omits requests, the requests are defaulted to the limits. A
container is not able to exceed the specified limit on the node.

The enforcement of limits is dependent upon the compute resource type. If a
container makes no request or limit, the container is scheduled to a node with
no resource guarantees. In practice, the container is able to consume as much of
the specified resource as is available with the lowest local priority. In low
resource situations, containers that specify no resource requests are given the
lowest quality of service.

Scheduling is based on resources requested, while quota and hard limits refer
to resource limits, which can be set higher than requested resources. The
difference between request and limit determines the level of overcommit;
for instance, if a container is given a memory request of 1Gi and a memory limit
of 2Gi, it is scheduled based on the 1Gi request being available on the node,
but could use up to 2Gi; so it is 200% overcommitted.
