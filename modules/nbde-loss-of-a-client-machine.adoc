// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-loss-of-a-client-machine_{context}"]
= Loss of a client machine

The loss of a cluster node that uses the Tang server to decrypt its disk partition is _not_ a disaster. Whether the machine was stolen, suffered hardware failure, or another loss scenario is not important: the disks are encrypted and considered unrecoverable.

However, in the event of theft, a precautionary rotation of the Tang server’s keys and rekeying of all remaining nodes would be prudent to ensure the disks remain unrecoverable even in the event the thieves subsequently gain access to the Tang servers.

To recover from this situation, either reinstall or replace the node.
