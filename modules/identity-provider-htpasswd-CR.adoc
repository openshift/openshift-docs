// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc

[id="identity-provider-htpasswd-CR_{context}"]
= Sample htpasswd CR

The following custom resource (CR) shows the parameters and acceptable values for an
htpasswd identity provider.

.htpasswd CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: my_htpasswd_provider <1>
    mappingMethod: claim <2>
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret <3>
----
<1> This provider name is prefixed to provider user names to form an identity
name.
<2> Controls how mappings are established between this provider's identities and `User` objects.
<3> An existing secret containing a file generated using
link:http://httpd.apache.org/docs/2.4/programs/htpasswd.html[`htpasswd`].
