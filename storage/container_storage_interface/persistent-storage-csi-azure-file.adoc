[id="persistent-storage-csi-azure-file"]
= Azure File CSI Driver Operator
include::_attributes/common-attributes.adoc[]
:context: persistent-storage-csi-azure-file

toc::[]

== Overview

{product-title} is capable of provisioning persistent volumes (PVs) by using the Container Storage Interface (CSI) driver for Microsoft Azure File Storage.

Familiarity with xref:../../storage/understanding-persistent-storage.adoc#understanding-persistent-storage[persistent storage] and xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[configuring CSI volumes] is recommended when working with a CSI Operator and driver.

To create CSI-provisioned PVs that mount to Azure File storage assets, {product-title} installs the Azure File CSI Driver Operator and the Azure File CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

* The _Azure File CSI Driver Operator_ provides a storage class that is named `azurefile-csi` that you can use to create persistent volume claims (PVCs). You can disable this default storage class if desired (see xref:../../storage/container_storage_interface/persistent-storage-csi-sc-manage.adoc#persistent-storage-csi-sc-manage[Managing the default storage class]).

* The _Azure File CSI driver_ enables you to create and mount Azure File PVs. The Azure File CSI driver supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage.

Azure File CSI Driver Operator does _not_ support:

* Virtual hard disks (VHD)

* Running on nodes with Federal Information Processing Standard (FIPS) mode enabled for Server Message Block (SMB) file share. However, Network File System (NFS) does support FIPS mode.

For more information about supported features, see xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#csi-drivers-supported_persistent-storage-csi[Supported CSI drivers and features].

include::modules/persistent-storage-csi-azure-file-nfs.adoc[leveloffset=+1]

include::modules/persistent-storage-csi-about.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../storage/persistent_storage/persistent-storage-azure-file.adoc#persistent-storage-using-azure-file[Persistent storage using Azure File]
* xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[Configuring CSI volumes]
