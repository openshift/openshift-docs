:_mod-docs-content-type: ASSEMBLY
[id="installing-azure-stack-hub-account"]
= Configuring an Azure Stack Hub account
include::_attributes/common-attributes.adoc[]
:context: installing-azure-stack-hub-account

toc::[]

Before you can install {product-title}, you must configure a Microsoft Azure account.

[IMPORTANT]
====
All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see link:https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name[Resolve reserved resource name errors] in the Azure documentation.
====

include::modules/installation-azure-limits.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../scalability_and_performance/optimization/optimizing-storage.adoc#optimizing-storage[Optimizing storage].

include::modules/installation-azure-stack-hub-network-config.adoc[leveloffset=+1]

include::modules/installation-azure-stack-hub-permissions.adoc[leveloffset=+1]

include::modules/installation-azure-service-principal.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* For more information about CCO modes, see xref:../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.adoc#about-cloud-credential-operator-modes[About the Cloud Credential Operator].

[id="next-steps_installing-azure-stack-hub-account"]
== Next steps

* Install an {product-title} cluster:
** xref:../../installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc#installing-azure-stack-hub-default[Installing a cluster quickly on Azure Stack Hub].
** Install an {product-title} cluster on Azure Stack Hub with user-provisioned infrastructure by following xref:../../installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc#installing-azure-stack-hub-user-infra[Installing a cluster on Azure Stack Hub using ARM templates].
