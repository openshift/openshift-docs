:_mod-docs-content-type: ASSEMBLY
[id="nodes-nodes-graceful-shutdown"]
= Managing graceful node shutdown
include::_attributes/common-attributes.adoc[]
:context: nodes-nodes-graceful-shutdown

toc::[]

Graceful node shutdown enables the kubelet to delay forcible eviction of pods during a node shutdown. When you configure a graceful node shutdown, you can define a time period for pods to complete running workloads before shutting down. This grace period minimizes interruption to critical workloads during unexpected node shutdown events. Using priority classes, you can also specify the order of pod shutdown.

// concept topic: how it works
include::modules/nodes-nodes-cluster-timeout-graceful-shutdown.adoc[leveloffset=+1]

// procedure topic: configuring Graceful node shutdown
include::modules/nodes-nodes-configuring-graceful-shutdown.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../nodes/pods/nodes-pods-priority.adoc#nodes-pods-priority[Understanding pod priority]
