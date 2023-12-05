// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-LowKVMNodesCount"]
= LowKVMNodesCount

[discrete]
[id="meaning-lowkvmnodescount"]
== Meaning

This alert fires when fewer than two nodes in the cluster have KVM resources.

[discrete]
[id="impact-lowkvmnodescount"]
== Impact

The cluster must have at least two nodes with KVM resources for live migration.

Virtual machines cannot be scheduled or run if no nodes have KVM resources.

[discrete]
[id="diagnosis-lowkvmnodescount"]
== Diagnosis

* Identify the nodes with KVM resources:
+
[source,terminal]
----
$ oc get nodes -o jsonpath='{.items[*].status.allocatable}' | \
  grep devices.kubevirt.io/kvm
----

[discrete]
[id="mitigation-lowkvmnodescount"]
== Mitigation

Install KVM on the nodes without KVM resources.
