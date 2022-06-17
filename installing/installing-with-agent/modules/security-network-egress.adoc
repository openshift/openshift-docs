// Module included in the following assemblies:
//
// * security/container_security/security-network.adoc

[id="security-network-egress_{context}"]
=  Securing egress traffic

{product-title} provides the ability to control egress traffic using either
a router or firewall method. For example, you can use IP whitelisting to control
database access.
A cluster administrator can assign one or more egress IP addresses to a project
in an {product-title} SDN network provider.
Likewise, a cluster administrator can prevent egress traffic from
going outside of an {product-title} cluster using an egress firewall.

By assigning a fixed egress IP address, you can have all outgoing traffic
assigned to that IP address for a particular project.
With the egress firewall, you can prevent a pod from connecting to an
external network, prevent a pod from connecting to an internal network,
or limit a pod's access to specific internal subnets.
