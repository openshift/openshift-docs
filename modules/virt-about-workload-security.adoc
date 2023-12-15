// Module included in the following assemblies:
//
// * virt/virt-security-policies.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-workload-security_{context}"]
= About workload security

By default, virtual machine (VM) workloads do not run with root privileges in {VirtProductName}, and there are no supported {VirtProductName} features that require root privileges.

For each VM, a `virt-launcher` pod runs an instance of `libvirt` in _session mode_ to manage the VM process. In session mode, the `libvirt` daemon runs as a non-root user account and only permits connections from clients that are running under the same user identifier (UID). Therefore, VMs run as unprivileged pods, adhering to the security principle of least privilege.