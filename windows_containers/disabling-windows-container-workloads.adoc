:_mod-docs-content-type: ASSEMBLY
[id="disabling-windows-container-workloads"]
= Disabling Windows container workloads
include::_attributes/common-attributes.adoc[]
:context: disabling-windows-container-workloads

toc::[]

You can disable the capability to run Windows container workloads by uninstalling the Windows Machine Config Operator (WMCO) and deleting the namespace that was added by default when you installed the WMCO.

include::modules/uninstalling-wmco.adoc[leveloffset=+1]

include::modules/deleting-wmco-namespace.adoc[leveloffset=+1]

[discrete]
[role="_additional-resources"]
== Additional resources

* xref:../operators/admin/olm-deleting-operators-from-cluster.adoc#olm-deleting-operators-from-a-cluster[Deleting Operators from a cluster]
* xref:../windows_containers/removing-windows-nodes.adoc#removing-windows-nodes[Removing Windows nodes]
