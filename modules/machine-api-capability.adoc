// Module included in the following assemblies:
//
// * installing/cluster-capabilities.adoc

:_mod-docs-content-type: REFERENCE
[id="machine-api-capability_{context}"]
= Machine API capability

[discrete]
== Purpose

The `machine-api-operator`, `cluster-autoscaler-operator`, and `cluster-control-plane-machine-set-operator` Operators provide the features for the `MachineAPI` capability. You can disable this capability only if you install a cluster with user-provisioned infrastructure.

The Machine API capability is responsible for all machine configuration and management in the cluster. If you disable the Machine API capability during installation, you need to manage all machine-related tasks manually.
