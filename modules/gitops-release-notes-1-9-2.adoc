// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

:_mod-docs-content-type: REFERENCE

[id="gitops-release-notes-1-9-2_{context}"]
= Release notes for {gitops-title} 1.9.2

{gitops-title} 1.9.2 is now available on {product-title} 4.12 and 4.13.

[id="errata-updates-1-9-2_{context}"]
== Errata updates

[id="rhsa-2023-5029-gitops-1-9-2-security-update-advisory_{context}"]
=== RHSA-2023:5029 - {gitops-title} 1.9.2 security update advisory

Issued: 2023-09-08

The list of security fixes that are included in this release is documented in the following advisory:

* link:https://access.redhat.com/errata/RHSA-2023:5029[RHSA-2023:5029]

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

[id="fixed-issues-1-9-2_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* Before this update, an old Redis image version was used when deploying the {gitops-title} Operator, which resulted in vulnerabilities. This update fixes the vulnerabilities on Redis by upgrading it to the latest version of the `registry.redhat.io/rhel-8/redis-6` image. link:https://issues.redhat.com/browse/GITOPS-3069[GITOPS-3069]

