// Module included in the following assemblies:
//
// * nodes/nodes-cluster-resource-configure.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-cluster-resource-configure-evicted_{context}"]
= Understanding pod eviction

{product-title} may evict a pod from its node when the node's memory is
exhausted. Depending on the extent of memory exhaustion, the eviction may or
may not be graceful. Graceful eviction implies the main process (PID 1) of each
container receiving a SIGTERM signal, then some time later a SIGKILL signal if
the process has not exited already. Non-graceful eviction implies the main
process of each container immediately receiving a SIGKILL signal.

An evicted pod has phase *Failed* and reason *Evicted*. It will not be
restarted, regardless of the value of `restartPolicy`. However, controllers
such as the replication controller will notice the pod's failed status and create
a new pod to replace the old one.

[source,terminal]
----
$ oc get pod test
----

.Example output
[source,terminal]
----
NAME      READY     STATUS    RESTARTS   AGE
test      0/1       Evicted   0          1m
----

[source,terminal]
----
$ oc get pod test -o yaml
----

.Example output
[source,terminal]
----
...
status:
  message: 'Pod The node was low on resource: [MemoryPressure].'
  phase: Failed
  reason: Evicted
----
