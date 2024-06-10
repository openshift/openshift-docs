// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cluster-overcommit-node-enforcing_{context}"]

= Disabling or enforcing CPU limits using CPU CFS quotas

Nodes by default enforce specified CPU limits using the Completely Fair Scheduler (CFS) quota support in the Linux kernel.

If you disable CPU limit enforcement, it is important to understand the impact on your node:

* If a container has a CPU request, the request continues to be enforced by CFS shares in the Linux kernel.
* If a container does not have a CPU request, but does have a CPU limit, the CPU request defaults to the specified CPU limit, and is enforced by CFS shares in the Linux kernel.
* If a container has both a CPU request and limit, the CPU request is enforced by CFS shares in the Linux kernel, and the CPU limit has no impact on the node.

.Prerequisites

* Obtain the label associated with the static `MachineConfigPool` CRD for the type of node you want to configure by entering the following command:
+
[source,terminal]
----
$ oc edit machineconfigpool <name>
----
+
For example:
+
[source,terminal]
----
$ oc edit machineconfigpool worker
----
+
.Example output
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  creationTimestamp: "2022-11-16T15:34:25Z"
  generation: 4
  labels:
    pools.operator.machineconfiguration.openshift.io/worker: "" <1>
  name: worker
----
<1> The label appears under Labels.
+
[TIP]
====
If the label is not present, add a key/value pair such as:

[source,terminal]
----
$ oc label machineconfigpool worker custom-kubelet=small-pods
----
====

.Procedure

. Create a custom resource (CR) for your configuration change.
+
.Sample configuration for a disabling CPU limits
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: disable-cpu-units <1>
spec:
  machineConfigPoolSelector:
    matchLabels:
      pools.operator.machineconfiguration.openshift.io/worker: "" <2>
  kubeletConfig:
    cpuCfsQuota: false <3>
----
<1> Assign a name to CR.
<2> Specify the label from the machine config pool.
<3> Set the `cpuCfsQuota` parameter to `false`.

. Run the following command to create the CR:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----
