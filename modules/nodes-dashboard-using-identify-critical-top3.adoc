// Module included in the following assemblies:
//
// * nodes/nodes-dashboard-using.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-dashboard-using-identify-critical-top3_{context}"]
= Top 3 containers with the most OOM kills in the last day

The *Top 3 containers with the most OOM kills in the last day* query fetches details regarding the top three containers that have experienced the most Out-Of-Memory (OOM) kills in the previous day.

.Example default query
----
topk(3, sum(increase(container_runtime_crio_containers_oom_count_total[1d])) by (name))
----

OOM kills force the system to terminate some processes due to low memory. Frequent OOM kills can hinder the functionality of the node and even the entire Kubernetes ecosystem. Containers experiencing frequent OOM kills might be consuming more memory than they should, which causes system instability.

Use this metric to identify containers that are experiencing frequent OOM kills and investigate why these containers are consuming an excessive amount of memory. Adjust the resource allocation if necessary and consider resizing the containers based on their memory usage. You can also review the metrics under the *Outliers*, *Average durations*, and *Number of operations* categories to gain further insights into the health and stability of your nodes.