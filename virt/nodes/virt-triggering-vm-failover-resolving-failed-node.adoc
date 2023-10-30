:_mod-docs-content-type: ASSEMBLY
[id="virt-triggering-vm-failover-resolving-failed-node"]
= Deleting a failed node to trigger virtual machine failover
include::_attributes/common-attributes.adoc[]
:context: virt-triggering-vm-failover-resolving-failed-node

toc::[]

If a node fails and xref:../../machine_management/deploying-machine-health-checks.adoc#machine-health-checks-about_deploying-machine-health-checks[machine health checks] are not deployed on your cluster, virtual machines (VMs) with `runStrategy: Always` configured are not automatically relocated to healthy nodes. To trigger VM failover, you must manually delete the `Node` object.

[NOTE]
====
If you installed your cluster by using xref:../../installing/installing_bare_metal_ipi/ipi-install-overview.adoc#ipi-install-overview[installer-provisioned infrastructure] and you properly configured machine health checks, the following events occur:

* Failed nodes are automatically recycled.
* Virtual machines with xref:../../virt/nodes/virt-node-maintenance.adoc#run-strategies[`runStrategy`] set to `Always` or `RerunOnFailure` are automatically scheduled on healthy nodes.
====

[id="prerequisites_{context}"]
== Prerequisites

* A node where a virtual machine was running has the `NotReady` xref:../../nodes/nodes/nodes-nodes-viewing.adoc#nodes-nodes-viewing-listing_nodes-nodes-viewing[condition].
* The virtual machine that was running on the failed node has `runStrategy` set to `Always`.
* You have installed the OpenShift CLI (`oc`).

include::modules/nodes-nodes-working-deleting-bare-metal.adoc[leveloffset=+1]

[id="verifying-vm-failover_{context}"]
== Verifying virtual machine failover

After all resources are terminated on the unhealthy node, a new virtual machine instance (VMI) is automatically created on a healthy node for each relocated VM. To confirm that the VMI was created, view all VMIs by using the `oc` CLI.

include::modules/virt-listing-vmis-cli.adoc[leveloffset=+2]
