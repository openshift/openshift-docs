// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtOperatorDown"]
= VirtOperatorDown

[discrete]
[id="meaning-virtoperatordown"]
== Meaning

This alert fires when no `virt-operator` pod in the `Running` state has
been detected for 10 minutes.

The `virt-operator` is the first Operator to start in a cluster. Its primary
responsibilities include the following:

* Installing, live-updating, and live-upgrading a cluster
* Monitoring the life cycle of top-level controllers, such as `virt-controller`,
`virt-handler`, `virt-launcher`, and managing their reconciliation
* Certain cluster-wide tasks, such as certificate rotation and infrastructure
management

The `virt-operator` deployment has a default replica of 2 pods.

[discrete]
[id="impact-virtoperatordown"]
== Impact

This alert indicates a failure at the level of the cluster. Critical cluster-wide
management functionalities, such as certification rotation, upgrade, and
reconciliation of controllers, might not be available.

The `virt-operator` is not directly responsible for virtual machines (VMs)
in the cluster. Therefore, its temporary unavailability does not significantly
affect VM workloads.

[discrete]
[id="diagnosis-virtoperatordown"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the status of the `virt-operator` deployment:
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

. Check the status of the `virt-operator` pods:
+
[source,terminal]
----
$ oc get pods -n $NAMESPACE -l=kubevirt.io=virt-operator
----

. Check for node issues, such as a `NotReady` state:
+
[source,terminal]
----
$ oc get nodes
----

[discrete]
[id="mitigation-virtoperatordown"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to find
the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
