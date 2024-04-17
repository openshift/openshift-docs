:_mod-docs-content-type: ASSEMBLY
[id="persistent-storage-csi-aws-efs"]
= AWS Elastic File Service CSI Driver Operator
include::_attributes/common-attributes.adoc[]
:context: persistent-storage-csi-aws-efs

toc::[]

// Content similar to osd-persistent-storage-csi-aws-efs.adoc and rosa-persistent-storage-aws-efs-csi.adoc. Modules are reused.

== Overview

{product-title} is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for AWS Elastic File Service (EFS).

Familiarity with xref:../../storage/understanding-persistent-storage.adoc#understanding-persistent-storage[persistent storage] and xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[configuring CSI volumes] is recommended when working with a CSI Operator and driver.

After installing the AWS EFS CSI Driver Operator, {product-title} installs the AWS EFS CSI Operator and the AWS EFS CSI driver by default in the `openshift-cluster-csi-drivers` namespace. This allows the AWS EFS CSI Driver Operator to create CSI-provisioned PVs that mount to AWS EFS assets.

* The _AWS EFS CSI Driver Operator_, after being installed, does not create a storage class by default to use to create persistent volume claims (PVCs). However, you can manually create the AWS EFS `StorageClass`.
The AWS EFS CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand.
This eliminates the need for cluster administrators to pre-provision storage.

* The _AWS EFS CSI driver_ enables you to create and mount AWS EFS PVs.

[NOTE]
====
AWS EFS only supports regional volumes, not zonal volumes.
====

include::modules/persistent-storage-csi-about.adoc[leveloffset=+1]

:FeatureName: AWS EFS
include::modules/persistent-storage-efs-csi-driver-operator-setup.adoc[leveloffset=+1]

ifdef::openshift-rosa,openshift-enterprise[]
include::modules/persistent-storage-csi-efs-sts.adoc[leveloffset=+2]

xref:../../storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc#persistent-storage-csi-olm-operator-install_persistent-storage-csi-aws-efs[Install the AWS EFS CSI Driver Operator].
[role="_additional-resources"]
.Additional resources
* xref:../../storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc#persistent-storage-csi-olm-operator-install_persistent-storage-csi-aws-efs[Installing the AWS EFS CSI Driver Operator]
* xref:../../installing/installing_aws/installing-aws-customizations.adoc#cco-ccoctl-configuring_installing-aws-customizations[Configuring the Cloud Credential Operator utility]
* xref:../../storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc#persistent-storage-csi-efs-driver-install_persistent-storage-csi-aws-efs[Installing the {FeatureName} CSI Driver]
endif::[]

include::modules/persistent-storage-csi-olm-operator-install.adoc[leveloffset=+2]

xref:../../storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc#persistent-storage-csi-efs-driver-install_persistent-storage-csi-aws-efs[Install the AWS EFS CSI Driver].

include::modules/persistent-storage-csi-efs-driver-install.adoc[leveloffset=+2]

:StorageClass: AWS EFS
:Provisioner: efs.csi.aws.com
include::modules/storage-create-storage-class.adoc[leveloffset=+1]
include::modules/storage-create-storage-class-console.adoc[leveloffset=+2]
include::modules/storage-create-storage-class-cli.adoc[leveloffset=+2]

include::modules/persistent-storage-csi-efs-cross-account.adoc[leveloffset=+1]

include::modules/persistent-storage-csi-efs-create-volume.adoc[leveloffset=+1]

include::modules/persistent-storage-csi-dynamic-provisioning-aws-efs.adoc[leveloffset=+1]
If you have problems setting up dynamic provisioning, see xref:../../storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc#efs-troubleshooting_persistent-storage-csi-aws-efs[AWS EFS troubleshooting].
[role="_additional-resources"]
.Additional resources
* xref:../../storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc#efs-create-volume_persistent-storage-csi-aws-efs[Creating and configuring access to AWS EFS volume(s)]
* xref:../../storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc#storage-create-storage-class_persistent-storage-csi-aws-efs[Creating the AWS EFS storage class]

// Undefine {StorageClass} attribute, so that any mistakes are easily spotted
:!StorageClass:

include::modules/persistent-storage-csi-efs-static-pv.adoc[leveloffset=+1]
If you have problems setting up static PVs, see xref:../../storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc#efs-troubleshooting_persistent-storage-csi-aws-efs[AWS EFS troubleshooting].

include::modules/persistent-storage-csi-efs-security.adoc[leveloffset=+1]

include::modules/persistent-storage-csi-efs-troubleshooting.adoc[leveloffset=+1]

:FeatureName: AWS EFS
include::modules/persistent-storage-csi-olm-operator-uninstall.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources
* xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[Configuring CSI volumes]
