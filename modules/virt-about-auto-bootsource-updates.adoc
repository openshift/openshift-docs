// Module included in the following assembly:
//
// * virt/virtual_machines/virt-creating-and-using-boot-sources.adoc
//

:_mod-docs-content-type: CONCEPT
[id="virt-about-auto-bootsource-updates_{context}"]
= About automatic boot source updates

Boot sources can make virtual machine (VM) creation more accessible and efficient for users. If automatic boot source updates are enabled, the Containerized Data Importer (CDI) imports, polls, and updates the images so that they are ready to be cloned for new VMs. By default, CDI automatically updates the _system-defined_ boot sources that {VirtProductName} provides.

You can opt out of automatic updates for all system-defined boot sources by disabling the `enableCommonBootImageImport` feature gate. If you disable this feature gate, all `DataImportCron` objects are deleted. This does not remove previously imported boot source objects that store operating system images, though administrators can delete them manually.

When the `enableCommonBootImageImport` feature gate is disabled, `DataSource` objects are reset so that they no longer point to the original boot source. An administrator can manually provide a boot source by populating a PVC with an operating system, optionally creating a volume snapshot from the PVC, and then referring to the PVC or volume snapshot from the `DataSource` object.

_Custom_ boot sources that are not provided by {VirtProductName} are not controlled by the feature gate. You must manage them individually by editing the `HyperConverged` custom resource (CR). You can also use this method to manage individual system-defined boot sources.

Cluster administrators can enable automatic subscription for {op-system-base-full} virtual machines in the {VirtProductName} xref:../../virt/getting_started/virt-web-console-overview.adoc#overview-settings-cluster_virt-web-console-overview[web console].