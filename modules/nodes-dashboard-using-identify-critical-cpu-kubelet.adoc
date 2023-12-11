// Module included in the following assemblies:
//
// * nodes/nodes-dashboard-using.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-dashboard-using-identify-critical-cpu-kubelet_{context}"]
= Nodes with Kubelet system reserved CPU utilization > 50%

The *Nodes with Kubelet system reserved CPU utilization > 50%* query calculates the percentage of the CPU that the Kubelet system is currently using from system reserved.

.Example default query
----
sum by (node) (rate(container_cpu_usage_seconds_total{id="/system.slice/kubelet.service"}[5m]) * 100) / sum by (node) (kube_node_status_capacity{resource="cpu"} - kube_node_status_allocatable{resource="cpu"}) >= 50
----

The Kubelet uses the system reserved CPU for its own operations and for running critical system services. For the node's health, it is important to ensure that system reserve CPU usage does not exceed the 50% threshold. Exceeding this limit could indicate heavy utilization or load on the Kubelet, which affects node stability and potentially the performance of the entire Kubernetes cluster.

If any node is displayed in this metric, the Kubelet and the system overall are under heavy load. You can reduce overload on a particular node by balancing the load across other nodes in the cluster. Check other query metrics under the *Outliers*, *Average durations*, and *Number of operations* categories to gain further insights and take necessary corrective action.