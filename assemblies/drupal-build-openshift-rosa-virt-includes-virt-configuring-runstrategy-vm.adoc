// Module included in the following assemblies:
//
// * virt/nodes/virt-node-maintenance.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-runstrategy-vm_{context}"]
= Configuring a VM run strategy by using the command line

You can configure a run strategy for a virtual machine (VM) by using the command line.

[IMPORTANT]
====
The `spec.runStrategy` and `spec.running` keys are mutually exclusive. A VM configuration that contains values for both keys is invalid.
====

.Procedure

* Edit the `VirtualMachine` resource by running the following command:
+
[source,terminal]
----
$ oc edit vm <vm_name> -n <namespace>
----
+
.Example run strategy
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  runStrategy: Always
# ...
----
