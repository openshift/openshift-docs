// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: PROCEDURE
[id="kmm-day1-oot-kernel-module-loading-flow_{context}"]
= OOT kernel module loading flow

The loading of the out-of-tree (OOT) kernel module leverages the Machine Config Operator (MCO). The flow sequence is as follows:

.Procedure

. Apply a `MachineConfig` resource to the existing running cluster. In order to identify the necessary nodes that need to be updated,
you must create an appropriate `MachineConfigPool` resource.

. MCO applies the reboots node by node. On any rebooted node, two new `systemd` services are deployed: `pull` service and `load` service.

. The `load` service is configured to run prior to the `NetworkConfiguration` service. The service tries to pull a predefined kernel module image and then, using that image, to unload an in-tree module and load an OOT kernel module.

. The `pull` service is configured to run after NetworkManager service. The service checks if the preconfigured kernel module image is located on the node's filesystem. If it is, the service exists normally, and the server continues with the boot process. If not, it pulls the image onto the node and reboots the node afterwards.
