// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-viewing-outdated-workloads_{context}"]
= Viewing outdated {VirtProductName} workloads

You can view a list of outdated workloads by using the CLI.

[NOTE]
====
If there are outdated virtualization pods in your cluster, the `OutdatedVirtualMachineInstanceWorkloads` alert fires.
====

.Procedure

* To view a list of outdated virtual machine instances (VMIs), run the following command:
+
[source,terminal]
----
$ oc get vmi -l kubevirt.io/outdatedLauncherImage --all-namespaces
----