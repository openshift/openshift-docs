// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-viewing-ips-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-viewing-vmi-ip-cli_{context}"]
= Viewing the IP address of a virtual machine by using the command line

You can view the IP address of a virtual machine (VM) by using the command line.

[NOTE]
====
You must install the QEMU guest agent on a VM to view the IP address of a secondary network interface. A pod network interface does not require the QEMU guest agent.
====

.Procedure

* Obtain the virtual machine instance configuration by running the following command:
+
[source,terminal]
----
$ oc describe vmi <vmi_name>
----
+
.Example output
[source,yaml]
----
# ...
Interfaces:
   Interface Name:  eth0
   Ip Address:      10.244.0.37/24
   Ip Addresses:
     10.244.0.37/24
     fe80::858:aff:fef4:25/64
   Mac:             0a:58:0a:f4:00:25
   Name:            default
   Interface Name:  v2
   Ip Address:      1.1.1.7/24
   Ip Addresses:
     1.1.1.7/24
     fe80::f4d9:70ff:fe13:9089/64
   Mac:             f6:d9:70:13:90:89
   Interface Name:  v1
   Ip Address:      1.1.1.1/24
   Ip Addresses:
     1.1.1.1/24
     1.1.1.2/24
     1.1.1.4/24
     2001:de7:0:f101::1/64
     2001:db8:0:f101::1/64
     fe80::1420:84ff:fe10:17aa/64
   Mac:             16:20:84:10:17:aa
----

