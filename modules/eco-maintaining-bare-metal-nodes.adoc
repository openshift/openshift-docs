// Module included in the following assemblies:
//
// nodes/nodes/eco-node-maintenance-operator.adoc

:_mod-docs-content-type: CONCEPT
[id="eco-maintaining-bare-metal-nodes_{context}"]
= Maintaining bare-metal nodes

When you deploy {product-title} on bare-metal infrastructure, you must take additional considerations into account compared to deploying on cloud infrastructure. Unlike in cloud environments, where the cluster nodes are considered ephemeral, reprovisioning a bare-metal node requires significantly more time and effort for maintenance tasks.

When a bare-metal node fails due to a kernel error or a NIC card hardware failure, workloads on the failed node need to be restarted on another node in the cluster while the problem node is repaired or replaced. Node maintenance mode allows cluster administrators to gracefully turn-off nodes, move workloads to other parts of the cluster, and ensure that workloads do not get interrupted. Detailed progress and node status details are provided during maintenance.

