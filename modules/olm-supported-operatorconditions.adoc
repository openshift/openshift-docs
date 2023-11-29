// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-operatorconditions.adoc

[id="olm-supported-operatorconditions_{context}"]
= Supported conditions

Operator Lifecycle Manager (OLM) supports the following Operator conditions.

[id="olm-upgradeable-operatorcondition_{context}"]
== Upgradeable condition

The `Upgradeable` Operator condition prevents an existing cluster service version (CSV) from being replaced by a newer version of the CSV. This condition is useful when:

* An Operator is about to start a critical process and should not be upgraded until the process is completed.
* An Operator is performing a migration of custom resources (CRs) that must be completed before the Operator is ready to be upgraded.

[IMPORTANT]
====
Setting the `Upgradeable` Operator condition to the `False` value does not avoid pod disruption. If you must ensure your pods are not disrupted, see "Using pod disruption budgets to specify the number of pods that must be up" and "Graceful termination" in the "Additional resources" section.
====

.Example `Upgradeable` Operator condition
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorCondition
metadata:
  name: my-operator
  namespace: operators
spec:
  conditions:
  - type: Upgradeable <1>
    status: "False" <2>
    reason: "migration"
    message: "The Operator is performing a migration."
    lastTransitionTime: "2020-08-24T23:15:55Z"
----
<1> Name of the condition.
<2> A `False` value indicates the Operator is not ready to be upgraded. OLM prevents a CSV that replaces the existing CSV of the Operator from leaving the `Pending` phase. A `False` value does not block cluster upgrades.
