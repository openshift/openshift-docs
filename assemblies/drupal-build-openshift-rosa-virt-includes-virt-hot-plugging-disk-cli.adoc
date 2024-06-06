// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-hot-plugging-virtual-disks.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-hot-plugging-disk-cli_{context}"]
= Hot plugging and hot unplugging a disk by using the command line

You can hot plug and hot unplug a disk while a virtual machine (VM) is running by using the command line.

You can make a hot plugged disk persistent so that it is permanently mounted on the VM.

.Prerequisites

* You must have at least one data volume or persistent volume claim (PVC) available for hot plugging.

.Procedure

* Hot plug a disk by running the following command:
+
[source,terminal]
----
$ virtctl addvolume <virtual-machine|virtual-machine-instance> \
  --volume-name=<datavolume|PVC> \
  [--persist] [--serial=<label-name>]
----
+
** Use the optional `--persist` flag to add the hot plugged disk to the virtual machine specification as a permanently mounted virtual disk. Stop, restart, or reboot the virtual machine to permanently mount the virtual disk. After specifying the `--persist` flag, you can no longer hot plug or hot unplug the virtual disk. The `--persist` flag applies to virtual machines, not virtual machine instances.
** The optional `--serial` flag allows you to add an alphanumeric string label of your choice. This helps you to identify the hot plugged disk in a guest virtual machine. If you do not specify this option, the label defaults to the name of the hot plugged data volume or PVC.

* Hot unplug a disk by running the following command:
+
[source,terminal]
----
$ virtctl removevolume <virtual-machine|virtual-machine-instance> \
  --volume-name=<datavolume|PVC>
----
