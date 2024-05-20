:_mod-docs-content-type: ASSEMBLY
[id="olm-managing-operatorconditions"]
= Managing Operator conditions
include::_attributes/common-attributes.adoc[]
:context: olm-managing-operatorconditions

toc::[]

ifndef::openshift-dedicated,openshift-rosa[]
As a cluster administrator, you can manage Operator conditions by using Operator Lifecycle Manager (OLM).
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
As an administrator with the `dedicated-admin` role, you can manage Operator conditions by using Operator Lifecycle Manager (OLM).
endif::openshift-dedicated,openshift-rosa[]

include::modules/olm-overriding-operatorconditions.adoc[leveloffset=+1]
include::modules/olm-updating-use-operatorconditions.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="olm-managing-operatorconditions-addtl-resources"]
== Additional resources

* xref:../../operators/understanding/olm/olm-operatorconditions.adoc#olm-operatorconditions[Operator conditions]
