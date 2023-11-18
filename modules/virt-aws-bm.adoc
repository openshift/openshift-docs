// Module included in the following assemblies:
//
// * virt/install/preparing-cluster-for-virt.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-aws-bm_{context}"]
= {VirtProductName} on AWS bare metal

You can run {VirtProductName} on an Amazon Web Services (AWS) bare-metal {product-title} cluster.

[NOTE]
====
{VirtProductName} is also supported on {product-rosa} (ROSA) Classic clusters, which have the same configuration requirements as AWS bare-metal clusters.
====

Before you set up your cluster, review the following summary of supported features and limitations:

Installing::
--
* You can install the cluster by using installer-provisioned infrastructure, ensuring that you specify bare-metal instance types for the worker nodes by editing the `install-config.yaml` file. For example, you can use the `c5n.metal` type value for a machine based on x86_64 architecture.
+
For more information, see the {product-title} documentation about installing on AWS.
--

Accessing virtual machines (VMs)::
--
* There is no change to how you access VMs by using the `virtctl` CLI tool or the {product-title} web console.
* You can expose VMs by using a `NodePort` or `LoadBalancer` service. 
** The load balancer approach is preferable because {product-title} automatically creates the load balancer in AWS and manages its lifecycle. A security group is also created for the load balancer, and you can use annotations to attach existing security groups. When you remove the service, {product-title} removes the load balancer and its associated resources.
--

Networking::
--
* You cannot use Single Root I/O Virtualization (SR-IOV) or bridge Container Network Interface (CNI) networks, including virtual LAN (VLAN). If your application requires a flat layer 2 network or control over the IP pool, consider using OVN-Kubernetes secondary overlay networks.
--

Storage::
--
* You can use any storage solution that is certified by the storage vendor to work with the underlying platform.
+
[IMPORTANT]
====
AWS bare-metal and ROSA clusters might have different supported storage solutions. Ensure that you confirm support with your storage vendor.
====
* Amazon Elastic File System (EFS) and Amazon Elastic Block Store (EBS) are not supported for use with {VirtProductName} due to performance and functionality limitations.
--