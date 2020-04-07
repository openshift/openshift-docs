[[nodes-configuring-nodes]]
= Understanding Pod restart policy
{product-author}
{product-version}
:data-uri:
:icons:
:experimental:
:toc: macro
:toc-title:


//from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
A Pod restart policy determines how {product-title} responds when containers in that Pod exit.
The policy applies to all containers in that Pod.

The possible values are:

* `Always` - Tries restarting a successfully exited container on the Pod continuously, with an exponential back-off delay (10s, 20s, 40s) until the Pod is restarted. The default is `Always`.
* `OnFailure` - Tries restarting a failed container on the Pod with an exponential back-off delay (10s, 20s, 40s) capped at 5 minutes.
* `Never` - Does not try to restart exited or failed containers on the Pod. Pods immediately fail and exit.

//https://kubernetes-v1-4.github.io/docs/user-guide/pod-states/
Once bound to a node, a Pod will never be bound to another node. This means that a controller is necessary in order for a Pod to survive node failure:

[cols="3",options="header"]
|===

|Condition
|Controller Type
|Restart Policy

|Pods that are expected to terminate (such as batch computations)
|xref:../../architecture/core_concepts/deployments.adoc#jobs[Job]
|`OnFailure` or `Never`

|Pods that are expected to not terminate (such as web servers)
|xref:../../architecture/core_concepts/deployments.adoc#replication-controllers[Replication Controller]
| `Always`.

|Pods that must run one-per-machine
|xref:../../dev_guide/daemonsets.adoc#dev-guide-daemonsets[Daemonset]
|Any
|===

If a container on a Pod fails and the restart policy is set to `OnFailure`, the Pod stays on the node and the container is restarted. If you do not want the container to
restart, use a restart policy of `Never`.

//https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#handling-pod-and-container-failures
If an entire Pod fails, {product-title} starts a new Pod. Developers must address the possibility that applications might be restarted in a new Pod. In particular,
applications must handle temporary files, locks, incomplete output, and so forth caused by previous runs.

For details on how {product-title} uses restart policy with failed containers, see
the link:https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#example-states[Example States] in the Kubernetes documentation.

