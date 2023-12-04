// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

:_mod-docs-content-type: REFERENCE

[id="gitops-release-notes-1-4-11_{context}"]
= Release notes for {gitops-title} 1.4.11

{gitops-title} 1.4.11 is now available on {product-title} 4.7, 4.8, 4.9, and 4.10.

[id="new-features-1-4-11_{context}"]
== New features

The current release adds the following improvements:

* With this update, the bundled Argo CD has been updated to version 2.2.12.

[id="fixed-issues-1-4-11_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, the `redis-ha-haproxy` pods of an ArgoCD instance failed when more restrictive SCCs were present in the cluster. This update fixes the issue by updating the security context in workloads. link:https://issues.redhat.com/browse/GITOPS-2034[GITOPS-2034]

[id="known-issues-1-4-11_{context}"]
== Known issues

*  {gitops-title} Operator can use RHSSO (KeyCloak) with OIDC and Dex. However, with a recent security fix applied, the Operator cannot validate the RHSSO certificate in some scenarios. link:https://issues.redhat.com/browse/GITOPS-2214[GITOPS-2214]
+
As a workaround, disable TLS validation for the OIDC (Keycloak/RHSSO) endpoint in the ArgoCD specification.
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  extraConfig:
    "admin.enabled": "true"
...
----