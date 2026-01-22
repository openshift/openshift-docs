// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: CONCEPT
[id="kmm-day1-mco-yaml-creation_{context}"]
= MCO yaml creation

KMM provides an API to create an MCO YAML manifest for the Day 1 functionality:

[source,console]
----
ProduceMachineConfig(machineConfigName, machineConfigPoolRef, kernelModuleImage, kernelModuleName string) (string, error)
----

The returned output is a string representation of the MCO YAML manifest to be applied. It is up to the customer to apply this YAML.

The parameters are:

`machineConfigName`:: The name of the MCO YAML manifest. This parameter is set as the `name` parameter of the metadata of the MCO YAML manifest.

`machineConfigPoolRef`:: The `MachineConfigPool` name used to identify the targeted nodes.

`kernelModuleImage`:: The name of the container image that includes the OOT kernel module.

`kernelModuleName`:: The name of the OOT kernel module. This parameter is used both to unload the in-tree kernel module (if loaded into the kernel) and to load the OOT kernel module.

The API is located under `pkg/mcproducer` package of the KMM source code. The KMM operator does not need to be running to use the Day 1 functionality. You only need to import the `pkg/mcproducer` package into their operator/utility code, call the API, and apply the produced MCO YAML to the cluster.
