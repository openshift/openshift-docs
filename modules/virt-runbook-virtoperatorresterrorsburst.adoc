// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtOperatorRESTErrorsBurst"]
= VirtOperatorRESTErrorsBurst

[discrete]
[id="meaning-virtoperatorresterrorsburst"]
== Meaning

This alert fires when more than 80% of the REST calls in the `virt-operator`
pods failed in the last 5 minutes. This usually indicates that the `virt-operator`
pods cannot connect to the API server.

This error is frequently caused by one of the following problems:

* The API server is overloaded, which causes timeouts. To verify if this is
the case, check the metrics of the API server, and view its response times and
overall calls.
* The `virt-operator` pod cannot reach the API server. This is commonly caused
by DNS issues on the node and networking connectivity issues.

[discrete]
[id="impact-virtoperatorresterrorsburst"]
== Impact

Cluster-level actions, such as upgrading and controller reconciliation, might
not be available.

However, workloads such as virtual machines (VMs) and VM instances
(VMIs) are not likely to be affected.

[discrete]
[id="diagnosis-virtoperatorresterrorsburst"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the status of the `virt-operator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE get pods -l kubevirt.io=virt-operator
----

. Check the `virt-operator` logs for error messages when connecting to the
API server:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs <virt-operator>
----

. Obtain the details of the `virt-operator` pod:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe pod <virt-operator>
----

[discrete]
[id="mitigation-virtoperatorresterrorsburst"]
== Mitigation

* If the `virt-operator` pod cannot connect to the API server, delete the pod
to force a restart:
+
[source,terminal]
----
$ oc delete -n $NAMESPACE <virt-operator>
----

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
