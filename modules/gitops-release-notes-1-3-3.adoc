// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-3-3_{context}"]
= Release notes for {gitops-title} 1.3.3

{gitops-title} 1.3.3 is now available on {product-title} 4.7, 4.8, 4.9, and 4.6 with limited GA support.

[id="fixed-issues-1-3-3_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* All versions of Argo CD are vulnerable to a path traversal bug that allows to pass arbitrary values to be consumed by Helm charts. This update fixes the `CVE-2022-24348 gitops` error, path traversal and dereference of symlinks when passing Helm value files. link:https://issues.redhat.com/browse/GITOPS-1756[GITOPS-1756]