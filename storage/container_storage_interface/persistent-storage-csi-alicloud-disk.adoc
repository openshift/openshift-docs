[id="persistent-storage-csi-alicloud-disk"]
= AliCloud Disk CSI Driver Operator
include::_attributes/common-attributes.adoc[]
:context: persistent-storage-csi-alicloud-disk

toc::[]

[id="persistent-storage-csi-alicloud-disk-overview"]
== Overview

{product-title} is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for Alibaba AliCloud Disk Storage.

Familiarity with xref:../../storage/understanding-persistent-storage.adoc#understanding-persistent-storage[persistent storage] and xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[configuring CSI volumes] is recommended when working with a CSI Operator and driver.

To create CSI-provisioned PVs that mount to AliCloud Disk storage assets, {product-title} installs the AliCloud Disk CSI Driver Operator and the AliCloud Disk CSI driver, by default, in the `openshift-cluster-csi-drivers` namespace.

* The _AliCloud Disk CSI Driver Operator_ provides a storage class (`alicloud-disk`) that you can use to create persistent volume claims (PVCs). The AliCloud Disk CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on demand, eliminating the need for cluster administrators to pre-provision storage. You can disable this default storage class if desired (see xref:../../storage/container_storage_interface/persistent-storage-csi-sc-manage.adoc#persistent-storage-csi-sc-manage[Managing the default storage class]).

* The _AliCloud Disk CSI driver_ enables you to create and mount AliCloud Disk PVs.

include::modules/persistent-storage-csi-about.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[Configuring CSI volumes]
