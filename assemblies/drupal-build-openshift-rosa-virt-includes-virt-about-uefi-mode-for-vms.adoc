// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-uefi-mode-for-vms.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-uefi-mode-for-vms_{context}"]
= About UEFI mode for virtual machines

Unified Extensible Firmware Interface (UEFI), like legacy BIOS, initializes hardware components and operating system image files when a computer starts. UEFI supports more modern features and customization options than BIOS, enabling faster boot times.

It stores all the information about initialization and startup in a file with a `.efi` extension, which is stored on a special partition called EFI System Partition (ESP). The ESP also contains the boot loader programs for the operating system that is installed on the computer.
