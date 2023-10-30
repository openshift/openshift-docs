// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-expanding-vm-disks.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-expanding-vm-disk-pvc_{context}"]
= Expanding a VM disk PVC

You can increase the size of a virtual machine (VM) disk by expanding the persistent volume claim (PVC) of the disk.

If the PVC uses the file system volume mode, the disk image file expands to the available size while reserving some space for file system overhead.

.Procedure

. Edit the `PersistentVolumeClaim` manifest of the VM disk that you want to expand:
+
[source,terminal]
----
$ oc edit pvc <pvc_name>
----

. Update the disk size:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
   name: vm-disk-expand
spec:
  accessModes:
     - ReadWriteMany
  resources:
    requests:
       storage: 3Gi <1>
# ...
----
<1> Specify the new disk size.
