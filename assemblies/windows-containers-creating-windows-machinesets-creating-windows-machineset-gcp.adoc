:_mod-docs-content-type: ASSEMBLY
[id="creating-windows-machineset-gcp"]
= Creating a Windows machine set on GCP
include::_attributes/common-attributes.adoc[]
:context: creating-windows-machineset-gcp

toc::[]

You can create a Windows `MachineSet` object to serve a specific purpose in your {product-title} cluster on Google Cloud Platform (GCP). For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines.

[discrete]
== Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a supported Windows Server as the operating system image.

include::modules/machine-api-overview.adoc[leveloffset=+1]
include::modules/windows-machineset-gcp.adoc[leveloffset=+1]
include::modules/machineset-creating.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="creating-windows-machineset-gcp-additional"]
== Additional resources

* xref:../../machine_management/index.adoc#overview-of-machine-management[Overview of machine management]
