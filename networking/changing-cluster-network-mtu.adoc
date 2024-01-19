:_mod-docs-content-type: ASSEMBLY
[id="changing-cluster-network-mtu"]
= Changing the MTU for the cluster network
include::_attributes/common-attributes.adoc[]
:context: changing-cluster-network-mtu

toc::[]

[role="_abstract"]
As a cluster administrator, you can change the MTU for the cluster network after cluster installation. This change is disruptive as cluster nodes must be rebooted to finalize the MTU change. You can change the MTU only for clusters using the OVN-Kubernetes or OpenShift SDN network plugins.

include::modules/nw-cluster-mtu-change-about.adoc[leveloffset=+1]
include::modules/nw-cluster-mtu-change.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="{context}-additional-resources"]
== Additional resources

* xref:../installing/installing_bare_metal/installing-bare-metal.adoc#installation-user-infra-machines-advanced_network_installing-bare-metal[Using advanced networking options for PXE and ISO installations]
* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/configuring_and_managing_networking/index#proc_manually-creating-a-networkmanager-profile-in-keyfile-format_assembly_networkmanager-connection-profiles-in-keyfile-format[Manually creating NetworkManager profiles in key file format]
* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/configuring_and_managing_networking/index#configuring-a-dynamic-ethernet-connection-using-nmcli_configuring-an-ethernet-connection[Configuring a dynamic Ethernet connection using nmcli]
