:_mod-docs-content-type: ASSEMBLY
[id="installing-azure-stack-hub-default"]
= Installing a cluster on Azure Stack Hub with an installer-provisioned infrastructure
include::_attributes/common-attributes.adoc[]
:context: installing-azure-stack-hub-default

toc::[]

In {product-title} version {product-version}, you can install a cluster on Microsoft Azure Stack Hub with an installer-provisioned infrastructure. However, you must manually configure the `install-config.yaml` file to specify values that are specific to Azure Stack Hub.

[NOTE]
====
While you can select `azure` when using the installation program to deploy a cluster using installer-provisioned infrastructure, this option is only supported for the Azure Public Cloud.
====

[id="prerequisites_installing-azure-stack-hub-default"]
== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.
* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].
* You xref:../../installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc#installing-azure-stack-hub-account[configured an Azure Stack Hub account] to host the cluster.
* If you use a firewall, you xref:../../installing/install_config/configuring-firewall.adoc#configuring-firewall[configured it to allow the sites] that your cluster requires access to.
* You verified that you have approximately 16 GB of local disk space. Installing the cluster requires that you download the {op-system} virtual hard disk (VHD) cluster image and upload it to your Azure Stack Hub environment so that it is accessible during deployment. Decompressing the VHD files requires this amount of local disk space.

include::modules/cluster-entitlements.adoc[leveloffset=+1]

include::modules/ssh-agent-using.adoc[leveloffset=+1]

include::modules/installation-azure-user-infra-uploading-rhcos.adoc[leveloffset=+1]

include::modules/installation-obtaining-installer.adoc[leveloffset=+1]

include::modules/installation-initializing-manual.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../installing/installing_azure_stack_hub/installation-config-parameters-ash.adoc#installation-config-parameters-ash[Installation configuration parameters for Azure Stack Hub]

include::modules/installation-azure-stack-hub-config-yaml.adoc[leveloffset=+2]

include::modules/manually-create-identity-access-management.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_installing-azure-stack-hub-default-cco"]
.Additional resources
* xref:../../updating/preparing_for_updates/preparing-manual-creds-update.adoc#manually-maintained-credentials-upgrade_preparing-manual-creds-update[Updating cloud provider resources with manually maintained credentials]

include::modules/azure-stack-hub-internal-ca.adoc[leveloffset=+1]

include::modules/installation-launching-installer.adoc[leveloffset=+1]

include::modules/cli-installing-cli.adoc[leveloffset=+1]

include::modules/cli-logging-in-kubeadmin.adoc[leveloffset=+1]

include::modules/logging-in-by-using-the-web-console.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_installing-azure-stack-hub-default-console"]
.Additional resources
* xref:../../web_console/web-console.adoc#web-console[Accessing the web console]

include::modules/cluster-telemetry.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_installing-azure-stack-hub-default-telemetry"]
.Additional resources
* xref:../../support/remote_health_monitoring/about-remote-health-monitoring.adoc#about-remote-health-monitoring[About remote health monitoring]

[id="next-steps_installing-azure-stack-hub-default"]
== Next steps

* xref:../../installing/validating-an-installation.adoc#validating-an-installation[Validating an installation].
* xref:../../post_installation_configuration/cluster-tasks.adoc#available_cluster_customizations[Customize your cluster].
* If necessary, you can xref:../../support/remote_health_monitoring/opting-out-of-remote-health-reporting.adoc#opting-out-remote-health-reporting_opting-out-remote-health-reporting[opt out of remote health reporting].
* If necessary, you can xref:../../post_installation_configuration/cluster-tasks.adoc#manually-removing-cloud-creds_post-install-cluster-tasks[remove cloud provider credentials].
