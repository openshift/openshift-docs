// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-sc-manage.adoc
//

:_mod-docs-content-type: PROCEDURE
[id="persistent-storage-csi-sc-managing-cli_{context}"]
= Managing the default storage class using the CLI

.Prerequisites
* Access to the cluster with cluster-admin privileges.

.Procedure

To manage the storage class using the CLI, run the following command:

[source,terminal]
----
oc patch clustercsidriver $DRIVERNAME --type=merge -p "{\"spec\":{\"storageClassState\":\"${STATE}\"}}" <1>
----
<1> Where `${STATE}` is "Removed" or "Managed" or "Unmanaged".
+
Where `$DRIVERNAME` is the provisioner name. You can find the provisioner name by running the command `oc get sc`.
