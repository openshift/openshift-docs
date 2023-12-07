// Module included in the following assemblies:
//
// * networking/hardware_networks/using-dpdk-and-rdma.adoc

:_mod-docs-content-type: CONCEPT
[id="nw-sriov-example-dpdk-line-rate_{context}"]
= Overview of achieving a specific DPDK line rate

To achieve a specific Data Plane Development Kit (DPDK) line rate, deploy a Node Tuning Operator and configure Single Root I/O Virtualization (SR-IOV). You must also tune the DPDK settings for the following resources:

- Isolated CPUs
- Hugepages
- The topology scheduler

[NOTE]
====
In previous versions of {product-title}, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for {product-title} applications. In {product-title} 4.11 and later, this functionality is part of the Node Tuning Operator.
====

.DPDK test environment
The following diagram shows the components of a traffic-testing environment:

image::261_OpenShift_DPDK_0722.png[DPDK test environment]

- **Traffic generator**: An application that can generate high-volume packet traffic.
- **SR-IOV-supporting NIC**: A network interface card compatible with SR-IOV. The card runs a number of virtual functions on a physical interface.
- **Physical Function (PF)**: A PCI Express (PCIe) function of a network adapter that supports the SR-IOV interface.
- **Virtual Function (VF)**:  A lightweight PCIe function on a network adapter that supports SR-IOV. The VF is associated with the PCIe PF on the network adapter. The VF represents a virtualized instance of the network adapter.
- **Switch**: A network switch. Nodes can also be connected back-to-back.
- **`testpmd`**: An example application included with DPDK. The `testpmd` application can be used to test the DPDK in a packet-forwarding mode. The `testpmd` application is also an example of how to build a fully-fledged application using the DPDK Software Development Kit (SDK).
- **worker 0** and **worker 1**: {product-title} nodes.
