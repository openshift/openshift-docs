// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-uefi-mode-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-booting-vms-uefi-mode_{context}"]
= Booting virtual machines in UEFI mode

You can configure a virtual machine to boot in UEFI mode by editing the `VirtualMachine` manifest.

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

. Edit or create a `VirtualMachine` manifest file. Use the `spec.firmware.bootloader` stanza to configure UEFI mode:
+
.Booting in UEFI mode with secure boot active
[source,yaml]
----
apiversion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    special: vm-secureboot
  name: vm-secureboot
spec:
  template:
    metadata:
      labels:
        special: vm-secureboot
    spec:
      domain:
        devices:
          disks:
          - disk:
              bus: virtio
            name: containerdisk
        features:
          acpi: {}
          smm:
            enabled: true <1>
        firmware:
          bootloader:
            efi:
              secureBoot: true <2>
# ...
----
<1> {VirtProductName} requires System Management Mode (`SMM`) to be enabled for Secure Boot in UEFI mode to occur.
<2> {VirtProductName} supports a VM with or without Secure Boot when using UEFI mode. If Secure Boot is enabled, then UEFI mode is required. However, UEFI mode can be enabled without using Secure Boot.

. Apply the manifest to your cluster by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----
