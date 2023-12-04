// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-attaching-vm-secondary-network-cli_{context}"]
= Configuring a VM network interface by using the command line

You can configure a virtual machine (VM) network interface for a bridge network by using the command line.

.Prerequisites

* Shut down the virtual machine before editing the configuration. If you edit a running virtual machine, you must restart the virtual machine for the changes to take effect.

.Procedure

. Add the bridge interface and the network attachment definition to the VM configuration as in the following example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
            - masquerade: {}
              name: default
            - bridge: {}
              name: bridge-net <1>
# ...
      networks:
        - name: default
          pod: {}
        - name: bridge-net <2>
          multus:
            networkName: a-bridge-network <3>
----
<1> The name of the bridge interface.
<2> The name of the network. This value must match the `name` value of the corresponding `spec.template.spec.domain.devices.interfaces` entry.
<3> The name of the network attachment definition.

. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f example-vm.yaml
----

. Optional: If you edited a running virtual machine, you must restart it for the changes to take effect.
