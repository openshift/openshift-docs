:_mod-docs-content-type: ASSEMBLY
[id="dr-restoring-cluster-state"]
= Restoring to a previous cluster state
include::_attributes/common-attributes.adoc[]
:context: dr-restoring-cluster-state

toc::[]

To restore the cluster to a previous state, you must have previously xref:../../../backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.adoc#backing-up-etcd-data_backup-etcd[backed up etcd data] by creating a snapshot. You will use this snapshot to restore the cluster state.

// About restoring to a previous cluster state
include::modules/dr-restoring-cluster-state-about.adoc[leveloffset=+1]

// Restoring to a previous cluster state
include::modules/dr-restoring-cluster-state.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_dr-restoring-cluster-state"]
== Additional resources

* xref:../../../installing/installing_bare_metal/installing-bare-metal.adoc#installing-bare-metal[Installing a user-provisioned cluster on bare metal]
* xref:../../../networking/accessing-hosts.adoc#accessing-hosts[Creating a bastion host to access {product-title} instances and the control plane nodes with SSH]
* xref:../../../installing/installing_bare_metal_ipi/ipi-install-expanding-the-cluster.adoc#replacing-a-bare-metal-control-plane-node_ipi-install-expanding[Replacing a bare-metal control plane node]

include::modules/dr-scenario-cluster-state-issues.adoc[leveloffset=+1]


