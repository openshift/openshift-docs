// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-options-configuring-mdevs_{context}"]
= Options for configuring mediated devices

There are two available methods for configuring mediated devices when using the NVIDIA GPU Operator. The method that Red Hat tests uses {VirtProductName} features to schedule mediated devices, while the NVIDIA method only uses the GPU Operator.

Using the NVIDIA GPU Operator to configure mediated devices::
This method exclusively uses the NVIDIA GPU Operator to configure mediated devices. To use this method, refer to link:https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/openshift-virtualization.html[NVIDIA GPU Operator with {VirtProductName}] in the NVIDIA documentation.

Using {VirtProductName} to configure mediated devices::
This method, which is tested by Red Hat, uses {VirtProductName}'s capabilities to configure mediated devices. In this case, the NVIDIA GPU Operator is only used for installing drivers with the NVIDIA vGPU Manager. The GPU Operator does not configure mediated devices.
+
When using the {VirtProductName} method, you still configure the GPU Operator by following link:https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/openshift-virtualization.html[the NVIDIA documentation]. However, this method differs from the NVIDIA documentation in the following ways:

* You must not overwrite the default `disableMDEVConfiguration: false` setting in the `HyperConverged` custom resource (CR).
+
[IMPORTANT]
====
Setting this feature gate as described in the link:https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/openshift-virtualization.html#prerequisites[NVIDIA documentation] prevents {VirtProductName} from configuring mediated devices.
====
* You must configure your `ClusterPolicy` manifest so that it matches the following example:
+
.Example manifest
[source,yaml]
----
kind: ClusterPolicy
apiVersion: nvidia.com/v1
metadata:
  name: gpu-cluster-policy
spec:
  operator:
    defaultRuntime: crio
    use_ocp_driver_toolkit: true
    initContainer: {}
  sandboxWorkloads:
    enabled: true
    defaultWorkload: vm-vgpu
  driver:
    enabled: false <1>
  dcgmExporter: {}
  dcgm:
    enabled: true
  daemonsets: {}
  devicePlugin: {}
  gfd: {}
  migManager:
    enabled: true
  nodeStatusExporter:
    enabled: true
  mig:
    strategy: single
  toolkit:
    enabled: true
  validator:
    plugin:
      env:
        - name: WITH_WORKLOAD
          value: "true"
  vgpuManager:
    enabled: true <2>
    repository: <vgpu_container_registry> <3>
    image: <vgpu_image_name>
    version: nvidia-vgpu-manager
  vgpuDeviceManager:
    enabled: false <4>
    config:
      name: vgpu-devices-config
      default: default
  sandboxDevicePlugin:
    enabled: false <5>
  vfioManager:
    enabled: false <6>
----
<1> Set this value to `false`. Not required for VMs.
<2> Set this value to `true`. Required for using vGPUs with VMs.
<3> Substitute `<vgpu_container_registry>` with your registry value.
<4> Set this value to `false` to allow {VirtProductName} to configure mediated devices instead of the NVIDIA GPU Operator.
<5> Set this value to `false` to prevent discovery and advertising of the vGPU devices to the kubelet.
<6> Set this value to `false` to prevent loading the `vfio-pci` driver. Instead, follow the {VirtProductName} documentation to configure PCI passthrough.
