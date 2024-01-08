:_mod-docs-content-type: ASSEMBLY
[id="virt-initiating-live-migration"]
= Initiating and canceling live migration
include::_attributes/common-attributes.adoc[]
:context: virt-initiating-live-migration

toc::[]

You can initiate the live migration of a virtual machine (VM) to another node by using the xref:../../virt/live_migration/virt-initiating-live-migration.adoc#virt-initiating-vm-migration-web_virt-initiating-live-migration[{product-title} web console] or the xref:../../virt/live_migration/virt-initiating-live-migration.adoc#virt-initiating-vm-migration-cli_virt-initiating-live-migration[command line].

You can cancel a live migration by using the xref:../../virt/live_migration/virt-initiating-live-migration.adoc#virt-canceling-vm-migration-web_virt-initiating-live-migration[web console] or the xref:../../virt/live_migration/virt-initiating-live-migration.adoc#virt-canceling-vm-migration-cli_virt-initiating-live-migration[command line]. The VM remains on its original node.

[TIP]
====
You can also initiate and cancel live migration by using the `virtctl migrate <vm_name>` and `virtctl migrate-cancel <vm_name>` commands.
====

[id="initating-live-migration_initiating-canceling"]
== Initiating live migration

include::modules/virt-initiating-vm-migration-web.adoc[leveloffset=+2]

include::modules/virt-initiating-vm-migration-cli.adoc[leveloffset=+2]

[id="canceling-live-migration_initiating-canceling"]
== Canceling live migration

include::modules/virt-canceling-vm-migration-web.adoc[leveloffset=+2]

include::modules/virt-canceling-vm-migration-cli.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_virt-initiating-live-migration"]
== Additional resources
* xref:../../virt/getting_started/virt-web-console-overview.adoc#overview-migrations_virt-web-console-overview[Monitoring the progress of all live migrations by using the web console]
* xref:../../virt/getting_started/virt-web-console-overview.adoc#virtualmachine-details-metrics_virt-web-console-overview[Viewing VM migration metrics by using the web console]