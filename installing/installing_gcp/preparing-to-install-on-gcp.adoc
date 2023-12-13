:_mod-docs-content-type: ASSEMBLY
[id="preparing-to-install-on-gcp"]
= Preparing to install on GCP
include::_attributes/common-attributes.adoc[]
:context: preparing-to-install-on-gcp

toc::[]

[id="{context}-prerequisites"]
== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.

* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].

[id="requirements-for-installing-ocp-on-gcp"]
== Requirements for installing {product-title} on GCP

Before installing {product-title} on Google Cloud Platform (GCP), you must create a service account and configure a GCP project. See xref:../../installing/installing_gcp/installing-gcp-account.adoc#installing-gcp-account[Configuring a GCP project] for details about creating a project, enabling API services, configuring DNS, GCP account limits, and supported GCP regions.

If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, see xref:../../installing/installing_gcp/installing-gcp-customizations.adoc#manually-create-iam_installing-gcp-customizations[Manually creating long-term credentials for GCP] for other options.

[id="choosing-an-method-to-install-ocp-on-gcp"]
== Choosing a method to install {product-title} on GCP

You can install {product-title} on installer-provisioned or user-provisioned infrastructure. The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster. You can also install {product-title} on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

See xref:../../architecture/architecture-installation.adoc#installation-process_architecture-installation[Installation process] for more information about installer-provisioned and user-provisioned installation processes.

[id="choosing-an-method-to-install-ocp-on-gcp-installer-provisioned"]
=== Installing a cluster on installer-provisioned infrastructure

You can install a cluster on GCP infrastructure that is provisioned by the {product-title} installation program, by using one of the following methods:

* **xref:../../installing/installing_gcp/installing-gcp-default.adoc#installing-gcp-default[Installing a cluster quickly on GCP]**: You can install {product-title} on GCP infrastructure that is provisioned by the {product-title} installation program. You can install a cluster quickly by using the default configuration options.

* **xref:../../installing/installing_gcp/installing-gcp-customizations.adoc#installing-gcp-customizations[Installing a customized cluster on GCP]**: You can install a customized cluster on GCP infrastructure that the installation program provisions. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available xref:../../post_installation_configuration/cluster-tasks.adoc#post-install-cluster-tasks[post-installation].

* **xref:../../installing/installing_gcp/installing-gcp-network-customizations.adoc#installing-gcp-network-customizations[Installing a cluster on GCP with network customizations]**: You can customize your {product-title} network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements.

* **xref:../../installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc#installing-restricted-networks-gcp-installer-provisioned[Installing a cluster on GCP in a restricted network]**: You can install {product-title} on GCP on installer-provisioned infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. While you can install {product-title} by using the mirrored content, your cluster still requires internet access to use the GCP APIs.

* **xref:../../installing/installing_gcp/installing-gcp-vpc.adoc#installing-gcp-vpc[Installing a cluster into an existing Virtual Private Cloud]**: You can install {product-title} on an existing GCP Virtual Private Cloud (VPC). You can use this installation method if you have constraints set by the guidelines of your company, such as limits on creating new accounts or infrastructure.

* **xref:../../installing/installing_gcp/installing-gcp-private.adoc#installing-gcp-private[Installing a private cluster on an existing VPC]**: You can install a private cluster on an existing GCP VPC. You can use this method to deploy {product-title} on an internal network that is not visible to the internet.

[id="choosing-an-method-to-install-ocp-on-gcp-user-provisioned"]
=== Installing a cluster on user-provisioned infrastructure

You can install a cluster on GCP infrastructure that you provision, by using one of the following methods:

* **xref:../../installing/installing_gcp/installing-gcp-user-infra.adoc#installing-gcp-user-infra[Installing a cluster on GCP with user-provisioned infrastructure]**: You can install {product-title} on GCP infrastructure that you provide. You can use the provided Deployment Manager templates to assist with the installation.

* **xref:../../installing/installing_gcp/installing-gcp-user-infra-vpc.adoc#installing-gcp-user-infra-vpc[Installing a cluster with shared VPC on user-provisioned infrastructure in GCP]**: You can use the provided Deployment Manager templates to create GCP resources in a shared VPC infrastructure.

* **xref:../../installing/installing_gcp/installing-restricted-networks-gcp.adoc#installing-restricted-networks-gcp[Installing a cluster on GCP in a restricted network with user-provisioned infrastructure]**: You can install {product-title} on GCP in a restricted network with user-provisioned infrastructure. By creating an internal mirror of the installation release content, you can install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

[id="preparing-to-install-on-gcp-next-steps"]
== Next steps

* xref:../../installing/installing_gcp/installing-gcp-account.adoc#installing-gcp-account[Configuring a GCP project]
