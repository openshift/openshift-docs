// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-2_{context}"]
= Release notes for {gitops-title} 1.4.2

[role="_abstract"]
{gitops-title} 1.4.2 is now available on {product-title} 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-4-2_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* Before this update, the *Route* resources got stuck in `Progressing` Health status if more than one `Ingress` were attached to the route.  This update fixes the health check and reports the correct health status of the *Route* resources. link:https://issues.redhat.com/browse/GITOPS-1751[GITOPS-1751]