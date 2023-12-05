:_mod-docs-content-type: ASSEMBLY
[id="configuring-node-port-service-range"]
= Configuring the node port service range
include::_attributes/common-attributes.adoc[]
:context: configuring-node-port-service-range

toc::[]

As a cluster administrator, you can expand the available node port range. If your cluster uses of a large number of node ports, you might need to increase the number of available ports.

The default port range is `30000-32767`. You can never reduce the port range, even if you first expand it beyond the default range.

[id="configuring-node-port-service-range-prerequisites"]
== Prerequisites

- Your cluster infrastructure must allow access to the ports that you specify within the expanded range. For example, if you expand the node port range to `30000-32900`, the inclusive port range of `32768-32900` must be allowed by your firewall or packet filtering configuration.

include::modules/nw-nodeport-service-range-edit.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="configuring-node-port-service-range-additional-resources"]
== Additional resources

* xref:../networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.adoc#configuring-ingress-cluster-traffic-nodeport[Configuring ingress cluster traffic using a NodePort]
* xref:../rest_api/config_apis/network-config-openshift-io-v1.adoc#network-config-openshift-io-v1[Network [config.openshift.io/v1]]
* xref:../rest_api/network_apis/service-v1.adoc#service-v1[Service [core/v1]]
