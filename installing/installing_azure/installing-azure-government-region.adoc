:_mod-docs-content-type: ASSEMBLY
[id="installing-azure-government-region"]
= Installing a cluster on Azure into a government region
include::_attributes/common-attributes.adoc[]
:context: installing-azure-government-region

toc::[]

In {product-title} version {product-version}, you can install a cluster on
Microsoft Azure into a government region. To configure the government region,
you modify parameters in the `install-config.yaml` file before you install the
cluster.

== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.
* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].
* You xref:../../installing/installing_azure/installing-azure-account.adoc#installing-azure-account[configured an Azure account] to host the cluster and determined the tested and validated government region to deploy the cluster to.
* If you use a firewall, you xref:../../installing/install_config/configuring-firewall.adoc#configuring-firewall[configured it to allow the sites] that your cluster requires access to.
* If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, you can xref:../../installing/installing_azure/installing-azure-customizations.adoc#manually-create-iam_installing-azure-customizations[manually create and maintain long-term credentials].
* If you use customer-managed encryption keys, you xref:../../installing/installing_azure/enabling-user-managed-encryption-azure.adoc#enabling-user-managed-encryption-azure[prepared your Azure environment for encryption].

include::modules/installation-azure-about-government-region.adoc[leveloffset=+1]

include::modules/private-clusters-default.adoc[leveloffset=+1]

include::modules/private-clusters-about-azure.adoc[leveloffset=+2]

include::modules/installation-azure-user-defined-routing.adoc[leveloffset=+2]

include::modules/installation-about-custom-azure-vnet.adoc[leveloffset=+1]

include::modules/cluster-entitlements.adoc[leveloffset=+1]

include::modules/ssh-agent-using.adoc[leveloffset=+1]

include::modules/installation-obtaining-installer.adoc[leveloffset=+1]

include::modules/installation-initializing-manual.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../installing/installing_azure/installation-config-parameters-azure.adoc#installation-config-parameters-azure[Installation configuration parameters for Azure]

include::modules/installation-minimum-resource-requirements.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../../scalability_and_performance/optimization/optimizing-storage.adoc#optimizing-storage[Optimizing storage]

include::modules/installation-azure-tested-machine-types.adoc[leveloffset=+2]

include::modules/installation-azure-trusted-launch.adoc[leveloffset=+2]
include::modules/installation-azure-confidential-vms.adoc[leveloffset=+2]

include::modules/installation-azure-config-yaml.adoc[leveloffset=+2]

include::modules/installation-configure-proxy.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* For more details about Accelerated Networking, see xref:../../machine_management/creating_machinesets/creating-machineset-azure.adoc#machineset-azure-accelerated-networking_creating-machineset-azure[Accelerated Networking for Microsoft Azure VMs].

include::modules/installation-launching-installer.adoc[leveloffset=+1]

include::modules/cli-installing-cli.adoc[leveloffset=+1]

include::modules/cli-logging-in-kubeadmin.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* See xref:../../web_console/web-console.adoc#web-console[Accessing the web console] for more details about accessing and understanding the {product-title} web console.

include::modules/cluster-telemetry.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* See xref:../../support/remote_health_monitoring/about-remote-health-monitoring.adoc#about-remote-health-monitoring[About remote health monitoring] for more information about the Telemetry service

== Next steps

* xref:../../post_installation_configuration/cluster-tasks.adoc#available_cluster_customizations[Customize your cluster].
* If necessary, you can
xref:../../support/remote_health_monitoring/opting-out-of-remote-health-reporting.adoc#opting-out-remote-health-reporting_opting-out-remote-health-reporting[opt out of remote health reporting].
