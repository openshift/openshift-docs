// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-advanced-usage.adoc

[id="file-integrity-operator-exploring-daemon-sets_{context}"]
= Exploring the daemon sets

Each `FileIntegrity` object represents a scan on a number of nodes. The scan
itself is performed by pods managed by a daemon set.

To find the daemon set that represents a `FileIntegrity` object, run:

[source,terminal]
----
$ oc -n openshift-file-integrity get ds/aide-worker-fileintegrity
----

To list the pods in that daemon set, run:

[source,terminal]
----
$ oc -n openshift-file-integrity get pods -lapp=aide-worker-fileintegrity
----

To view logs of a single AIDE pod, call `oc logs` on one of the pods.

[source,terminal]
----
$ oc -n openshift-file-integrity logs pod/aide-worker-fileintegrity-mr8x6
----

.Example output
[source,terminal]
----
Starting the AIDE runner daemon
initializing AIDE db
initialization finished
running aide check
...
----

The config maps created by the AIDE daemon are not retained and are deleted
after the File Integrity Operator processes them. However, on failure and error,
the contents of these config maps are copied to the config map that the
`FileIntegrityNodeStatus` object points to.
