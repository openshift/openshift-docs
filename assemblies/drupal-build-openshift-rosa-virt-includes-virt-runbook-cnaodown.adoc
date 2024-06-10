// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-CnaoDown"]
= CnaoDown

[discrete]
[id="meaning-cnaodown"]
== Meaning

This alert fires when the Cluster Network Addons Operator (CNAO) is down.
The CNAO deploys additional networking components on top of the cluster.

[discrete]
[id="impact-cnaodown"]
== Impact

If the CNAO is not running, the cluster cannot reconcile changes to virtual
machine components. As a result, the changes might fail to take effect.

[discrete]
[id="diagnosis-cnaodown"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get deployment -A | \
  grep cluster-network-addons-operator | awk '{print $1}')"
----

. Check the status of the `cluster-network-addons-operator` pod:
+
[source,terminal]
----
$ oc -n $NAMESPACE get pods -l name=cluster-network-addons-operator
----

. Check the `cluster-network-addons-operator` logs for error messages:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs -l name=cluster-network-addons-operator
----

. Obtain the details of the `cluster-network-addons-operator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe pods -l name=cluster-network-addons-operator
----

[discrete]
[id="mitigation-cnaodown"]
== Mitigation

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
