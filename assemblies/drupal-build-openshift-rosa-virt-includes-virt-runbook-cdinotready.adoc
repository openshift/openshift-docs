// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-CDINotReady"]
= CDINotReady

[discrete]
[id="meaning-cdinotready"]
== Meaning

This alert fires when the Containerized Data Importer (CDI) is in
a degraded state:

* Not progressing
* Not available to use

[discrete]
[id="impact-cdinotready"]
== Impact

CDI is not usable, so users cannot build virtual machine disks on
persistent volume claims (PVCs) using CDI's data volumes.
CDI components are not ready and they stopped progressing towards
a ready state.

[discrete]
[id="diagnosis-cdinotready"]
== Diagnosis

. Set the `CDI_NAMESPACE` environment variable:
+
[source,terminal]
----
$ export CDI_NAMESPACE="$(oc get deployment -A | \
  grep cdi-operator | awk '{print $1}')"
----

. Check the CDI deployment for components that are not ready:
+
[source,terminal]
----
$ oc -n $CDI_NAMESPACE get deploy -l cdi.kubevirt.io
----

. Check the details of the failing pod:
+
[source,terminal]
----
$ oc -n $CDI_NAMESPACE describe pods <pod>
----

. Check the logs of the failing pod:
+
[source,terminal]
----
$ oc -n $CDI_NAMESPACE logs <pod>
----

[discrete]
[id="mitigation-cdinotready"]
== Mitigation

Try to identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
