:_mod-docs-content-type: ASSEMBLY
include::_attributes/attributes-openshift-dedicated.adoc[]
[id="osd-nodes-about-autoscaling-nodes"]
= About autoscaling nodes on a cluster
:context: osd-nodes-about-autoscaling-nodes
toc::[]

[IMPORTANT]
====
Autoscaling is available only on clusters that were purchased through Google Cloud Marketplace and Red Hat Marketplace.
====

The autoscaler option can be configured to automatically scale the number of machines in a cluster.

The cluster autoscaler increases the size of the cluster when there are pods that failed to schedule on any of the current nodes due to insufficient resources or when another node is necessary to meet deployment needs. The cluster autoscaler does not increase the cluster resources beyond the limits that you specify.

Additionally, the cluster autoscaler decreases the size of the cluster when some nodes are consistently not needed for a significant period, such as when it has low resource use and all of its important pods can fit on other nodes.

When you enable autoscaling, you must also set a minimum and maximum number of worker nodes.

[NOTE]
====
Only cluster owners and organization admins can scale or delete a cluster.
====

[id="osd-nodes-enabling-autoscaling-nodes"]
== Enabling autoscaling nodes on a cluster

You can enable autoscaling on worker nodes to increase or decrease the number of nodes available by editing the machine pool definition for an existing cluster.

[discrete]
include::modules/ocm-enabling-autoscaling-nodes.adoc[leveloffset=+2]

[id="osd-nodes-disabling-autoscaling-nodes"]
== Disabling autoscaling nodes on a cluster

You can disable autoscaling on worker nodes to increase or decrease the number of nodes available by editing the machine pool definition for an existing cluster.

You can disable autoscaling on a cluster using {cluster-manager} console.

[discrete]
include::modules/ocm-disabling-autoscaling-nodes.adoc[leveloffset=+2]

Applying autoscaling to an {product-title} cluster involves deploying a cluster autoscaler and then deploying machine autoscalers for each machine type in your cluster.

[IMPORTANT]
====
You can configure the cluster autoscaler only in clusters where the Machine API is operational.
====

include::modules/cluster-autoscaler-about.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="nodes-about-autoscaling-nodes-additional-resources"]
== Additional resources
* xref:../../osd_cluster_admin/osd_nodes/osd-nodes-machinepools-about.adoc#osd-machinepools-about[About machinepools]
