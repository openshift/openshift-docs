// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-configuring-performance-addons_{context}"]
= Performance profile

{sno-caps} clusters that run DU workloads require a Node Tuning Operator performance profile to use real-time host capabilities and services.

[NOTE]
====
In earlier versions of {product-title}, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In {product-title} 4.11 and later, this functionality is part of the Node Tuning Operator.
====

The following example `PerformanceProfile` CR illustrates the required {sno} cluster configuration.

.Recommended performance profile configuration (`PerformanceProfile.yaml`)
[source,yaml]
----
include::snippets/ztp_PerformanceProfile.yaml[]
----

include::snippets/performance-profile-workload-partitioning.adoc[]
