// Module included in the following assemblies:
//
// * nodes/nodes-dashboard-using.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-dashboard-using-identify-critical-cpu-crio"]
= Nodes with CRI-O system reserved CPU utilization > 50%

The *Nodes with CRI-O system reserved CPU utilization > 50%* query identifies nodes where the CRI-O system reserved CPU utilization has exceeded 50% in the last 5 minutes. The query monitors CPU resource consumption by CRI-O, your container runtime, on a per-node basis.

.Example default query
----
sum by (node) (rate(container_cpu_usage_seconds_total{id="/system.slice/crio.service"}[5m]) * 100) / sum by (node) (kube_node_status_capacity{resource="cpu"} - kube_node_status_allocatable{resource="cpu"}) >= 50
----

This query allows for quick identification of abnormal start times that could negatively impact pod performance. If this query returns a high value, your pod start times are slower than usual, which suggests potential issues with the kubelet, pod configuration, or resources.

Investigate further by checking your pod configurations and allocated resources. Make sure that they align with your system capabilities. If you still see high start times, explore metrics panels from other categories on the dashboard to determine the state of your system components.