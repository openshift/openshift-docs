:_mod-docs-content-type: ASSEMBLY
[id="configuring-ingress-cluster-traffic-aws"]
= Configuring ingress cluster traffic on AWS
include::_attributes/common-attributes.adoc[]
:context: configuring-ingress-cluster-traffic-aws

toc::[]

{product-title} provides methods for communicating from outside the cluster with services running in the cluster. This method uses load balancers on AWS, specifically a Network Load Balancer (NLB) or a Classic Load Balancer (CLB). Both types of load balancers can forward the client's IP address to the node, but a CLB requires proxy protocol support, which {product-title} automatically enables.

There are two ways to configure an Ingress Controller to use an NLB:

. By force replacing the Ingress Controller that is currently using a CLB. This deletes the `IngressController` object and an outage will occur while the new DNS records propagate and the NLB is being provisioned.
. By editing an existing Ingress Controller that uses a CLB to use an NLB. This changes the load balancer without having to delete and recreate the `IngressController` object.

Both methods can be used to switch from an NLB to a CLB.

You can configure these load balancers on a new or existing AWS cluster.

include::modules/nw-configuring-elb-timeouts-aws-classic.adoc[leveloffset=+1]

include::modules/nw-configuring-route-timeouts.adoc[leveloffset=+2]

include::modules/nw-configuring-clb-timeouts.adoc[leveloffset=+2]

include::modules/nw-configuring-ingress-cluster-traffic-aws-networking-load-balancer.adoc[leveloffset=+1]

include::modules/nw-aws-switching-clb-with-nlb.adoc[leveloffset=+2]

include::modules/nw-aws-switching-nlb-with-clb.adoc[leveloffset=+2]

include::modules/nw-aws-replacing-clb-with-nlb.adoc[leveloffset=+2]

include::modules/nw-aws-nlb-existing-cluster.adoc[leveloffset=+2]

[IMPORTANT]
====
Before you can configure an Ingress Controller NLB on a new AWS cluster, you must complete the xref:../../installing/installing_aws/installing-aws-network-customizations.adoc#installation-initializing_installing-aws-network-customizations[Creating the installation configuration file] procedure.
====

include::modules/nw-aws-nlb-new-cluster.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_configuring-ingress-cluster-traffic-aws"]
== Additional resources

* xref:../../installing/installing_aws/installing-aws-network-customizations.adoc#installing-aws-network-customizations[Installing a cluster on AWS with network customizations].
* For more information on support for NLBs, see link:https://kubernetes.io/docs/concepts/services-networking/service/#aws-nlb-support[Network Load Balancer support on AWS].
* For more information on proxy protocol support for CLBs, see link:https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-proxy-protocol.html[Configure proxy protocol support for your Classic Load Balancer]
