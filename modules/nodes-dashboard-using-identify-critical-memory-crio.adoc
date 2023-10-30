// Module included in the following assemblies:
//
// * nodes/nodes-dashboard-using.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-dashboard-using-identify-critical-memory-crio_{context}"]
= Nodes with CRI-O system reserved memory utilization > 50%

The *Nodes with CRI-O system reserved memory utilization > 50%* query calculates all nodes where the percentage of used memory reserved for the CRI-O system is greater than or equal to 50%. In this case, memory usage is defined by the resident set size (RSS), which is the portion of the CRI-O system's memory held in RAM.

.Example default query
----
sum by (node) (container_memory_rss{id="/system.slice/crio.service"}) / sum by (node) (kube_node_status_capacity{resource="memory"} - kube_node_status_allocatable{resource="memory"}) * 100 >= 50
----

This query helps you monitor the status of memory reserved for the CRI-O system on each node. High utilization could indicate a lack of available resources and potential performance issues. If the memory reserved for the CRI-O system exceeds the advised limit of 50%, it indicates that half of the system reserved memory is being used by CRI-O on a node.

Check memory allocation and usage and assess whether memory resources need to be shifted or increased to prevent possible node instability. You can also examine the metrics under the *Outliers*, *Average durations*, and *Number of operations* categories to gain further insights.