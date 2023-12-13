// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-enabling-sctp_{context}"]
= SCTP

Stream Control Transmission Protocol (SCTP) is a key protocol used in RAN applications. This `MachineConfig` object adds the SCTP kernel module to the node to enable this protocol.

.Recommended control plane node SCTP configuration (`03-sctp-machine-config-master.yaml`)
[source,yaml]
----
include::snippets/ztp_03-sctp-machine-config-master.yaml[]
----

.Recommended worker node SCTP configuration (`03-sctp-machine-config-worker.yaml`)
[source,yaml]
----
include::snippets/ztp_03-sctp-machine-config-worker.yaml[]
----
