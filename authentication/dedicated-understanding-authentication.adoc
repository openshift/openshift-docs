:_mod-docs-content-type: ASSEMBLY
[id="understanding-identity-provider"]
= Understanding identity provider configuration
include::_attributes/common-attributes.adoc[]
:context: understanding-identity-provider

toc::[]

include::modules/identity-provider-parameters.adoc[leveloffset=+1]

[id="supported-identity-providers"]
== Supported identity providers

You can configure the following types of identity providers:

[cols="2a,8a",options="header"]
|===

|Identity provider
|Description

|xref:../authentication/identity_providers/configuring-ldap-identity-provider.adoc#configuring-ldap-identity-provider[LDAP]
|Configure the `ldap` identity provider to validate user names and passwords
against an LDAPv3 server, using simple bind authentication.

|xref:../authentication/identity_providers/configuring-github-identity-provider.adoc#configuring-github-identity-provider[GitHub or GitHub Enterprise]
|Configure a `github` identity provider to validate user names and passwords
against GitHub or GitHub Enterprise's OAuth authentication server.

|xref:../authentication/identity_providers/configuring-google-identity-provider.adoc#configuring-google-identity-provider[Google]
|Configure a `google` identity provider using
link:https://developers.google.com/identity/protocols/OpenIDConnect[Google's OpenID Connect integration].

|xref:../authentication/identity_providers/configuring-oidc-identity-provider.adoc#configuring-oidc-identity-provider[OpenID Connect]
|Configure an `oidc` identity provider to integrate with an OpenID Connect
identity provider using an
link:http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth[Authorization Code Flow].

|===
