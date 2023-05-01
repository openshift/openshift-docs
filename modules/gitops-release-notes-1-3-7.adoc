// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-3-7_{context}"]
= Release notes for {gitops-title} 1.3.7

{gitops-title} 1.3.7 is now available on {product-title} 4.7, 4.8, 4.9, and 4.6 with limited GA support.

[id="fixed-issues-1-3-7_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* Before this update, a flaw was found in OpenSSL. This update fixes the issue by updating the base images to the latest version to avoid the OpenSSL flaw. link:https://access.redhat.com/security/cve/CVE-2022-0778[(CVE-2022-0778)].

[NOTE]
====
To install the current release of {gitops-title} 1.3 and receive further updates during its product life cycle, switch to the **GitOps-1.3** channel.
====
