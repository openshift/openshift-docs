// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtApiRESTErrorsHigh"]
= VirtApiRESTErrorsHigh

[discrete]
[id="meaning-virtapiresterrorshigh"]
== Meaning

More than 5% of REST calls have failed in the `virt-api` pods in the last 60 minutes.

[discrete]
[id="impact-virtapiresterrorshigh"]
== Impact

A high rate of failed REST calls to `virt-api` might lead to slow response and
execution of API calls.

However, currently running virtual machine workloads are not likely to be affected.

[discrete]
[id="diagnosis-virtapiresterrorshigh"]
== Diagnosis

. Set the `NAMESPACE` environment variable as follows:
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

. Check the `virt-api` logs:
+
[source,terminal]
----
$ oc logs -n  $NAMESPACE <virt-api>
----

. Obtain the details of the `virt-api` pods:
+
[source,terminal]
----
$ oc describe -n $NAMESPACE <virt-api>
----

. Check if any problems occurred with the nodes. For example, they might be in
a `NotReady` state:
+
[source,terminal]
----
$ oc get nodes
----

. Check the status of the `virt-api` deployment:
+
[source,terminal]
----
$ oc -n $NAMESPACE get deploy virt-api -o yaml
----

. Obtain the details of the `virt-api` deployment:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe deploy virt-api
----

[discrete]
[id="mitigation-virtapiresterrorshigh"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to
identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
