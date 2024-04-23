:_mod-docs-content-type: ASSEMBLY
[id="enabling-user-managed-encryption-azure"]
= Enabling user-managed encryption for Azure
include::_attributes/common-attributes.adoc[]
:context: enabling-user-managed-encryption-azure

toc::[]

In {product-title} version {product-version}, you can install a cluster with a user-managed encryption key in Azure. To enable this feature, you can prepare an Azure DiskEncryptionSet before installation, modify the `install-config.yaml` file, and then complete the installation.

include::modules/installation-azure-preparing-diskencryptionsets.adoc[leveloffset=+1]

[id="enabling-disk-encryption-sets-azure-next-steps"]
== Next steps

* Install an {product-title} cluster:
** xref:../../installing/installing_azure/installing-azure-customizations.adoc#installing-azure-customizations[Install a cluster with customizations on installer-provisioned infrastructure]
** xref:../../installing/installing_azure/installing-azure-network-customizations.adoc#installing-azure-network-customizations[Install a cluster with network customizations on installer-provisioned infrastructure]
** xref:../../installing/installing_azure/installing-azure-vnet.adoc#installing-azure-vnet[Install a cluster into an existing VNet on installer-provisioned infrastructure]
** xref:../../installing/installing_azure/installing-azure-private.adoc#installing-azure-private[Install a private cluster on installer-provisioned infrastructure]
** xref:../../installing/installing_azure/installing-azure-government-region.adoc#installing-azure-government-region[Install a cluster into an government region on installer-provisioned infrastructure]
