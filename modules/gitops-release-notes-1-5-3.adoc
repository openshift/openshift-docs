// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

:_mod-docs-content-type: REFERENCE

[id="gitops-release-notes-1-5-3_{context}"]
= Release notes for {gitops-title} 1.5.3

{gitops-title} 1.5.3 is now available on {product-title} 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-5-3_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, all unpatched versions of Argo CD v1.0.0 and later were vulnerable to a cross-site scripting bug. As a result, an unauthorized user would be able to inject a javascript link in the UI. This issue is now fixed. link:https://bugzilla.redhat.com/show_bug.cgi?id=2096278[CVE-2022-31035]

* Before this update, all versions of Argo CD v0.11.0 and later were vulnerable to multiple attacks when SSO login was initiated from the Argo CD CLI or the UI. This issue is now fixed. link:https://bugzilla.redhat.com/show_bug.cgi?id=2096282[CVE-2022-31034]

* Before this update, all unpatched versions of Argo CD v0.7 and later were vulnerable to a memory consumption bug. As a result, an unauthorized user would be able to crash the Argo CD's repo-server. This issue is now fixed. link:https://bugzilla.redhat.com/show_bug.cgi?id=2096283[CVE-2022-31016]

* Before this update, all unpatched versions of Argo CD v1.3.0 and later were vulnerable to a symlink-following bug. As a result, an unauthorized user with repository write access would be able to leak sensitive YAML files from Argo CD's repo-server. This issue is now fixed. link:https://bugzilla.redhat.com/show_bug.cgi?id=2096291[CVE-2022-31036]