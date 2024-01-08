// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-managing-vms-openshift-pipelines.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-supported-ssp-tasks_{context}"]
= Virtual machine tasks supported by the SSP Operator

The following table shows the tasks that are included as part of the SSP Operator.

.Virtual machine tasks supported by the SSP Operator
[cols="1,1",options="header"]
|===
| Task | Description

| `create-vm-from-manifest`
| Create a virtual machine from a provided manifest or with `virtctl`.

| `create-vm-from-template`
| Create a virtual machine from a template.

| `copy-template`
| Copy a virtual machine template.

| `modify-vm-template`
| Modify a virtual machine template.

| `modify-data-object`
| Create or delete data volumes or data sources.

| `cleanup-vm`
| Run a script or a command in a virtual machine and stop or delete the virtual machine afterward.

| `disk-virt-customize`
| Use the `virt-customize` tool to run a customization script on a target PVC.

| `disk-virt-sysprep`
| Use the `virt-sysprep` tool to run a sysprep script on a target PVC.

| `wait-for-vmi-status`
| Wait for a specific status of a virtual machine instance and fail or succeed based on the status.
|===

[NOTE]
====
Virtual machine creation in pipelines now utilizes `ClusterInstanceType` and `ClusterPreference` instead of template-based tasks, which have been deprecated. The `create-vm-from-template`, `copy-template`, and `modify-vm-template` commands remain available but are not used in default pipeline tasks.
====