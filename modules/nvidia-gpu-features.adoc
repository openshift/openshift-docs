// Module included in the following assemblies:
//
// * architecture/nvidia-gpu-architecture-overview.adoc


:_mod-docs-content-type: CONCEPT
[id="nvidia-gpu-features_{context}"]
= NVIDIA GPU features for {product-title}

// NVIDIA GPU Operator::
// The NVIDIA GPU Operator is a Kubernetes Operator that enables {product-title} {VirtProductName} to expose GPUs to virtualized workloads running on {product-title}.
// It allows users to easily provision and manage GPU-enabled virtual machines, providing them with the ability to run complex artificial intelligence/machine learning (AI/ML) workloads on the same platform as their other workloads.
// It also provides an easy way to scale the GPU capacity of their infrastructure, allowing for rapid growth of GPU-based workloads.

NVIDIA Container Toolkit::
NVIDIA Container Toolkit enables you to create and run GPU-accelerated containers. The toolkit includes a container runtime library and utilities to automatically configure containers to use NVIDIA GPUs.

NVIDIA AI Enterprise::
NVIDIA AI Enterprise is an end-to-end, cloud-native suite of AI and data analytics software optimized, certified, and supported with NVIDIA-Certified systems.
+
NVIDIA AI Enterprise includes support for Red Hat {product-title}. The following installation methods are supported:
+
* {product-title} on bare metal or VMware vSphere with GPU Passthrough.

* {product-title} on VMware vSphere with NVIDIA vGPU.

GPU Feature Discovery::
NVIDIA GPU Feature Discovery for Kubernetes is a software component that enables you to automatically generate labels for the GPUs available on a node. GPU Feature Discovery uses node feature discovery (NFD) to perform this labeling.
+
The Node Feature Discovery Operator (NFD) manages the discovery of hardware features and configurations in an OpenShift Container Platform cluster by labeling nodes with hardware-specific information. NFD labels the host with node-specific attributes, such as PCI cards, kernel, OS version, and so on.
+
You can find the NFD Operator in the Operator Hub by searching for “Node Feature Discovery”.


NVIDIA GPU Operator with OpenShift Virtualization::
Up until this point, the GPU Operator only provisioned worker nodes to run GPU-accelerated containers. Now, the GPU Operator can also be used to provision worker nodes for running GPU-accelerated virtual machines (VMs).
+
You can configure the GPU Operator to deploy different software components to worker nodes depending on which GPU workload is configured to run on those nodes.

GPU Monitoring dashboard::
You can install a monitoring dashboard to display GPU usage information on the cluster *Observe* page in the {product-title} web console. GPU utilization information includes the number of available GPUs, power consumption (in watts), temperature (in degrees Celsius), utilization (in percent), and other metrics for each GPU.
