// Module included in the following assemblies:
//
// * post_installation_configuration/node-tasks.adoc

[id="recommended-node-host-practices_{context}"]
= Recommended node host practices

The {product-title} node configuration file contains important options. For
example, two parameters control the maximum number of pods that can be scheduled
to a node: `podsPerCore` and `maxPods`.

When both options are in use, the lower of the two values limits the number of
pods on a node. Exceeding these values can result in:

* Increased CPU utilization.
* Slow pod scheduling.
* Potential out-of-memory scenarios, depending on the amount of memory in the node.
* Exhausting the pool of IP addresses.
* Resource overcommitting, leading to poor user application performance.

[IMPORTANT]
====
In Kubernetes, a pod that is holding a single container actually uses two
containers. The second container is used to set up networking prior to the
actual container starting. Therefore, a system running 10 pods will actually
have 20 containers running.
====

[NOTE]
====
Disk IOPS throttling from the cloud provider might have an impact on CRI-O and kubelet.
They might get overloaded when there are large number of I/O intensive pods running on
the nodes. It is recommended that you monitor the disk I/O on the nodes and use volumes
with sufficient throughput for the workload.
====

`podsPerCore` sets the number of pods the node can run based on the number of
processor cores on the node. For example, if `podsPerCore` is set to `10` on a
node with 4 processor cores, the maximum number of pods allowed on the node will
be `40`.

[source,yaml]
----
kubeletConfig:
  podsPerCore: 10
----

Setting `podsPerCore` to `0` disables this limit. The default is `0`.
`podsPerCore` cannot exceed `maxPods`.

`maxPods` sets the number of pods the node can run to a fixed value, regardless
of the properties of the node.

[source,yaml]
----
 kubeletConfig:
    maxPods: 250
----
