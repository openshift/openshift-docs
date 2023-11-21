// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-default-pod-network.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-masquerade-mode-cli_{context}"]
= Configuring masquerade mode from the command line

You can use masquerade mode to hide a virtual machine's outgoing traffic behind
the pod IP address. Masquerade mode uses Network Address Translation (NAT) to
connect virtual machines to the pod network backend through a Linux bridge.

Enable masquerade mode and allow traffic to enter the virtual machine by
editing your virtual machine configuration file.

.Prerequisites

* The virtual machine must be configured to use DHCP to acquire IPv4 addresses.

.Procedure

. Edit the `interfaces` spec of your virtual machine configuration file:
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
            - name: default
              masquerade: {} <1>
              ports: <2>
                - port: 80
# ...
      networks:
      - name: default
        pod: {}
----
<1> Connect using masquerade mode.
<2> Optional: List the ports that you want to expose from the virtual machine, each specified by the `port` field. The `port` value must be a number between 0 and 65536. When the `ports` array is not used, all ports in the valid range are open to incoming traffic. In this example, incoming traffic is allowed on port `80`.
+
[NOTE]
====
Ports 49152 and 49153 are reserved for use by the libvirt platform and all other incoming traffic to these ports is dropped.
====

. Create the virtual machine:
+

[source,terminal]
----
$ oc create -f <vm-name>.yaml
----
