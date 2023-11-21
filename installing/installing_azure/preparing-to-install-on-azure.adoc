:_mod-docs-content-type: ASSEMBLY
[id="preparing-to-install-on-azure"]
= Preparing to install on Azure
include::_attributes/common-attributes.adoc[]
:context: preparing-to-install-on-azure

toc::[]

[id="preparing-to-install-on-azure-prerequisites"]
== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.
* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].

[id="requirements-for-installing-ocp-on-azure"]
== Requirements for installing {product-title} on Azure

Before installing {product-title} on Microsoft Azure, you must configure an Azure account. See xref:../../installing/installing_azure/installing-azure-account.adoc#installing-azure-account[Configuring an Azure account] for details about account configuration, account limits, public DNS zone configuration, required roles, creating service principals, and supported Azure regions.

If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, see xref:../../installing/installing_azure/installing-azure-customizations.adoc#installing-azure-manual-modes_installing-azure-customizations[Alternatives to storing administrator-level secrets in the kube-system project] for other options.

[id="choosing-an-method-to-install-ocp-on-azure"]
== Choosing a method to install {product-title} on Azure

You can install {product-title} on installer-provisioned or user-provisioned infrastructure. The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster. You can also install {product-title} on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

See xref:../../architecture/architecture-installation.adoc#installation-process_architecture-installation[Installation process] for more information about installer-provisioned and user-provisioned installation processes.

[id="choosing-an-method-to-install-ocp-on-azure-installer-provisioned"]
=== Installing a cluster on installer-provisioned infrastructure

You can install a cluster on Azure infrastructure that is provisioned by the {product-title} installation program, by using one of the following methods:

* **xref:../../installing/installing_azure/installing-azure-default.adoc#installing-azure-default[Installing a cluster quickly on Azure]**: You can install {product-title} on Azure infrastructure that is provisioned by the {product-title} installation program. You can install a cluster quickly by using the default configuration options.

* **xref:../../installing/installing_azure/installing-azure-customizations.adoc#installing-azure-customizations[Installing a customized cluster on Azure]**: You can install a customized cluster on Azure infrastructure that the installation program provisions. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available xref:../../post_installation_configuration/cluster-tasks.adoc#post-install-cluster-tasks[post-installation].

* **xref:../../installing/installing_azure/installing-azure-network-customizations.adoc#installing-azure-network-customizations[Installing a cluster on Azure with network customizations]**: You can customize your {product-title} network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements.

* **xref:../../installing/installing_azure/installing-azure-vnet.adoc#installing-azure-vnet[Installing a cluster on Azure into an existing VNet]**: You can install {product-title} on an existing Azure Virtual Network (VNet) on Azure. You can use this installation method if you have constraints set by the guidelines of your company, such as limits when creating new accounts or infrastructure.

* **xref:../../installing/installing_azure/installing-azure-private.adoc#installing-azure-private[Installing a private cluster on Azure]**: You can install a private cluster into an existing Azure Virtual Network (VNet) on Azure. You can use this method to deploy {product-title} on an internal network that is not visible to the internet.

* **xref:../../installing/installing_azure/installing-azure-government-region.adoc#installing-azure-government-region[Installing a cluster on Azure into a government region]**: {product-title} can be deployed into Microsoft Azure Government (MAG) regions that are specifically designed for US government agencies at the federal, state, and local level, as well as contractors, educational institutions, and other US customers that must run sensitive workloads on Azure.

[id="choosing-an-method-to-install-ocp-on-azure-user-provisioned"]
=== Installing a cluster on user-provisioned infrastructure

You can install a cluster on Azure infrastructure that you provision, by using the following method:

* **xref:../../installing/installing_azure/installing-azure-user-infra.adoc#installing-azure-user-infra[Installing a cluster on Azure using ARM templates]**: You can install {product-title} on Azure by using infrastructure that you provide. You can use the provided Azure Resource Manager (ARM) templates to assist with an installation.

[id="preparing-to-install-on-azure-next-steps"]
== Next steps

* xref:../../installing/installing_azure/installing-azure-account.adoc#installing-azure-account[Configuring an Azure account]
