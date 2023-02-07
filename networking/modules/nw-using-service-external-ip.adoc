// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-service-external-ip.adoc

[id="nw-service-external-ip_{context}"]
= Using a service external IP to get traffic into the cluster

One method to expose a service is to assign an external IP address directly to
the service you want to make accessible from outside the cluster.

The external IP address that you use must be provisioned on your infrastructure
platform and attached to a cluster node.

With an external IP on the service, {product-title} sets up NAT rules to
allow traffic arriving at any cluster node attached to that IP address to be
sent to one of the internal pods. This is similar to the internal
service IP addresses, but the external IP tells {product-title} that this
service should also be exposed externally at the given IP. The administrator
must assign the IP address to a host (node) interface on one of the nodes in the
cluster. Alternatively, the address can be used as a virtual IP (VIP).

These IP addresses are not managed by {product-title}. The cluster administrator is responsible for ensuring that traffic arrives at a node with this IP address.
