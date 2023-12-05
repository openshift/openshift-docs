// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
:_mod-docs-content-type: CONCEPT
[id="install-osp-dualstack_{context}"]
= Optional: Configuring a cluster with dual-stack networking

:FeatureName: Dual-stack configuration for OpenStack
include::snippets/technology-preview.adoc[]

You can create a dual-stack cluster on {rh-openstack}. However, the dual-stack configuration is enabled only if you are using an {rh-openstack} network with IPv4 and IPv6 subnets.

[NOTE]
====
{rh-openstack} does not support the following configurations:

* Conversion of an IPv4 single-stack cluster to a dual-stack cluster network.

* IPv6 as the primary address family for dual-stack cluster network.
====

