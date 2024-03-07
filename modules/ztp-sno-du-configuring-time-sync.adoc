// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: REFERENCE
[id="ztp-sno-du-configuring-time-sync_{context}"]
= Configuring cluster time synchronization

Run a one-time system time synchronization job for control plane or worker nodes.

.Recommended one time time-sync for control plane nodes (`99-sync-time-once-master.yaml`)
[source,yaml]
----
include::snippets/ztp_99-sync-time-once-master.yaml[]
----

.Recommended one time time-sync for worker nodes (`99-sync-time-once-worker.yaml`)
[source,yaml]
----
include::snippets/ztp_99-sync-time-once-worker.yaml[]
----
