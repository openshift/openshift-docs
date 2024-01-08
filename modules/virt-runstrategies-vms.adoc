// Module included in the following assemblies:
//
// * virt/nodes/virt-node-maintenance.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runstrategies-vms_{context}"]
= Run strategies

The `spec.runStrategy` key has four possible values:

`Always`::
The virtual machine instance (VMI) is always present when a virtual machine (VM) is created on another node. A new VMI is created if the original stops for any reason. This is the same behavior as `running: true`.

`RerunOnFailure`::
The VMI is re-created on another node if the previous instance fails. The instance is not re-created if the VM stops successfully, such as when it is shut down.

`Manual`::
You control the VMI state manually with the `start`, `stop`, and `restart` virtctl client commands. The VM is not automatically restarted.

`Halted`::
No VMI is present when a VM is created. This is the same behavior as `running: false`.

Different combinations of the `virtctl start`, `stop` and `restart` commands affect the run strategy.

The following table describes a VM's transition between states. The first column shows the VM's initial run strategy. The remaining columns show a virtctl command and the new run strategy after that command is run.

.Run strategy before and after `virtctl` commands
[options="header"]
|===
|Initial run strategy |Start |Stop |Restart

|Always
|-
|Halted
|Always

|RerunOnFailure
|-
|Halted
|RerunOnFailure

|Manual
|Manual
|Manual
|Manual

|Halted
|Always
|-
|-
|===

[NOTE]
====
If a node in a cluster installed by using installer-provisioned infrastructure fails the machine health check and is unavailable, VMs with `runStrategy: Always` or `runStrategy: RerunOnFailure` are rescheduled on a new node.
====

