:_mod-docs-content-type: ASSEMBLY
[id="metallb-configure-return-traffic"]
= Managing symmetric routing with MetalLB
include::_attributes/common-attributes.adoc[]
:context: metallb-configure-return-traffic

toc::[]

As a cluster administrator, you can effectively manage traffic for pods behind a MetalLB load-balancer service with multiple host interfaces by implementing features from MetalLB, NMState, and OVN-Kubernetes. By combining these features in this context, you can provide symmetric routing, traffic segregation, and support clients on different networks with overlapping CIDR addresses.

To achieve this functionality, learn how to implement virtual routing and forwarding (VRF) instances with MetalLB, and configure egress services.

:FeatureName: Configuring symmetric traffic by using a VRF instance with MetalLB and an egress service
include::snippets/technology-preview.adoc[]

[id="challenges-of-managing-symmetric-routing-with-metallb"]
== Challenges of managing symmetric routing with MetalLB

When you use MetalLB with multiple host interfaces, MetalLB exposes and announces a service through all available interfaces on the host. This can present challenges relating to network isolation, asymmetric return traffic and overlapping CIDR addresses.

One option to ensure that return traffic reaches the correct client is to use static routes. However, with this solution, MetalLB cannot isolate the services and then announce each service through a different interface. Additionally, static routing requires manual configuration and requires maintenance if remote sites are added.

A further challenge of symmetric routing when implementing a MetalLB service is scenarios where external systems expect the source and destination IP address for an application to be the same. The default behavior for {product-title} is to assign the IP address of the host network interface as the source IP address for traffic originating from pods. This is problematic with multiple host interfaces.

You can overcome these challenges by implementing a configuration that combines features from MetalLB, NMState, and OVN-Kubernetes.

[id="overview-of-managing-symmetric-routing-using-vrf-based-networks-with-metallb"]
== Overview of managing symmetric routing by using VRFs with MetalLB

You can overcome the challenges of implementing symmetric routing by using NMState to configure a VRF instance on a host, associating the VRF instance with a MetalLB `BGPPeer` resource, and configuring an egress service for egress traffic with OVN-Kubernetes.

.Network overview of managing symmetric routing by using VRFs with MetalLB
image::357_OpenShift_MetalLB_VRF_0823.png[Network overview of managing symmetric routing by using VRFs with MetalLB]

The configuration process involves three stages:

.1. Define a VRF and routing rules

* Configure a `NodeNetworkConfigurationPolicy` custom resource (CR) to associate a VRF instance with a network interface.
* Use the VRF routing table to direct ingress and egress traffic.

.2. Link the VRF to a MetalLB `BGPPeer`

* Configure a MetalLB `BGPPeer` resource to use the VRF instance on a network interface.
* By associating the `BGPPeer` resource with the VRF instance, the designated network interface becomes the primary interface for the BGP session, and MetalLB advertises the services through this interface.

.3. Configure an egress service

* Configure an egress service to choose the network associated with the VRF instance for egress traffic.
* Optional: Configure an egress service to use the IP address of the MetalLB load-balancer service as the source IP for egress traffic.

// Deploying an egress service for VRF
include::modules/nw-metallb-configure-return-traffic-proc.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../networking/multiple_networks/about-virtual-routing-and-forwarding.adoc#cnf-about-virtual-routing-and-forwarding_about-virtual-routing-and-forwarding[About virtual routing and forwarding]

* xref:../../networking/metallb/metallb-configure-bgp-peers.adoc#nw-metallb-bgp-peer-vrf_configure-metallb-bgp-peers[Exposing a service through a network VRF]

* xref:../../networking/k8s_nmstate/k8s-nmstate-updating-node-network-config.adoc#virt-example-host-vrf_k8s_nmstate-updating-node-network-config[Example: Network interface with a VRF instance node network configuration policy]

* xref:../../networking/ovn_kubernetes_network_provider/configuring-egress-traffic-for-vrf-loadbalancer-services.adoc#configuring-egress-traffic-loadbalancer-services[Configuring an egress service]
