:_mod-docs-content-type: PROCEDURE
[id="encrypting-virtual-machines_{context}"]
= Encrypting virtual machines

You can encrypt your virtual machines with the following process. You can drain your virtual machines, power them down and encrypt them using the vCenter interface. Finally, you can create a storage class to use the encrypted storage.

.Prerequisites

* You have configured a Standard key provider in vSphere. For more information, see link:https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vsan.doc/GUID-AC06B3C3-901F-402E-B25F-1EE7809D1264.html[Adding a KMS to vCenter Server].
+
[IMPORTANT]
====
The Native key provider in vCenter is not supported. For more information, see link:https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-54B9FBA2-FDB1-400B-A6AE-81BF3AC9DF97.html[vSphere Native Key Provider Overview].
====

* You have enabled host encryption mode on all of the ESXi hosts that are hosting the cluster. For more information, see link:https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-A9E1F016-51B3-472F-B8DE-803F6BDB70BC.html[Enabling host encryption mode].
* You have a vSphere account which has all cryptographic privileges enabled. For more information, see link:https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-660CCB35-847F-46B3-81CA-10DDDB9D7AA9.html[Cryptographic Operations Privileges].

.Procedure

. Drain and cordon one of your nodes. For detailed instructions on node management, see "Working with Nodes".
. Shutdown the virtual machine associated with that node in the vCenter interface.
. Right-click on the virtual machine in the vCenter interface and select *VM Policies* -> *Edit VM Storage Policies*.
. Select an encrypted storage policy and select *OK*.
. Start the encrypted virtual machine in the vCenter interface.
. Repeat steps 1-5 for all nodes that you want to encrypt.
. Configure a storage class that uses the encrypted storage policy. For more information about configuring an encrypted storage class, see "VMware vSphere CSI Driver Operator".