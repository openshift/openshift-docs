:_mod-docs-content-type: ASSEMBLY
[id="installing-azure-default"]
= Installing a cluster quickly on Azure
include::_attributes/common-attributes.adoc[]
:context: installing-azure-default

toc::[]

In {product-title} version {product-version}, you can install a cluster on
Microsoft Azure that uses the default configuration options.

== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.
* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].
* You xref:../../installing/installing_azure/installing-azure-account.adoc#installing-azure-account[configured an Azure account] to host the cluster and determined the tested and validated region to deploy the cluster to.
* If you use a firewall, you xref:../../installing/install_config/configuring-firewall.adoc#configuring-firewall[configured it to allow the sites] that your cluster requires access to.

include::modules/cluster-entitlements.adoc[leveloffset=+1]

include::modules/ssh-agent-using.adoc[leveloffset=+1]

include::modules/installation-obtaining-installer.adoc[leveloffset=+1]

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
