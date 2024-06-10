:_mod-docs-content-type: ASSEMBLY
[id="configuring-google-identity-provider"]
= Configuring a Google identity provider
include::_attributes/common-attributes.adoc[]
:context: configuring-google-identity-provider

toc::[]

Configure the `google` identity provider using the link:https://developers.google.com/identity/protocols/OpenIDConnect[Google OpenID Connect integration].

ifdef::openshift-origin,openshift-enterprise,openshift-webscale[]
include::modules/identity-provider-overview.adoc[leveloffset=+1]
endif::openshift-origin,openshift-enterprise,openshift-webscale[]

include::modules/identity-provider-google-about.adoc[leveloffset=+1]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
include::modules/identity-provider-secret.adoc[leveloffset=+1]

include::modules/identity-provider-google-CR.adoc[leveloffset=+1]

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See xref:../../authentication/understanding-identity-provider.adoc#identity-provider-parameters_understanding-identity-provider[Identity provider parameters] for information on parameters, such as `mappingMethod`, that are common to all identity providers.

include::modules/identity-provider-add.adoc[leveloffset=+1]
endif::[]
