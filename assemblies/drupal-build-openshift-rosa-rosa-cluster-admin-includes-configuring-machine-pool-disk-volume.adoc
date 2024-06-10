// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

:_mod-docs-content-type: CONCEPT
[id="configuring_machine_pool_disk_volume{context}"]
= Configuring machine pool disk volume

Machine pool disk volume size can be configured for additional flexibility. The default disk size is 300 GiB. For cluster version 4.13 or earlier, the disk size can be configured to a minimum of 128 GiB to a maximum of 1 TiB. For cluster version 4.14 and later, the disk size can be configured to a minimum of 128 GiB to a maximum of 16 TiB.

You can configure the machine pool disk size for your cluster by using {cluster-manager} or the ROSA CLI (`rosa`).

[NOTE]
====
Existing cluster and machine pool node volumes cannot be resized.
====


[IMPORTANT]
====
The default disk size is 300 GiB. For cluster version 4.13 or earlier, the disk size can be configured to a minimum of 128 GiB to a maximum of 1 TiB. For cluster version 4.14 and later, the disk size can be configured to a minimum of 128 GiB to a maximum of 16 TiB.
====