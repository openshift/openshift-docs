[id="persistent-storage-csi-google-cloud-file"]
= Google Compute Platform Filestore CSI Driver Operator
include::_attributes/common-attributes.adoc[]
:context: persistent-storage-csi-google-cloud-file

toc::[]

// TP features should be excluded from OSD and ROSA. When this feature is GA, it can be included in the OSD/ROSA docs, but with a warning that it is available as of version 4.x.

[id="persistent-storage-csi-google-cloud-file-overview"]
== Overview

{product-title} is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for Google Compute Platform (GCP) Filestore Storage.

Familiarity with xref:../../storage/understanding-persistent-storage.adoc#understanding-persistent-storage[persistent storage] and xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[configuring CSI volumes] is recommended when working with a CSI Operator and driver.

To create CSI-provisioned PVs that mount to GCP Filestore Storage assets, you install the GCP Filestore CSI Driver Operator and the GCP Filestore CSI driver in the `openshift-cluster-csi-drivers` namespace.

* The _GCP Filestore CSI Driver Operator_ does not provide a storage class by default, but xref:../../storage/container_storage_interface/persistent-storage-csi-google-cloud-file.adoc#persistent-storage-csi-google-cloud-file-create-sc_persistent-storage-csi-google-cloud-file[you can create one if needed]. The GCP Filestore CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on demand, eliminating the need for cluster administrators to pre-provision storage.

* The _GCP Filestore CSI driver_ enables you to create and mount GCP Filestore PVs.

include::modules/persistent-storage-csi-about.adoc[leveloffset=+1]

include::modules/persistent-storage-csi-gcp-file-install.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* link:https://cloud.google.com/endpoints/docs/openapi/enable-api[Enabling an API in your Google Cloud].
* link:https://support.google.com/googleapi/answer/6158841?hl=en[Enabling an API using the Google Cloud web console].

include::modules/persistent-storage-csi-google-cloud-file-create-sc.adoc[leveloffset=+1]

include::modules/persistent-storage-csi-google-cloud-file-delete-instances.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources
* xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[Configuring CSI volumes]
