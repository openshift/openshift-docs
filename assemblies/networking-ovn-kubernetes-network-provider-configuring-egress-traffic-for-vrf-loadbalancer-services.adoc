:_mod-docs-content-type: ASSEMBLY
[id="configuring-egress-traffic-loadbalancer-services"]
= Configuring an egress service
include::_attributes/common-attributes.adoc[]
:context: configuring-egress-traffic-loadbalancer-services

toc::[]

As a cluster administrator, you can configure egress traffic for pods behind a load balancer service by using an egress service.

:FeatureName: Egress service
include::snippets/technology-preview.adoc[]

You can use the `EgressService` custom resource (CR) to manage egress traffic in the following ways:

* Assign a load balancer service IP address as the source IP address for egress traffic for pods behind the load balancer service.
+
Assigning the load balancer IP address as the source IP address in this context is useful to present a single point of egress and ingress. For example, in some scenarios, an external system communicating with an application behind a load balancer service can expect the source and destination IP address for the application to be the same.
+
[NOTE]
====
When you assign the load balancer service IP address to egress traffic for pods behind the service, OVN-Kubernetes restricts the ingress and egress point to a single node. This limits the load balancing of traffic that MetalLB typically provides.
====

* Assign the egress traffic for pods behind a load balancer to a different network than the default node network.
+
This is useful to assign the egress traffic for applications behind a load balancer to a different network than the default network. Typically, the different network is implemented by using a VRF instance associated with a network interface.

// Describe the CR and provide an example.
include::modules/nw-egress-service-cr.adoc[leveloffset=+1]

// Deploying an egress service
include::modules/nw-egress-service-ovn.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../networking/metallb/metallb-configure-bgp-peers.adoc#nw-metallb-bgp-peer-vrf_configure-metallb-bgp-peers[Exposing a service through a network VRF]

* xref:../../networking/k8s_nmstate/k8s-nmstate-updating-node-network-config.adoc#virt-example-host-vrf_k8s_nmstate-updating-node-network-config[Example: Network interface with a VRF instance node network configuration policy]

* xref:../../networking/metallb/metallb-configure-return-traffic.adoc#metallb-configure-return-traffic[Managing symmetric routing with MetalLB]

* xref:../../networking/multiple_networks/about-virtual-routing-and-forwarding.adoc#cnf-about-virtual-routing-and-forwarding_about-virtual-routing-and-forwarding[About virtual routing and forwarding]
