// Module included in the following assemblies:
//
// * nodes/nodes-dashboard-using.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-dashboard-using-identify-critical-cpu"]
= Nodes with System Reserved CPU Utilization > 80%

The *Nodes with system reserved CPU utilization > 80%* query identifies nodes where the system-reserved CPU utilization is more than 80%. The query focuses on the system-reserved capacity to calculate the rate of CPU usage in the last 5 minutes and compares that to the CPU resources available on the nodes. If the ratio exceeds 80%, the node's result is displayed in the metric.

.Example default query
----
sum by (node) (rate(container_cpu_usage_seconds_total{id="/system.slice"}[5m]) * 100) / sum by (node) (kube_node_status_capacity{resource="cpu"} - kube_node_status_allocatable{resource="cpu"}) >= 80
----

This query indicates a critical level of system-reserved CPU usage, which can lead to resource exhaustion. High system-reserved CPU usage can result in the inability of the system processes (including the Kubelet and CRI-O) to adequately manage resources on the node. This query can indicate excessive system processes or misconfigured CPU allocation.

Potential corrective measures include rebalancing workloads to other nodes or increasing the CPU resources allocated to the nodes. Investigate the cause of the high system CPU utilization and review the corresponding metrics in the *Outliers*, *Average durations*, and *Number of operations* categories for additional insights into the node's behavior.