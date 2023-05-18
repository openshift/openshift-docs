// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc

[id="identity-provider-oidc-supported_{context}"]
= Supported OIDC providers

Red Hat tests and supports specific OpenID Connect (OIDC) providers with {product-title}. The following OpenID Connect (OIDC) providers are tested and supported with {product-title}. Using an OIDC provider that is not on the following list might work with {product-title}, but the provider was not tested by Red Hat and therefore is not supported by Red Hat.

* Active Directory Federation Services for Windows Server
+
[NOTE]
====
Currently, it is not supported to use Active Directory Federation Services for Windows Server with {product-title} when custom claims are used.
====
* GitLab
* Google
* Keycloak
* Microsoft identity platform (Azure Active Directory v2.0)
+
[NOTE]
====
Currently, it is not supported to use Microsoft identity platform when group names are required to be synced.
====
* Okta
* Ping Identity
* Red Hat Single Sign-On
