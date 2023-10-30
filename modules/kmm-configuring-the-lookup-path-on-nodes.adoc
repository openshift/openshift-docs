// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: PROCEDURE
[id="kmm-configuring-the-lookup-path-on-nodes_{context}"]
= Configuring the lookup path on nodes

On {product-title} nodes, the set of default lookup paths for firmwares does not include the `/var/lib/firmware` path.

.Procedure

. Use the Machine Config Operator to create a `MachineConfig` custom resource (CR) that contains the `/var/lib/firmware` path:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker <1>
  name: 99-worker-kernel-args-firmware-path
spec:
  kernelArguments:
    - 'firmware_class.path=/var/lib/firmware'
----
<1> You can configure the label based on your needs. In the case of {sno}, use either `control-pane` or `master` objects.


. By applying the `MachineConfig` CR, the nodes are automatically rebooted.
