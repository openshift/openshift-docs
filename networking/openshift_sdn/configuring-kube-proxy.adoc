:_mod-docs-content-type: ASSEMBLY
[id="configuring-kube-proxy"]
= Configuring kube-proxy
include::_attributes/common-attributes.adoc[]
:context: configuring-kube-proxy

toc::[]

The Kubernetes network proxy (kube-proxy) runs on each node and is managed by
the Cluster Network Operator (CNO). kube-proxy maintains network rules for
forwarding connections for endpoints associated with services.

include::modules/nw-kube-proxy-sync.adoc[leveloffset=+1]
include::modules/nw-kube-proxy-config.adoc[leveloffset=+1]
include::modules/nw-kube-proxy-configuring.adoc[leveloffset=+1]
