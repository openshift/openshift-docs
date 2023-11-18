// Module included in the following assemblies:
//
// * microshift_storage/volume-snapshots-microshift.adoc

:_mod-docs-content-type: CONCEPT
[id="microshift-storage-volume-cloning_{context}"]
= About LVM volume cloning

The logical volume manager storage (LVMS) supports persistent volume claim (PVC) cloning for logical volume manager (LVM) thin volumes. A clone is a duplicate of an existing volume that can be used like any other volume. When provisioned, an exact duplicate of the original volume is created if the data source references a source PVC in the same namespace. After a cloned PVC is created, it is considered a new object and completely separate from the source PVC. The clone represents the data from the source at the moment in time it was created.

[NOTE]
====
Cloning is only possible when the source and destination PVCs are in the same namespace. To create PVC clones, you must configure thin volumes on the {op-system-ostree} host.
====
