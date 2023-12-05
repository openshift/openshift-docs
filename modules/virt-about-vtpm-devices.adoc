// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-using-vtpm-devices.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-vtpm-devices_{context}"]
= About vTPM devices

A virtual Trusted Platform Module (vTPM) device functions like a
physical Trusted Platform Module (TPM) hardware chip.

You can use a vTPM device with any operating system, but Windows 11 requires
the presence of a TPM chip to install or boot. A vTPM device allows VMs created
from a Windows 11 image to function without a physical TPM chip.

If you do not enable vTPM, then the VM does not recognize a TPM device, even if
the node has one.

A vTPM device also protects virtual machines by storing secrets without physical hardware. {VirtProductName} supports persisting vTPM device state by using Persistent Volume Claims (PVCs) for VMs. You must specify the storage class to be used by the PVC by setting the `vmStateStorageClass` attribute in the `HyperConverged` custom resource (CR):

[source,yaml]
----
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  vmStateStorageClass: <storage_class_name>

# ...
----

[NOTE]
====
The storage class must be of type `Filesystem` and support the `ReadWriteMany` (RWX) access mode.
====
