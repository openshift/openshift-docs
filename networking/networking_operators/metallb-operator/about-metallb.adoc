:_mod-docs-content-type: ASSEMBLY
[id="about-metallb"]
= About MetalLB and the MetalLB Operator
include::_attributes/common-attributes.adoc[]
:context: about-metallb-and-metallb-operator

toc::[]

As a cluster administrator, you can add the MetalLB Operator to your cluster so that when a service of type `LoadBalancer` is added to the cluster, MetalLB can add an external IP address for the service.
The external IP address is added to the host network for your cluster.

// When to deploy MetalLB
include::modules/nw-metallb-when-metallb.adoc[leveloffset=+1]

// MetalLB Operator custom resources
include::modules/nw-metallb-operator-custom-resources.adoc[leveloffset=+1]

// MetalLB software components
include::modules/nw-metallb-software-components.adoc[leveloffset=+1]

// External traffic policy, common to layer 2 and BGP
include::modules/nw-metallb-extern-traffic-pol.adoc[leveloffset=+1]

// Layer 2
include::modules/nw-metallb-layer2.adoc[leveloffset=+1]

// BGP
include::modules/nw-metallb-bgp.adoc[leveloffset=+1]

[id="limitations-and-restrictions_{context}"]
== Limitations and restrictions

// Infra considerations
include::modules/nw-metallb-infra-considerations.adoc[leveloffset=+2]

// Layer 2 limitations
include::modules/nw-metallb-layer2-limitations.adoc[leveloffset=+2]

// BGP limitations
include::modules/nw-metallb-bgp-limitations.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_about-metallb-and-metallb-operator"]
== Additional resources

* xref:../../networking/configuring_ingress_cluster_traffic/overview-traffic.adoc#overview-traffic-comparision_overview-traffic[Comparison: Fault tolerant access to external IP addresses]

* xref:../../networking/configuring-ipfailover.adoc#nw-ipfailover-remove_configuring-ipfailover[Removing IP failover]

* xref:../../networking/metallb/metallb-operator-install.adoc#nw-metallb-operator-deployment-specifications-for-metallb_metallb-operator-install[Deployment specifications for MetalLB]