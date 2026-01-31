// Module included in the following assemblies:
//
// * nodes/nodes-dashboard-using.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-dashboard-using-identify-critical-memory_{context}"]
= Nodes with system reserved memory utilization > 80%

The *Nodes with system reserved memory utilization > 80%* query calculates the percentage of system reserved memory that is utilized for each node. The calculation divides the total resident set size (RSS) by the total memory capacity of the node subtracted from the allocatable memory. RSS is the portion of the system's memory occupied by a process that is held in main memory (RAM). Nodes are flagged if their resulting value equals or exceeds an 80% threshold.

.Example default query
----
sum by (node) (container_memory_rss{id="/system.slice"}) / sum by (node) (kube_node_status_capacity{resource="memory"} - kube_node_status_allocatable{resource="memory"}) * 100 >= 80
----

System reserved memory is crucial for a Kubernetes node as it is utilized to run system daemons and Kubernetes system daemons. System reserved memory utilization that exceeds 80% indicates that the system and Kubernetes daemons are consuming too much memory and can suggest node instability that could affect the performance of running pods. Excessive memory consumption can cause Out-of-Memory (OOM) killers that can terminate critical system processes to free up memory.

If a node is flagged by this metric, identify which system or Kubernetes processes are consuming excessive memory and take appropriate actions to mitigate the situation. These actions may include scaling back non-critical processes, optimizing program configurations to reduce memory usage, or upgrading node systems to hardware with greater memory capacity. You can also review the metrics under the *Outliers*, *Average durations*, and *Number of operations* categories to gain further insights into node performance.