:_mod-docs-content-type: ASSEMBLY
[id="configuring-github-identity-provider"]
= Configuring a GitHub or GitHub Enterprise identity provider
include::_attributes/common-attributes.adoc[]
:context: configuring-github-identity-provider

toc::[]

Configure the `github` identity provider to validate user names and passwords against GitHub or GitHub Enterprise's OAuth authentication server. OAuth facilitates a token exchange flow between {product-title} and GitHub or GitHub Enterprise.

You can use the GitHub integration to connect to either GitHub or GitHub Enterprise. For GitHub Enterprise integrations, you must provide the `hostname` of your instance and can optionally provide a `ca` certificate bundle to use in requests to the server.

[NOTE]
====
The following steps apply to both GitHub and GitHub Enterprise unless noted.
====

ifdef::openshift-origin,openshift-enterprise,openshift-webscale[]
include::modules/identity-provider-overview.adoc[leveloffset=+1]
endif::openshift-origin,openshift-enterprise,openshift-webscale[]

include::modules/identity-provider-github-about.adoc[leveloffset=+1]

include::modules/identity-provider-registering-github.adoc[leveloffset=+1]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
include::modules/identity-provider-secret.adoc[leveloffset=+1]

include::modules/identity-provider-config-map.adoc[leveloffset=+1]

include::modules/identity-provider-github-CR.adoc[leveloffset=+1]

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See xref:../../authentication/understanding-identity-provider.adoc#identity-provider-parameters_understanding-identity-provider[Identity provider parameters] for information on parameters, such as `mappingMethod`, that are common to all identity providers.

include::modules/identity-provider-add.adoc[leveloffset=+1]
endif::[]
