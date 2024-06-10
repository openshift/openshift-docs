// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtHandlerRESTErrorsBurst"]
= VirtHandlerRESTErrorsBurst

[discrete]
[id="meaning-virthandlerresterrorsburst"]
== Meaning

More than 80% of REST calls failed in `virt-handler` in the last 5 minutes.
This alert usually indicates that the `virt-handler` pods cannot connect
to the API server.

This error is frequently caused by one of the following problems:

* The API server is overloaded, which causes timeouts. To verify if this
is the case, check the metrics of the API server, and view its response
times and overall calls.
* The `virt-handler` pod cannot reach the API server. This is commonly
caused by DNS issues on the node and networking connectivity issues.

[discrete]
[id="impact-virthandlerresterrorsburst"]
== Impact

Status updates are not propagated and node-related actions, such as migrations,
fail. However, running workloads on the affected node are not impacted.

[discrete]
[id="diagnosis-virthandlerresterrorsburst"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the status of the `virt-handler` pod:
+
[source,terminal]
----
$ oc get pods -n $NAMESPACE -l=kubevirt.io=virt-handler
----

. Check the `virt-handler` logs for error messages when connecting to
the API server:
+
[source,terminal]
----
$ oc logs -n  $NAMESPACE <virt-handler>
----

[discrete]
[id="mitigation-virthandlerresterrorsburst"]
== Mitigation

* If the `virt-handler` cannot connect to the API server, delete the pod
to force a restart:
+
[source,terminal]
----
$ oc delete -n $NAMESPACE <virt-handler>
----

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
