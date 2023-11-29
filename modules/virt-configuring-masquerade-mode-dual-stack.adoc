// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-default-pod-network.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-masquerade-mode-dual-stack_{context}"]
= Configuring masquerade mode with dual-stack (IPv4 and IPv6)

You can configure a new virtual machine (VM) to use both IPv6 and IPv4 on the default pod network by using cloud-init.

The `Network.pod.vmIPv6NetworkCIDR` field in the virtual machine instance configuration determines the static IPv6 address of the VM and the gateway IP address. These are used by the virt-launcher pod to route IPv6 traffic to the virtual machine and are not used externally. The `Network.pod.vmIPv6NetworkCIDR` field specifies an IPv6 address block in Classless Inter-Domain Routing (CIDR) notation. The default value is `fd10:0:2::2/120`. You can edit this value based on your network requirements.

When the virtual machine is running, incoming and outgoing traffic for the virtual machine is routed to both the IPv4 address and the unique IPv6 address of the virt-launcher pod. The virt-launcher pod then routes the IPv4 traffic to the DHCP address of the virtual machine, and the IPv6 traffic to the statically set IPv6 address of the virtual machine.

.Prerequisites

* The {product-title} cluster must use the OVN-Kubernetes Container Network Interface (CNI) network plugin configured for dual-stack.

.Procedure

. In a new virtual machine configuration, include an interface with `masquerade` and configure the IPv6 address and default gateway by using cloud-init.
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm-ipv6
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
            - name: default
              masquerade: {} <1>
              ports:
                - port: 80 <2>
# ...
      networks:
      - name: default
        pod: {}
      volumes:
      - cloudInitNoCloud:
          networkData: |
            version: 2
            ethernets:
              eth0:
                dhcp4: true
                addresses: [ fd10:0:2::2/120 ] <3>
                gateway6: fd10:0:2::1 <4>
----
<1> Connect using masquerade mode.
<2> Allows incoming traffic on port 80 to the virtual machine.
<3> The static IPv6 address as determined by the `Network.pod.vmIPv6NetworkCIDR` field in the virtual machine instance configuration. The default value is `fd10:0:2::2/120`.
<4> The gateway IP address as determined by the `Network.pod.vmIPv6NetworkCIDR` field in the virtual machine instance configuration. The default value is `fd10:0:2::1`.

. Create the virtual machine in the namespace:
+
[source,terminal]
----
$ oc create -f example-vm-ipv6.yaml
----

.Verification

* To verify that IPv6 has been configured, start the virtual machine and view the interface status of the virtual machine instance to ensure it has an IPv6 address:

[source,terminal]
----
$ oc get vmi <vmi-name> -o jsonpath="{.status.interfaces[*].ipAddresses}"
----
