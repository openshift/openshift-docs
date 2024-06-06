// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-olm.adoc
// * operators/understanding/olm/olm-operatorconditions.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-about-operatorconditions_{context}"]
ifeval::["{context}" == "olm-understanding-olm"]
= Operator conditions
endif::[]
ifeval::["{context}" != "olm-understanding-olm"]
= About Operator conditions
endif::[]

As part of its role in managing the lifecycle of an Operator, Operator Lifecycle Manager (OLM) infers the state of an Operator from the state of Kubernetes resources that define the Operator. While this approach provides some level of assurance that an Operator is in a given state, there are many instances where an Operator might need to communicate information to OLM that could not be inferred otherwise. This information can then be used by OLM to better manage the lifecycle of the Operator.

OLM provides a custom resource definition (CRD) called `OperatorCondition` that allows Operators to communicate conditions to OLM. There are a set of supported conditions that influence management of the Operator by OLM when present in the `Spec.Conditions` array of an `OperatorCondition` resource.

[NOTE]
====
By default, the `Spec.Conditions` array is not present in an `OperatorCondition` object until it is either added by a user or as a result of custom Operator logic.
====
