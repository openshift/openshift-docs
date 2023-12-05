:_mod-docs-content-type: ASSEMBLY
[id="configuring-externalip"]
= Configuring ExternalIPs for services
include::_attributes/common-attributes.adoc[]
:context: configuring-externalip

toc::[]

As a cluster administrator, you can designate an IP address block that is external to the cluster that can send traffic to services in the cluster.

This functionality is generally most useful for clusters installed on bare-metal hardware.

== Prerequisites

* Your network infrastructure must route traffic for the external IP addresses to your cluster.

include::modules/nw-externalip-about.adoc[leveloffset=+1]

include::modules/nw-externalip-object.adoc[leveloffset=+1]

include::modules/nw-externalip-configuring.adoc[leveloffset=+1]

[id="configuring-externalip-next-steps"]
== Next steps

* xref:../../networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-service-external-ip.adoc#configuring-ingress-cluster-traffic-service-external-ip[Configuring ingress cluster traffic for a service external IP]
