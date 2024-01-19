// Module included in the following assemblies:
//
// * virt/storage/virt-reserving-pvc-space-fs-overhead.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-overriding-default-fs-overhead-value_{context}"]
= Overriding the default file system overhead value

Change the amount of persistent volume claim (PVC) space that the {VirtProductName} reserves for file system overhead by editing the `spec.filesystemOverhead` attribute of the `HCO` object.

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

. Open the `HCO` object for editing by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit hyperconverged kubevirt-hyperconverged -n {CNVNamespace}
----

. Edit the `spec.filesystemOverhead` fields, populating them with your chosen values:
+
[source,yaml]
----
# ...
spec:
  filesystemOverhead:
    global: "<new_global_value>" <1>
    storageClass:
      <storage_class_name>: "<new_value_for_this_storage_class>" <2>
----
<1> The default file system overhead percentage used for any storage classes that do not already have a set value. For example, `global: "0.07"` reserves 7% of the PVC for file system overhead.
<2> The file system overhead percentage for the specified storage class. For example, `mystorageclass: "0.04"` changes the default overhead value for PVCs in the `mystorageclass` storage class to 4%.

. Save and exit the editor to update the `HCO` object.

.Verification

* View the `CDIConfig` status and verify your changes by running one of the following commands:
+
To generally verify changes to `CDIConfig`:
+
[source,terminal]
----
$ oc get cdiconfig -o yaml
----
+
To view your specific changes to `CDIConfig`:
+
[source,terminal]
----
$ oc get cdiconfig -o jsonpath='{.items..status.filesystemOverhead}'
----
