:_mod-docs-content-type: ASSEMBLY
[id="installing-openstack-user-sr-iov"]
= Installing a cluster on OpenStack on your own SR-IOV infrastructure
include::_attributes/common-attributes.adoc[]
:context: installing-openstack-user-sr-iov

toc::[]

In {product-title} {product-version}, you can install a cluster on
{rh-openstack-first} that runs on user-provisioned infrastructure and uses single-root input/output virtualization (SR-IOV) networks to run compute machines.

Using your own infrastructure allows you to integrate your cluster with existing infrastructure and modifications. The process requires more labor on your part than installer-provisioned installations, because you must create all {rh-openstack} resources, such as Nova servers, Neutron ports, and security groups. However, Red Hat provides Ansible playbooks to help you in the deployment process.

== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.
* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].
* You verified that {product-title} {product-version} is compatible with your {rh-openstack} version by using the xref:../../architecture/architecture-installation.adoc#supported-platforms-for-openshift-clusters_architecture-installation[Supported platforms for OpenShift clusters] section. You can also compare platform support across different versions by viewing the link:https://access.redhat.com/articles/4679401[{product-title} on {rh-openstack} support matrix].
* Your network configuration does not rely on a provider network. Provider networks are not supported.
* You have an {rh-openstack} account where you want to install {product-title}.
* You understand performance and scalability practices for cluster scaling, control plane sizing, and etcd. For more information, see xref:../../scalability_and_performance/recommended-performance-scale-practices/recommended-control-plane-practices.adoc#recommended-host-practices[Recommended practices for scaling the cluster].
* On the machine where you run the installation program, you have:
** A single directory in which you can keep the files you create during the installation process
** Python 3

include::modules/cluster-entitlements.adoc[leveloffset=+1]
include::modules/installation-osp-default-deployment.adoc[leveloffset=+1]
include::modules/installation-osp-control-compute-machines.adoc[leveloffset=+2]
include::modules/installation-osp-bootstrap-machine.adoc[leveloffset=+2]
include::modules/installation-osp-downloading-modules.adoc[leveloffset=+1]
include::modules/installation-osp-downloading-playbooks.adoc[leveloffset=+1]
include::modules/installation-obtaining-installer.adoc[leveloffset=+1]
include::modules/ssh-agent-using.adoc[leveloffset=+1]
include::modules/installation-osp-creating-image.adoc[leveloffset=+1]
include::modules/installation-osp-verifying-external-network.adoc[leveloffset=+1]
include::modules/installation-osp-accessing-api.adoc[leveloffset=+1]
include::modules/installation-osp-accessing-api-floating.adoc[leveloffset=+2]
include::modules/installation-osp-accessing-api-no-floating.adoc[leveloffset=+2]
include::modules/installation-osp-describing-cloud-parameters.adoc[leveloffset=+1]
include::modules/installation-initializing.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../installing/installing_openstack/installation-config-parameters-openstack.adoc#installation-config-parameters-openstack[Installation configuration parameters for OpenStack]

include::modules/installation-osp-config-yaml.adoc[leveloffset=+2]
include::modules/installation-osp-custom-subnet.adoc[leveloffset=+2]
include::modules/installation-osp-fixing-subnet.adoc[leveloffset=+2]
include::modules/installation-osp-emptying-worker-pools.adoc[leveloffset=+2]
include::modules/installation-user-infra-generate-k8s-manifest-ignition.adoc[leveloffset=+1]
include::modules/installation-osp-converting-ignition-resources.adoc[leveloffset=+1]
include::modules/installation-osp-creating-control-plane-ignition.adoc[leveloffset=+1]
include::modules/installation-osp-creating-network-resources.adoc[leveloffset=+1]
Optionally, you can use the `inventory.yaml` file that you created to customize your installation. For example, you can deploy a cluster that uses bare metal machines.

include::modules/installation-osp-deploying-bare-metal-machines.adoc[leveloffset=+2]
include::modules/installation-osp-creating-bootstrap-machine.adoc[leveloffset=+1]
include::modules/installation-osp-creating-control-plane.adoc[leveloffset=+1]
include::modules/cli-logging-in-kubeadmin.adoc[leveloffset=+1]
include::modules/installation-osp-deleting-bootstrap-resources.adoc[leveloffset=+1]
include::modules/installation-osp-configuring-sr-iov.adoc[leveloffset=+1]
include::modules/installation-osp-creating-sr-iov-compute-machines.adoc[leveloffset=+1]
include::modules/installation-approve-csrs.adoc[leveloffset=+1]
include::modules/installation-osp-verifying-installation.adoc[leveloffset=+1]
The cluster is operational. Before you can configure it for SR-IOV networks though, you must perform additional tasks.

include::modules/networking-osp-preparing-for-sr-iov.adoc[leveloffset=+1]
include::modules/networking-osp-enabling-metadata.adoc[leveloffset=+2]
include::modules/networking-osp-enabling-vfio-noiommu.adoc[leveloffset=+2]

[NOTE]
====
After you apply the machine config to the machine pool, you can xref:../../post_installation_configuration/machine-configuration-tasks.adoc#checking-mco-status_post-install-machine-configuration-tasks[watch the machine config pool status] to see when the machines are available.
====

// TODO: If bullet one of Next steps is truly required for this flow, these topics (in full or in part) could be added here rather than linked to.
// This document is quite long, however, and operator installation and configuration should arguably remain in their their own assemblies.

The cluster is installed and prepared for SR-IOV configuration. You must now perform the SR-IOV configuration tasks in "Next steps".

include::modules/cluster-telemetry.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_cluster-telemetry"]
.Additional resources

* See xref:../../support/remote_health_monitoring/about-remote-health-monitoring.adoc#about-remote-health-monitoring[About remote health monitoring] for more information about the Telemetry service

[role="_additional-resources"]
[id="additional-resources_installing-openstack-user-sr-iov"]
== Additional resources
* xref:../../scalability_and_performance/cnf-low-latency-tuning.adoc#cnf-understanding-low-latency_cnf-master[Low latency tuning of OpenShift Container Platform nodes]

[id="next-steps_installing-user-sr-iov"]
== Next steps

* To complete SR-IOV configuration for your cluster:
** xref:../../scalability_and_performance/what-huge-pages-do-and-how-they-are-consumed-by-apps.adoc#what-huge-pages-do_huge-pages[Configure huge pages support].
** xref:../../networking/hardware_networks/installing-sriov-operator.adoc#installing-sr-iov-operator_installing-sriov-operator[Install the SR-IOV Operator].
** xref:../../networking/hardware_networks/configuring-sriov-device.adoc#nw-sriov-networknodepolicy-object_configuring-sriov-device[Configure your SR-IOV network device].
* xref:../../post_installation_configuration/cluster-tasks.adoc#available_cluster_customizations[Customize your cluster].
* If necessary, you can
xref:../../support/remote_health_monitoring/opting-out-of-remote-health-reporting.adoc#opting-out-remote-health-reporting_opting-out-remote-health-reporting[opt out of remote health reporting].
* If you need to enable external access to node ports, xref:../../networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.adoc#nw-using-nodeport_configuring-ingress-cluster-traffic-nodeport[configure ingress cluster traffic by using a node port].
* If you did not configure {rh-openstack} to accept application traffic over floating IP addresses, xref:../../post_installation_configuration/network-configuration.adoc#installation-osp-configuring-api-floating-ip_post-install-network-configuration[configure {rh-openstack} access with floating IP addresses].
