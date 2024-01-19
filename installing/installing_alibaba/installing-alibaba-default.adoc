:_mod-docs-content-type: ASSEMBLY
[id="installing-alibaba-default"]
= Installing a cluster quickly on Alibaba Cloud
include::_attributes/common-attributes.adoc[]
:context: installing-alibaba-default

toc::[]

In {product-title} version {product-version}, you can install a cluster on
Alibaba Cloud that uses the default configuration options.

:FeatureName: Alibaba Cloud on {product-title}
include::snippets/technology-preview.adoc[]

[id="prerequisites_installing-alibaba-default"]
== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.
* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].
* You xref:../../installing/installing_alibaba/preparing-to-install-on-alibaba.adoc#installation-alibaba-dns_preparing-to-install-on-alibaba[registered your domain].
* If you use a firewall, you xref:../../installing/install_config/configuring-firewall.adoc#configuring-firewall[configured it to allow the sites] that your cluster requires access to.
* You have xref:../../installing/installing_alibaba/manually-creating-alibaba-ram.adoc#manually-creating-alibaba-ram[created the required Alibaba Cloud resources].
* If the cloud Resource Access Management (RAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the kube-system namespace, you can xref:../../installing/installing_alibaba/manually-creating-alibaba-ram.adoc#manually-creating-alibaba-ram[manually create and maintain Resource Access Management (RAM) credentials].

include::modules/cluster-entitlements.adoc[leveloffset=+1]

include::modules/ssh-agent-using.adoc[leveloffset=+1]

include::modules/installation-obtaining-installer.adoc[leveloffset=+1]

include::modules/installation-initializing.adoc[leveloffset=+1]

include::modules/manually-creating-alibaba-manifests.adoc[leveloffset=+1]

include::modules/cco-ccoctl-creating-at-once.adoc[leveloffset=+1]

include::modules/installation-launching-installer.adoc[leveloffset=+1]

include::modules/cli-installing-cli.adoc[leveloffset=+1]

include::modules/cli-logging-in-kubeadmin.adoc[leveloffset=+1]

include::modules/logging-in-by-using-the-web-console.adoc[leveloffset=+1]

include::modules/cluster-telemetry.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* See xref:../../web_console/web-console.adoc#web-console[Accessing the web console] for more details about accessing and understanding the {product-title} web console.
* See xref:../../support/remote_health_monitoring/about-remote-health-monitoring.adoc#about-remote-health-monitoring[About remote health monitoring] for more information about the Telemetry service

[id="next-steps_installing-alibaba-default"]
== Next steps

* xref:../../installing/validating-an-installation.adoc#validating-an-installation[Validating an installation].
* xref:../../post_installation_configuration/cluster-tasks.adoc#available_cluster_customizations[Customize your cluster].
* If necessary, you can xref:../../support/remote_health_monitoring/opting-out-of-remote-health-reporting.adoc#opting-out-remote-health-reporting_opting-out-remote-health-reporting[opt out of remote health reporting].
//Given that manual mode is required to install on Alibaba Cloud, I do not believe this xref is necessary.
//* If necessary, you can xref:../../post_installation_configuration/cluster-tasks.adoc#manually-removing-cloud-creds_post-install-cluster-tasks[remove cloud provider credentials]
