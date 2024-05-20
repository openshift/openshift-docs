:_mod-docs-content-type: ASSEMBLY
:context: multi-architecture-configuration
[id="post-install-multi-architecture-configuration"]
= Configuring a multi-architecture cluster
include::_attributes/common-attributes.adoc[]

toc::[]

A multi-architecture cluster is a cluster that supports worker machines with different architectures. You can deploy a multi-architecture cluster by creating an Azure installer-provisioned cluster using the multi-architecture installer binary. For Azure installation, see xref:../installing/installing_azure/installing-azure-customizations.adoc[Installing on Azure with customizations].

[WARNING]
====
The multi-architecture clusters Technology Preview feature has limited usability with installing, upgrading, and running payloads.
====

The following procedures explain how to generate an `arm64` boot image and create an Azure compute machine set with the `arm64` boot image. This will add `arm64` worker nodes to your multi-architecture cluster and deploy the desired amount of ARM64 virtual machines (VM). This section also shows how to upgrade your existing cluster to a multi-architecture cluster. Multi-architecture clusters are only available on Azure installer-provisioned infrastructures with `x86_64` control planes.

:FeatureName: Multi-architecture clusters for {product-title} on Azure installer-provisioned infrastructure installations
include::snippets/technology-preview.adoc[leveloffset=+1]

include::modules/multi-architecture-creating-arm64-bootimage.adoc[leveloffset=+1]

include::modules/multi-architecture-modify-machine-set.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../machine_management/creating_machinesets/creating-machineset-azure.adoc[Creating a compute machine set on Azure]
include::modules/multi-architecture-upgrade-mirrors.adoc[leveloffset=+1]

include::modules/multi-architecture-import-imagestreams.adoc[leveloffset=+1]