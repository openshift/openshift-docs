:_mod-docs-content-type: ASSEMBLY
[id="configuring-oauth-clients"]
= Configuring OAuth clients
include::_attributes/common-attributes.adoc[]
:context: configuring-oauth-clients

toc::[]

Several OAuth clients are created by default in {product-title}. You can also register and configure additional OAuth clients.

// Default OAuth clients
include::modules/oauth-default-clients.adoc[leveloffset=+1]

// Register an additional OAuth client
include::modules/oauth-register-additional-client.adoc[leveloffset=+1]

// Configuring token inactivity timeout for OAuth clients
include::modules/oauth-configuring-token-inactivity-timeout-clients.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources

* xref:../rest_api/oauth_apis/oauthclient-oauth-openshift-io-v1.adoc#oauthclient-oauth-openshift-io-v1[OAuthClient [oauth.openshift.io/v1]]
