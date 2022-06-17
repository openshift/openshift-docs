// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc

[id="persistent-storage-csi-manila-uninstall-operator_{context}"]
= Uninstalling the Manila CSI Driver Operator

Before you uninstall the Manila Container Storage Interface (CSI) Driver Operator, you must delete all persistent volume claims (PVCs) that are in use by the Operator.

.Prerequisites
* Access to the {product-title} web console.

.Procedure
To uninstall the Manila CSI Driver Operator from the web console:

. Log in to the web console.

. Navigate to *Storage* -> *Persistent Volume Claims*.

. Select any PVCs that are in use by the Manila CSI Driver Operator and click *Delete*.

. From the *Operators* -> *Installed Operators* page, scroll or type *Manila CSI* into the *Filter by name* field to find the Operator. Then, click on it.

. On the right-hand side of the *Installed Operators* details page, select *Uninstall Operator* from the *Actions* drop-down menu.

. When prompted by the *Uninstall Operator* window, click the *Uninstall* button to remove the Operator from the namespace. Any applications deployed by the Operator on the cluster will need to be cleaned up manually.

Once finished, the Manila CSI Driver Operator is no longer listed in the *Installed Operators* section of the web console.
