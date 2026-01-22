// Module included in the following assemblies:
//
// * configuring-sso-for-argo-cd-using-keycloak.adoc

:_mod-docs-content-type: PROCEDURE
[id="gitops-creating-a-new-client-in-keycloak_{context}"]
= Configuring a new client in Keycloak

Dex is installed by default for all the Argo CD instances created by the Operator. However, you can delete the Dex configuration and add Keycloak instead to log in to Argo CD using your OpenShift credentials. Keycloak acts as an identity broker between Argo CD and OpenShift.

.Procedure

To configure Keycloak, follow these steps:

. Delete the Dex configuration by removing the `.spec.sso.dex` parameter from the Argo CD custom resource (CR), and save the CR:
+
[source,yaml]
----
dex:
    openShiftOAuth: true
    resources:
      limits:
        cpu:
        memory:
      requests:
        cpu:
        memory:
----

. Set the value of the `provider` parameter to `keycloak` in the Argo CD CR.

. Configure Keycloak by performing one of the following steps:

* For a secure connection, set the value of the `rootCA` parameter as shown in the following example:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  sso:
    provider: keycloak
    keycloak:
      rootCA: "<PEM-encoded-root-certificate>" <1>
  server:
    route:
      enabled: true
----
<1> A custom certificate used to verify the Keycloak's TLS certificate.
+
The Operator reconciles changes in the `.spec.keycloak.rootCA` parameter and updates the `oidc.config` parameter with the PEM encoded root certificate in the `argocd-cm` configuration map.

* For an insecure connection, leave the value of the `rootCA` parameter empty and use the `oidc.tls.insecure.skip.verify` parameter as shown below:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  extraConfig:
    oidc.tls.insecure.skip.verify: "true"
  sso:
    provider: keycloak
    keycloak:
      rootCA: ""
----

[NOTE]
====
The Keycloak instance takes 2-3 minutes to install and run.
====

