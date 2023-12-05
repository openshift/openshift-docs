// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
:_mod-docs-content-type: REFERENCE

[id="gitops-release-notes-1-7-0_{context}"]
= Release notes for {gitops-title} 1.7.0

{gitops-title} 1.7.0 is now available on {product-title} 4.10, 4.11, and 4.12.

[id="new-features-1-7-0_{context}"]
== New features

The current release adds the following improvements:

* With this update, you can add environment variables to the Notifications controller. link:https://issues.redhat.com/browse/GITOPS-2313[GITOPS-2313]

* With this update, the default nodeSelector `"kubernetes.io/os": "linux"` key-value pair is added to all workloads such that they only schedule on Linux nodes. In addition, any custom node selectors are added to the default and take precedence if they have the same key. link:https://issues.redhat.com/browse/GITOPS-2215[GITOPS-2215]

* With this update, you can set custom node selectors in the Operator workloads by editing their `GitopsService` custom resource. link:https://issues.redhat.com/browse/GITOPS-2164[GITOPS-2164]

* With this update, you can use the RBAC policy matcher mode to select from the following options: `glob` (default) and `regex`.link:https://issues.redhat.com/browse/GITOPS-1975[GITOPS-1975]

* With this update, you can customize resource behavior using the following additional subkeys:
+
[options=header]
|===
| Subkey | Key form | Mapped field in argocd-cm
| resourceHealthChecks | resource.customizations.health.<group_kind> | resource.customizations.health
| resourceIgnoreDifferences | resource.customizations.ignoreDifferences.<group_kind> | resource.customizations.ignoreDifferences
| resourceActions | resource.customizations.actions.<group_kind> | resource.customizations.actions
|===
+
link:https://issues.redhat.com/browse/GITOPS-1561[GITOPS-1561]
+
[NOTE]
====
In future releases, there is a possibility to deprecate the old method of customizing resource behavior by using only resourceCustomization and not subkeys.
====

* With this update, to use the *Environments* page in the *Developer* perspective, you must upgrade if you are using a {gitops-title} version prior to 1.7 and {product-title} 4.15 or above. link:https://issues.redhat.com/browse/GITOPS-2415[GITOPS-2415]

* With this update, you can create applications, which are managed by the same control plane Argo CD instance, in any namespace in the same cluster. As an administrator, perform the following actions to enable this update:
** Add the namespace to the `.spec.sourceNamespaces` attribute for a cluster-scoped Argo CD instance that manages the application.
** Add the namespace to the `.spec.sourceNamespaces` attribute in the `AppProject` custom resource that is associated with the application. 
+
link:https://issues.redhat.com/browse/GITOPS-2341[GITOPS-2341]

:FeatureName: Argo CD applications in non-control plane namespaces
include::snippets/technology-preview.adoc[]

* With this update, Argo CD supports the Server-Side Apply feature, which helps users to perform the following tasks:
** Manage large resources which are too big for the allowed annotation size of 262144 bytes.
** Patch an existing resource that is not managed or deployed by Argo CD.
+
You can configure this feature at application or resource level. link:https://issues.redhat.com/browse/GITOPS-2340[GITOPS-2340]

[id="fixed-issues-1-7-0_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, {gitops-title} releases were affected by an issue of Dex pods failing with `CreateContainerConfigError` error when the `anyuid` SCC was assigned to the Dex service account. This update fixes the issue by assigning a default user id to the Dex container. link:https://issues.redhat.com/browse/GITOPS-2235[GITOPS-2235]

* Before this update, {gitops-title} used the RHSSO (Keycloak) through OIDC in addition to Dex. However, with a recent security fix, the certificate of RHSSO could not be validated when configured with a certificate not signed by one of the well-known certificate authorities. This update fixes the issue; you can now provide a custom certificate to verify the KeyCloak's TLS certificate while communicating with it. In addition, you can add `rootCA` to the Argo CD custom resource `.spec.keycloak.rootCA` field. The Operator reconciles such changes and updates the `oidc.config in argocd-cm` config map with the PEM encoded root certificate. link:https://issues.redhat.com/browse/GITOPS-2214[GITOPS-2214]

Example Argo CD with Keycloak configuration:

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  sso:
    keycloak:
      rootCA: '<PEM encoded root certificate>'
    provider: keycloak
.......
.......
----

* Before this update, the application controllers restarted multiple times due to the unresponsiveness of liveness probes. This update fixes the issue by removing the liveness probe in the `statefulset` application controller. link:https://issues.redhat.com/browse/GITOPS-2153[GITOPS-2153]

[id="known-issues-1-7-0_{context}"]
== Known issues

* Before this update, the Operator did not reconcile the `mountsatoken` and `ServiceAccount` settings for the repository server. While this has been fixed, deletion of the service account does not revert to the default. link:https://issues.redhat.com/browse/GITOPS-1873[GITOPS-1873]

* Workaround: Manually set the `spec.repo.serviceaccountfield to thedefault` service account. link:https://issues.redhat.com/browse/GITOPS-2452[GITOPS-2452]
