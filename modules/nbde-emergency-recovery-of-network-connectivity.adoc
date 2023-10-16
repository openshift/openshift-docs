// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-emergency-recovery-of-network-connectivity_{context}"]
= Emergency recovery of network connectivity

If you are unable to recover network connectivity manually, consider the following steps. Be aware that these steps are discouraged if other methods to recover network connectivity are available.

* This method must only be performed by a highly trusted technician.
* Taking the Tang server’s key material to the remote site is considered to be a breach of the key material and all servers must be rekeyed and re-encrypted.
* This method must be used in extreme cases only, or as a proof of concept recovery method to demonstrate its viability.
* Equally extreme, but theoretically possible, is to power the server in question with an Uninterruptible Power Supply (UPS), transport the server to a location with network connectivity to boot and decrypt the disks, and then restore the server at the original location on battery power to continue operation.
* If you want to use a backup manual passphrase, you must create it before the failure situation occurs.
* Just as attack scenarios become more complex with TPM and Tang compared to a stand-alone Tang installation, so emergency disaster recovery processes are also made more complex if leveraging the same method.
