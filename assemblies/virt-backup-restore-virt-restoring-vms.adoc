:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="virt-restoring-vms"]
= Restoring virtual machines
:context: virt-restoring-vms

toc::[]

You restore an OpenShift API for Data Protection (OADP) `Backup` custom resource (CR) by creating a xref:../../virt/backup_restore/virt-restoring-vms.adoc#oadp-creating-restore-cr_virt-restoring-vms[`Restore` CR].

You can add xref:../../virt/backup_restore/virt-restoring-vms.adoc#oadp-creating-restore-hooks_virt-restoring-vms[hooks] to the `Restore` CR to run commands in init containers, before the application container starts, or in the application container itself.

include::modules/oadp-creating-restore-cr.adoc[leveloffset=+1]
include::modules/oadp-creating-restore-hooks.adoc[leveloffset=+2]
