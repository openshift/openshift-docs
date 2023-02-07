// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-unexpected-loss-of-network-connectivity_{context}"]
= Unexpected loss of network connectivity

If the network disruption is unexpected and a node reboots, consider the following scenarios:

* If any nodes are still online, ensure that they do not reboot until network connectivity is restored. This is not applicable for single-node clusters.
* The node will remain offline until such time that either network connectivity is restored, or a pre-established passphrase is entered manually at the console. In exceptional circumstances, network administrators might be able to reconfigure network segments to reestablish access, but this is counter to the intent of NBDE, which is that lack of network access means lack of ability to boot.
* The lack of network access at the node can reasonably be expected to impact that node’s ability to function as well as its ability to boot. Even if the node were to boot via manual intervention, the lack of network access would make it effectively useless.
