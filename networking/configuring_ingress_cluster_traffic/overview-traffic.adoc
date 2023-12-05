:_mod-docs-content-type: ASSEMBLY
[id="overview-traffic"]
= Configuring ingress cluster traffic overview
include::_attributes/common-attributes.adoc[]
:context: overview-traffic

toc::[]

{product-title} provides the following methods for communicating from
outside the cluster with services running in the cluster.

The methods are recommended, in order or preference:

* If you have HTTP/HTTPS, use an Ingress Controller.
* If you have a TLS-encrypted protocol other than HTTPS. For example, for TLS
with the SNI header, use an Ingress Controller.
* Otherwise, use a Load Balancer, an External IP, or a `NodePort`.

[[external-access-options-table]]
[options="header"]
|===

|Method |Purpose

|xref:../../networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-ingress-controller.adoc#configuring-ingress-cluster-traffic-ingress-controller[Use an Ingress Controller]
|Allows access to HTTP/HTTPS traffic and TLS-encrypted protocols other than HTTPS (for example, TLS with the SNI header).

|xref:../../networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-load-balancer.adoc#configuring-ingress-cluster-traffic-load-balancer[Automatically assign an external IP using a load balancer service]
|Allows traffic to non-standard ports through an IP address assigned from a pool.
Most cloud platforms offer a method to start a service with a load-balancer IP address.

|xref:../../networking/metallb/about-metallb.adoc#about-metallb[About MetalLB and the MetalLB Operator]
|Allows traffic to a specific IP address or address from a pool on the machine network.
For bare-metal installations or platforms that are like bare metal, MetalLB provides a way to start a service with a load-balancer IP address.

|xref:../../networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-service-external-ip.adoc#configuring-ingress-cluster-traffic-service-external-ip[Manually assign an external IP to a service]
|Allows traffic to non-standard ports through a specific IP address.

|xref:../../networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.adoc#configuring-ingress-cluster-traffic-nodeport[Configure a `NodePort`]
|Expose a service on all nodes in the cluster.
|===

[id="overview-traffic-comparision_{context}"]
== Comparision: Fault tolerant access to external IP addresses

For the communication methods that provide access to an external IP address, fault tolerant access to the IP address is another consideration.
The following features provide fault tolerant access to an external IP address.

IP failover::
IP failover manages a pool of virtual IP address for a set of nodes.
It is implemented with Keepalived and Virtual Router Redundancy Protocol (VRRP).
IP failover is a layer 2 mechanism only and relies on multicast.
Multicast can have disadvantages for some networks.

MetalLB::
MetalLB has a layer 2 mode, but it does not use multicast.
Layer 2 mode has a disadvantage that it transfers all traffic for an external IP address through one node.

Manually assigning external IP addresses::
You can configure your cluster with an IP address block that is used to assign external IP addresses to services.
By default, this feature is disabled.
This feature is flexible, but places the largest burden on the cluster or network administrator.
The cluster is prepared to receive traffic that is destined for the external IP, but each customer has to decide how they want to route traffic to nodes.
