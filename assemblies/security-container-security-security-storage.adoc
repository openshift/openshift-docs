:_mod-docs-content-type: ASSEMBLY
[id="security-storage"]
= Securing attached storage
include::_attributes/common-attributes.adoc[]
:context: security-storage

toc::[]

{product-title} supports multiple types of storage, both
for on-premise and cloud providers. In particular,
{product-title} can use storage types that support the Container
Storage Interface.

// Persistent volume plugins
include::modules/security-storage-persistent.adoc[leveloffset=+1]

// Shared storage
include::modules/security-storage-shared.adoc[leveloffset=+1]

// Block storage
include::modules/security-storage-block.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../storage/understanding-persistent-storage.adoc#understanding-persistent-storage[Understanding persistent storage]
* xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-using-csi[Configuring CSI volumes]
* xref:../../storage/dynamic-provisioning.adoc#dynamic-provisioning[Dynamic provisioning]
* xref:../../storage/persistent_storage/persistent-storage-nfs.adoc#persistent-storage-using-nfs[Persistent storage using NFS]
* xref:../../storage/persistent_storage/persistent-storage-aws.adoc#persistent-storage-using-aws-ebs[Persistent storage using AWS Elastic Block Store]
* xref:../../storage/persistent_storage/persistent-storage-gce.adoc#persistent-storage-using-gce[Persistent storage using GCE Persistent Disk]
