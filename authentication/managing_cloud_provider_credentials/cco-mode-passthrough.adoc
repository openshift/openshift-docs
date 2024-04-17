:_mod-docs-content-type: ASSEMBLY
[id="cco-mode-passthrough"]
= The Cloud Credential Operator in passthrough mode
include::_attributes/common-attributes.adoc[]
:context: cco-mode-passthrough

toc::[]

Passthrough mode is supported for Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), {rh-openstack-first}, and VMware vSphere.

In passthrough mode, the Cloud Credential Operator (CCO) passes the provided cloud credential to the components that request cloud credentials. The credential must have permissions to perform the installation and complete the operations that are required by components in the cluster, but does not need to be able to create new credentials. The CCO does not attempt to create additional limited-scoped credentials in passthrough mode.

[NOTE]
====
xref:../../authentication/managing_cloud_provider_credentials/cco-mode-manual.adoc#cco-mode-manual[Manual mode] is the only supported CCO configuration for Microsoft Azure Stack Hub.
====

[id="passthrough-mode-permissions"]
== Passthrough mode permissions requirements
When using the CCO in passthrough mode, ensure that the credential you provide meets the requirements of the cloud on which you are running or installing {product-title}. If the provided credentials the CCO passes to a component that creates a `CredentialsRequest` CR are not sufficient, that component will report an error when it tries to call an API that it does not have permissions for.

[id="passthrough-mode-permissions-aws"]
=== Amazon Web Services (AWS) permissions
The credential you provide for passthrough mode in AWS must have all the requested permissions for all `CredentialsRequest` CRs that are required by the version of {product-title} you are running or installing.

To locate the `CredentialsRequest` CRs that are required, see xref:../../installing/installing_aws/installing-aws-customizations.adoc#manually-create-iam_installing-aws-customizations[Manually creating long-term credentials for AWS].

[id="passthrough-mode-permissions-azure"]
=== Microsoft Azure permissions
The credential you provide for passthrough mode in Azure must have all the requested permissions for all `CredentialsRequest` CRs that are required by the version of {product-title} you are running or installing.

To locate the `CredentialsRequest` CRs that are required, see xref:../../installing/installing_azure/installing-azure-customizations.adoc#manually-create-iam_installing-azure-customizations[Manually creating long-term credentials for Azure].

[id="passthrough-mode-permissions-gcp"]
=== Google Cloud Platform (GCP) permissions
The credential you provide for passthrough mode in GCP must have all the requested permissions for all `CredentialsRequest` CRs that are required by the version of {product-title} you are running or installing.

To locate the `CredentialsRequest` CRs that are required, see xref:../../installing/installing_gcp/installing-gcp-customizations.adoc#manually-create-iam_installing-gcp-customizations[Manually creating long-term credentials for GCP].

[id="passthrough-mode-permissions-rhosp"]
=== {rh-openstack-first} permissions
To install an {product-title} cluster on {rh-openstack}, the CCO requires a credential with the permissions of a `member` user role.

[id="passthrough-mode-permissions-vsware"]
=== VMware vSphere permissions
To install an {product-title} cluster on VMware vSphere, the CCO requires a credential with the following vSphere privileges:

.Required vSphere privileges
[cols="1,2"]
|====
|Category |Privileges

|Datastore
|_Allocate space_

|Folder
|_Create folder_, _Delete folder_

|vSphere Tagging
|All privileges

|Network
|_Assign network_

|Resource
|_Assign virtual machine to resource pool_

|Profile-driven storage
|All privileges

|vApp
|All privileges

|Virtual machine
|All privileges

|====

//Admin credentials root secret format
include::modules/admin-credentials-root-secret-formats.adoc[leveloffset=+1]

[id="passthrough-mode-maintenance"]
== Passthrough mode credential maintenance
If `CredentialsRequest` CRs change over time as the cluster is upgraded, you must manually update the passthrough mode credential to meet the requirements. To avoid credentials issues during an upgrade, check the `CredentialsRequest` CRs in the release image for the new version of {product-title} before upgrading. To locate the `CredentialsRequest` CRs that are required for your cloud provider, see _Manually creating long-term credentials_ for xref:../../installing/installing_aws/installing-aws-customizations.adoc#manually-create-iam_installing-aws-customizations[AWS], xref:../../installing/installing_azure/installing-azure-customizations.adoc#manually-create-iam_installing-azure-customizations[Azure], or xref:../../installing/installing_gcp/installing-gcp-customizations.adoc#manually-create-iam_installing-gcp-customizations[GCP].

//Rotating cloud provider credentials manually
include::modules/manually-rotating-cloud-creds.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* xref:../../storage/container_storage_interface/persistent-storage-csi-vsphere.adoc[vSphere CSI Driver Operator]

[id="passthrough-mode-reduce-permissions"]
== Reducing permissions after installation
When using passthrough mode, each component has the same permissions used by all other components. If you do not reduce the permissions after installing, all components have the broad permissions that are required to run the installer.

After installation, you can reduce the permissions on your credential to only those that are required to run the cluster, as defined by the `CredentialsRequest` CRs in the release image for the version of {product-title} that you are using.

To locate the `CredentialsRequest` CRs that are required for AWS, Azure, or GCP and learn how to change the permissions the CCO uses, see _Manually creating long-term credentials_ for xref:../../installing/installing_aws/installing-aws-customizations.adoc#manually-create-iam_installing-aws-customizations[AWS], xref:../../installing/installing_azure/installing-azure-customizations.adoc#manually-create-iam_installing-azure-customizations[Azure], or xref:../../installing/installing_gcp/installing-gcp-customizations.adoc#manually-create-iam_installing-gcp-customizations[GCP].

[role="_additional-resources"]
== Additional resources

* xref:../../installing/installing_aws/installing-aws-customizations.adoc#manually-create-iam_installing-aws-customizations[Manually creating long-term credentials for AWS]
* xref:../../installing/installing_azure/installing-azure-customizations.adoc#manually-create-iam_installing-azure-customizations[Manually creating long-term credentials for Azure]
* xref:../../installing/installing_gcp/installing-gcp-customizations.adoc#manually-create-iam_installing-gcp-customizations[Manually creating long-term credentials for GCP]
