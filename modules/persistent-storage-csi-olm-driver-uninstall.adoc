// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="persistent-storage-csi-olm-driver-uninstall_{context}"]
= Uninstalling the {FeatureName} CSI driver

.Prerequisites
* Access to the {product-title} web console.

To uninstall the {FeatureName} CSI driver:

. Log in to the web console.

. Stop all applications that use {FeatureName} persistent volumes (PVs).

. Click *administration* -> *CustomResourceDefinitions* -> *ClusterCSIDriver*.

. On the *Instances* tab, for *{provisioner}*, on the far left side, click the drop-down menu, and then click *Delete ClusterCSIDriver*.

. When prompted, click *Delete*.
