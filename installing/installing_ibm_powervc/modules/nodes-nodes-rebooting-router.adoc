// Module included in the following assemblies:
//
// * nodes/nodes-nodes-rebooting.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-nodes-rebooting-router_{context}"]
= Understanding how to reboot nodes running routers

In most cases, a pod running an {product-title} router exposes a host port.

The `PodFitsPorts` scheduler predicate ensures that no router pods using the
same port can run on the same node, and pod anti-affinity is achieved. If the
routers are relying on IP failover for high availability, there is nothing else that is needed.

For router pods relying on an external service such as AWS Elastic Load Balancing for high
availability, it is that service's responsibility to react to router pod restarts.

In rare cases, a router pod may not have a host port configured. In those cases,
it is important to follow the recommended restart process for infrastructure nodes.
