// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-du-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-ran-workload-partitioning_{context}"]
= Workload partitioning

New in this release::
* No reference design updates in this release

Description::
Workload partitioning pins OpenShift platform and Day 2 Operator pods that are part of the DU profile to the reserved `cpuset` and removes the reserved CPU from node accounting.
This leaves all unreserved CPU cores available for user workloads.
+
The method of enabling and configuring workload partitioning changed in {product-title} 4.14.
+
--
4.14 and later::
* Configure partitions by setting installation parameters:
+
[source,yaml]
----
cpuPartitioningMode: AllNodes
----

* Configure management partition cores with the reserved CPU set in the `PerformanceProfile` CR

4.13 and earlier::
* Configure partitions with extra `MachineConfiguration` CRs applied at install-time
--

Limits and requirements::
* `Namespace` and `Pod` CRs must be annotated to allow the pod to be applied to the management partition

* Pods with CPU limits cannot be allocated to the partition.
This is because mutation can change the pod QoS.

* For more information about the minimum number of CPUs that can be allocated to the management partition, see xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-components.adoc#telco-ran-node-tuning-operator_ran-ref-design-components[Node Tuning Operator].

Engineering considerations::
* Workload Partitioning pins all management pods to reserved cores.
A sufficient number of cores must be allocated to the reserved set to account for operating system, management pods, and expected spikes in CPU use that occur when the workload starts, the node reboots, or other system events happen.
