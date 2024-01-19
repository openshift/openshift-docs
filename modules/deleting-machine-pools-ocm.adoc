// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-managing-worker-nodes.adoc

:_mod-docs-content-type: PROCEDURE
[id="deleting-machine-pools-ocm{context}"]
ifndef::openshift-rosa[]
= Deleting a machine pool
endif::openshift-rosa[]
ifdef::openshift-rosa[]
= Deleting a machine pool using OpenShift Cluster Manager
endif::openshift-rosa[]

You can delete a machine pool for your Red Hat OpenShift Service on AWS (ROSA) cluster by using OpenShift Cluster Manager.

.Prerequisites

ifdef::openshift-rosa[]
* You created a ROSA cluster.
* The cluster is in the ready state.
* You have an existing machine pool without any taints and with at least two instances for a single-AZ cluster or three instances for a multi-AZ cluster.
endif::openshift-rosa[]
ifndef::openshift-rosa[]
* You have created an {product-title} cluster.
* The newly created cluster is in the ready state.
endif::openshift-rosa[]

.Procedure
. From {cluster-manager-url}, navigate to the *Clusters* page and select the cluster that contains the machine pool that you want to delete.

. On the selected cluster, select the *Machine pools* tab.

. Under the *Machine pools* tab, click the options menu {kebab} for the machine pool that you want to delete.
. Click Delete.

The selected machine pool is deleted.