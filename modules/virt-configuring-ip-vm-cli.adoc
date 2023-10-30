// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-viewing-ips-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-ip-vm-cli_{context}"]
= Configuring an IP address when creating a virtual machine by using the command line

You can configure a static or dynamic IP address when you create a virtual machine (VM). The IP address is provisioned with cloud-init.

[NOTE]
====
If the VM is connected to the pod network, the pod network interface is the default route unless you update it.
====

.Prerequisites

* The virtual machine is connected to a secondary network.
* You have a DHCP server available on the secondary network to configure a dynamic IP for the virtual machine.

.Procedure

* Edit the `spec.template.spec.volumes.cloudInitNoCloud.networkData` stanza of the virtual machine configuration:

** To configure a dynamic IP address, specify the interface name and enable DHCP:
+
[source,yaml]
----
kind: VirtualMachine
spec:
# ...
  template:
  # ...
    spec:
      volumes:
      - cloudInitNoCloud:
          networkData: |
            version: 2
            ethernets:
              eth1: <1>
                dhcp4: true
----
<1> Specify the interface name.

** To configure a static IP, specify the interface name and the IP address:
+
[source,yaml]
----
kind: VirtualMachine
spec:
# ...
  template:
  # ...
    spec:
      volumes:
      - cloudInitNoCloud:
          networkData: |
            version: 2
            ethernets:
              eth1: <1>
                addresses:
                - 10.10.10.14/24 <2>
----
<1> Specify the interface name.
<2> Specify the static IP address.
