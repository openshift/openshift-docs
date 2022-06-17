// Module included in the following assemblies:
//
// * ingress/getting-traffic-cluster.adoc

[id="nw-using-load-balancer-getting-traffic_{context}"]
= Using a load balancer to get traffic into the cluster

If you do not need a specific external IP address, you can configure a load
balancer service to allow external access to an {product-title} cluster.

A load balancer service allocates a unique IP. The load balancer has a single
edge router IP, which can be a virtual IP (VIP), but is still a single machine
for initial load balancing.

[NOTE]
====
If a pool is configured, it is done at the infrastructure level, not by a cluster
administrator.
====
