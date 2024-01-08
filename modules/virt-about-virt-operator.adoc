// Module included in the following assemblies:
//
// * virt/virt-architecture.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-virt-operator_{context}"]
= About the {VirtProductName} Operator

The {VirtProductName} Operator, `virt-operator` deploys, upgrades, and manages {VirtProductName} without disrupting current virtual machine (VM) workloads.

image::cnv_components_virt-operator.png[virt-operator components]

.virt-operator components
[cols="1,1"]
|===
|*Component* |*Description*

|`deployment/virt-api`
|HTTP API server that serves as the entry point for all virtualization-related flows.

|`deployment/virt-controller`
|Observes the creation of a new VM instance object and creates a corresponding pod. When the pod is scheduled on a node, `virt-controller` updates the VM with the node name.

|`daemonset/virt-handler`
|Monitors any changes to a VM and instructs `virt-launcher` to perform the required operations. This component is node-specific.

|`pod/virt-launcher`
|Contains the VM that was created by the user as implemented by `libvirt` and `qemu`.
|===
