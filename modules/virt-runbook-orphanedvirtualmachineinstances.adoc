// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-OrphanedVirtualMachineInstances"]
= OrphanedVirtualMachineInstances

[discrete]
[id="meaning-orphanedvirtualmachineinstances"]
== Meaning

This alert fires when a virtual machine instance (VMI), or `virt-launcher`
pod, runs on a node that does not have a running `virt-handler` pod.
Such a VMI is called _orphaned_.

[discrete]
[id="impact-orphanedvirtualmachineinstances"]
== Impact

Orphaned VMIs cannot be managed.

[discrete]
[id="diagnosis-orphanedvirtualmachineinstances"]
== Diagnosis

. Check the status of the `virt-handler` pods to view the nodes on
which they are running:
+
[source,terminal]
----
$ oc get pods --all-namespaces -o wide -l kubevirt.io=virt-handler
----

. Check the status of the VMIs to identify VMIs running on nodes
that do not have a running `virt-handler` pod:
+
[source,terminal]
----
$ oc get vmis --all-namespaces
----

. Check the status of the `virt-handler` daemon:
+
[source,terminal]
----
$ oc get daemonset virt-handler --all-namespaces
----
+
.Example output
+
[source,text]
----
NAME          DESIRED  CURRENT  READY  UP-TO-DATE  AVAILABLE ...
virt-handler  2        2        2      2           2         ...
----
+
The daemon set is considered healthy if the `Desired`, `Ready`,
and `Available` columns contain the same value.

. If the `virt-handler` daemon set is not healthy, check the `virt-handler`
daemon set for pod deployment issues:
+
[source,terminal]
----
$ oc get daemonset virt-handler --all-namespaces -o yaml | jq .status
----

. Check the nodes for issues such as a `NotReady` status:
+
[source,terminal]
----
$ oc get nodes
----

. Check the `spec.workloads` stanza of the `KubeVirt` custom resource
(CR) for a workloads placement policy:
+
[source,terminal]
----
$ oc get kubevirt kubevirt --all-namespaces -o yaml
----

[discrete]
[id="mitigation-orphanedvirtualmachineinstances"]
== Mitigation

If a workloads placement policy is configured, add the node with the
VMI to the policy.

Possible causes for the removal of a `virt-handler` pod from a node
include changes to the node's taints and tolerations or to a pod's
scheduling rules.

Try to identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
