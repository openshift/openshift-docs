// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-core-ref-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-core-scheduling_{context}"]
= Scheduling

New in this release::

* NUMA-aware scheduling with the NUMA Resources Operator is now generally available in {product-title} {product-version}.
* With this release, you can exclude advertising the Non-Uniform Memory Access (NUMA) node for the SR-IOV network to the Topology Manager. By not advertising the NUMA node for the SR-IOV network, you can permit more flexible SR-IOV network deployments during NUMA-aware pod scheduling. To exclude advertising the NUMA node for the SR-IOV network resource to the Topology Manager, set the value `excludeTopology` to `true` in the `SriovNetworkNodePolicy` CR. For more information, see link:https://docs.openshift.com/container-platform/4.14/networking/hardware_networks/configuring-sriov-device.html#nw-sriov-exclude-topology-manager_configuring-sriov-device[Exclude the SR-IOV network topology for NUMA-aware scheduling].

Description::

* The scheduler is a cluster-wide component responsible for selecting the right node for a given workload. It is a core part of the platform and does not require any specific configuration in the common deployment scenarios. However, there are few specific use cases described in the following section.

Limits and requirements::

* The default scheduler does not understand the NUMA locality of workloads. It only knows about the sum of all free resources on a worker node. This might cause workloads to be rejected when scheduled to a node with https://docs.openshift.com/container-platform/latest/scalability_and_performance/using-cpu-manager.html#topology_manager_policies_using-cpu-manager-and-topology_manager[Topology manager policy] set to `single-numa-node` or `restricted`.
** For example, consider a pod requesting 6 CPUs and being scheduled to an empty node that has 4 CPUs per NUMA node. The total allocatable capacity of the node is 8 CPUs and the scheduler will place the pod there. The node local admission will fail, however, as there are only 4 CPUs available in each of the NUMA nodes.
** All clusters with multi-NUMA nodes are required to use the https://docs.openshift.com/container-platform/latest/scalability_and_performance/cnf-numa-aware-scheduling.html#installing-the-numa-resources-operator_numa-aware[NUMA Resources Operator]. The `machineConfigPoolSelector` of the NUMA Resources Operator must select all nodes where NUMA aligned scheduling is needed.
* All machine config pools must have consistent hardware configuration for example all nodes are expected to have the same NUMA zone count.

Engineering considerations::

* Pods might require annotations for correct scheduling and isolation. For more information on annotations, see the "CPU Partitioning and performance tuning" section.

