// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtAPIDown"]
= VirtAPIDown

[discrete]
[id="meaning-virtapidown"]
== Meaning

This alert fires when all the API Server pods are down.

[discrete]
[id="impact-virtapidown"]
== Impact

{VirtProductName} objects cannot send API calls.

[discrete]
[id="diagnosis-virtapidown"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the status of the `virt-api` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE get pods -l kubevirt.io=virt-api
----

. Check the status of the `virt-api` deployment:
+
[source,terminal]
----
$ oc -n $NAMESPACE get deploy virt-api -o yaml
----

. Check the `virt-api` deployment details for issues such as crashing pods or
image pull failures:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe deploy virt-api
----

. Check for issues such as nodes in a `NotReady` state:
+
[source,terminal]
----
$ oc get nodes
----

[discrete]
[id="mitigation-virtapidown"]
== Mitigation

Try to identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
