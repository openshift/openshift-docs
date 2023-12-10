// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtHandlerRESTErrorsHigh"]
= VirtHandlerRESTErrorsHigh

[discrete]
[id="meaning-virthandlerresterrorshigh"]
== Meaning

More than 5% of REST calls failed in `virt-handler` in the last 60 minutes.
This alert usually indicates that the `virt-handler` pods have partially
lost connection to the API server.

This error is frequently caused by one of the following problems:

* The API server is overloaded, which causes timeouts. To verify if this
is the case, check the metrics of the API server, and view its response
times and overall calls.
* The `virt-handler` pod cannot reach the API server. This is commonly
caused by DNS issues on the node and networking connectivity issues.

[discrete]
[id="impact-virthandlerresterrorshigh"]
== Impact

Node-related actions, such as starting and migrating workloads, are delayed
on the node that `virt-handler` is running on. Running workloads are not
affected, but reporting their current status might be delayed.

[discrete]
[id="diagnosis-virthandlerresterrorshigh"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. List the available `virt-handler` pods to identify the failing
`virt-handler` pod:
+
[source,terminal]
----
$ oc get pods -n $NAMESPACE -l=kubevirt.io=virt-handler
----

. Check the failing `virt-handler` pod log for API server
connectivity errors:
+
[source,terminal]
----
$ oc logs -n $NAMESPACE <virt-handler>
----
+
Example error message:
+
[source,json]
----
{"component":"virt-handler","level":"error","msg":"Can't patch node my-node","pos":"heartbeat.go:96","reason":"the server has received too many API requests and has asked us to try again later","timestamp":"2023-11-06T11:11:41.099883Z","uid":"132c50c2-8d82-4e49-8857-dc737adcd6cc"}
----

[discrete]
[id="mitigation-virthandlerresterrorshigh"]
== Mitigation

Delete the pod to force a restart:

[source,terminal]
----
$ oc delete -n $NAMESPACE <virt-handler>
----

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
