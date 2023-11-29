:_mod-docs-content-type: ASSEMBLY
[id="understanding-identity-provider"]
= Understanding identity provider configuration
include::_attributes/common-attributes.adoc[]
:context: understanding-identity-provider

toc::[]

The {product-title} master includes a built-in OAuth server. Developers and
administrators obtain OAuth access tokens to authenticate themselves to the API.

As an administrator, you can configure OAuth to specify an identity provider
after you install your cluster.

include::modules/identity-provider-overview.adoc[leveloffset=+1]

[id="supported-identity-providers"]
== Supported identity providers

You can configure the following types of identity providers:

[cols="2a,8a",options="header"]
|===

|Identity provider
|Description

|xref:../authentication/identity_providers/configuring-htpasswd-identity-provider.adoc#configuring-htpasswd-identity-provider[htpasswd]
|Configure the `htpasswd` identity provider to validate user names and passwords
against a flat file generated using
link:http://httpd.apache.org/docs/2.4/programs/htpasswd.html[`htpasswd`].

|xref:../authentication/identity_providers/configuring-keystone-identity-provider.adoc#configuring-keystone-identity-provider[Keystone]
|Configure the `keystone` identity provider to integrate
your {product-title} cluster with Keystone to enable shared authentication with
an OpenStack Keystone v3 server configured to store users in an internal
database.

|xref:../authentication/identity_providers/configuring-ldap-identity-provider.adoc#configuring-ldap-identity-provider[LDAP]
|Configure the `ldap` identity provider to validate user names and passwords
against an LDAPv3 server, using simple bind authentication.

|xref:../authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc#configuring-basic-authentication-identity-provider[Basic authentication]
|Configure a `basic-authentication` identity provider for users to log in to
{product-title} with credentials validated against a remote identity provider.
Basic authentication is a generic backend integration mechanism.

|xref:../authentication/identity_providers/configuring-request-header-identity-provider.adoc#configuring-request-header-identity-provider[Request header]
|Configure a `request-header` identity provider to identify users from request
header values, such as `X-Remote-User`. It is typically used in combination with
an authenticating proxy, which sets the request header value.

|xref:../authentication/identity_providers/configuring-github-identity-provider.adoc#configuring-github-identity-provider[GitHub or GitHub Enterprise]
|Configure a `github` identity provider to validate user names and passwords
against GitHub or GitHub Enterprise's OAuth authentication server.

|xref:../authentication/identity_providers/configuring-gitlab-identity-provider.adoc#configuring-gitlab-identity-provider[GitLab]
|Configure a `gitlab` identity provider to use
link:https://gitlab.com/[GitLab.com] or any other GitLab instance as an identity
provider.

|xref:../authentication/identity_providers/configuring-google-identity-provider.adoc#configuring-google-identity-provider[Google]
|Configure a `google` identity provider using
link:https://developers.google.com/identity/protocols/OpenIDConnect[Google's OpenID Connect integration].

|xref:../authentication/identity_providers/configuring-oidc-identity-provider.adoc#configuring-oidc-identity-provider[OpenID Connect]
|Configure an `oidc` identity provider to integrate with an OpenID Connect
identity provider using an
link:http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth[Authorization Code Flow].

|===

Once an identity provider has been defined, you can
xref:../authentication/using-rbac.adoc#authorization-overview_using-rbac[use RBAC to define and apply permissions].

include::modules/authentication-remove-kubeadmin.adoc[leveloffset=+1]

include::modules/identity-provider-parameters.adoc[leveloffset=+1]

include::modules/identity-provider-default-CR.adoc[leveloffset=+1]
