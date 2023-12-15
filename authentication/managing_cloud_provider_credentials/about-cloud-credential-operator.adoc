:_mod-docs-content-type: ASSEMBLY
[id="about-cloud-credential-operator"]
= About the Cloud Credential Operator
include::_attributes/common-attributes.adoc[]
:context: about-cloud-credential-operator

toc::[]

The Cloud Credential Operator (CCO) manages cloud provider credentials as  custom resource definitions (CRDs). The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow {product-title} components to request cloud provider credentials with the specific permissions that are required for the cluster to run.

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in several different modes. If no mode is specified, or the `credentialsMode` parameter is set to an empty string (`""`), the CCO operates in its default mode.

[id="about-cloud-credential-operator-modes_{context}"]
== Modes

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in _mint_, _passthrough_, or _manual_ mode. These options provide transparency and flexibility in how the CCO uses cloud credentials to process `CredentialsRequest` CRs in the cluster, and allow the CCO to be configured to suit the security requirements of your organization. Not all CCO modes are supported for all cloud providers.

* **xref:../../authentication/managing_cloud_provider_credentials/cco-mode-mint.adoc#cco-mode-mint[Mint]**: In mint mode, the CCO uses the provided admin-level cloud credential to create new credentials for components in the cluster with only the specific permissions that are required.

* **xref:../../authentication/managing_cloud_provider_credentials/cco-mode-passthrough.adoc#cco-mode-passthrough[Passthrough]**: In passthrough mode, the CCO passes the provided cloud credential to the components that request cloud credentials.

* **xref:../../authentication/managing_cloud_provider_credentials/cco-mode-manual.adoc#cco-mode-manual[Manual mode with long-term credentials for components]**: In manual mode, you can manage long-term cloud credentials instead of the CCO.

* **xref:../../authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc#cco-short-term-creds[Manual mode with short-term credentials for components]**: For some providers, you can use the CCO utility (`ccoctl`) during installation to implement short-term credentials for individual components. These credentials are created and managed outside the {product-title} cluster.

.CCO mode support matrix
[cols="<.^2,^.^1,^.^1,^.^1,^.^1"]
|====
|Cloud provider |Mint |Passthrough |Manual with long-term credentials |Manual with short-term credentials

|{alibaba}
|
|
|X ^[1]^
|

|Amazon Web Services (AWS)
|X
|X
|X
|X

|Global Microsoft Azure
|
|X
|X
|X

|Microsoft Azure Stack Hub
|
|
|X
|

|Google Cloud Platform (GCP)
|X
|X
|X
|X

|{ibm-cloud-name}
|
|
|X ^[1]^
|

|Nutanix
|
|
|X ^[1]^
|

|{rh-openstack-first}
|
|X
|
|

|VMware vSphere
|
|X
|
|

|====
[.small]
--
1. This platform uses the `ccoctl` utility during installation to configure long-term credentials.
--

[id="cco-determine-mode_{context}"]
== Determining the Cloud Credential Operator mode

For platforms that support using the CCO in multiple modes, you can determine what mode the CCO is configured to use by using the web console or the CLI.

.Determining the CCO configuration
image::334_OpenShift_cluster_updating_and_CCO_workflows_0923_4.11_A.png[Decision tree showing how to determine the configured CCO credentials mode for your cluster.]

//Determining the Cloud Credential Operator mode by using the web console
include::modules/cco-determine-mode-gui.adoc[leveloffset=+2]

//Determining the Cloud Credential Operator mode by using the CLI
include::modules/cco-determine-mode-cli.adoc[leveloffset=+2]

[id="about-cloud-credential-operator-default_{context}"]
== Default behavior
For platforms on which multiple modes are supported (AWS, Azure, and GCP), when the CCO operates in its default mode, it checks the provided credentials dynamically to determine for which mode they are sufficient to process `CredentialsRequest` CRs.

By default, the CCO determines whether the credentials are sufficient for mint mode, which is the preferred mode of operation, and uses those credentials to create appropriate credentials for components in the cluster. If the credentials are not sufficient for mint mode, it determines whether they are sufficient for passthrough mode. If the credentials are not sufficient for passthrough mode, the CCO cannot adequately process `CredentialsRequest` CRs.

If the provided credentials are determined to be insufficient during installation, the installation fails. For AWS, the installation program fails early in the process and indicates which required permissions are missing. Other providers might not provide specific information about the cause of the error until errors are encountered.

If the credentials are changed after a successful installation and the CCO determines that the new credentials are insufficient, the CCO puts conditions on any new `CredentialsRequest` CRs to indicate that it cannot process them because of the insufficient credentials.

To resolve insufficient credentials issues, provide a credential with sufficient permissions. If an error occurred during installation, try installing again. For issues with new `CredentialsRequest` CRs, wait for the CCO to try to process the CR again. As an alternative, you can configure your cluster to use a different CCO mode that is supported for your cloud provider.

[role="_additional-resources"]
[id="additional-resources_about-cloud-credential-operator_{context}"]
== Additional resources

* xref:../../operators/operator-reference.adoc#cloud-credential-operator_cluster-operators-ref[Cluster Operators reference page for the Cloud Credential Operator]
