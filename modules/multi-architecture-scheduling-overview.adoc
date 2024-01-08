// module included in the following assembly
//
//post_installation_configuration/configuring-multi-arch-compute-machines/multi-architecture-compute-managing.adoc

:_mod-docs-content-type: CONCEPT
[id="multi-architecture-scheduling-overview_{context}"]
= Scheduling workloads on clusters with multi-architecture compute machines

Before deploying a workload onto a cluster with compute nodes of different architectures, you must configure your compute node scheduling process so the pods in your cluster are correctly assigned.

You can schedule workloads onto multi-architecture nodes for your cluster in several ways. For example, you can use a node affinity or a node selector to select the node you want the pod to schedule onto. You can also use scheduling mechanisms, like taints and tolderations, when using node affinity or node selector to correctly schedule workloads.


