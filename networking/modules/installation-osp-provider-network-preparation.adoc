// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-kuryr.adoc
// * installing/installing_openstack/installing-openstack-user-kuryr.adoc
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-provider-network-preparation_{context}"]
= {rh-openstack} provider network requirements for cluster installation

Before you install an {product-title} cluster, your {rh-openstack-first} deployment and provider network must meet a number of conditions:

* The link:https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/networking-overview_rhosp-network#install-networking_network-overview[{rh-openstack} networking service (Neutron) is enabled] and accessible through the {rh-openstack} networking API.
* The {rh-openstack} networking service has the link:https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/config-allowed-address-pairs_rhosp-network#overview-allow-addr-pairs_config-allowed-address-pairs[port security and allowed address pairs extensions enabled].
* The provider network can be shared with other tenants.
+
[TIP]
====
Use the `openstack network create` command with the `--share` flag to create a network that can be shared.
====
* The {rh-openstack} project that you use to install the cluster must own the provider network, as well as an appropriate subnet.
+
[TIP]
====
To create a network for a project that is named "openshift," enter the following command::
[source,terminal]
----
$ openstack network create --project openshift
----

To create a subnet for a project that is named "openshift," enter the following command::
[source,terminal]
----
$ openstack subnet create --project openshift
----

To learn more about creating networks on {rh-openstack}, read link:https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/networking-overview_rhosp-network#tenant-provider-networks_network-overview[the provider networks documentation].
====
+
If the cluster is owned by the `admin` user, you must run the installer as that user to create ports on the network.
+
[IMPORTANT]
====
Provider networks must be owned by the {rh-openstack} project that is used to create the cluster. If they are not, the {rh-openstack} Compute service (Nova) cannot request a port from that network.
====

* Verify that the provider network can reach the {rh-openstack} metadata service IP address, which is `169.254.169.254` by default.
+
Depending on your {rh-openstack} SDN and networking service configuration, you might need to provide the route when you create the subnet. For example:
+
[source,terminal]
----
$ openstack subnet create --dhcp --host-route destination=169.254.169.254/32,gateway=192.0.2.2 ...
----

* Optional: To secure the network, create link:https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/config-rbac-policies_rhosp-network#proc_create-rbac-policies_config-rbac-policies[role-based access control (RBAC)] rules that limit network access to a single project.
