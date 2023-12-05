// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
:_mod-docs-content-type: REFERENCE
[id="gitops-release-notes-1-8-3_{context}"]
= Release notes for {gitops-title} 1.8.3

{gitops-title} 1.8.3 is now available on {product-title} 4.10, 4.11, 4.12, and 4.13.

[id="errata-updates-1-8-3_{context}"]
== Errata updates

=== RHBA-2023:3206 and RHSA-2023:3229 - {gitops-title} 1.8.3 security update advisory

Issued: 2023-05-18

The list of security fixes that are included in this release is documented in the following advisories:

* link:https://access.redhat.com/errata/RHBA-2023:3206[RHBA-2023:3206]
* link:https://access.redhat.com/errata/RHSA-2023:3229[RHSA-2023:3229]

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

[id="fixed-issues-1-8-3_{context}"]
== Fixed issues

* Before this update, when `Autoscale` was enabled and the horizontal pod autoscaler (HPA) controller tried to edit the replica settings in server deployment, the Operator overwrote it. In addition, any changes specified to the autoscaler parameters were not propagated correctly to the HPA on the cluster. This update fixes the issue. Now the Operator reconciles on replica drift only if `Autoscale` is disabled and the HPA parameters are updated correctly. link:https://issues.redhat.com/browse/GITOPS-2629[GITOPS-2629]
