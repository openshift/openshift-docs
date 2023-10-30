:_mod-docs-content-type: ASSEMBLY
[id="backup-etcd"]
= Backing up etcd
include::_attributes/common-attributes.adoc[]
:context: backup-etcd

toc::[]

etcd is the key-value store for {product-title}, which persists the state of all resource objects.

Back up your cluster's etcd data regularly and store in a secure location ideally outside the {product-title} environment. Do not take an etcd backup before the first certificate rotation completes, which occurs 24 hours after installation, otherwise the backup will contain expired certificates. It is also recommended to take etcd backups during non-peak usage hours because the etcd snapshot has a high I/O cost.

Be sure to take an etcd backup after you upgrade your cluster. This is important because when you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an {product-title} 4.y.z cluster must use an etcd backup that was taken from 4.y.z.

[IMPORTANT]
====
Back up your cluster's etcd data by performing a single invocation of the backup script on a control plane host. Do not take a backup for each control plane host.
====

After you have an etcd backup, you can xref:../../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.adoc#dr-restoring-cluster-state[restore to a previous cluster state].

// Backing up etcd data
include::modules/backup-etcd.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_backup-etcd"]
== Additional resources
* xref:../../hosted_control_planes/hcp-backup-restore-dr.adoc#hcp-backup-restore[Backing up and restoring etcd on a hosted cluster]

// Creating automated etcd backups
include::modules/etcd-creating-automated-backups.adoc[leveloffset=+1]
