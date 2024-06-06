:_mod-docs-content-type: ASSEMBLY
[id="metallb-configure-address-pools"]
= Configuring MetalLB address pools
include::_attributes/common-attributes.adoc[]
:context: configure-metallb-address-pools

toc::[]

As a cluster administrator, you can add, modify, and delete address pools.
The MetalLB Operator uses the address pool custom resources to set the IP addresses that MetalLB can assign to services. The namespace used in the examples assume the namespace is `metallb-system`.

// Address pool custom resource
include::modules/nw-metallb-addresspool-cr.adoc[leveloffset=+1]

// Add an address pool
include::modules/nw-metallb-configure-address-pool.adoc[leveloffset=+1]

// Examples
include::modules/nw-metallb-example-addresspool.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_metallb-configure-address-pools"]
== Additional resources

* xref:../../networking/metallb/about-advertising-ipaddresspool.adoc#nw-metallb-configure-with-L2-advertisement-label_about-advertising-ip-address-pool[Configuring MetalLB with an L2 advertisement and label].

[id="next-steps_{context}"]
== Next steps

* For BGP mode, see xref:../../networking/metallb/metallb-configure-bgp-peers.adoc#metallb-configure-bgp-peers[Configuring MetalLB BGP peers].

* xref:../../networking/metallb/metallb-configure-services.adoc#metallb-configure-services[Configuring services to use MetalLB].
