// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

:_mod-docs-content-type: CONCEPT
[id="about-using-nvidia-gpu_{context}"]
= About using the NVIDIA GPU Operator

You can use the NVIDIA GPU Operator with {VirtProductName} to rapidly provision worker nodes for running GPU-enabled virtual machines (VMs). The NVIDIA GPU Operator manages NVIDIA GPU resources in an {product-title} cluster and automates tasks that are required when preparing nodes for GPU workloads.

Before you can deploy application workloads to a GPU resource, you must install components such as the NVIDIA drivers that enable the compute unified device architecture (CUDA), Kubernetes device plugin, container runtime, and other features, such as automatic node labeling and monitoring. By automating these tasks, you can quickly scale the GPU capacity of your infrastructure. The NVIDIA GPU Operator can especially facilitate provisioning complex artificial intelligence and machine learning (AI/ML) workloads.