:_mod-docs-content-type: ASSEMBLY
[id="osd-cluster-autoscaling"]
= Cluster autoscaling
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: osd-cluster-autoscaling

toc::[]

Applying autoscaling to {product-title} clusters involves configuring a cluster autoscaler and then configuring a machine autoscaler for at least one machine pool in your cluster.

[IMPORTANT]
====
You can configure the cluster autoscaler only in clusters where the machine API is operational.

Only one cluster autoscaler can be created per cluster.
====

include::modules/cluster-autoscaler-about.adoc[leveloffset=+1]

include::modules/rosa-cluster-autoscaler-ui-during.adoc[leveloffset=+1]

include::modules/rosa-cluster-autoscaler-ui-after.adoc[leveloffset=+1]

include::modules/rosa-cluster-autoscaler-ui-settings.adoc[leveloffset=+1]
