// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

:_mod-docs-content-type: REFERENCE
[id="how-vgpus-are-assigned-to-nodes_{context}"]
= How vGPUs are assigned to nodes

For each physical device, {VirtProductName} configures the following values:

* A single mdev type.
* The maximum number of instances of the selected `mdev` type.

The cluster architecture affects how devices are created and assigned to nodes.

Large cluster with multiple cards per node:: On nodes with multiple cards that can support similar vGPU types, the relevant device types are created in a round-robin manner.
For example:
+
[source,yaml]
----
# ...
mediatedDevicesConfiguration:
  mediatedDeviceTypes:
  - nvidia-222
  - nvidia-228
  - nvidia-105
  - nvidia-108
# ...
----
+
In this scenario, each node has two cards, both of which support the following vGPU types:
+
[source,yaml]
----
nvidia-105
# ...
nvidia-108
nvidia-217
nvidia-299
# ...
----
+
On each node, {VirtProductName} creates the following vGPUs:

* 16 vGPUs of type nvidia-105 on the first card.
* 2 vGPUs of type nvidia-108 on the second card.

One node has a single card that supports more than one requested vGPU type:: {VirtProductName} uses the supported type that comes first on the `mediatedDeviceTypes` list.
+
For example, the card on a node card supports `nvidia-223` and `nvidia-224`. The following `mediatedDeviceTypes` list is configured:
+
[source,yaml]
----
# ...
mediatedDevicesConfiguration:
  mediatedDeviceTypes:
  - nvidia-22
  - nvidia-223
  - nvidia-224
# ...
----
+
In this example, {VirtProductName} uses the `nvidia-223` type.