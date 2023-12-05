:_mod-docs-content-type: ASSEMBLY
[id="updating-hardware-on-nodes-running-on-vsphere"]
= Updating hardware on nodes running on vSphere
include::_attributes/common-attributes.adoc[]
:context: updating-hardware-on-nodes-running-in-vsphere

toc::[]

////
WARNING: This assembly has been moved into a subdirectory for 4.14+. Changes to this assembly for earlier versions should be done in separate PRs based off of their respective version branches. Otherwise, your cherry picks may fail.

To do: Remove this comment once 4.13 docs are EOL.
////

You must ensure that your nodes running in vSphere are running on the hardware version supported by {product-title}. Currently, hardware version 15 or later is supported for vSphere virtual machines in a cluster.

You can update your virtual hardware immediately or schedule an update in vCenter.

[IMPORTANT]
====
* Version {product-version} of {product-title} requires VMware virtual hardware version 15 or later.

* Before upgrading OpenShift 4.12 to OpenShift 4.13, you must update vSphere to *v7.0.2 or later*; otherwise, the OpenShift 4.12 cluster is marked *un-upgradeable*.
====

[id="updating-virtual-hardware-on-vsphere_{context}"]
== Updating virtual hardware on vSphere

To update the hardware of your virtual machines (VMs) on VMware vSphere, update your virtual machines separately to reduce the risk of downtime for your cluster.

[IMPORTANT]
====
As of {product-title} 4.13, VMware virtual hardware version 13 is no longer supported. You need to update to VMware version 15 or later for supporting functionality.
====

// Updating the virtual hardware for control plane nodes on vSphere
include::modules/update-vsphere-virtual-hardware-on-control-plane-nodes.adoc[leveloffset=+2]

// Updating the virtual hardware for compute nodes on vSphere
include::modules/update-vsphere-virtual-hardware-on-compute-nodes.adoc[leveloffset=+2]

// Updating the virtual hardware for template on vSphere
include::modules/update-vsphere-virtual-hardware-on-template.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../../nodes/nodes/nodes-nodes-working.adoc#nodes-nodes-working-evacuating_nodes-nodes-working[Understanding how to evacuate pods on nodes]

// Scheduling an update for virtual hardware on vSphere
include::modules/scheduling-virtual-hardware-update-on-vsphere.adoc[leveloffset=+1]
