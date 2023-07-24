// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-2-2_{context}"]
= Release notes for {gitops-title} 1.2.2

{gitops-title} 1.2.2 is now available on {product-title} 4.8.

[id="fixed-issues-1-2-2_{context}"]
== Fixed issues
The following issue was resolved in the current release:

* All versions of Argo CD are vulnerable to a path traversal bug that allows to pass arbitrary values to be consumed by Helm charts. This update fixes the CVE-2022-24348 gitops error, path traversal and dereference of symlinks when passing Helm value files.
link:https://issues.redhat.com/browse/GITOPS-1756[GITOPS-1756]