:_mod-docs-content-type: ASSEMBLY
[id="configuring-request-header-identity-provider"]
= Configuring a request header identity provider
include::_attributes/common-attributes.adoc[]
:context: configuring-request-header-identity-provider

toc::[]

Configure the `request-header` identity provider to identify users from request header values, such as `X-Remote-User`. It is typically used in combination with an authenticating proxy, which sets the request header value.

include::modules/identity-provider-overview.adoc[leveloffset=+1]

include::modules/identity-provider-about-request-header.adoc[leveloffset=+1]

include::modules/identity-provider-config-map.adoc[leveloffset=+1]

include::modules/identity-provider-request-header-CR.adoc[leveloffset=+1]

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See xref:../../authentication/understanding-identity-provider.adoc#identity-provider-parameters_understanding-identity-provider[Identity provider parameters] for information on parameters, such as `mappingMethod`, that are common to all identity providers.

include::modules/identity-provider-add.adoc[leveloffset=+1]

[id="example-apache-auth-config-using-request-header"]
== Example Apache authentication configuration using request header

This example configures an Apache authentication proxy for the {product-title}
using the request header identity provider.

[discrete]
include::modules/identity-provider-apache-custom-proxy-configuration.adoc[leveloffset=+2]

[discrete]
include::modules/identity-provider-configuring-apache-request-header.adoc[leveloffset=+2]
