// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-NoReadyVirtController"]
= NoReadyVirtController

[discrete]
[id="meaning-noreadyvirtcontroller"]
== Meaning

This alert fires when no available `virt-controller` devices have been
detected for 5 minutes.

The `virt-controller` devices monitor the custom resource definitions of
virtual machine instances (VMIs) and manage the associated pods. The devices
create pods for VMIs and manage the lifecycle of the pods.

Therefore, `virt-controller` devices are critical for all cluster-wide
virtualization functionality.

[discrete]
[id="impact-noreadyvirtcontroller"]
== Impact

Any actions related to VM lifecycle management fail. This notably includes
launching a new VMI or shutting down an existing VMI.

[discrete]
[id="diagnosis-noreadyvirtcontroller"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Verify the number of `virt-controller` devices:
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
status conditions such as crashing pods or failure to pull images:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe deploy virt-controller
----

. Obtain the details of the `virt-controller` pods:
+
[source,terminal]
----
$ get pods -n $NAMESPACE | grep virt-controller
----

. Check the logs of the `virt-controller` pods for error messages:
+
[source,terminal]
----
$ oc logs -n $NAMESPACE <virt-controller>
----

. Check the nodes for problems, such as a `NotReady` state:
+
[source,terminal]
----
$ oc get nodes
----

[discrete]
[id="mitigation-noreadyvirtcontroller"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to find
the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
