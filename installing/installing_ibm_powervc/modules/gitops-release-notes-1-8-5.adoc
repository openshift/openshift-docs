// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

:_mod-docs-content-type: REFERENCE

[id="gitops-release-notes-1-8-5_{context}"]
= Release notes for {gitops-title} 1.8.5

{gitops-title} 1.8.5 is now available on {product-title} 4.10, 4.11, 4.12, and 4.13.

[id="errata-updates-1-8-5_{context}"]
== Errata updates

[id="rhsa-2023-5030-gitops-1-8-5-security-update-advisory_{context}"]
=== RHSA-2023:5030 - {gitops-title} 1.8.5 security update advisory

Issued: 2023-09-08

The list of security fixes that are included in this release is documented in the following advisory:

* link:https://access.redhat.com/errata/RHSA-2023:5030[RHSA-2023:5030]

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

