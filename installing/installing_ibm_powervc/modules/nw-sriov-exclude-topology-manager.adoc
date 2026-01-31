// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-device.adoc

:_mod-docs-content-type: CONCEPT
[id="nw-sriov-exclude-topology-manager_{context}"]
= Exclude the SR-IOV network topology for NUMA-aware scheduling

You can exclude advertising the Non-Uniform Memory Access (NUMA) node for the SR-IOV network to the Topology Manager for more flexible SR-IOV network deployments during NUMA-aware pod scheduling.

In some scenarios, it is a priority to maximize CPU and memory resources for a pod on a single NUMA node. By not providing a hint to the Topology Manager about the NUMA node for the pod's SR-IOV network resource, the Topology Manager can deploy the SR-IOV network resource and the pod CPU and memory resources to different NUMA nodes. This can add to network latency because of the data transfer between NUMA nodes. However, it is acceptable in scenarios when workloads require optimal CPU and memory performance.

For example, consider a compute node, `compute-1`, that features two NUMA nodes: `numa0` and `numa1`. The SR-IOV-enabled NIC is present on `numa0`. The CPUs available for pod scheduling are present on `numa1` only. By setting the `excludeTopology` specification to `true`, the Topology Manager can assign CPU and memory resources for the pod to `numa1` and can assign the SR-IOV network resource for the same pod to `numa0`. This is only possible when you set the `excludeTopology` specification to `true`. Otherwise, the Topology Manager attempts to place all resources on the same NUMA node.
