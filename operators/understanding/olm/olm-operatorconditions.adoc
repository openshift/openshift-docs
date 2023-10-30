:_mod-docs-content-type: ASSEMBLY
[id="olm-operatorconditions"]
= Operator conditions
include::_attributes/common-attributes.adoc[]
:context: olm-operatorconditions

toc::[]

This guide outlines how Operator Lifecycle Manager (OLM) uses Operator conditions.

include::modules/olm-operatorconditions-about.adoc[leveloffset=+1]
include::modules/olm-supported-operatorconditions.adoc[leveloffset=+1]

[id="olm-operatorconditions-addtl-resources"]
[role="_additional-resources"]
== Additional resources

* xref:../../../operators/admin/olm-managing-operatorconditions.adoc#olm-operatorconditions[Managing Operator conditions]
* xref:../../../operators/operator_sdk/osdk-generating-csvs.adoc#osdk-operatorconditions_osdk-generating-csvs[Enabling Operator conditions]
// The following xrefs point to topics that are not currently included in the OSD/ROSA docs.
ifndef::openshift-dedicated,openshift-rosa[]
* xref:../../../nodes/pods/nodes-pods-configuring.adoc#nodes-pods-configuring-pod-distruption-about_nodes-pods-configuring[Using pod disruption budgets to specify the number of pods that must be up]
* xref:../../../applications/deployments/route-based-deployment-strategies.adoc#deployments-graceful-termination_route-based-deployment-strategies[Graceful termination]
endif::openshift-dedicated,openshift-rosa[]
