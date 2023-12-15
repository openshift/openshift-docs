:_mod-docs-content-type: ASSEMBLY
[id="installing-with-ai"]
= Installing with the Assisted Installer
include::_attributes/common-attributes.adoc[]
:context: assisted-installer-installing

toc::[]

After you ensure the cluster nodes and network requirements are met, you can begin installing the cluster.

include::modules/assisted-installer-pre-installation-considerations.adoc[leveloffset=+1]

include::modules/assisted-installer-setting-the-cluster-details.adoc[leveloffset=+1]

include::modules/assisted-installer-configuring-host-network-interfaces.adoc[leveloffset=+1]

[role="_additional_resources"]
.Additional resources
* xref:../installing_bare_metal_ipi/ipi-install-installation-workflow.adoc#configuring-host-network-interfaces-in-the-install-config-yaml-file_ipi-install-installation-workflow[Configuring network interfaces]

* link:http://nmstate.io[NMState version 2.1.4]

include::modules/assisted-installer-adding-hosts-to-the-cluster.adoc[leveloffset=+1]

include::modules/installing-with-usb-media.adoc[leveloffset=+1]

include::modules/assisted-installer-booting-with-a-usb-drive.adoc[leveloffset=+1]

include::modules/install-booting-from-an-iso-over-http-redfish.adoc[leveloffset=+1]

[role="_additional_resources"]
.Additional resources

* xref:../installing_bare_metal_ipi/ipi-install-installation-workflow.adoc#bmc-addressing_ipi-install-installation-workflow[BMC addressing].

* xref:../installing_bare_metal_ipi/ipi-install-prerequisites.adoc#ipi-install-firmware-requirements-for-installing-with-virtual-media_ipi-install-prerequisites[Firmware requirements for installing with virtual media]

include::modules/assisted-installer-configuring-hosts.adoc[leveloffset=+1]

include::modules/assisted-installer-configuring-networking.adoc[leveloffset=+1]

include::modules/assisted-installer-installing-the-cluster.adoc[leveloffset=+1]

include::modules/assisted-installer-completing-the-installation.adoc[leveloffset=+1]


[role="_additional_resources"]
[id="ai-saas-installing-additional-resources_{context}"]
== Additional resources

* xref:../../cli_reference/openshift_cli/getting-started-cli.adoc#cli-installing-cli_cli-developer-commands[Installing the OpenShift CLI].

* xref:../../cli_reference/openshift_cli/getting-started-cli.adoc#cli-logging-in_cli-developer-commands[Logging in to the OpenShift CLI]

* xref:../../post_installation_configuration/preparing-for-users.adoc#creating-cluster-admin_post-install-preparing-for-users[Creating a cluster admin]

* xref:../../post_installation_configuration/preparing-for-users.adoc#removing-kubeadmin_post-install-preparing-for-users[Removing the kubeadmin user]
