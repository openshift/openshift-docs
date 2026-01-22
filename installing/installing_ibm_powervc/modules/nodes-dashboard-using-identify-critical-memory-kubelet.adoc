// Module included in the following assemblies:
//
// * nodes/nodes-dashboard-using.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-dashboard-using-identify-critical-memory-kubelet_{context}"]
= Nodes with Kubelet system reserved memory utilization > 50%

The *Nodes with Kubelet system reserved memory utilization > 50%* query indicates nodes where the Kubelet's system reserved memory utilization exceeds 50%. The query examines the memory that the Kubelet process itself is consuming on a node.

.Example default query
----
sum by (node) (container_memory_rss{id="/system.slice/kubelet.service"}) / sum by (node) (kube_node_status_capacity{resource="memory"} - kube_node_status_allocatable{resource="memory"}) * 100 >= 50
----

This query helps you identify any possible memory pressure situations in your nodes that could affect the stability and efficiency of node operations. Kubelet memory utilization that consistently exceeds 50% of the system reserved memory, indicate that the system reserved settings are not configured properly and that there is a high risk of the node becoming unstable.

If this metric is highlighted, review your configuration policy and consider adjusting the system reserved settings or the resource limits settings for the Kubelet. Additionally, if your Kubelet memory utilization consistently exceeds half of your total reserved system memory, examine metrics under the *Outliers*, *Average durations*, and *Number of operations* categories to gain further insights for more precise diagnostics.