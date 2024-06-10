// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-LowReadyVirtControllersCount"]
= LowReadyVirtControllersCount

[discrete]
[id="meaning-lowreadyvirtcontrollerscount"]
== Meaning

This alert fires when one or more `virt-controller` pods are running, but
none of these pods has been in the `Ready` state for the past 5 minutes.

A `virt-controller` device monitors the custom resource definitions (CRDs)
of a virtual machine instance (VMI) and manages the associated pods. The
device creates pods for VMIs and manages their lifecycle. The device is
critical for cluster-wide virtualization functionality.

[discrete]
[id="impact-lowreadyvirtcontrollerscount"]
== Impact

This alert indicates that a cluster-level failure might occur. Actions
related to VM lifecycle management, such as launching a new VMI or
shutting down an existing VMI, will fail.

[discrete]
[id="diagnosis-lowreadyvirtcontrollerscount"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Verify a `virt-controller` device is available:
+
[source,terminal]
----
$ oc get deployment -n $NAMESPACE virt-controller \
  -o jsonpath='{.status.readyReplicas}'
----

. Check the status of the `virt-controller` deployment:
+
[source,terminal]
----
$ oc -n $NAMESPACE get deploy virt-controller -o yaml
----

. Obtain the details of the `virt-controller` deployment to check for
status conditions, such as crashing pods or failures to pull images:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe deploy virt-controller
----

. Check if any problems occurred with the nodes. For example, they might
be in a `NotReady` state:
+
[source,terminal]
----
$ oc get nodes
----

[discrete]
[id="mitigation-lowreadyvirtcontrollerscount"]
== Mitigation

This alert can have multiple causes, including the following:

* The cluster has insufficient memory.
* The nodes are down.
* The API server is overloaded. For example, the scheduler might be under
a heavy load and therefore not completely available.
* There are network issues.

Try to identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
