:_mod-docs-content-type: ASSEMBLY
[id="configuring-htpasswd-identity-provider"]
= Configuring an htpasswd identity provider
include::_attributes/common-attributes.adoc[]
:context: configuring-htpasswd-identity-provider

toc::[]

Configure the `htpasswd` identity provider to allow users to log in to {product-title} with credentials from an htpasswd file.

To define an htpasswd identity provider, perform the following tasks:

. xref:../../authentication/identity_providers/configuring-htpasswd-identity-provider.adoc#creating-htpasswd-file[Create an `htpasswd` file] to store the user and password information.
. xref:../../authentication/identity_providers/configuring-htpasswd-identity-provider.adoc#identity-provider-creating-htpasswd-secret_{context}[Create
a secret] to represent the `htpasswd` file.
. xref:../../authentication/identity_providers/configuring-htpasswd-identity-provider.adoc#identity-provider-htpasswd-CR_{context}[Define an htpasswd identity provider resource] that references the secret.
. xref:../../authentication/identity_providers/configuring-htpasswd-identity-provider.adoc#add-identity-provider_{context}[Apply the resource] to
the default OAuth configuration to add the identity provider.

ifdef::openshift-origin,openshift-enterprise,openshift-webscale[]
include::modules/identity-provider-overview.adoc[leveloffset=+1]
endif::openshift-origin,openshift-enterprise,openshift-webscale[]

include::modules/identity-provider-htpasswd-about.adoc[leveloffset=+1]

[id="creating-htpasswd-file"]
== Creating the htpasswd file

See one of the following sections for instructions about how to create the htpasswd file:

* xref:../../authentication/identity_providers/configuring-htpasswd-identity-provider.adoc#identity-provider-creating-htpasswd-file-linux_configuring-htpasswd-identity-provider[Creating an htpasswd file using Linux]
* xref:../../authentication/identity_providers/configuring-htpasswd-identity-provider.adoc#identity-provider-creating-htpasswd-file-windows_configuring-htpasswd-identity-provider[Creating an htpasswd file using Windows]

include::modules/identity-provider-creating-htpasswd-file-linux.adoc[leveloffset=+2]

include::modules/identity-provider-creating-htpasswd-file-windows.adoc[leveloffset=+2]

include::modules/identity-provider-htpasswd-secret.adoc[leveloffset=+1]

include::modules/identity-provider-htpasswd-CR.adoc[leveloffset=+1]

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See xref:../../authentication/understanding-identity-provider.adoc#identity-provider-parameters_understanding-identity-provider[Identity provider parameters] for information on parameters, such as `mappingMethod`, that are common to all identity providers.

include::modules/identity-provider-add.adoc[leveloffset=+1]

include::modules/identity-provider-htpasswd-update-users.adoc[leveloffset=+1]

include::modules/identity-provider-configuring-using-web-console.adoc[leveloffset=+1]
