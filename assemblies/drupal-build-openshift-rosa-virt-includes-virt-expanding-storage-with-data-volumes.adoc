// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-expanding-vm-disks.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-expanding-storage-with-data-volumes_{context}"]
= Expanding available virtual storage by adding blank data volumes

You can expand the available storage of a virtual machine (VM) by adding blank data volumes.

.Prerequisites

* You must have at least one persistent volume.

.Procedure

. Create a `DataVolume` manifest as shown in the following example:
+
.Example `DataVolume` manifest
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: blank-image-datavolume
spec:
  source:
    blank: {}
  storage:
    resources:
      requests:
        storage: <2Gi> <1>
  storageClassName: "<storage_class>" <2>
----
<1> Specify the amount of available space requested for the data volume.
<2> Optional: If you do not specify a storage class, the default storage class is used.

. Create the data volume by running the following command:
+
[source,terminal]
----
$ oc create -f <blank-image-datavolume>.yaml
----
