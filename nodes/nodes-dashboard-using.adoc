:_mod-docs-content-type: ASSEMBLY
[id="nodes-dashboard-using"]
= Node metrics dashboard
include::_attributes/common-attributes.adoc[]
:context: nodes-dashboard-using

toc::[]

The node metrics dashboard is a visual analytics dashboard that helps you identify potential pod scaling issues.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// About the node metrics dashboard
include::modules/nodes-dashboard-using-about.adoc[leveloffset=+1]

// Accessing the node metrics dashboard
include::modules/nodes-dashboard-using-accessing.adoc[leveloffset=+1]

// Identify metrics for indicating optimal node resource usage
include::modules/nodes-dashboard-using-identify.adoc[leveloffset=+1]

// Top 3 Containers With the Most OOM Kills in the Last Day
include::modules/nodes-dashboard-using-identify-critical-top3.adoc[leveloffset=+2]

// Failure Rate for Image Pulls in the Last Hour
include::modules/nodes-dashboard-using-identify-critical-pulls.adoc[leveloffset=+2]

// Nodes with System Reserved Memory Utilization > 80%
include::modules/nodes-dashboard-using-identify-critical-memory.adoc[leveloffset=+2]

// Nodes with Kubelet System Reserved Memory Utilization > 50%
include::modules/nodes-dashboard-using-identify-critical-memory-kubelet.adoc[leveloffset=+2]

// Nodes with CRI-O System Reserved Memory Utilization > 50%
include::modules/nodes-dashboard-using-identify-critical-memory-crio.adoc[leveloffset=+2]

// Nodes with System Reserved CPU Utilization > 80%
include::modules/nodes-dashboard-using-identify-critical-cpu.adoc[leveloffset=+2]

// Nodes with Kubelet System Reserved CPU Utilization > 50%
include::modules/nodes-dashboard-using-identify-critical-cpu-kubelet.adoc[leveloffset=+2]

// Nodes with CRI-O System Reserved CPU Utilization > 50%
include::modules/nodes-dashboard-using-identify-critical-cpu-crio.adoc[leveloffset=+2]

// Customizing dashboard queries
include::modules/nodes-dashboard-using-queries.adoc[leveloffset=+1]