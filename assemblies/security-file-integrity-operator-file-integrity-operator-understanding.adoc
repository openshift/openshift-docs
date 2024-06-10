:_mod-docs-content-type: ASSEMBLY
[id="understanding-file-integrity-operator"]
= Understanding the File Integrity Operator
include::_attributes/common-attributes.adoc[]
:context: file-integrity-operator

toc::[]

The File Integrity Operator is an {product-title} Operator that continually runs file integrity checks on the cluster nodes. It deploys a daemon set that initializes and runs privileged advanced intrusion detection environment (AIDE) containers on each node, providing a status object with a log of files that are modified during the initial run of the daemon set pods.

[IMPORTANT]
====
Currently, only {op-system-first} nodes are supported.
====

include::modules/file-integrity-understanding-file-integrity-cr.adoc[leveloffset=+1]
include::modules/checking-file-intergrity-cr-status.adoc[leveloffset=+1]
include::modules/file-integrity-CR-phases.adoc[leveloffset=+1]
include::modules/file-integrity-understanding-file-integrity-node-statuses-object.adoc[leveloffset=+1]
include::modules/file-integrity-node-status.adoc[leveloffset=+1]
include::modules/file-integrity-node-status-success.adoc[leveloffset=+2]
include::modules/file-integrity-node-status-failure.adoc[leveloffset=+2]
include::modules/file-integrity-events.adoc[leveloffset=+1]
