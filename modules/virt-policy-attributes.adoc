// Module included in the following assembly:
//
// * virt/virtual_machines/advanced_vm_management/virt-schedule-vms.adoc
//

[id="policy-attributes_{context}"]
= Policy attributes

You can schedule a virtual machine (VM) by specifying a policy attribute and a CPU feature that is matched for compatibility when the VM is scheduled on a node. A policy attribute specified for a VM determines how that VM is scheduled on a node.

[cols="30,70"]
|===
|Policy attribute | Description

|force
|The VM is forced to be scheduled on a node. This is true even if the host CPU does not support the VM's CPU.

|require
|Default policy that applies to a VM if the VM is not configured with a specific CPU model and feature specification. If a node is not configured to support CPU node discovery with this default policy attribute or any one of the other policy attributes, VMs are not scheduled on that node. Either the host CPU must support the VM's CPU or the hypervisor must be able to emulate the supported CPU model.

|optional
|The VM is added to a node if that VM is supported by the host's physical machine CPU.

|disable
|The VM cannot be scheduled with CPU node discovery.

|forbid
|The VM is not scheduled even if the feature is supported by the host CPU and CPU node discovery is enabled.
|===
