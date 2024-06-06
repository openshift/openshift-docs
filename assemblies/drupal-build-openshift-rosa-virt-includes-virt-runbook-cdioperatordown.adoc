// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-CDIOperatorDown"]
= CDIOperatorDown

[discrete]
[id="meaning-cdioperatordown"]
== Meaning

This alert fires when the Containerized Data Importer (CDI) Operator is down.
The CDI Operator deploys and manages the CDI infrastructure components, such
as data volume and persistent volume claim (PVC) controllers. These controllers
help users build virtual machine disks on PVCs.

[discrete]
[id="impact-cdioperatordown"]
== Impact

The CDI components might fail to deploy or to stay in a required state. The
CDI installation might not function correctly.

[discrete]
[id="diagnosis-cdioperatordown"]
== Diagnosis

. Set the `CDI_NAMESPACE` environment variable:
+
[source,terminal]
----
$ export CDI_NAMESPACE="$(oc get deployment -A | grep cdi-operator | \
  awk '{print $1}')"
----

. Check whether the `cdi-operator` pod is currently running:
+
[source,terminal]
----
$ oc -n $CDI_NAMESPACE get pods -l name=cdi-operator
----

. Obtain the details of the `cdi-operator` pod:
+
[source,terminal]
----
$ oc -n $CDI_NAMESPACE describe pods -l name=cdi-operator
----

. Check the log of the `cdi-operator` pod for errors:
+
[source,terminal]
----
$ oc -n $CDI_NAMESPACE logs -l name=cdi-operator
----

[discrete]
[id="mitigation-cdioperatordown"]
== Mitigation

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
