// Module included in the following assemblies:
//
// * nodes/nodes-dashboard-using.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-dashboard-using-identify-critical-pulls_{context}"]
= Failure rate for image pulls in the last hour

The *Failure rate for image pulls in the last hour* query divides the total number of failed image pulls by the sum of successful and failed image pulls to provide a ratio of failures.

.Example default query
----
rate(container_runtime_crio_image_pulls_failure_total[1h]) / (rate(container_runtime_crio_image_pulls_success_total[1h]) + rate(container_runtime_crio_image_pulls_failure_total[1h]))
----

Understanding the failure rate of image pulls is crucial for maintaining the health of the node. A high failure rate might indicate networking issues, storage problems, misconfigurations, or other issues that could disrupt pod density and the deployment of new containers.

If the outcome of this query is high, investigate possible causes such as network connections, the availability of remote repositories, node storage, and the accuracy of image references. You can also review the metrics under the *Outliers*, *Average durations*, and *Number of operations* categories to gain further insights.