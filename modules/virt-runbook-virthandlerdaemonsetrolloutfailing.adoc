// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtHandlerDaemonSetRolloutFailing"]
= VirtHandlerDaemonSetRolloutFailing

[discrete]
[id="meaning-virthandlerdaemonsetrolloutfailing"]
== Meaning

The `virt-handler` daemon set has failed to deploy on one or more worker
nodes after 15 minutes.

[discrete]
[id="impact-virthandlerdaemonsetrolloutfailing"]
== Impact

This alert is a warning. It does not indicate that all `virt-handler` daemon
sets have failed to deploy. Therefore, the normal lifecycle of virtual
machines is not affected unless the cluster is overloaded.

[discrete]
[id="diagnosis-virthandlerdaemonsetrolloutfailing"]
== Diagnosis

Identify worker nodes that do not have a running `virt-handler` pod:

. Export the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the status of the `virt-handler` pods to identify pods that have
not deployed:
+
[source,terminal]
----
$ oc get pods -n $NAMESPACE -l=kubevirt.io=virt-handler
----

. Obtain the name of the worker node of the `virt-handler` pod:
+
[source,terminal]
----
$ oc -n $NAMESPACE get pod <virt-handler> -o jsonpath='{.spec.nodeName}'
----

[discrete]
[id="mitigation-virthandlerdaemonsetrolloutfailing"]
== Mitigation

If the `virt-handler` pods failed to deploy because of insufficient resources,
you can delete other pods on the affected worker node.
