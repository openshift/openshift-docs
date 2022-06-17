// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-kuryr.adoc

[id="installation-osp-default-kuryr-deployment_{context}"]
= Resource guidelines for installing {product-title} on {rh-openstack} with Kuryr

When using Kuryr SDN, the pods, services, namespaces, and network policies are
using resources from the {rh-openstack} quota; this increases the minimum
requirements. Kuryr also has some additional requirements on top of what a
default install requires.

Use the following quota to satisfy a default cluster's minimum requirements:

.Recommended resources for a default {product-title} cluster on {rh-openstack} with Kuryr

[options="header"]
|==============================================================================================
|Resource                | Value
|Floating IP addresses   | 3 - plus the expected number of Services of LoadBalancer type
|Ports                   | 1500 - 1 needed per Pod
|Routers                 | 1
|Subnets                 | 250 - 1 needed per Namespace/Project
|Networks                | 250 - 1 needed per Namespace/Project
|RAM                     | 112 GB
|vCPUs                   | 28
|Volume storage          | 275 GB
|Instances               | 7
|Security groups         | 250 - 1 needed per Service and per NetworkPolicy
|Security group rules    | 1000
|Server groups           | 2 - plus 1 for each additional availability zone in each machine pool
|Load balancers          | 100 - 1 needed per Service
|Load balancer listeners | 500 - 1 needed per Service-exposed port
|Load balancer pools     | 500 - 1 needed per Service-exposed port
|==============================================================================================

A cluster might function with fewer than recommended resources, but its performance is not guaranteed.

[IMPORTANT]
====
If {rh-openstack} object storage (Swift) is available and operated by a user account with the `swiftoperator` role, it is used as the default backend for the {product-title} image registry. In this case, the volume storage requirement is 175 GB. Swift space requirements vary depending on the size of the image registry.
====

[IMPORTANT]
====
If you are using {rh-openstack-first} version 16 with the Amphora driver rather than the OVN Octavia driver, security groups are associated with service accounts instead of user projects.
====

Take the following notes into consideration when setting resources:

* The number of ports that are required is larger than the number of pods. Kuryr
uses ports pools to have pre-created ports ready to be used by pods and speed up
the pods' booting time.

* Each network policy is mapped into an {rh-openstack} security group, and
depending on the `NetworkPolicy` spec, one or more rules are added to the
security group.

* Each service is mapped to an {rh-openstack} load balancer. Consider this requirement
 when estimating the number of security groups required for the quota.
+
If you are using
{rh-openstack} version 15 or earlier, or the `ovn-octavia driver`, each load balancer
has a security group with the user project.

* The quota does not account for load balancer resources (such as VM
resources), but you must consider these resources when you decide the
{rh-openstack} deployment's size. The default installation will have more than
50 load balancers; the clusters must be able to accommodate them.
+
If you are using {rh-openstack} version 16 with the OVN Octavia driver enabled, only one load balancer
VM is generated; services are load balanced through OVN flows.

An {product-title} deployment comprises control plane machines, compute
machines, and a bootstrap machine.

To enable Kuryr SDN, your environment must meet the following requirements:

* Run {rh-openstack} 13+.
* Have Overcloud with Octavia.
* Use Neutron Trunk ports extension.
* Use `openvswitch` firewall driver if ML2/OVS Neutron driver is used instead
of `ovs-hybrid`.
