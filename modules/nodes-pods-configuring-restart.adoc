// Module included in the following assemblies:
//
// * nodes/nodes-pods-configuring.adoc
// * nodes/nodes-cluster-pods-configuring

[id="nodes-pods-configuring-restart_{context}"]
= Configuring how pods behave after restart

A pod restart policy determines how {product-title} responds when Containers in that pod exit.
The policy applies to all Containers in that pod.

The possible values are:

* `Always` - Tries restarting a successfully exited Container on the pod continuously, with an exponential back-off delay (10s, 20s, 40s) capped at 5 minutes. The default is `Always`.
* `OnFailure` - Tries restarting a failed Container on the pod with an exponential back-off delay (10s, 20s, 40s) capped at 5 minutes.
* `Never` - Does not try to restart exited or failed Containers on the pod. Pods immediately fail and exit.

After the pod is bound to a node, the pod will never be bound to another node. This means that a controller is necessary in order for a pod to survive node failure:

[cols="3",options="header"]
|===

|Condition
|Controller Type
|Restart Policy

|Pods that are expected to terminate (such as batch computations)
|Job
|`OnFailure` or `Never`

|Pods that are expected to not terminate (such as web servers)
|Replication controller
| `Always`.

|Pods that must run one-per-machine
|Daemon set
|Any
|===

If a Container on a pod fails and the restart policy is set to `OnFailure`, the pod stays on the node and the Container is restarted. If you do not want the Container to
restart, use a restart policy of `Never`.

If an entire pod fails, {product-title} starts a new pod. Developers must address the possibility that applications might be restarted in a new pod. In particular,
applications must handle temporary files, locks, incomplete output, and so forth caused by previous runs.

[NOTE]
====
Kubernetes architecture expects reliable endpoints from cloud providers. When a cloud provider is down, the kubelet prevents {product-title} from restarting.

If the underlying cloud provider endpoints are not reliable, do not install a cluster using cloud provider integration. Install the cluster as if it was in a no-cloud environment. It is not recommended to toggle cloud provider integration on or off in an installed cluster.
====

For details on how {product-title} uses restart policy with failed Containers, see
the link:https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#example-states[Example States] in the Kubernetes documentation.
