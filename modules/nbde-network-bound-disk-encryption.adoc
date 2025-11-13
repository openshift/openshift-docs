// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-network-bound-disk-encryption_{context}"]
= Network-Bound Disk Encryption (NBDE)

Network-Bound Disk Encryption (NBDE) effectively ties the encryption key to an external server or set of servers in a secure and anonymous way across the network. This is not a key escrow, in that the nodes do not store the encryption key or transfer it over the network, but otherwise behaves in a similar fashion.

Clevis and Tang are generic client and server components that provide network-bound encryption. {op-system-first}
uses these components in conjunction with Linux Unified Key Setup-on-disk-format (LUKS) to encrypt and decrypt root and non-root storage volumes to accomplish
Network-Bound Disk Encryption.

When a node starts, it attempts to contact a predefined set of Tang servers by performing a cryptographic handshake. If it can reach the required number of Tang servers, the node can construct its disk decryption key and unlock the disks to continue booting. If the node cannot access a Tang server due to a network outage or server unavailability, the node cannot boot and continues retrying indefinitely until the Tang servers become available again. Because the key is effectively tied to the node’s presence in a network, an attacker attempting to gain access to the data at rest would need to obtain both the disks on the node, and  network access to the Tang server as well.

The following figure illustrates the deployment model for NBDE.

image::179_OpenShift_NBDE_implementation_0821_1.png[NBDE deployment model]

The following figure illustrates NBDE behavior during a reboot.

image::179_OpenShift_NBDE_implementation_0821_2.png[NBDE reboot behavior]
