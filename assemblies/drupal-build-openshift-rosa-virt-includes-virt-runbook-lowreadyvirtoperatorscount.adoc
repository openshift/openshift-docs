// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-LowReadyVirtOperatorsCount"]
= LowReadyVirtOperatorsCount

[discrete]
[id="meaning-lowreadyvirtoperatorscount"]
== Meaning

This alert fires when one or more `virt-operator` pods are running, but
none of these pods has been in a `Ready` state for the last 10 minutes.

The `virt-operator` is the first Operator to start in a cluster. The `virt-operator`
deployment has a default replica of two `virt-operator` pods.

Its primary responsibilities include the following:

* Installing, live-updating, and live-upgrading a cluster
* Monitoring the lifecycle of top-level controllers, such as `virt-controller`,
`virt-handler`, `virt-launcher`, and managing their reconciliation
* Certain cluster-wide tasks, such as certificate rotation and infrastructure
management

[discrete]
[id="impact-lowreadyvirtoperatorscount"]
== Impact

A cluster-level failure might occur. Critical cluster-wide management
functionalities, such as certification rotation, upgrade, and reconciliation of
controllers, might become unavailable. Such a state also triggers the
`NoReadyVirtOperator` alert.

The `virt-operator` is not directly responsible for virtual machines (VMs)
in the cluster. Therefore, its temporary unavailability does not significantly
affect VM workloads.

[discrete]
[id="diagnosis-lowreadyvirtoperatorscount"]
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

. Obtain the details of the `virt-operator` deployment:
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
[id="mitigation-lowreadyvirtoperatorscount"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to
identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
