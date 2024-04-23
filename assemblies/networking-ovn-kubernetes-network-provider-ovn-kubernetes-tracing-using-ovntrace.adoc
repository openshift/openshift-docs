:_mod-docs-content-type: ASSEMBLY
[id="ovn-kubernetes-tracing-using-ovntrace"]
= Tracing Openflow with ovnkube-trace
include::_attributes/common-attributes.adoc[]
:context: ovn-kubernetes-tracing-with-ovnkube

toc::[]

OVN and OVS traffic flows can be simulated in a single utility called `ovnkube-trace`. The `ovnkube-trace` utility runs `ovn-trace`, `ovs-appctl ofproto/trace` and `ovn-detrace` and correlates that information in a single output.

You can execute the `ovnkube-trace` binary from a dedicated container. For releases after {product-title} 4.7, you can also copy the binary to a local host and execute it from that host.

include::modules/nw-ovn-kubernetes-install-ovnkube-trace-local.adoc[leveloffset=+1]

include::modules/nw-ovn-kubernetes-running-ovnkube-trace.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_ovn-kubernetes-tracing-with-ovnkube"]
== Additional resources

* link:https://access.redhat.com/solutions/5887511[Tracing Openflow with ovnkube-trace utility]
* link:https://github.com/ovn-org/ovn-kubernetes/blob/master/docs/ovnkube-trace.md[ovnkube-trace]