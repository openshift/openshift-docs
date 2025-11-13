// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-google-identity-provider.adoc

[id="identity-provider-google-CR_{context}"]
= Sample Google CR

The following custom resource (CR) shows the parameters and acceptable
values for a Google identity provider.

.Google CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: googleidp <1>
    mappingMethod: claim <2>
    type: Google
    google:
      clientID: {...} <3>
      clientSecret: <4>
        name: google-secret
      hostedDomain: "example.com" <5>
----
<1> This provider name is prefixed to the Google numeric user ID to form an
identity name. It is also used to build the redirect URL.
<2> Controls how mappings are established between this provider's identities and `User` objects.
<3> The client ID of a link:https://console.developers.google.com/[registered
Google project]. The project must be configured with a redirect URI of
`\https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>`.
<4> Reference to an {product-title} `Secret` object containing the client secret
issued by Google.
<5> A
link:https://developers.google.com/identity/protocols/OpenIDConnect#hd-param[hosted domain]
used to restrict sign-in accounts. Optional if the `lookup` `mappingMethod`
is used. If empty, any Google account is allowed to authenticate.
