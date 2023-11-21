:_mod-docs-content-type: ASSEMBLY
[id="cpmso-disabling"]
= Disabling the control plane machine set
include::_attributes/common-attributes.adoc[]
:context: cpmso-disabling

toc::[]

The `.spec.state` field in an activated `ControlPlaneMachineSet` custom resource (CR) cannot be changed from `Active` to `Inactive`. To disable the control plane machine set, you must delete the CR so that it is removed from the cluster.

When you delete the CR, the Control Plane Machine Set Operator performs cleanup operations and disables the control plane machine set. The Operator then removes the CR from the cluster and creates an inactive control plane machine set with default settings.

//Deleting the control plane machine set
include::modules/cpmso-deleting.adoc[leveloffset=+1]

//Checking the control plane machine set custom resource status
include::modules/cpmso-checking-status.adoc[leveloffset=+1]

[id="cpmso-reenabling_{context}"]
== Re-enabling the control plane machine set

To re-enable the control plane machine set, you must ensure that the configuration in the CR is correct for your cluster and activate it.

[role="_additional-resources"]
.Additional resources
* xref:../../machine_management/control_plane_machine_management/cpmso-getting-started.adoc#cpmso-activating_cpmso-getting-started[Activating the control plane machine set custom resource]
