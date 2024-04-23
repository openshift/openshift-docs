:_mod-docs-content-type: ASSEMBLY
[id="graceful-shutdown-cluster"]
= Shutting down the cluster gracefully
include::_attributes/common-attributes.adoc[]
:context: graceful-shutdown-cluster

toc::[]

This document describes the process to gracefully shut down your cluster. You might need to temporarily shut down your cluster for maintenance reasons, or to save on resource costs.

== Prerequisites

* Take an xref:../backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.adoc#backing-up-etcd-data_backup-etcd[etcd backup] prior to shutting down the cluster.
+
[IMPORTANT]
====
It is important to take an etcd backup before performing this procedure so that your cluster can be restored if you encounter any issues when restarting the cluster.

For example, the following conditions can cause the restarted cluster to malfunction:

* etcd data corruption during shutdown
* Node failure due to hardware
* Network connectivity issues

If your cluster fails to recover, follow the steps to xref:../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.adoc#dr-restoring-cluster-state[restore to a previous cluster state].
====

// Shutting down the cluster
include::modules/graceful-shutdown.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_restarting-restoring-cluster"]
== Additional resources

* xref:../backup_and_restore/graceful-cluster-restart.adoc#graceful-restart-cluster[Restarting the cluster gracefully]
