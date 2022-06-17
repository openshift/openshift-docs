// Module is included in the following assemblies:
//
// * cicd/gitops/configuring-sso-for-argo-cd-on-openshift.adoc

[id="configuring-argo-cd-oidc_{context}"]
= Configuring Argo CD OIDC

To configure Argo CD OpenID Connect (OIDC), you must generate your client secret, encode it, and add it to your custom resource.

.Prerequisites

* You have obtained your client secret.

.Procedure

. Store the client secret you generated.

.. Encode the client secret in base64:
+
[source,terminal]
----
$ echo -n '83083958-8ec6-47b0-a411-a8c55381fbd2' | base64
----

.. Edit the secret and add the base64 value to an `oidc.keycloak.clientSecret` key:
+
[source,terminal]
----
$ oc edit secret argocd-secret -n <namespace>
----
+
.Example YAML of the secret
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: argocd-secret
data:
  oidc.keycloak.clientSecret: ODMwODM5NTgtOGVjNi00N2IwLWE0MTEtYThjNTUzODFmYmQy
----

. Edit the `argocd` custom resource and add the OIDC configuration to enable the Keycloak authentication:
+
[source,terminal]
----
$ oc edit argocd -n <your_namespace>
----
+
.Example of `argocd` custom resource
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  creationTimestamp: null
  name: argocd
  namespace: argocd
spec:
  resourceExclusions: |
    - apiGroups:
      - tekton.dev
      clusters:
      - '*'
      kinds:
      - TaskRun
      - PipelineRun
  oidcConfig: |
    name: OpenShift Single Sign-On
    issuer: https://keycloak.example.com/auth/realms/myrealm <1>
    clientID: argocd <2>
    clientSecret: $oidc.keycloak.clientSecret <3>
    requestedScopes: ["openid", "profile", "email", "groups"] <4>
  server:
    route:
      enabled: true
----
<1> `issuer` must end with the correct realm name (in this example `myrealm`).
<2> `clientID` is the Client ID you configured in your Keycloak account.
<3> `clientSecret` points to the right key you created in the argocd-secret secret.
<4> `requestedScopes` contains the groups claim if you did not add it to the Default scope.
