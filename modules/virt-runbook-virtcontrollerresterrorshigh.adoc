// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtControllerRESTErrorsHigh"]
= VirtControllerRESTErrorsHigh

[discrete]
[id="meaning-virtcontrollerresterrorshigh"]
== Meaning

More than 5% of REST calls failed in `virt-controller` in the last 60 minutes.

This is most likely because `virt-controller` has partially lost connection
to the API server.

This error is frequently caused by one of the following problems:

* The API server is overloaded, which causes timeouts. To verify if this
is the case, check the metrics of the API server, and view its response
times and overall calls.
* The `virt-controller` pod cannot reach the API server. This is commonly
caused by DNS issues on the node and networking connectivity issues.

[discrete]
[id="impact-virtcontrollerresterrorshigh"]
== Impact

Node-related actions, such as starting and migrating, and scheduling virtual
machines, are delayed. Running workloads are not affected, but reporting
their current status might be delayed.

[discrete]
[id="diagnosis-virtcontrollerresterrorshigh"]
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

. Check the `virt-controller` logs for error messages when connecting
to the API server:
+
[source,terminal]
----
$ oc logs -n  $NAMESPACE <virt-controller>
----

[discrete]
[id="mitigation-virtcontrollerresterrorshigh"]
== Mitigation

* If the `virt-controller` pod cannot connect to the API server, delete
the pod to force a restart:
+
[source,terminal]
----
$ oc delete -n $NAMESPACE <virt-controller>
----

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
