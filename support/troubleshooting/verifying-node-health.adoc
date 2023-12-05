:_mod-docs-content-type: ASSEMBLY
[id="verifying-node-health"]
= Verifying node health
include::_attributes/common-attributes.adoc[]
:context: verifying-node-health

toc::[]

// Reviewing node status, resource usage, and configuration
include::modules/reviewing-node-status-usage-and-configuration.adoc[leveloffset=+1]

// cannot create resource "namespaces"
ifndef::openshift-rosa,openshift-dedicated[]
// Querying the kubelet's status on a node
include::modules/querying-kubelet-status-on-a-node.adoc[leveloffset=+1]

// cannot get resource "nodes/proxy"
// Querying node journal logs
include::modules/querying-cluster-node-journal-logs.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]

