:_mod-docs-content-type: ASSEMBLY
[id="configuring-ingress-cluster-traffic-service-external-ip"]
= Configuring ingress cluster traffic for a service external IP
include::_attributes/common-attributes.adoc[]
:context: configuring-ingress-cluster-traffic-service-external-ip

toc::[]

You can attach an external IP address to a service so that it is available to traffic outside the cluster.
This is generally useful only for a cluster installed on bare metal hardware.
The external network infrastructure must be configured correctly to route traffic to the service.

[id="configuring-ingress-cluster-traffic-service-external-ip-prerequisites"]
== Prerequisites

* Your cluster is configured with ExternalIPs enabled. For more information, read xref:../../networking/configuring_ingress_cluster_traffic/configuring-externalip.adoc#configuring-externalip[Configuring ExternalIPs for services].
+
[NOTE]
====
Do not use the same ExternalIP for the egress IP.
====

include::modules/nw-service-externalip-create.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="configuring-ingress-cluster-traffic-service-external-ip-additional-resources"]
== Additional resources

* xref:../../networking/configuring_ingress_cluster_traffic/configuring-externalip.adoc#configuring-externalip[Configuring ExternalIPs for services]
