:_mod-docs-content-type: ASSEMBLY
[id="troubleshooting-local-persistent-storage"]
= Troubleshooting local persistent storage using LVMS
include::_attributes/common-attributes.adoc[]
:context: troubleshooting-local-persistent-storage-using-lvms

toc::[]

Because {product-title} does not scope a persistent volume (PV) to a single project, it can be shared across the cluster and claimed by any project using a persistent volume claim (PVC). This can lead to a number of issues that require troubleshooting.

include::modules/lvms-troubleshooting-investigating-a-pvc-stuck-in-the-pending-state.adoc[leveloffset=+1]

include::modules/lvms-troubleshooting-recovering-from-missing-lvms-or-operator-components.adoc[leveloffset=+1]

include::modules/lvms-troubleshooting-recovering-from-node-failure.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources-forced-cleanup-1"]
.Additional resources

* xref:../../../troubleshooting-local-persistent-storage-using-lvms.adoc#performing-a-forced-cleanup_troubleshooting-local-persistent-storage-using-lvms[Performing a forced cleanup]

include::modules/lvms-troubleshooting-recovering-from-disk-failure.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources-forced-cleanup-2"]
.Additional resources

* xref:../../../troubleshooting-local-persistent-storage-using-lvms.adoc#performing-a-forced-cleanup_troubleshooting-local-persistent-storage-using-lvms[Performing a forced cleanup]

include::modules/lvms-troubleshooting-performing-a-forced-cleanup.adoc[leveloffset=+1]
