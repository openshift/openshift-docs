// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VirtControllerDown"]
= VirtControllerDown

[discrete]
[id="meaning-virtcontrollerdown"]
== Meaning

No running `virt-controller` pod has been detected for 5 minutes.

[discrete]
[id="impact-virtcontrollerdown"]
== Impact

Any actions related to virtual machine (VM) lifecycle management fail.
This notably includes launching a new virtual machine instance (VMI)
or shutting down an existing VMI.

[discrete]
[id="diagnosis-virtcontrollerdown"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the status of the `virt-controller` deployment:
+
[source,terminal]
----
$ oc get deployment -n $NAMESPACE virt-controller -o yaml
----

. Review the logs of the `virt-controller` pod:
+
[source,terminal]
----
$ oc get logs <virt-controller>
----

[discrete]
[id="mitigation-virtcontrollerdown"]
== Mitigation

This alert can have a variety of causes, including the following:

* Node resource exhaustion
* Not enough memory on the cluster
* Nodes are down
* The API server is overloaded. For example, the scheduler might be
under a heavy load and therefore not completely available.
* Networking issues

Identify the root cause and fix it, if possible.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
