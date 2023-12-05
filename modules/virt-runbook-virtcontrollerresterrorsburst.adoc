// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtControllerRESTErrorsBurst"]
= VirtControllerRESTErrorsBurst

[discrete]
[id="meaning-virtcontrollerresterrorsburst"]
== Meaning

More than 80% of REST calls in `virt-controller` pods failed in the last 5
minutes.

The `virt-controller` has likely fully lost the connection to the API server.

This error is frequently caused by one of the following problems:

* The API server is overloaded, which causes timeouts. To verify if this is
the case, check the metrics of the API server, and view its response times and
overall calls.
* The `virt-controller` pod cannot reach the API server. This is commonly
caused by DNS issues on the node and networking connectivity issues.

[discrete]
[id="impact-virtcontrollerresterrorsburst"]
== Impact

Status updates are not propagated and actions like migrations cannot take place.
However, running workloads are not impacted.

[discrete]
[id="diagnosis-virtcontrollerresterrorsburst"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. List the available `virt-controller` pods:
+
[source,terminal]
----
$ oc get pods -n $NAMESPACE -l=kubevirt.io=virt-controller
----

. Check the `virt-controller` logs for error messages when connecting to the
API server:
+
[source,terminal]
----
$ oc logs -n  $NAMESPACE <virt-controller>
----

[discrete]
[id="mitigation-virtcontrollerresterrorsburst"]
== Mitigation

* If the `virt-controller` pod cannot connect to the API server, delete the
pod to force a restart:
+
[source,terminal]
----
$ oc delete -n $NAMESPACE <virt-controller>
----

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
