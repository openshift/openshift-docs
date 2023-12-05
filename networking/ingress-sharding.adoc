:_mod-docs-content-type: ASSEMBLY
[id="ingress-sharding"]
= Ingress sharding in {product-title}
include::_attributes/common-attributes.adoc[]
:context: ingress-sharding

toc::[]

In {product-title}, an Ingress Controller can serve all routes, or it can serve a subset of routes. By default, the Ingress Controller serves any route created in any namespace in the cluster. You can add additional Ingress Controllers to your cluster to optimize routing by creating _shards_, which are subsets of routes based on selected characteristics. To mark a route as a member of a shard, use labels in the route or namespace `metadata` field. The Ingress Controller uses _selectors_, also known as a _selection expression_, to select a subset of routes from the entire pool of routes to serve.

Ingress sharding is useful in cases where you want to load balance incoming traffic across multiple Ingress Controllers, when you want to isolate traffic to be routed to a specific Ingress Controller, or for a variety of other reasons described in the next section.

By default, each route uses the default domain of the cluster. However, routes can be configured to use the domain of the router instead. For more information, see xref:../networking/ingress-sharding.adoc#nw-ingress-sharding-route-configuration_ingress-sharding[Creating a route for Ingress Controller Sharding].

include::modules/nw-ingress-sharding.adoc[leveloffset=+1]

include::modules/nw-ingress-sharding-default.adoc[leveloffset=+2]

include::modules/nw-ingress-sharding-dns.adoc[leveloffset=+2]

include::modules/nw-ingress-sharding-route-labels.adoc[leveloffset=+2]

include::modules/nw-ingress-sharding-namespace-labels.adoc[leveloffset=+2]

include::modules/nw-ingress-sharding-route-configuration.adoc[leveloffset=+1]

[discrete]
[role="_additional-resources"]
[id="additional-resources_ingress-sharding"]
== Additional Resources

* xref:../scalability_and_performance/optimization/routing-optimization.adoc#baseline-router-performance_routing-optimization[Baseline Ingress Controller (router) performance]
