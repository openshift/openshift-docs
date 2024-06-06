:_mod-docs-content-type: ASSEMBLY
[id="virt-configuring-live-migration"]
= Configuring live migration
include::_attributes/common-attributes.adoc[]
:context: virt-configuring-live-migration

toc::[]

You can configure live migration settings to ensure that the migration processes do not overwhelm the cluster.

You can configure live migration policies to apply different migration configurations to groups of virtual machines (VMs).

[id="live-migration-settings"]
== Live migration settings

You can configure the following live migration settings:

* xref:../../virt/live_migration/virt-configuring-live-migration.adoc#virt-configuring-live-migration-limits_virt-configuring-live-migration[Limits and timeouts]
* xref:../../virt/getting_started/virt-web-console-overview.adoc#overview-settings-cluster_virt-web-console-overview[Maximum number of migrations per node or cluster]

include::modules/virt-configuring-live-migration-limits.adoc[leveloffset=+2]

[id="live-migration-policies"]
== Live migration policies

You can create live migration policies to apply different migration configurations to groups of VMs that are defined by VM or project labels.

[TIP]
====
You can create live migration policies by using the xref:../../virt/getting_started/virt-web-console-overview.adoc#migrationpolicies-page_virt-web-console-overview[web console].
====

include::modules/virt-configuring-a-live-migration-policy.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_virt-configuring-live-migration"]
== Additional resources
* xref:../../virt/vm_networking/virt-dedicated-network-live-migration.adoc#virt-dedicated-network-live-migration[Configuring a dedicated Multus network for live migration]
