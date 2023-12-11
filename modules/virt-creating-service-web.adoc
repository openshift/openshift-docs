// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-accessing-vm-ssh.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-service-web_{context}"]
= Creating a service by using the web console

You can create a node port or load balancer service for a virtual machine (VM) by using the {product-title} web console.

.Prerequisites

* You configured the cluster network to support either a load balancer or a node port.
* To create a load balancer service, you enabled the creation of load balancer services.

.Procedure

. Navigate to *VirtualMachines* and select a virtual machine to view the *VirtualMachine details* page.
. On the *Details* tab, select *SSH over LoadBalancer* from the *SSH service type* list.
. Optional: Click the copy icon to copy the `SSH` command to your clipboard.

.Verification

* Check the *Services* pane on the *Details* tab to view the new service.