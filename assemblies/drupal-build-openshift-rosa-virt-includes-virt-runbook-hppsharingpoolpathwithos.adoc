// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-HPPSharingPoolPathWithOS"]
= HPPSharingPoolPathWithOS

[discrete]
[id="meaning-hppsharingpoolpathwithos"]
== Meaning

This alert fires when the hostpath provisioner (HPP) shares a file
system with other critical components, such as `kubelet` or the operating
system (OS).

HPP dynamically provisions hostpath volumes to provide storage for
persistent volume claims (PVCs).

[discrete]
[id="impact-hppsharingpoolpathwithos"]
== Impact

A shared hostpath pool puts pressure on the node's disks. The node
might have degraded performance and stability.

[discrete]
[id="diagnosis-hppsharingpoolpathwithos"]
== Diagnosis

. Configure the `HPP_NAMESPACE` environment variable:
+
[source,terminal]
----
$ export HPP_NAMESPACE="$(oc get deployment -A | \
  grep hostpath-provisioner-operator | awk '{print $1}')"
----

. Obtain the status of the `hostpath-provisioner-csi` daemon set
pods:
+
[source,terminal]
----
$ oc -n $HPP_NAMESPACE get pods | grep hostpath-provisioner-csi
----

. Check the `hostpath-provisioner-csi` logs to identify the shared
pool and path:
+
[source,terminal]
----
$ oc -n $HPP_NAMESPACE logs <csi_daemonset> -c hostpath-provisioner
----
+
.Example output
+
[source,text]
----
I0208 15:21:03.769731       1 utils.go:221] pool (<legacy, csi-data-dir>/csi),
shares path with OS which can lead to node disk pressure
----

[discrete]
[id="mitigation-hppsharingpoolpathwithos"]
== Mitigation

Using the data obtained in the Diagnosis section, try to prevent the
pool path from being shared with the OS. The specific steps vary based
on the node and other circumstances.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
