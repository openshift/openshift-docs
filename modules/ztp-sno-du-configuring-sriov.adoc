// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-configuring-sriov_{context}"]
= SR-IOV

Single root I/O virtualization (SR-IOV) is commonly used to enable fronthaul and midhaul networks. The following YAML example configures SR-IOV for a {sno} cluster.

[NOTE]
====
The configuration of the `SriovNetwork` CR will vary depending on your specific network and infrastructure requirements.
====

.Recommended `SriovOperatorConfig` CR configuration (`SriovOperatorConfig.yaml`)
[source,yaml]
----
include::snippets/ztp_SriovOperatorConfig.yaml[]
----

.`SriovOperatorConfig` CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|SriovOperatorConfig CR field
|Description

|`spec.enableInjector`
a|Disable `Injector` pods to reduce the number of management pods.
Start with the `Injector` pods enabled, and only disable them after verifying the user manifests.
If the injector is disabled, containers that use SR-IOV resources must explicitly assign them in the `requests` and `limits` section of the container spec.

For example:
[source,yaml]
----
containers:
- name: my-sriov-workload-container
  resources:
    limits:
      openshift.io/<resource_name>:  "1"
    requests:
      openshift.io/<resource_name>:  "1"
----

|`spec.enableOperatorWebhook`
|Disable `OperatorWebhook` pods to reduce the number of management pods. Start with the `OperatorWebhook` pods enabled, and only disable them after verifying the user manifests.

|====

.Recommended `SriovNetwork` configuration (`SriovNetwork.yaml`)
[source,yaml]
----
include::snippets/ztp_SriovNetwork.yaml[]
----

.`SriovNetwork` CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|SriovNetwork CR field
|Description

|`spec.vlan`
|Configure `vlan` with the VLAN for the midhaul network.
|====

.Recommended `SriovNetworkNodePolicy` CR configuration (`SriovNetworkNodePolicy.yaml`)
[source,yaml]
----
include::snippets/ztp_SriovNetworkNodePolicy.yaml[]
----

.`SriovNetworkPolicy` CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|SriovNetworkNodePolicy CR field
|Description

|`spec.deviceType`
|Configure `deviceType` as `vfio-pci` or `netdevice`.
For Mellanox NICs, set `deviceType: netdevice`, and `isRdma: true`.
For Intel based NICs, set `deviceType: vfio-pci` and `isRdma: false`.

|`spec.nicSelector.pfNames`
|Specifies the interface connected to the fronthaul network.

|`spec.numVfs`
|Specifies the number of VFs for the fronthaul network.

|`spec.nicSelector.pfNames`
|The exact name of physical function must match the hardware.
|====

.Recommended SR-IOV kernel configurations (`07-sriov-related-kernel-args-master.yaml`)
[source,yaml]
----
include::snippets/ztp_07-sriov-related-kernel-args-master.yaml[]
----
