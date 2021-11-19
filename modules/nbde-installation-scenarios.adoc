// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-installation-scenarios_{context}"]
= Installation scenarios

Consider the following recommendations when planning Tang server installations:

* Small environments can use a single set of key material, even when using multiple Tang servers:
** Key rotations are easier.
** Tang servers can scale easily to permit high availability.

* Large environments can benefit from multiple sets of key material:
** Physically diverse installations do not require the copying and synchronizing of key material between geographic regions.
** Key rotations are more complex in large environments.
** Node installation and rekeying require network connectivity to all Tang servers.
** A small increase in network traffic can occur due to a booting node querying all Tang servers during decryption. Note that while only one Clevis client query must succeed, Clevis queries all Tang servers.

* Further complexity:
** Additional manual reconfiguration can permit the Shamir’s secret sharing (sss) of `any N of M servers online` in order to decrypt the disk partition.  Decrypting disks in this scenario requires multiple sets of key material, and manual management of Tang servers and nodes with Clevis clients after the initial installation.

* High level recommendations:
** For a single RAN deployment, a limited set of Tang servers can run in the corresponding domain controller (DC).
** For multiple RAN deployments, you must decide whether to run Tang servers in each corresponding DC or whether a global Tang environment better suits the other needs and requirements of the system.
