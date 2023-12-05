:_mod-docs-content-type: ASSEMBLY
[id="routing-optimization"]
= Optimizing routing
include::_attributes/common-attributes.adoc[]
:context: routing-optimization

toc::[]

The {product-title} HAProxy router can be scaled or configured to optimize performance.

include::modules/baseline-router-performance.adoc[leveloffset=+1]

For more information on Ingress sharding, see xref:../../networking/ingress-operator.adoc#nw-ingress-sharding-route-labels_configuring-ingress[Configuring Ingress Controller sharding by using route labels] and xref:../../networking/ingress-operator.adoc#nw-ingress-sharding-namespace-labels_configuring-ingress[Configuring Ingress Controller sharding by using namespace labels].

You can modify the Ingress Controller deployment using the information provided in xref:../../networking/ingress-operator.adoc#nw-ingress-setting-thread-count[Setting Ingress Controller thread count] for threads and xref:../../networking/ingress-operator.adoc#nw-ingress-controller-configuration-parameters_configuring-ingress[Ingress Controller configuration parameters] for timeouts, and other tuning configurations in the Ingress Controller specification.

include::modules/ingress-liveness-readiness-startup-probes.adoc[leveloffset=+1]
include::modules/configuring-haproxy-interval.adoc[leveloffset=+1]
