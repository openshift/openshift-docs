// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-understanding.adoc

:_mod-docs-content-type: CONCEPT
[id="understanding-file-integrity-node-statuses-object_{context}"]
= Understanding the FileIntegrityNodeStatuses object

The scan results of the `FileIntegrity` CR are reported in another object called `FileIntegrityNodeStatuses`.

[source,terminal]
----
$ oc get fileintegritynodestatuses
----

.Example output
[source,terminal]
----
NAME                                                AGE
worker-fileintegrity-ip-10-0-130-192.ec2.internal   101s
worker-fileintegrity-ip-10-0-147-133.ec2.internal   109s
worker-fileintegrity-ip-10-0-165-160.ec2.internal   102s
----

[NOTE]
====
It might take some time for the `FileIntegrityNodeStatus` object results to be available.
====

There is one result object per node. The `nodeName` attribute of each `FileIntegrityNodeStatus` object corresponds to the node being scanned. The
status of the file integrity scan is represented in the `results` array, which holds scan conditions.

[source,terminal]
----
$ oc get fileintegritynodestatuses.fileintegrity.openshift.io -ojsonpath='{.items[*].results}' | jq
----

The `fileintegritynodestatus` object reports the latest status of an AIDE run and exposes the status as `Failed`, `Succeeded`, or `Errored` in a `status` field.

[source,terminal]
----
$ oc get fileintegritynodestatuses -w
----

.Example output
[source,terminal]
----
NAME                                                               NODE                                         STATUS
example-fileintegrity-ip-10-0-134-186.us-east-2.compute.internal   ip-10-0-134-186.us-east-2.compute.internal   Succeeded
example-fileintegrity-ip-10-0-150-230.us-east-2.compute.internal   ip-10-0-150-230.us-east-2.compute.internal   Succeeded
example-fileintegrity-ip-10-0-169-137.us-east-2.compute.internal   ip-10-0-169-137.us-east-2.compute.internal   Succeeded
example-fileintegrity-ip-10-0-180-200.us-east-2.compute.internal   ip-10-0-180-200.us-east-2.compute.internal   Succeeded
example-fileintegrity-ip-10-0-194-66.us-east-2.compute.internal    ip-10-0-194-66.us-east-2.compute.internal    Failed
example-fileintegrity-ip-10-0-222-188.us-east-2.compute.internal   ip-10-0-222-188.us-east-2.compute.internal   Succeeded
example-fileintegrity-ip-10-0-134-186.us-east-2.compute.internal   ip-10-0-134-186.us-east-2.compute.internal   Succeeded
example-fileintegrity-ip-10-0-222-188.us-east-2.compute.internal   ip-10-0-222-188.us-east-2.compute.internal   Succeeded
example-fileintegrity-ip-10-0-194-66.us-east-2.compute.internal    ip-10-0-194-66.us-east-2.compute.internal    Failed
example-fileintegrity-ip-10-0-150-230.us-east-2.compute.internal   ip-10-0-150-230.us-east-2.compute.internal   Succeeded
example-fileintegrity-ip-10-0-180-200.us-east-2.compute.internal   ip-10-0-180-200.us-east-2.compute.internal   Succeeded
----
