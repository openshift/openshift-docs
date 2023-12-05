:_mod-docs-content-type: ASSEMBLY
[id="uninstalling-sriov-operator"]
= Uninstalling the SR-IOV Network Operator
include::_attributes/common-attributes.adoc[]
:context: uninstalling-sr-iov-operator

toc::[]

To uninstall the SR-IOV Network Operator, you must delete any running SR-IOV workloads, uninstall the Operator, and delete the webhooks that the Operator used.

include::modules/nw-sriov-operator-uninstall.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../operators/admin/olm-deleting-operators-from-cluster.adoc#olm-deleting-operators-from-a-cluster[Deleting Operators from a cluster]
