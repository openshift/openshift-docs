// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-setting-rcu-normal_{context}"]
= Setting rcu_normal

The following `MachineConfig` CR configures the system to set `rcu_normal` to 1 after the system has finished startup. This improves kernel latency for vDU applications.

.Recommended configuration for disabling `rcu_expedited` after the node has finished startup (`08-set-rcu-normal-master.yaml`)
[source,yaml]
----
include::snippets/ztp_08-set-rcu-normal-master.yaml[]
----
