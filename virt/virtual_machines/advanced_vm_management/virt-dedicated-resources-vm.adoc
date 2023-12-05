:_mod-docs-content-type: ASSEMBLY
[id="virt-dedicated-resources-vm"]
= Enabling dedicated resources for virtual machines
include::_attributes/common-attributes.adoc[]
:context: virt-dedicated-resources-vm

toc::[]

To improve performance, you can dedicate node resources, such as CPU, to a virtual machine.

include::modules/virt-about-dedicated-resources.adoc[leveloffset=+1]

== Prerequisites

* The xref:../../../scalability_and_performance/using-cpu-manager.adoc[CPU Manager]  must be configured on the node. Verify that the node has the `cpumanager = true` label before scheduling virtual machine workloads.

* The virtual machine must be powered off.

include::modules/virt-enabling-dedicated-resources.adoc[leveloffset=+1]
