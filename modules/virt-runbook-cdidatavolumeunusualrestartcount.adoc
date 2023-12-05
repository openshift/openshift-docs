// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-CDIDataVolumeUnusualRestartCount"]
= CDIDataVolumeUnusualRestartCount

[discrete]
[id="meaning-cdidatavolumeunusualrestartcount"]
== Meaning

This alert fires when a `DataVolume` object restarts more than three times.

[discrete]
[id="impact-cdidatavolumeunusualrestartcount"]
== Impact

Data volumes are responsible for importing and creating a virtual machine disk
on a persistent volume claim. If a data volume restarts more than three times,
these operations are unlikely to succeed. You must diagnose and resolve the issue.

[discrete]
[id="diagnosis-cdidatavolumeunusualrestartcount"]
== Diagnosis

. Find Containerized Data Importer (CDI) pods with more than three restarts:
+
[source,terminal]
----
$ oc get pods --all-namespaces -l app=containerized-data-importer -o=jsonpath='{range .items[?(@.status.containerStatuses[0].restartCount>3)]}{.metadata.name}{"/"}{.metadata.namespace}{"\n"}'
----

. Obtain the details of the pods:
+
[source,terminal]
----
$ oc -n <namespace> describe pods <pod>
----

. Check the pod logs for error messages:
+
[source,terminal]
----
$ oc -n <namespace> logs <pod>
----

[discrete]
[id="mitigation-cdidatavolumeunusualrestartcount"]
== Mitigation

Delete the data volume, resolve the issue, and create a new data volume.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the Diagnosis procedure.
