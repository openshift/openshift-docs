:_mod-docs-content-type: ASSEMBLY
[id="creating-machineset-azure-stack-hub"]
= Creating a compute machine set on Azure Stack Hub
include::_attributes/common-attributes.adoc[]
:context: creating-machineset-azure-stack-hub

toc::[]

You can create a different compute machine set to serve a specific purpose in your {product-title} cluster on Microsoft Azure Stack Hub. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

//[IMPORTANT] admonition for UPI
include::modules/machine-user-provisioned-limitations.adoc[leveloffset=+1]

//Sample YAML for a compute machine set custom resource on Azure Stack Hub
include::modules/machineset-yaml-azure-stack-hub.adoc[leveloffset=+1]

//Creating a compute machine set
include::modules/machineset-creating.adoc[leveloffset=+1]

//Enabling Azure boot diagnostics on compute machines
include::modules/machineset-azure-boot-diagnostics.adoc[leveloffset=+1]

//Enabling customer-managed encryption keys for a compute machine set
include::modules/machineset-customer-managed-encryption-azure.adoc[leveloffset=+1]
