// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
:_mod-docs-content-type: REFERENCE

[id="gitops-release-notes-1-7-1_{context}"]
= Release notes for {gitops-title} 1.7.1

{gitops-title} 1.7.1 is now available on {product-title} 4.10, 4.11, and 4.12.

[id="errata-updates-1-7-1_{context}"]
== Errata updates

=== RHSA-2023:0467 - {gitops-title} 1.7.1 security update advisory

Issued: 2023-01-25

The list of security fixes that are included in this release is documented in the link:https://access.redhat.com/errata/RHSA-2023:0467[RHSA-2023:0467] advisory.

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----
