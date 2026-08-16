:_mod-docs-content-type: ASSEMBLY
[id="configuring-keystone-identity-provider"]
= Configuring a Keystone identity provider
include::_attributes/common-attributes.adoc[]
:context: configuring-keystone-identity-provider

toc::[]

Configure the `keystone` identity provider to integrate your {product-title} cluster with Keystone to enable shared authentication with an OpenStack Keystone v3 server configured to store users in an internal database. This configuration allows users to log in to {product-title} with their Keystone credentials.

include::modules/identity-provider-overview.adoc[leveloffset=+1]

include::modules/identity-provider-keystone-about.adoc[leveloffset=+1]

include::modules/identity-provider-secret-tls.adoc[leveloffset=+1]

include::modules/identity-provider-config-map.adoc[leveloffset=+1]

include::modules/identity-provider-keystone-CR.adoc[leveloffset=+1]

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See xref:../../authentication/understanding-identity-provider.adoc#identity-provider-parameters_understanding-identity-provider[Identity provider parameters] for information on parameters, such as `mappingMethod`, that are common to all identity providers.

include::modules/identity-provider-add.adoc[leveloffset=+1]
