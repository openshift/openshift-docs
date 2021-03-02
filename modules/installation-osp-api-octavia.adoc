// Module included in the following assemblies:
//
// * networking/load-balancing-openstack.adoc

[id="installation-osp-api-octavia_{context}"]
= Scaling clusters for application traffic by using Octavia

{product-title} clusters that run on {rh-openstack-first} can use the Octavia load balancing service to distribute traffic across multiple virtual machines (VMs) or floating IP addresses. This feature mitigates the bottleneck that single machines or addresses create.

If your cluster uses Kuryr, the Cluster Network Operator created an internal Octavia load balancer at deployment. You can use this load balancer for application network scaling.

If your cluster does not use Kuryr, you must create your own Octavia load balancer to use it for application network scaling.