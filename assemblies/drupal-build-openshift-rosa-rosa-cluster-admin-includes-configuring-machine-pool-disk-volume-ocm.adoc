// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

:_mod-docs-content-type: PROCEDURE
ifdef::openshift-rosa[]
[id="configuring_machine_pool_disk_volume_ocm{context}"]
= Configuring machine pool disk volume using OpenShift Cluster Manager
endif::openshift-rosa[]
.Prerequisite for cluster creation
* You have the option to select the node disk sizing for the default machine pool during cluster installation.

.Procedure for cluster creation

. From ROSA cluster wizard, navigate to Cluster settings.

. Navigate to *Machine pool* step.

. Select the desired *Root disk size*.

. Select *Next* to continue creating your cluster.

.Prerequisite for machine pool creation
* You have the option to select the node disk sizing for the new machine pool after the cluster has been installed.

.Procedure for machine pool creation

. Navigate to {cluster-manager-url} and select your cluster.

. Navigate to *Machine pool tab*.

. Click *Add machine pool*.

. Select the desired *Root disk size*.

. Select *Add machine pool* to create the machine pool.
