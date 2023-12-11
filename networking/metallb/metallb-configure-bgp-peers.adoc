:_mod-docs-content-type: ASSEMBLY
[id="metallb-configure-bgp-peers"]
= Configuring MetalLB BGP peers
include::_attributes/common-attributes.adoc[]
:context: configure-metallb-bgp-peers

toc::[]

As a cluster administrator, you can add, modify, and delete Border Gateway Protocol (BGP) peers.
The MetalLB Operator uses the BGP peer custom resources to identify which peers that MetalLB `speaker` pods contact to start BGP sessions.
The peers receive the route advertisements for the load-balancer IP addresses that MetalLB assigns to services.

// Dear reviewers and maintainers, I capitalized Autonomous System (AS)
// to match the capitalization that is shown in the common terms section
// of the foll RFC: https://datatracker.ietf.org/doc/html/rfc4271

// BGP peer custom resource
include::modules/nw-metallb-bgppeer-cr.adoc[leveloffset=+1]

// Add a BGP peer
include::modules/nw-metallb-configure-bgppeer.adoc[leveloffset=+1]

// Add a BGP peer
include::modules/nw-metallb-configure-specificpools-to-bgppeer.adoc[leveloffset=+1]

// Add a BGP peer with VRF
include::modules/nw-metallb-configure-vrf-bgppeer.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../networking/multiple_networks/about-virtual-routing-and-forwarding.adoc#cnf-about-virtual-routing-and-forwarding_about-virtual-routing-and-forwarding[About virtual routing and forwarding]

* xref:../../networking/k8s_nmstate/k8s-nmstate-updating-node-network-config.adoc#virt-example-host-vrf_k8s_nmstate-updating-node-network-config[Example: Network interface with a VRF instance node network configuration policy]

* xref:../../networking/ovn_kubernetes_network_provider/configuring-egress-traffic-for-vrf-loadbalancer-services.adoc#configuring-egress-traffic-loadbalancer-services[Configuring an egress service]

* xref:../../networking/metallb/metallb-configure-return-traffic.adoc#metallb-configure-return-traffic[Managing symmetric routing with MetalLB]

// Examples
include::modules/nw-metallb-example-bgppeer.adoc[leveloffset=+1]

[id="next-steps_{context}"]
== Next steps

* xref:../../networking/metallb/metallb-configure-services.adoc#metallb-configure-services[Configuring services to use MetalLB]
