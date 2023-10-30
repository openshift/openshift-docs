// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-NoReadyVirtOperator"]
= NoReadyVirtOperator

[discrete]
[id="meaning-noreadyvirtoperator"]
== Meaning

This alert fires when no `virt-operator` pod in a `Ready` state has been
detected for 10 minutes.

The `virt-operator` is the first Operator to start in a cluster. Its primary
responsibilities include the following:

* Installing, live-updating, and live-upgrading a cluster
* Monitoring the life cycle of top-level controllers, such as `virt-controller`,
`virt-handler`, `virt-launcher`, and managing their reconciliation
* Certain cluster-wide tasks, such as certificate rotation and infrastructure
management

The default deployment is two `virt-operator` pods.

[discrete]
[id="impact-noreadyvirtoperator"]
== Impact

This alert indicates a cluster-level failure. Critical cluster management
functionalities, such as certification rotation, upgrade, and reconciliation
of controllers, might not be not available.

The `virt-operator` is not directly responsible for virtual machines in
the cluster. Therefore, its temporary unavailability does not significantly
affect workloads.

[discrete]
[id="diagnosis-noreadyvirtoperator"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Obtain the name of the `virt-operator` deployment:
+
[source,terminal]
----
$ oc -n $NAMESPACE get deploy virt-operator -o yaml
----

. Generate the description of the `virt-operator` deployment:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe deploy virt-operator
----

. Check for node issues, such as a `NotReady` state:
+
[source,terminal]
----
$ oc get nodes
----

[discrete]
[id="mitigation-noreadyvirtoperator"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to
identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the link:https://access.redhat.com[Customer Portal]
and open a support case, attaching the artifacts gathered during the Diagnosis
procedure.
