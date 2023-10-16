// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc

[id="identity-provider-oidc-about_{context}"]
= About OpenID Connect authentication

The Authentication Operator in {product-title} requires that the configured OpenID Connect identity provider implements the link:https://openid.net/specs/openid-connect-discovery-1_0.html[OpenID Connect Discovery] specification.

ifdef::openshift-origin[]
You can link:https://www.keycloak.org/docs/latest/server_admin/index.html#openshift[configure a Keycloak] server as an OpenID Connect identity provider for {product-title}.
endif::[]

[NOTE]
====
`ID Token` and `UserInfo` decryptions are not supported.
====

By default, the `openid` scope is requested. If required, extra scopes can be specified in the `extraScopes` field.

Claims are read from the JWT `id_token` returned from the OpenID identity provider and, if specified, from the JSON returned by the `UserInfo` URL.

At least one claim must be configured to use as the user's identity. The standard identity claim is `sub`.

You can also indicate which claims to use as the user's preferred user name, display name, and email address. If multiple claims are specified, the first one with a non-empty value is used. The following table lists the standard claims:

[cols="1,2",options="header"]
|===

|Claim
|Description

|`sub`
|Short for "subject identifier." The remote identity for the user at the
issuer.

|`preferred_username`
|The preferred user name when provisioning a user. A shorthand name that the user wants to be referred to as, such as `janedoe`. Typically a value that corresponding to the user's login or username in the authentication system, such as username or email.

|`email`
|Email address.

|`name`
|Display name.
|===

See the link:http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims[OpenID claims documentation] for more information.

[NOTE]
====
Unless your OpenID Connect identity provider supports the resource owner password credentials (ROPC) grant flow, users must get a token from `<namespace_route>/oauth/token/request` to use with command-line tools.
====
