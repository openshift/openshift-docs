// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-configuring-ptp_{context}"]
= PTP

{sno-caps} clusters use Precision Time Protocol (PTP) for network time synchronization.
The following example `PtpConfig` CRs illustrate the required PTP configurations for ordinary clocks, boundary clocks, and grandmaster clocks.
The exact configuration you apply will depend on the node hardware and specific use case.

.Recommended PTP ordinary clock configuration (`PtpConfigSlave.yaml`)
[source,yaml]
----
include::snippets/ztp_PtpConfigSlave.yaml[]
----


.Recommended boundary clock configuration (`PtpConfigBoundary.yaml`)
[source,yaml]
----
include::snippets/ztp_PtpConfigBoundary.yaml[]
----

.Recommended PTP Westport Channel e810 grandmaster clock configuration (`PtpConfigGmWpc.yaml`)
[source,yaml]
----
include::snippets/ztp_PtpConfigGmWpc.yaml[]
----

The following optional `PtpOperatorConfig` CR configures PTP events reporting for the node.

.Recommended PTP events configuration (`PtpOperatorConfigForEvent.yaml`)
[source,yaml]
----
include::snippets/ztp_PtpOperatorConfigForEvent.yaml[]
----
