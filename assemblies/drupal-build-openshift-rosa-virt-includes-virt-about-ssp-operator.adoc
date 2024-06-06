// Module included in the following assemblies:
//
// * virt/about_virt/virt-architecture.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-ssp-operator_{context}"]
= About the Scheduling, Scale, and Performance (SSP) Operator

The SSP Operator, `ssp-operator`, deploys the common templates, the related default boot sources, the pipeline tasks, and the template validator.

image::cnv_components_ssp-operator.png[ssp-operator components]

.SSP Operator components
[cols="1,1"]
|===
|*Component* |*Description*

|`deployment/create-vm-from-template`
|	Creates a VM from a template.

|`deployment/copy-template`
|	Copies a VM template.

|`deployment/modify-vm-template`
|	Creates or removes a VM template.

|`deployment/modify-data-object`
|	Creates or removes data volumes or data sources.

|`deployment/cleanup-vm`
|	Runs a script or a command on a VM, then stops or deletes the VM afterward.

|`deployment/disk-virt-customize`
|	Runs a `customize` script on a target persistent volume claim (PVC) using `virt-customize`.

|`deployment/disk-virt-sysprep`
|	Runs a `sysprep` script on a target PVC by using `virt-sysprep`.

|`deployment/wait-for-vmi-status`
|	Waits for a specific virtual machine instance (VMI) status, then fails or succeeds according to that status.

|`deployment/create-vm-from-manifest`
|   Creates a VM from a manifest.
|===