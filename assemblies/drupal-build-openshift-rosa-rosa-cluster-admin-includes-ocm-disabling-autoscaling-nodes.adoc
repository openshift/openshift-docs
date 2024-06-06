// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-nodes-about-autoscaling-nodes.adoc
// * nodes/nodes-about-autoscaling-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-nodes-about-autoscaling-nodes.adoc

:_mod-docs-content-type: PROCEDURE
[id="ocm-disabling-autoscaling_{context}"]
= Disabling autoscaling nodes in an existing cluster using {cluster-manager-first}

Disable autoscaling for worker nodes in the machine pool definition from {cluster-manager} console.

.Procedure

. From {cluster-manager-url}, navigate to the *Clusters* page and select the cluster with autoscaling that must be disabled.

. On the selected cluster, select the *Machine pools* tab.

. Click the Options menu {kebab} at the end of the machine pool with autoscaling and select *Scale*.

. On the "Edit node count" dialog, deselect the *Enable autoscaling* checkbox.

. Select *Apply* to save these changes and disable autoscaling from the cluster.
