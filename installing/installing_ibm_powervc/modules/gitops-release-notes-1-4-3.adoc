// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-3_{context}"]
= Release notes for {gitops-title} 1.4.3

[role="_abstract"]
{gitops-title} 1.4.3 is now available on {product-title} 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-4-3_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* Before this update, the TLS certificate in the `argocd-tls-certs-cm` configuration map was deleted by the {gitops-title} unless the certificate was configured in the ArgoCD CR specification `tls.initialCerts` field. This update fixes this issue. link:https://issues.redhat.com/browse/GITOPS-1725[GITOPS-1725]