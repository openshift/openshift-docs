// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc

[id="nodes-cluster-overcommit-node-memory_{context}"]

= Reserving memory across quality of service tiers

You can use the `qos-reserved` parameter to specify a percentage of memory to be reserved
by a pod in a particular QoS level. This feature attempts to reserve requested resources to exclude pods
from lower OoS classes from using resources requested by pods in higher QoS classes.

By reserving resources for higher QOS levels, pods that do not have resource limits are prevented from encroaching on the resources
requested by pods at higher QoS levels.

.Prerequisites

. Obtain the label associated with the static Machine Config Pool CRD for the type of node you want to configure.
Perform one of the following steps:

.. View the Machine Config Pool:
+
----
$ oc describe machineconfigpool <name>
----
+
For example:
+
[source,yaml]
----
$ oc describe machineconfigpool worker

apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  creationTimestamp: 2019-02-08T14:52:39Z
  generation: 1
  labels:
    custom-kubelet: small-pods <1>
----
<1> If a label has been added it appears under `labels`.

.. If the label is not present, add a key/value pair:
+
----
$ oc label machineconfigpool worker custom-kubelet=small-pods
----
+
[TIP]
====
You can alternatively apply the following YAML to add the label:

[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  labels:
    custom-kubelet: small-pods
  name: worker
----
====

.Procedure

. Create a Custom Resource (CR) for your configuration change.
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
      custom-kubelet: small-pods <2>
  kubeletConfig:
    cgroups-per-qos:
    - true
    cgroup-driver:
    - 'systemd'
    cgroup-root:
    - '/'
    qos-reserved: <3>
    - 'memory=50%'
----
<1> Assign a name to CR.
<2> Specify the label to apply the configuration change.
<3> Specifies how pod resource requests are reserved at the QoS level.
{product-title} uses the `qos-reserved` parameter as follows:
- A value of `qos-reserved=memory=100%` will prevent the `Burstable` and `BestEffort` QOS classes from consuming memory
that was requested by a higher QoS class. This increases the risk of inducing OOM
on `BestEffort` and `Burstable` workloads in favor of increasing memory resource guarantees
for `Guaranteed` and `Burstable` workloads.
- A value of `qos-reserved=memory=50%` will allow the `Burstable` and `BestEffort` QOS classes
to consume half of the memory requested by a higher QoS class.
- A value of `qos-reserved=memory=0%`
will allow a `Burstable` and `BestEffort` QoS classes to consume up to the full node
allocatable amount if available, but increases the risk that a `Guaranteed` workload
will not have access to requested memory. This condition effectively disables this feature.
