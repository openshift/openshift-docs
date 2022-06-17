// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-loss-of-a-network-segment_{context}"]
= Loss of a network segment

The loss of a network segment, making a Tang server temporarily unavailable, has the following consequences:

* {product-title} nodes continue to boot as normal, provided other servers are available.

* New nodes cannot establish their encryption keys until the network segment is restored. In this case, ensure connectivity to remote geographic locations for the purposes of high availability and redundancy. This is because when you are installing a new node or rekeying an existing node, all of the Tang servers you are referencing in that operation must be available.

A hybrid model for a vastly diverse network, such as five geographic regions in which each client is connected to the closest three clients is worth investigating.

In this scenario, new clients are able to establish their encryption keys with the subset of servers that are reachable. For example, in the set of `tang1`, `tang2` and `tang3` servers, if `tang2` becomes unreachable clients can still establish their encryption keys with `tang1` and `tang3`, and at a later time re-establish with the full set. This can involve either a manual intervention or a more complex automation to be available.
