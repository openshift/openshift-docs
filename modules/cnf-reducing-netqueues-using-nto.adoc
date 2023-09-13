// Module included in the following assemblies:
//CNF-1483 (4.8)
// * scalability_and_performance/low-latency-tuning.adoc

[id="reducing-nic-queues-using-the-node-tuning-operator_{context}"]
= Reducing NIC queues using the Node Tuning Operator

The Node Tuning Operator allows you to adjust the network interface controller (NIC) queue count for each network device by configuring the performance profile. Device network queues allows the distribution of packets among different physical queues and each queue gets a separate thread for packet processing.

In real-time or low latency systems, all the unnecessary interrupt request lines (IRQs) pinned to the isolated CPUs must be moved to reserved or housekeeping CPUs.

In deployments with applications that require system, {product-title} networking or in mixed deployments with Data Plane Development Kit (DPDK) workloads, multiple queues are needed to achieve good throughput and the number of NIC queues should be adjusted or remain unchanged. For example, to achieve low latency the number of NIC queues for DPDK based workloads should be reduced to just the number of reserved or housekeeping CPUs.

Too many queues are created by default for each CPU and these do not fit into the interrupt tables for housekeeping CPUs when tuning for low latency. Reducing the number of queues makes proper tuning possible. Smaller number of queues means a smaller number of interrupts that then fit in the IRQ table.

[NOTE]
====
In earlier versions of {product-title}, the Performance Addon Operator provided automatic, low latency performance tuning for applications. In {product-title} 4.11 and later, this functionality is part of the Node Tuning Operator.
====
