// Module included in the following assemblies:
//
// *scalability_and_performance/cnf-numa-aware-scheduling.adoc
:_mod-docs-content-type: CONCEPT
[id="cnf-scheduling-numa-aware-workloads-with-manual-perofrmance-settings_{context}"]
= Scheduling NUMA-aware workloads with manual performance settings

Clusters running latency-sensitive workloads typically feature performance profiles that help to minimize workload latency and optimize performance. However, you can schedule NUMA-aware workloads in a pristine cluster that does not feature a performance profile. The following workflow features a pristine cluster that you can manually configure for performance by using the `KubeletConfig` resource. This is not the typical environment for scheduling NUMA-aware workloads.
