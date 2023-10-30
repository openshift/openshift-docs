// Module included in the following assemblies:
//
// * operators/admin/olm-managing-operatorconditions.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-supported-operatorconditions_{context}"]
= Overriding Operator conditions

ifndef::openshift-dedicated,openshift-rosa[]
As a cluster administrator,
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
As an administrator with the `dedicated-admin` role,
endif::openshift-dedicated,openshift-rosa[]
you might want to ignore a supported Operator condition reported by an Operator. When present, Operator conditions in the `Spec.Overrides` array override the conditions in the `Spec.Conditions` array, allowing
ifndef::openshift-dedicated,openshift-rosa[]
cluster administrators
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
`dedicated-admin` administrators
endif::openshift-dedicated,openshift-rosa[]
to deal with situations where an Operator is incorrectly reporting a state to Operator Lifecycle Manager (OLM).

[NOTE]
====
By default, the `Spec.Overrides` array is not present in an `OperatorCondition` object until it is added by
ifndef::openshift-dedicated,openshift-rosa[]
a cluster administrator
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
an administrator with the `dedicated-admin` role
endif::openshift-dedicated,openshift-rosa[]
. The `Spec.Conditions` array is also not present until it is either added by a user or as a result of custom Operator logic.
====

For example, consider a known version of an Operator that always communicates that it is not upgradeable. In this instance, you might want to upgrade the Operator despite the Operator communicating that it is not upgradeable. This could be accomplished by overriding the Operator condition by adding the condition `type` and `status` to the `Spec.Overrides` array in the `OperatorCondition` object.

.Prerequisites

ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]
* An Operator with an `OperatorCondition` object, installed using OLM.

.Procedure

. Edit the `OperatorCondition` object for the Operator:
+
[source,terminal]
----
$ oc edit operatorcondition <name>
----

. Add a `Spec.Overrides` array to the object:
+
.Example Operator condition override
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorCondition
metadata:
  name: my-operator
  namespace: operators
spec:
  overrides:
  - type: Upgradeable <1>
    status: "True"
    reason: "upgradeIsSafe"
    message: "This is a known issue with the Operator where it always reports that it cannot be upgraded."
  conditions:
  - type: Upgradeable
    status: "False"
    reason: "migration"
    message: "The operator is performing a migration."
    lastTransitionTime: "2020-08-24T23:15:55Z"
----
ifndef::openshift-dedicated,openshift-rosa[]
<1> Allows the cluster administrator to change the upgrade readiness to `True`.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
<1> Allows the `dedicated-admin` user to change the upgrade readiness to `True`.
endif::openshift-dedicated,openshift-rosa[]
