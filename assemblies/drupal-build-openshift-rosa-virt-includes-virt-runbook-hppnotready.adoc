// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-HPPNotReady"]
= HPPNotReady

[discrete]
[id="meaning-hppnotready"]
== Meaning

This alert fires when a hostpath provisioner (HPP) installation is in a
degraded state.

The HPP dynamically provisions hostpath volumes to provide storage for
persistent volume claims (PVCs).

[discrete]
[id="impact-hppnotready"]
== Impact

HPP is not usable. Its components are not ready and they are not progressing
towards a ready state.

[discrete]
[id="diagnosis-hppnotready"]
== Diagnosis

. Set the `HPP_NAMESPACE` environment variable:
+
[source,terminal]
----
$ export HPP_NAMESPACE="$(oc get deployment -A | \
  grep hostpath-provisioner-operator | awk '{print $1}')"
----

. Check for HPP components that are currently not ready:
+
[source,terminal]
----
$ oc -n $HPP_NAMESPACE get all -l k8s-app=hostpath-provisioner
----

. Obtain the details of the failing pod:
+
[source,terminal]
----
$ oc -n $HPP_NAMESPACE describe pods <pod>
----

. Check the logs of the failing pod:
+
[source,terminal]
----
$ oc -n $HPP_NAMESPACE logs <pod>
----

[discrete]
[id="mitigation-hppnotready"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to
identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
