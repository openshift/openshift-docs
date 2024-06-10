// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-HPPOperatorDown"]
= HPPOperatorDown

[discrete]
[id="meaning-hppoperatordown"]
== Meaning

This alert fires when the hostpath provisioner (HPP) Operator is down.

The HPP Operator deploys and manages the HPP infrastructure components, such
as the daemon set that provisions hostpath volumes.

[discrete]
[id="impact-hppoperatordown"]
== Impact

The HPP components might fail to deploy or to remain in the required state.
As a result, the HPP installation might not work correctly in the cluster.

[discrete]
[id="diagnosis-hppoperatordown"]
== Diagnosis

. Configure the `HPP_NAMESPACE` environment variable:
+
[source,terminal]
----
$ HPP_NAMESPACE="$(oc get deployment -A | grep \
  hostpath-provisioner-operator | awk '{print $1}')"
----

. Check whether the `hostpath-provisioner-operator` pod is currently running:
+
[source,terminal]
----
$ oc -n $HPP_NAMESPACE get pods -l name=hostpath-provisioner-operator
----

. Obtain the details of the `hostpath-provisioner-operator` pod:
+
[source,terminal]
----
$ oc -n $HPP_NAMESPACE describe pods -l name=hostpath-provisioner-operator
----

. Check the log of the `hostpath-provisioner-operator` pod for errors:
+
[source,terminal]
----
$ oc -n $HPP_NAMESPACE logs -l name=hostpath-provisioner-operator
----

[discrete]
[id="mitigation-hppoperatordown"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to
identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
