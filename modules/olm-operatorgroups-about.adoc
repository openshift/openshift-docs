// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-olm.adoc
// * operators/understanding/olm/olm-understanding-operatorgroups.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-operatorgroups-about_{context}"]
ifeval::["{context}" == "olm-understanding-olm"]
= Operator groups
endif::[]
ifeval::["{context}" != "olm-understanding-olm"]
= About Operator groups
endif::[]

An _Operator group_, defined by the `OperatorGroup` resource, provides multitenant configuration to OLM-installed Operators. An Operator group selects target namespaces in which to generate required RBAC access for its member Operators.

The set of target namespaces is provided by a comma-delimited string stored in the `olm.targetNamespaces` annotation of a cluster service version (CSV). This annotation is applied to the CSV instances of member Operators and is projected into their deployments.
