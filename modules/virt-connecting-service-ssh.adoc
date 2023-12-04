// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-accessing-vm-ssh.adoc
// * virt/vm_networking/virt-creating-service-vm.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-connecting-service-ssh_{context}"]
= Connecting to a VM exposed by a service by using SSH

You can connect to a virtual machine (VM) that is exposed by a service by using SSH.

.Prerequisites

* You created a service to expose the VM.
* You have an SSH client installed.
* You are logged in to the cluster.

.Procedure

* Run the following command to access the VM:
+
[source,terminal]
----
$ ssh <user_name>@<ip_address> -p <port> <1>
----
<1> Specify the cluster IP for a cluster IP service, the node IP for a node port service, or the external IP address for a load balancer service.
