:_mod-docs-content-type: ASSEMBLY
[id="tracking-network-flows"]
= Tracking network flows
include::_attributes/common-attributes.adoc[]
:context: tracking-network-flows

toc::[]

As a cluster administrator, you can collect information about pod network flows from your cluster to assist with the following areas:

* Monitor ingress and egress traffic on the pod network.

* Troubleshoot performance issues.

* Gather data for capacity planning and security audits.

When you enable the collection of the network flows, only the metadata about the traffic is collected.
For example, packet data is not collected, but the protocol, source address, destination address, port numbers, number of bytes, and other packet-level information is collected.

The data is collected in one or more of the following record formats:

* NetFlow

* sFlow

* IPFIX

When you configure the Cluster Network Operator (CNO) with one or more collector IP addresses and port numbers, the Operator configures Open vSwitch (OVS) on each node to send the network flows records to each collector.

You can configure the Operator to send records to more than one type of network flow collector. For example, you can send records to NetFlow collectors and also send records to sFlow collectors.

When OVS sends data to the collectors, each type of collector receives identical records. For example, if you configure two NetFlow collectors, OVS on a node sends identical records to the two collectors. If you also configure two sFlow collectors, the two sFlow collectors receive identical records. However, each collector type has a unique record format.

Collecting the network flows data and sending the records to collectors affects performance. Nodes process packets at a slower rate. If the performance impact is too great, you can delete the destinations for collectors to disable collecting network flows data and restore performance.

[NOTE]
====
Enabling network flow collectors might have an impact on the overall performance of the cluster network.
====

include::modules/nw-network-flows-object.adoc[leveloffset=+1]

include::modules/nw-network-flows-create.adoc[leveloffset=+1]

include::modules/nw-network-flows-delete.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_tracking-network-flows"]
== Additional resources

* xref:../../rest_api/operator_apis/network-operator-openshift-io-v1.adoc#network-operator-openshift-io-v1[Network [operator.openshift.io/v1]]
