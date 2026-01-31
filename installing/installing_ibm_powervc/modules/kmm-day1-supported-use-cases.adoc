// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: CONCEPT
[id="kmm-day1-supported-use-cases_{context}"]
= Day 1 supported use cases

The Day 1 functionality supports a limited number of use cases. The main use case is to allow loading out-of-tree (OOT) kernel modules prior to NetworkManager service initialization. It does not support loading kernel module at the `initramfs` stage.

The following are the conditions needed for Day 1 functionality:

* The kernel module is not loaded in the kernel.

* The in-tree kernel module is loaded into the kernel, but can be unloaded and replaced by the OOT kernel module. This means that the in-tree module is not referenced by any other kernel modules.

* In order for Day 1 functionlity to work, the node must have a functional network interface, that is, an in-tree kernel driver for that interface. The OOT kernel module can be a network driver that will replace the functional network driver.
