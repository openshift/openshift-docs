// Module included in the following assemblies:
//
// * machine_management/cpmso-about.adoc

:_mod-docs-content-type: CONCEPT
[id="cpmso-overview_{context}"]
= Control Plane Machine Set Operator overview

The Control Plane Machine Set Operator uses the `ControlPlaneMachineSet` custom resource (CR) to automate management of the control plane machine resources within your {product-title} cluster.

When the state of the cluster control plane machine set is set to `Active`, the Operator ensures that the cluster has the correct number of control plane machines with the specified configuration. This allows the automated replacement of degraded control plane machines and rollout of changes to the control plane.

A cluster has only one control plane machine set, and the Operator only manages objects in the `openshift-machine-api` namespace.