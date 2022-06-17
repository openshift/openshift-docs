// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-kuryr.adoc
// * installing/installing_openstack/installing-openstack-user-kuryr.adoc
// * post_installation_configuration/network-configuration.adoc

[id="installation-osp-kuryr-port-pools_{context}"]
= Kuryr ports pools

A Kuryr ports pool maintains a number of ports on standby for pod creation.

Keeping ports on standby minimizes pod creation time. Without ports pools, Kuryr must explicitly request port creation or deletion whenever a pod is created or deleted.

The Neutron ports that Kuryr uses are created in subnets that are tied to namespaces. These pod ports are also added as subports to the primary port of {product-title} cluster nodes.

Because Kuryr keeps each namespace in a separate subnet, a separate ports pool is maintained for each namespace-worker pair.

Prior to installing a cluster, you can set the following parameters in the `cluster-network-03-config.yml` manifest file to configure ports pool behavior:

* The `enablePortPoolsPrepopulation` parameter controls pool prepopulation, which forces Kuryr to add Neutron ports to the pools when the first pod that is configured to use the dedicated network for pods is created in a namespace. The default value is `false`.
* The `poolMinPorts` parameter is the minimum number of free ports that are kept in the pool. The default value is `1`.
* The `poolMaxPorts` parameter is the maximum number of free ports that are kept in the pool. A value of `0` disables that upper bound. This is the default setting.
+
If your OpenStack port quota is low, or you have a limited number of IP addresses on the pod network, consider setting this option to ensure that unneeded ports are deleted.
* The `poolBatchPorts` parameter defines the maximum number of Neutron ports that can be created at once. The default value is `3`.
