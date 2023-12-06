:_mod-docs-content-type: ASSEMBLY
[id="virt-connecting-vm-to-linux-bridge"]
= Connecting a virtual machine to a Linux bridge network
include::_attributes/common-attributes.adoc[]
:context: virt-connecting-vm-to-linux-bridge

toc::[]

By default, {VirtProductName} is installed with a single, internal pod network.

You can create a Linux bridge network and attach a virtual machine (VM) to the network by performing the following steps:

. xref:../../virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc#virt-creating-linux-bridge-nncp_virt-connecting-vm-to-linux-bridge[Create a Linux bridge node network configuration policy (NNCP)].
. Create a Linux bridge network attachment definition (NAD) by using the xref:../../virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc#virt-creating-linux-bridge-nad-web_virt-connecting-vm-to-linux-bridge[web console] or the xref:../../virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc#virt-creating-linux-bridge-nad-cli_virt-connecting-vm-to-linux-bridge[command line].
. Configure the VM to recognize the NAD by using the xref:../../virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc#virt-vm-creating-nic-web_virt-connecting-vm-to-linux-bridge[web console] or the xref:../../virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc#virt-attaching-vm-secondary-network-cli_virt-connecting-vm-to-linux-bridge[command line].

include::modules/virt-creating-linux-bridge-nncp.adoc[leveloffset=+1]

[id="creating-linux-bridge-nad"]
== Creating a Linux bridge NAD

You can create a Linux bridge network attachment definition (NAD) by using the {product-title} web console or command line.

include::modules/virt-creating-linux-bridge-nad-web.adoc[leveloffset=+2]

include::modules/virt-creating-linux-bridge-nad-cli.adoc[leveloffset=+2]

[id="configuring-vm-network-interface"]
== Configuring a VM network interface

You can configure a virtual machine (VM) network interface by using the {product-title} web console or command line.

include::modules/virt-vm-creating-nic-web.adoc[leveloffset=+2]

[discrete]
include::modules/virt-networking-wizard-fields-web.adoc[leveloffset=+3]

include::modules/virt-attaching-vm-secondary-network-cli.adoc[leveloffset=+2]
