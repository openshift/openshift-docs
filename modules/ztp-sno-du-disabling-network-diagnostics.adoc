// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-disabling-network-diagnostics_{context}"]
= Network diagnostics

{sno-caps} clusters that run DU workloads require less inter-pod network connectivity checks to reduce the additional load created by these pods. The following custom resource (CR) disables these checks.

.Recommended network diagnostics configuration (`DisableSnoNetworkDiag.yaml`)
[source,yaml]
----
include::snippets/ztp_DisableSnoNetworkDiag.yaml[]
----
