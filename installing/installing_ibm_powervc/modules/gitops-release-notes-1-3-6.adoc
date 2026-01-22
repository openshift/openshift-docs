// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-3-6_{context}"]
= Release notes for {gitops-title} 1.3.6

{gitops-title} 1.3.6 is now available on {product-title} 4.7, 4.8, 4.9, and 4.6 with limited GA support.

[id="fixed-issues-1-3-6_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* In {gitops-title}, improper access control allows admin privilege escalation link:https://access.redhat.com/security/cve/CVE-2022-1025[(CVE-2022-1025)]. This update fixes the issue.

* A path traversal flaw allows leaking of out-of-bound files link:https://access.redhat.com/security/cve/CVE-2022-24731[(CVE-2022-24731)]. This update fixes the issue.

* A path traversal flaw and improper access control allows leaking of out-of-bound files link:https://access.redhat.com/security/cve/CVE-2022-24730[(CVE-2022-24730)]. This update fixes the issue.

