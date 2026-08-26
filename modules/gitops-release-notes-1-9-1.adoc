// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

:_mod-docs-content-type: REFERENCE

[id="gitops-release-notes-1-9-1_{context}"]
= Release notes for {gitops-title} 1.9.1

{gitops-title} 1.9.1 is now available on {product-title} 4.12 and 4.13.

[id="errata-updates-1-9-1_{context}"]
== Errata updates

=== RHSA-2023:3591 and RHBA-2023:4117 - {gitops-title} 1.9.1 security update advisory

Issued: 2023-07-17

The list of security fixes that are included in this release is documented in the following advisories:

* link:https://access.redhat.com/errata/RHSA-2023:3591[RHSA-2023:3591]
* link:https://access.redhat.com/errata/RHBA-2023:4117[RHBA-2023:4117]

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

[id="new-features-1-9-1_{context}"]
== New features

The current release adds the following improvements:

* With this update, the bundled Argo CD has been updated to version 2.7.6.

[id="fixed-issues-1-9-1_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, Argo CD was becoming unresponsive when there was an increase in namespaces and applications. This update fixes the issue by removing a deadlock. Deadlock occurs when two functions are competing for resources. Now, you should not experience crashes or unresponsiveness when there is an increase in namespaces or applications. link:https://issues.redhat.com/browse/GITOPS-2782[GITOPS-2782]

* Before this update, the Argo CD application controller resource could suddenly stop working when resynchronizing applications. This update fixes the issue by adding logic to prevent a cluster cache deadlock. Now, you should not experience the deadlock situation, and applications should resynchronize successfully. link:https://issues.redhat.com/browse/GITOPS-2880[GITOPS-2880]

* Before this update, there was a mismatch in the RSA key for known hosts in the `argocd-ssh-known-hosts-cm` config map. This update fixes the issue by matching the RSA key with the upstream project. Now, you can use the default RSA keys on default deployments. link:https://issues.redhat.com/browse/GITOPS-3042[GITOPS-3042]

* Before this update, the reconciliation timeout setting in the `argocd-cm` config map was not being correctly applied to the Argo CD application controller resource. This update fixes the issue by correctly reading and applying the reconciliation timeout setting from the `argocd-cm` config map. Now, you can modify the reconciliation timeout value from the `AppSync` setting without a problem. link:https://issues.redhat.com/browse/GITOPS-2810[GITOPS-2810]
