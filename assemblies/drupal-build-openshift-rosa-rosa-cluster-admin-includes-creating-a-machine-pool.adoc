// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

:_mod-docs-content-type: CONCEPT
[id="creating_a_machine_pool_{context}"]
= Creating a machine pool

A machine pool is created when you install a {product-title} (ROSA) cluster. After installation, you can create additional machine pools for your cluster by using {cluster-manager} or the ROSA CLI (`rosa`).
[NOTE]
====
For users of ROSA CLI `rosa` version 1.2.25 and earlier versions, the machine pool created along with the cluster is identified as `Default`. For users of ROSA CLI  `rosa` version 1.2.26 and later, the machine pool created along with the cluster is identified as `worker`.
====