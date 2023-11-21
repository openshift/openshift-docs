:_mod-docs-content-type: ASSEMBLY
[id="installing-azure-account"]
= Configuring an Azure account
include::_attributes/common-attributes.adoc[]
:context: installing-azure-account

toc::[]

Before you can install {product-title}, you must configure a Microsoft Azure account to meet installation requirements.

[IMPORTANT]
====
All Azure resources that are available through public endpoints are subject to
resource name restrictions, and you cannot create resources that use certain
terms. For a list of terms that Azure restricts, see
link:https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name[Resolve reserved resource name errors]
in the Azure documentation.
====

include::modules/installation-azure-limits.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../scalability_and_performance/optimization/optimizing-storage.adoc#optimizing-storage[Optimizing storage].

include::modules/installation-azure-network-config.adoc[leveloffset=+1]

include::modules/installation-azure-increasing-limits.adoc[leveloffset=+1]

include::modules/installation-azure-subscription-tenant-id.adoc[leveloffset=+1]

include::modules/installation-azure-identities.adoc[leveloffset=+1]

include::modules/installation-azure-permissions.adoc[leveloffset=+2]
include::modules/minimum-required-permissions-ipi-azure.adoc[leveloffset=+2]
include::modules/installation-using-azure-managed-identities.adoc[leveloffset=+2]
include::modules/installation-creating-azure-service-principal.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.adoc#about-cloud-credential-operator-modes[About the Cloud Credential Operator]

include::modules/installation-azure-marketplace.adoc[leveloffset=+1]

include::modules/installation-azure-regions.adoc[leveloffset=+1]

== Next steps

* Install an {product-title} cluster on Azure. You can
xref:../../installing/installing_azure/installing-azure-customizations.adoc#installing-azure-customizations[install a customized cluster]
or
xref:../../installing/installing_azure/installing-azure-default.adoc#installing-azure-default[quickly install a cluster] with default options.
