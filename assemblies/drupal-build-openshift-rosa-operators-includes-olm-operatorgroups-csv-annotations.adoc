// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-operatorgroups.adoc

[id="olm-operatorgroups-csv-annotations_{context}"]
= Operator group CSV annotations

Member CSVs of an Operator group have the following annotations:

[cols="1,1",options="header"]
|===
|Annotation |Description

|`olm.operatorGroup=<group_name>`
|Contains the name of the Operator group.

|`olm.operatorNamespace=<group_namespace>`
|Contains the namespace of the Operator group.

|`olm.targetNamespaces=<target_namespaces>`
|Contains a comma-delimited string that lists the target namespace selection of the Operator group.
|===

[NOTE]
====
All annotations except `olm.targetNamespaces` are included with copied CSVs. Omitting the `olm.targetNamespaces` annotation on copied CSVs prevents the duplication of target namespaces between tenants.
====
