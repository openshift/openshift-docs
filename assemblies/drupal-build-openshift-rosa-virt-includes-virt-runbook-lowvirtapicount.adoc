// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-LowVirtAPICount"]
= LowVirtAPICount

[discrete]
[id="meaning-lowvirtapicount"]
== Meaning

This alert fires when only one available `virt-api` pod is detected during a
60-minute period, although at least two nodes are available for scheduling.

[discrete]
[id="impact-lowvirtapicount"]
== Impact

An API call outage might occur during node eviction because the `virt-api` pod
becomes a single point of failure.

[discrete]
[id="diagnosis-lowvirtapicount"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the number of available `virt-api` pods:
+
[source,terminal]
----
$ oc get deployment -n $NAMESPACE virt-api \
  -o jsonpath='{.status.readyReplicas}'
----

. Check the status of the `virt-api` deployment for error conditions:
+
[source,terminal]
----
$ oc -n $NAMESPACE get deploy virt-api -o yaml
----

. Check the nodes for issues such as nodes in a `NotReady` state:
+
[source,terminal]
----
$ oc get nodes
----

[discrete]
[id="mitigation-lowvirtapicount"]
== Mitigation

Try to identify the root cause and to resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
