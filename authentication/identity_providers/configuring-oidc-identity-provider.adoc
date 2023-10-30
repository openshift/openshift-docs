:_mod-docs-content-type: ASSEMBLY
[id="configuring-oidc-identity-provider"]
= Configuring an OpenID Connect identity provider
include::_attributes/common-attributes.adoc[]
:context: configuring-oidc-identity-provider

toc::[]

Configure the `oidc` identity provider to integrate with an OpenID Connect identity provider using an link:http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth[Authorization Code Flow].

ifdef::openshift-origin,openshift-enterprise,openshift-webscale[]
include::modules/identity-provider-overview.adoc[leveloffset=+1]
endif::openshift-origin,openshift-enterprise,openshift-webscale[]

include::modules/identity-provider-oidc-about.adoc[leveloffset=+1]

ifdef::openshift-enterprise[]
include::modules/identity-provider-oidc-supported.adoc[leveloffset=+1]
endif::openshift-enterprise[]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
include::modules/identity-provider-secret.adoc[leveloffset=+1]

include::modules/identity-provider-config-map.adoc[leveloffset=+1]

include::modules/identity-provider-oidc-CR.adoc[leveloffset=+1]

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See xref:../../authentication/understanding-identity-provider.adoc#identity-provider-parameters_understanding-identity-provider[Identity provider parameters] for information on parameters, such as `mappingMethod`, that are common to all identity providers.

include::modules/identity-provider-add.adoc[leveloffset=+1]

include::modules/identity-provider-configuring-using-web-console.adoc[leveloffset=+1]
endif::[]
