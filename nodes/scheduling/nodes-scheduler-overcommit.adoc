:_mod-docs-content-type: ASSEMBLY
:context: nodes-scheduler-overcommit
[id="nodes-scheduler-overcommit"]
= Placing pods onto overcommited nodes
include::_attributes/common-attributes.adoc[]

toc::[]






In an _overcommited_ state, the sum of the container compute resource requests and limits exceeds the resources available on the system.
Overcommitment might be desirable in development environments where a trade-off of guaranteed performance for capacity is acceptable.

Requests and limits enable administrators to allow and manage the overcommitment of resources on a node.
The scheduler uses requests for scheduling your container and providing a minimum service guarantee.
Limits constrain the amount of compute resource that may be consumed on your node.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.


include::modules/nodes-cluster-overcommit-about.adoc[leveloffset=+1]

include::modules/nodes-cluster-overcommit-configure-nodes.adoc[leveloffset=+1]
