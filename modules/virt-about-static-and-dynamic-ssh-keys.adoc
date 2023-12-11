// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-accessing-vm-ssh.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-about-static-and-dynamic-ssh-keys_{context}"]
= About static and dynamic SSH key management

You can add public SSH keys to virtual machines (VMs) statically at first boot or dynamically at runtime.

[NOTE]
====
Only {op-system-base-full} 9 supports dynamic key injection.
====

[discrete]
[id="static-key-management_{context}"]
== Static SSH key management

You can add a statically managed SSH key to a VM with a guest operating system that supports configuration by using a cloud-init data source. The key is added to the virtual machine (VM) at first boot.

You can add the key by using one of the following methods:

* Add a key to a single VM when you create it by using the web console or the command line.
* Add a key to a project by using the web console. Afterwards, the key is automatically added to the VMs that you create in this project.

.Use cases

* As a VM owner, you can provision all your newly created VMs with a single key.

[discrete]
[id="dynamic-key-management_{context}"]
== Dynamic SSH key management

You can enable dynamic SSH key management for a VM with {op-system-base-full} 9 installed. Afterwards, you can update the key during runtime. The key is added by the QEMU guest agent, which is installed with Red Hat boot sources.

You can disable dynamic key management for security reasons. Then, the VM inherits the key management setting of the image from which it was created.

.Use cases

* Granting or revoking access to VMs: As a cluster administrator, you can grant or revoke remote VM access by adding or removing the keys of individual users from a `Secret` object that is applied to all VMs in a namespace.
* User access: You can add your access credentials to all VMs that you create and manage.

* Ansible provisioning:

** As an operations team member, you can create a single secret that contains all the keys used for Ansible provisioning.
** As a VM owner, you can create a VM and attach the keys used for Ansible provisioning.

* Key rotation:

** As a cluster administrator, you can rotate the Ansible provisioner keys used by VMs in a namespace.
** As a workload owner, you can rotate the key for the VMs that you manage.
