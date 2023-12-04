// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtApiRESTErrorsBurst"]
= VirtApiRESTErrorsBurst

[discrete]
[id="meaning-virtapiresterrorsburst"]
== Meaning

More than 80% of REST calls have failed in the `virt-api` pods in the last
5 minutes.

[discrete]
[id="impact-virtapiresterrorsburst"]
== Impact

A very high rate of failed REST calls to `virt-api` might lead to slow
response and execution of API calls, and potentially to API calls being
completely dismissed.

However, currently running virtual machine workloads are not likely to
be affected.

[discrete]
[id="diagnosis-virtapiresterrorsburst"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Obtain the list of `virt-api` pods on your deployment:
+
[source,terminal]
----
$ oc -n $NAMESPACE get pods -l kubevirt.io=virt-api
----

. Check the `virt-api` logs for error messages:
+
[source,terminal]
----
$ oc logs -n $NAMESPACE <virt-api>
----

. Obtain the details of the `virt-api` pods:
+
[source,terminal]
----
$ oc describe -n $NAMESPACE <virt-api>
----

. Check if any problems occurred with the nodes. For example, they might
be in a `NotReady` state:
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
[id="mitigation-virtapiresterrorsburst"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to
identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
