:_mod-docs-content-type: ASSEMBLY
[id="configuring-basic-authentication-identity-provider"]
= Configuring a basic authentication identity provider
include::_attributes/common-attributes.adoc[]
:context: configuring-basic-authentication-identity-provider

toc::[]

Configure the `basic-authentication` identity provider for users to log in to {product-title} with credentials validated against a remote identity provider. Basic authentication is a generic back-end integration mechanism.

include::modules/identity-provider-overview.adoc[leveloffset=+1]

include::modules/identity-provider-about-basic-authentication.adoc[leveloffset=+1]

include::modules/identity-provider-secret-tls.adoc[leveloffset=+1]

include::modules/identity-provider-config-map.adoc[leveloffset=+1]

include::modules/identity-provider-basic-authentication-CR.adoc[leveloffset=+1]

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See xref:../../authentication/understanding-identity-provider.adoc#identity-provider-parameters_understanding-identity-provider[Identity provider parameters] for information on parameters, such as `mappingMethod`, that are common to all identity providers.

include::modules/identity-provider-add.adoc[leveloffset=+1]

include::modules/example-apache-httpd-configuration.adoc[leveloffset=+1]

include::modules/identity-provider-basic-authentication-troubleshooting.adoc[leveloffset=+1]
