:_mod-docs-content-type: ASSEMBLY
[id="preparing-to-install-on-azure-stack-hub"]
= Preparing to install on Azure Stack Hub
include::_attributes/common-attributes.adoc[]
:context: preparing-to-install-on-azure-stack-hub

toc::[]

[id="preparing-to-install-on-ash-prerequisites"]
== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.
* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].
* You have installed Azure Stack Hub version 2008 or later.

[id="requirements-for-installing-ocp-on-ash"]
== Requirements for installing {product-title} on Azure Stack Hub

Before installing {product-title} on Microsoft Azure Stack Hub, you must configure an Azure account.

See xref:../../installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc#installing-azure-stack-hub-account[Configuring an Azure Stack Hub account] for details about account configuration, account limits, DNS zone configuration, required roles, and creating service principals.

[id="choosing-a-method-to-install-ocp-on-ash"]
== Choosing a method to install {product-title} on Azure Stack Hub

You can install {product-title} on installer-provisioned or user-provisioned infrastructure. The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster. You can also install {product-title} on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

See xref:../../architecture/architecture-installation.adoc#installation-process_architecture-installation[Installation process] for more information about installer-provisioned and user-provisioned installation processes.

[id="choosing-a-method-to-install-ocp-on-ash-installer-provisioned"]
=== Installing a cluster on installer-provisioned infrastructure

You can install a cluster on Azure Stack Hub infrastructure that is provisioned by the {product-title} installation program, by using the following method:

* **xref:../../installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc#installing-azure-stack-hub-default[Installing a cluster on Azure Stack Hub with an installer-provisioned infrastructure]**: You can install {product-title} on Azure Stack Hub infrastructure that is provisioned by the {product-title} installation program.

[id="choosing-a-method-to-install-ocp-on-ash-user-provisioned"]
=== Installing a cluster on user-provisioned infrastructure

You can install a cluster on Azure Stack Hub infrastructure that you provision, by using the following method:

* **xref:../../installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc#installing-azure-stack-hub-user-infra[Installing a cluster on Azure Stack Hub using ARM templates]**: You can install {product-title} on Azure Stack Hub by using infrastructure that you provide. You can use the provided Azure Resource Manager (ARM) templates to assist with an installation.

[id="preparing-to-install-on-ash-next-steps"]
== Next steps

* xref:../../installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc#installing-azure-stack-hub-account[Configuring an Azure Stack Hub account]
