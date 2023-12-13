// Module included in the following assemblies:
//
// * updating/index.adoc

:_mod-docs-content-type: CONCEPT
[id="understanding_clusteroperator_conditiontypes_{context}"]
= Understanding cluster Operator condition types

The status of cluster Operators includes their condition type, which informs you of the current state of your Operator's health. The following definitions cover a list of some common ClusterOperator condition types. Operators that have additional condition types and use Operator-specific language have been omitted.

The Cluster Version Operator (CVO) is responsible for collecting the status conditions from cluster Operators so that cluster administrators can better understand the state of the {product-title} cluster.

//Condition types, as well as additional information about your operator, can be retrieved in either YAML or JSON format through the `oc get clusterversion -o` command:

//[source,terminal]
//----
//$ oc get clusterversion -o yaml
//----


* Available:
The condition type `Available` indicates that an Operator is functional and available in the cluster. If the status is `False`, at least one part of the operand is non-functional and the condition requires an administrator to intervene.

* Progressing:
The condition type `Progressing` indicates that an Operator is actively rolling out new code, propagating configuration changes, or otherwise moving from one steady state to another.
+
Operators do not report the condition type `Progressing` as `True` when they are reconciling a previous known state. If the observed cluster state has changed and the Operator is reacting to it, then the status reports back as `True`, since it is moving from one steady state to another.
+
* Degraded:
The condition type `Degraded` indicates that an Operator has a current state that does not match its required state over a period of time. The period of time can vary by component, but a `Degraded` status represents persistent observation of an Operator's condition.  As a result, an Operator does not fluctuate in and out of the `Degraded` state.
+
There might be a different condition type if the transition from one state to another does not persist over a long enough period to report `Degraded`.
An Operator does not report `Degraded` during the course of a normal update.  An Operator may report `Degraded` in response to a persistent infrastructure failure that requires eventual administrator intervention.
+
[NOTE]
====
This condition type is only an indication that something may need investigation and adjustment. As long as the Operator is available, the `Degraded` condition does not cause user workload failure or application downtime.
====
+
* Upgradeable:
The condition type `Upgradeable` indicates whether the Operator is safe to update based on the current cluster state. The message field contains a human-readable description of what the administrator needs to do for the cluster to successfully update. The CVO allows updates when this condition is `True`, `Unknown` or missing.
+
When the `Upgradeable` status is `False`, only minor updates are impacted, and the CVO prevents the cluster from performing impacted updates unless forced.
