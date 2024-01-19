:_mod-docs-content-type: ASSEMBLY
[id="creating-windows-machineset-azure"]
= Creating a Windows machine set on Azure
include::_attributes/common-attributes.adoc[]
:context: creating-windows-machineset-azure

toc::[]

You can create a Windows `MachineSet` object to serve a specific purpose in your {product-title} cluster on Microsoft Azure. For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines.

[discrete]
== Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a supported Windows Server as the operating system image.

include::modules/machine-api-overview.adoc[leveloffset=+1]
include::modules/windows-machineset-azure.adoc[leveloffset=+1]
include::modules/machineset-creating.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources

* xref:../../machine_management/index.adoc#overview-of-machine-management[Overview of machine management]
//Should be an xref some day --- and today is the day!
