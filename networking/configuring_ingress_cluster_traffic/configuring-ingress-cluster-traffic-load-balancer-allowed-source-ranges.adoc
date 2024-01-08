:_mod-docs-content-type: ASSEMBLY
[id="configuring-ingress-cluster-traffic-lb-allowed-source-ranges"]
= Configuring ingress cluster traffic using load balancer allowed source ranges
include::_attributes/common-attributes.adoc[]
:context: configuring-ingress-cluster-traffic-lb-allowed-source-ranges

toc::[]

You can specify a list of IP address ranges for the `IngressController`. This restricts access to the load balancer service when the `endpointPublishingStrategy` is `LoadBalancerService`.

include::modules/nw-configuring-lb-allowed-source-ranges.adoc[leveloffset=+1]
include::modules/nw-configuring-lb-allowed-source-ranges-migration.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources
* xref:../../updating/understanding_updates/intro-to-updates.adoc#understanding-openshift-updates[Introduction to OpenShift updates]
