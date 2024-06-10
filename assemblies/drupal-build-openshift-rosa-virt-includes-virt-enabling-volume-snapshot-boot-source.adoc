// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

:_mod-docs-content-type: PROCEDURE
[id="virt-enabling-volume-snapshot-boot-source_{context}"]
= Enabling volume snapshot boot sources

Enable volume snapshot boot sources by setting the parameter in the `StorageProfile` associated with the storage class that stores operating system base images. Although `DataImportCron` was originally designed to maintain only PVC sources, `VolumeSnapshot` sources scale better than PVC sources for certain storage types.

[NOTE]
====
Use volume snapshots on a storage profile that is proven to scale better when cloning from a single snapshot.
====

.Prerequisites

* You must have access to a volume snapshot with the operating system image.
* The storage must support snapshotting.

.Procedure

. Open the storage profile object that corresponds to the storage class used to provision boot sources by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit storageprofile <storage_class>
----

. Review the `dataImportCronSourceFormat` specification of the `StorageProfile` to confirm whether or not the VM is using PVC or volume snapshot by default.

. Edit the storage profile, if needed, by updating the `dataImportCronSourceFormat` specification to `snapshot`.
+
.Example storage profile
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: StorageProfile
metadata:
# ...
spec:
  dataImportCronSourceFormat: snapshot
----

.Verification

. Open the storage profile object that corresponds to the storage class used to provision boot sources.
+
[source,terminal,subs="attributes+"]
----
$ oc get storageprofile <storage_class>  -oyaml
----

. Confirm that the `dataImportCronSourceFormat` specification of the `StorageProfile` is set to 'snapshot', and that any `DataSource` objects that the `DataImportCron` points to now reference volume snapshots.

You can now use these boot sources to create virtual machines.
