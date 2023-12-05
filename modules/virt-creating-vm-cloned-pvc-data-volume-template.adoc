// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-by-cloning-pvcs.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-vm-cloning-pvc-data-volume-template_{context}"]
= Creating a VM from a cloned PVC by using a data volume template

You can create a virtual machine (VM) that clones the persistent volume claim (PVC) of an existing VM by using a data volume template.

This method creates a data volume whose lifecycle is dependent on the original VM. Deleting the original VM deletes the cloned data volume and its associated PVC.

.Prerequisites

* The VM with the source PVC must be powered down.

.Procedure

. Create a `VirtualMachine` manifest as shown in the following example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    kubevirt.io/vm: vm-dv-clone
  name: vm-dv-clone <1>
spec:
  running: false
  template:
    metadata:
      labels:
        kubevirt.io/vm: vm-dv-clone
    spec:
      domain:
        devices:
          disks:
          - disk:
              bus: virtio
            name: root-disk
        resources:
          requests:
            memory: 64M
      volumes:
      - dataVolume:
          name: favorite-clone
        name: root-disk
  dataVolumeTemplates:
  - metadata:
      name: favorite-clone
    spec:
      storage:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 2Gi
      source:
        pvc:
          namespace: <source_namespace> <2>
          name: "<source_pvc>" <3>
----
<1> Specify the name of the VM.
<2> Specify the namespace of the source PVC.
<3> Specify the name of the source PVC.

. Create the virtual machine with the PVC-cloned data volume:
+
[source,terminal]
----
$ oc create -f <vm-clone-datavolumetemplate>.yaml
----
