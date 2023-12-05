// Module included in the following assemblies:
//
// * virt/virtual_machines/cloning_vms/virt-cloning-vm-disk-into-new-datavolume.adoc
// * virt/virtual_machines/cloning_vms/virt-cloning-vm-disk-to-new-block-storage-pvc.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-cloning-pvc-of-vm-disk-into-new-datavolume_{context}"]
= Cloning the PVC of a VM disk into a new data volume

You can clone the persistent volume claim (PVC) of an existing (virtual machine) VM disk
into a new data volume. The new data volume can then be used for a new virtual
machine.

[NOTE]
====
When a data volume is created independently of a VM, the lifecycle of the data volume is independent of the VM. If the VM is deleted, neither the data volume nor its associated PVC is deleted.
====

.Prerequisites

* The VM must be stopped.

.Procedure

. Create a YAML file for a data volume as shown in the following example:
+
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: <datavolume> <1>
spec:
  source:
    pvc:
      namespace: "<source_namespace>" <2>
      name: "<my_vm_disk>" <3>
  storage: {}
----
<1> Specify the name of the new data volume.
<2> Specify the namespace of the source PVC.
<3> Specify the name of the source PVC.

. Create the data volume by running the following command:
+
[source,terminal]
----
$ oc create -f <datavolume>.yaml
----
+
[NOTE]
====
Data volumes prevent a VM from starting before the PVC is prepared. You can create a VM that references the new data volume while the
PVC is being cloned.
====
