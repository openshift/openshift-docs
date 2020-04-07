// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-allow-all-identity-provider.adoc
// * authentication/identity_providers/configuring-deny-all-identity-provider.adoc
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc
// * authentication/identity_providers/configuring-keystone-identity-provider.adoc
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc
// * authentication/identity_providers/configuring-github-identity-provider.adoc
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc
// * authentication/identity_providers/configuring-google-identity-provider.adoc
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc

[id="identity-provider-create-CR_{context}"]
= Creating the CR that describes an identity provider

Before you can add an identity provider to your cluster, create a Custom
Resource (CR) that describes it.

.Prerequisites

* Create an {product-title} cluster.

.Procedure

Create a CR file to describe the identity provider. A generic file displaying
the structure is below.

----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: my_identity_provider <1>
    mappingMethod: claim <2>
    type: <type> <3>
    ...
----
<1> A unique name defining the identity provider. This provider name is
prefixed to provider user names to form an identity name.
<2> Controls how mappings are established between this provider's identities and user objects.
<3> The type of identity provider to be configured.
+
Provide the parameters that are required for your identity provider type.
