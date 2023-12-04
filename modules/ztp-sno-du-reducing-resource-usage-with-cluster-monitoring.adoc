// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-reducing-resource-usage-with-cluster-monitoring_{context}"]
= Alertmanager

{sno-caps} clusters that run DU workloads require reduced CPU resources consumed by the {product-title} monitoring components. The following `ConfigMap` custom resource (CR) disables Alertmanager.

.Recommended cluster monitoring configuration (`ReduceMonitoringFootprint.yaml`)
[source,yaml]
----
include::snippets/ztp_ReduceMonitoringFootprint.yaml[]
----
