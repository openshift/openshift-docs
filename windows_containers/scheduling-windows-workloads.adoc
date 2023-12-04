:_mod-docs-content-type: ASSEMBLY
[id="scheduling-windows-workloads"]
= Scheduling Windows container workloads
include::_attributes/common-attributes.adoc[]
:context: scheduling-windows-workloads

toc::[]

You can schedule Windows workloads to Windows compute nodes.

[discrete]
== Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a Windows container as the OS image.
* You have created a Windows compute machine set.

include::modules/windows-pod-placement.adoc[leveloffset=+1]

[discrete]
[role="_additional-resources"]
=== Additional resources

* xref:../nodes/scheduling/nodes-scheduler-about.adoc#nodes-scheduler-about[Controlling pod placement using the scheduler]
* xref:../nodes/scheduling/nodes-scheduler-taints-tolerations.adoc#nodes-scheduler-taints-tolerations[Controlling pod placement using node taints]
* xref:../nodes/scheduling/nodes-scheduler-node-selectors.adoc#nodes-scheduler-node-selectors[Placing pods on specific nodes using node selectors]

include::modules/creating-runtimeclass.adoc[leveloffset=+1]

include::modules/sample-windows-workload-deployment.adoc[leveloffset=+1]

include::modules/machineset-manually-scaling.adoc[leveloffset=+1]
