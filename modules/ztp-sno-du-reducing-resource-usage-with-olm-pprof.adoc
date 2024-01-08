// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-reducing-resource-usage-with-olm-pprof_{context}"]
= Operator Lifecycle Manager

{sno-caps} clusters that run distributed unit workloads require consistent access to CPU resources. Operator Lifecycle Manager (OLM) collects performance data from Operators at regular intervals, resulting in an increase in CPU utilisation. The following `ConfigMap` custom resource (CR) disables the collection of Operator performance data by OLM.

.Recommended cluster OLM configuration (`ReduceOLMFootprint.yaml`)
[source,yaml]
----
include::snippets/ztp_ReduceOLMFootprint.yaml[]
----
