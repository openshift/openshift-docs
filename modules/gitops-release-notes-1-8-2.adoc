// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
:_mod-docs-content-type: REFERENCE
[id="gitops-release-notes-1-8-2_{context}"]
= Release notes for {gitops-title} 1.8.2

{gitops-title} 1.8.2 is now available on {product-title} 4.10, 4.11, 4.12, and 4.13.

[id="fixed-issues-1-8-2_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, when you configured Dex using the `.spec.dex` parameter and tried to log in to the Argo CD UI by using the *LOG IN VIA OPENSHIFT* option, you were not able to log in. This update fixes the issue.
+
[IMPORTANT]
====
The `spec.dex` parameter in the ArgoCD CR is deprecated. In a future release of {gitops-title} v1.9, configuring Dex using the `spec.dex` parameter in the ArgoCD CR is planned to be removed. Consider using the `.spec.sso` parameter instead. See "Enabling or disabling Dex using .spec.sso".  link:https://issues.redhat.com/browse/GITOPS-2761[GITOPS-2761]
====

* Before this update, the cluster and `kam` CLI pods failed to start with a new installation of {gitops-title} v1.8.0 on the {product-title} 4.10 cluster. This update fixes the issue and now all pods run as expected. link:https://issues.redhat.com/browse/GITOPS-2762[GITOPS-2762]