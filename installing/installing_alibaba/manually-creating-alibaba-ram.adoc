:_mod-docs-content-type: ASSEMBLY
[id="manually-creating-alibaba-ram"]
= Creating the required Alibaba Cloud resources
include::_attributes/common-attributes.adoc[]
:context: manually-creating-alibaba-ram

toc::[]

Before you install {product-title}, you must use the Alibaba Cloud console to create a Resource Access Management (RAM) user that has sufficient permissions to install {product-title} into your Alibaba Cloud. This user must also have permissions to create new RAM users. You can also configure and use the `ccoctl` tool to create new credentials for the {product-title} components with the permissions that they require.

:FeatureName: Alibaba Cloud on {product-title}
include::snippets/technology-preview.adoc[]

//Task part 1: Manually creating the required RAM user
include::modules/manually-creating-alibaba-ram-user.adoc[leveloffset=+1]

//Task part 2: Configuring the Cloud Credential Operator utility
include::modules/cco-ccoctl-configuring.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../../updating/preparing_for_updates/preparing-manual-creds-update.adoc#preparing-manual-creds-update[Preparing to update a cluster with manually maintained credentials]

//Task part 3: Creating Alibaba resources with a single command
// modules/cco-ccoctl-creating-at-once.adoc[leveloffset=+1]

[id="next-steps_manually-creating-alibaba-ram"]
== Next steps

* Install a cluster on Alibaba Cloud infrastructure that is provisioned by the {product-title} installation program, by using one of the following methods:

** **xref:../../installing/installing_alibaba/installing-alibaba-default.adoc#installing-alibaba-default[Installing a cluster quickly on Alibaba Cloud]**: You can install a cluster quickly by using the default configuration options.

** **xref:../../installing/installing_alibaba/installing-alibaba-customizations.adoc#installing-alibaba-customizations[Installing a customized cluster on Alibaba Cloud]**: The installation program allows for some customization to be applied at the installation stage. Many other customization options are available xref:../../post_installation_configuration/cluster-tasks.adoc#post-install-cluster-tasks[post-installation].

