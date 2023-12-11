// Module included in the following assemblies:
//
// * networking/configuring-hardware-offloading.adoc

:_mod-docs-content-type: CONCEPT
[id="about-hardware-offloading_{context}"]
= About hardware offloading

Open vSwitch hardware offloading is a method of processing network tasks by diverting them away from the CPU and offloading them to a dedicated processor on a network interface controller.
As a result, clusters can benefit from faster data transfer speeds, reduced CPU workloads, and lower computing costs.

The key element for this feature is a modern class of network interface controllers known as SmartNICs.
A SmartNIC is a network interface controller that is able to handle computationally-heavy network processing tasks.
In the same way that a dedicated graphics card can improve graphics performance, a SmartNIC can improve network performance.
In each case, a dedicated processor improves performance for a specific type of processing task.

In {product-title}, you can configure hardware offloading for bare metal nodes that have a compatible SmartNIC.
Hardware offloading is configured and enabled by the SR-IOV Network Operator.

Hardware offloading is not compatible with all workloads or application types.
Only the following two communication types are supported:

* pod-to-pod
* pod-to-service, where the service is a ClusterIP service backed by a regular pod

In all cases, hardware offloading takes place only when those pods and services are assigned to nodes that have a compatible SmartNIC.
Suppose, for example, that a pod on a node with hardware offloading tries to communicate with a service on a regular node.
On the regular node, all the processing takes place in the kernel, so the overall performance of the pod-to-service communication is limited to the maximum performance of that regular node.
Hardware offloading is not compatible with DPDK applications.

Enabling hardware offloading on a node, but not configuring pods to use, it can result in decreased throughput performance for pod traffic. You cannot configure hardware offloading for pods that are managed by {product-title}.