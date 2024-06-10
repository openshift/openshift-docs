// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-LowVirtControllersCount"]
= LowVirtControllersCount

[discrete]
[id="meaning-lowvirtcontrollerscount"]
== Meaning

This alert fires when a low number of `virt-controller` pods is detected. At
least one `virt-controller` pod must be available in order to ensure high
availability. The default number of replicas is 2.

A `virt-controller` device monitors the custom resource definitions (CRDs) of a
virtual machine instance (VMI) and manages the associated pods. The device
create pods for VMIs and manages the lifecycle of the pods. The device is
critical for cluster-wide virtualization functionality.

[discrete]
[id="impact-lowvirtcontrollerscount"]
== Impact

The responsiveness of {VirtProductName} might become negatively
affected. For example, certain requests might be missed.

In addition, if another `virt-launcher` instance terminates unexpectedly,
{VirtProductName} might become completely unresponsive.

[discrete]
[id="diagnosis-lowvirtcontrollerscount"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Verify that running `virt-controller` pods are available:
+
[source,terminal]
----
$ oc -n $NAMESPACE get pods -l kubevirt.io=virt-controller
----

. Check the `virt-launcher` logs for error messages:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs <virt-launcher>
----

. Obtain the details of the `virt-launcher` pod to check for status conditions
such as unexpected termination or a `NotReady` state.
+
[source,terminal]
----
$ oc -n $NAMESPACE describe pod/<virt-launcher>
----

[discrete]
[id="mitigation-lowvirtcontrollerscount"]
== Mitigation

This alert can have a variety of causes, including:

* Not enough memory on the cluster
* Nodes are down
* The API server is overloaded. For example, the scheduler might be under a
heavy load and therefore not completely available.
* Networking issues

Identify the root cause and fix it, if possible.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
