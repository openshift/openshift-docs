:_mod-docs-content-type: ASSEMBLY
[id="about-sriov"]
= About Single Root I/O Virtualization (SR-IOV) hardware networks
include::_attributes/common-attributes.adoc[]
:context: about-sriov

toc::[]

The Single Root I/O Virtualization (SR-IOV) specification is a standard for a type of PCI device assignment that can share a single device with multiple pods.

SR-IOV can segment a compliant network device, recognized on the host node as a physical function (PF), into multiple virtual functions (VFs).
The VF is used like any other network device.
The SR-IOV network device driver for the device determines how the VF is exposed in the container:

* `netdevice` driver: A regular kernel network device in the `netns` of the container
* `vfio-pci` driver: A character device mounted in the container

You can use SR-IOV network devices with additional networks on your {product-title} cluster installed on bare metal or {rh-openstack-first} infrastructure for applications that require high bandwidth or low latency.

You can configure multi-network policies for SR-IOV networks. The support for this is technology preview and SR-IOV additional networks are only supported with kernel NICs. They are not supported for Data Plane Development Kit (DPDK) applications.

[NOTE]
====
Creating multi-network policies on SR-IOV networks might not deliver the same performance to applications compared to SR-IOV networks without a multi-network policy configured.
====

:FeatureName: Multi-network policies for SR-IOV network
include::snippets/technology-preview.adoc[leveloffset=+2]

You can enable SR-IOV on a node by using the following command:
[source,terminal]
----
$ oc label node <node_name> feature.node.kubernetes.io/network-sriov.capable="true"
----

[id="components-sr-iov-network-devices"]
== Components that manage SR-IOV network devices

The SR-IOV Network Operator creates and manages the components of the SR-IOV stack.
It performs the following functions:

- Orchestrates discovery and management of SR-IOV network devices
- Generates `NetworkAttachmentDefinition` custom resources for the SR-IOV Container Network Interface (CNI)
- Creates and updates the configuration of the SR-IOV network device plugin
- Creates node specific `SriovNetworkNodeState` custom resources
- Updates the `spec.interfaces` field in each `SriovNetworkNodeState` custom resource

The Operator provisions the following components:

SR-IOV network configuration daemon::
A daemon set that is deployed on worker nodes when the SR-IOV Network Operator starts. The daemon is responsible for discovering and initializing SR-IOV network devices in the cluster.

SR-IOV Network Operator webhook::
A dynamic admission controller webhook that validates the Operator custom resource and sets appropriate default values for unset fields.

SR-IOV Network resources injector::
A dynamic admission controller webhook that provides functionality for patching Kubernetes pod specifications with requests and limits for custom network resources such as SR-IOV VFs. The SR-IOV network resources injector adds the `resource` field to only the first container in a pod automatically.

SR-IOV network device plugin::
A device plugin that discovers, advertises, and allocates SR-IOV network virtual function (VF) resources. Device plugins are used in Kubernetes to enable the use of limited resources, typically in physical devices. Device plugins give the Kubernetes scheduler awareness of resource availability, so that the scheduler can schedule pods on nodes with sufficient resources.

SR-IOV CNI plugin::
A CNI plugin that attaches VF interfaces allocated from the SR-IOV network device plugin directly into a pod.

SR-IOV InfiniBand CNI plugin::
A CNI plugin that attaches InfiniBand (IB) VF interfaces allocated from the SR-IOV network device plugin directly into a pod.

[NOTE]
====
The SR-IOV Network resources injector and SR-IOV Network Operator webhook are enabled by default and can be disabled by editing the `default` `SriovOperatorConfig` CR.
Use caution when disabling the SR-IOV Network Operator Admission Controller webhook. You can disable the webhook under specific circumstances, such as troubleshooting, or if you want to use unsupported devices.
====

include::modules/nw-sriov-supported-platforms.adoc[leveloffset=+2]
include::modules/nw-sriov-supported-devices.adoc[leveloffset=+2]
include::modules/nw-sriov-device-discovery.adoc[leveloffset=+2]
include::modules/nw-sriov-example-vf-function-in-pod.adoc[leveloffset=+2]
include::modules/nw-sriov-app-netutil.adoc[leveloffset=+2]
include::modules/nw-sriov-huge-pages.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="configure-multi-networks-additional-resources"]
== Additional resources

* xref:../../networking/multiple_networks/configuring-multi-network-policy.adoc#configuring-multi-network-policy[Configuring multi-network policy]

[id="about-sriov-next-steps"]
== Next steps

* xref:../../networking/hardware_networks/installing-sriov-operator.adoc#installing-sriov-operator[Installing the SR-IOV Network Operator]
* Optional: xref:../../networking/hardware_networks/configuring-sriov-operator.adoc#configuring-sriov-operator[Configuring the SR-IOV Network Operator]
* xref:../../networking/hardware_networks/configuring-sriov-device.adoc#configuring-sriov-device[Configuring an SR-IOV network device]
* If you use {VirtProductName}: xref:../../virt/vm_networking/virt-connecting-vm-to-sriov.adoc#virt-connecting-vm-to-sriov[Connecting a virtual machine to an SR-IOV network]
* xref:../../networking/hardware_networks/configuring-sriov-net-attach.adoc#configuring-sriov-net-attach[Configuring an SR-IOV network attachment]
* xref:../../networking/hardware_networks/add-pod.adoc#add-pod[Adding a pod to an SR-IOV additional network]
