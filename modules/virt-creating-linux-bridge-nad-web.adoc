// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc
//This file contains UI elements and/or package names that need to be updated.

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-linux-bridge-nad-web_{context}"]
= Creating a Linux bridge NAD by using the web console

You can create a network attachment definition (NAD) to provide layer-2 networking to pods and virtual machines by using the {product-title} web console.

A Linux bridge network attachment definition is the most efficient method for connecting a virtual machine to a VLAN.

[WARNING]
====
Configuring IP address management (IPAM) in a network attachment definition for virtual machines is not supported.
====

.Procedure

. In the web console, click *Networking* -> *NetworkAttachmentDefinitions*.
. Click *Create Network Attachment Definition*.
+
[NOTE]
====
The network attachment definition must be in the same namespace as the pod or virtual machine.
====
+
. Enter a unique *Name* and optional *Description*.
. Select *CNV Linux bridge* from the *Network Type* list.
. Enter the name of the bridge in the *Bridge Name* field.
. Optional: If the resource has VLAN IDs configured, enter the ID numbers in the *VLAN Tag Number* field.
. Optional: Select *MAC Spoof Check* to enable MAC spoof filtering. This feature provides security against a MAC spoofing attack by allowing only a single MAC address to exit the pod.
. Click *Create*.