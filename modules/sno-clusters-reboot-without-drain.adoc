// Module included in the following assemblies:
//
// * nodes/nodes/nodes-nodes-working.adoc

:_mod-docs-content-type: CONCEPT
[id="sno-clusters-reboot-without-drain_{context}"]
= Handling errors in {sno} clusters when the node reboots without draining application pods

In {sno} clusters and in {product-title} clusters in general, a situation can arise where a node reboot occurs without first draining the node. This can occur where an application pod requesting devices fails with the `UnexpectedAdmissionError` error. `Deployment`, `ReplicaSet`, or `DaemonSet` errors are reported because the application pods that require those devices start before the pod serving those devices. You cannot control the order of pod restarts.

While this behavior is to be expected, it can cause a pod to remain on the cluster even though it has failed to deploy successfully. The pod continues to report `UnexpectedAdmissionError`. This issue is mitigated by the fact that application pods are typically included in a `Deployment`, `ReplicaSet`, or `DaemonSet`. If a pod is in this error state, it is of little concern because another instance should be running. Belonging to a `Deployment`, `ReplicaSet`, or `DaemonSet` guarantees the successful creation and execution of subsequent pods and ensures the successful deployment of the application.

There is ongoing work upstream to ensure that such pods are gracefully terminated. Until that work is resolved, run the following command for a {sno} cluster to remove the failed pods:

[source,terminal,subs="+quotes"]
----
$ oc delete pods --field-selector status.phase=Failed -n _<POD_NAMESPACE>_
----

[NOTE]
====
The option to drain the node is unavailable for {sno} clusters.
====
