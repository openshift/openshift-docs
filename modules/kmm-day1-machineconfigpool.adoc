// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: CONCEPT
[id="kmm-day1-machineconfigpool_{context}"]
= The MachineConfigPool

The `MachineConfigPool` identifies a collection of nodes that are affected by the applied MCO.

[source,yaml]
----
kind: MachineConfigPool
metadata:
  name: sfc
spec:
  machineConfigSelector: <1>
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker, sfc]}
  nodeSelector: <2>
    matchLabels:
      node-role.kubernetes.io/sfc: ""
  paused: false
  maxUnavailable: 1
----
<1> Matches the labels in the MachineConfig.
<2> Matches the labels on the node.

There are predefined `MachineConfigPools` in the OCP cluster:

* `worker`: Targets all worker nodes in the cluster

* `master`: Targets all master nodes in the cluster

Define the following `MachineConfig` to target the master `MachineConfigPool`:

[source,yaml]
----
metadata:
  labels:
    machineconfiguration.opensfhit.io/role: master
----


Define the following `MachineConfig` to target the worker `MachineConfigPool`:

[source,yaml]
----
metadata:
  labels:
    machineconfiguration.opensfhit.io/role: worker
----
