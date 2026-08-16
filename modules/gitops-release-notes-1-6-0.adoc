// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
:_mod-docs-content-type: REFERENCE

[id="gitops-release-notes-1-6-0_{context}"]
= Release notes for {gitops-title} 1.6.0

{gitops-title} 1.6.0 is now available on {product-title} 4.8, 4.9, 4.10, and 4.11.

[id="new-features-1-6-0_{context}"]
== New features

The current release adds the following improvements:

* Previously, the Argo CD `ApplicationSet` controller was a technology preview (TP) feature. With this update, it is a general availability (GA) feature. link:https://issues.redhat.com/browse/GITOPS-1958[GITOPS-1958]

* With this update, the latest releases of the {gitops-title} are available in `latest` and version-based channels. To get these upgrades, update the `channel` parameter in the `Subscription` object YAML file: change its value from `stable` to `latest` or a version-based channel such as `gitops-1.6`. link:https://issues.redhat.com/browse/GITOPS-1791[GITOPS-1791]

* With this update, the parameters of the `spec.sso` field that controlled the keycloak configurations are moved to `.spec.sso.keycloak`.
The parameters of the `.spec.dex` field have been added to `.spec.sso.dex`. Start using `.spec.sso.provider` to enable or disable Dex. The `.spec.dex` parameters are deprecated and planned to be removed in version 1.9, along with the  `DISABLE_DEX` and `.spec.sso` fields for keycloak configuration. link:https://issues.redhat.com/browse/GITOPS-1983[GITOPS-1983]

* With this update, the Argo CD Notifications controller is available as an optional workload that can be enabled or disabled by using the `.spec.notifications.enabled` parameter in the Argo CD custom resource. The Argo CD Notifications controller is available as a Technical Preview feature. link:https://issues.redhat.com/browse/GITOPS-1917[GITOPS-1917]

:FeatureName: Argo CD Notifications controller
include::snippets/technology-preview.adoc[]

* With this update, resource exclusions for Tekton pipeline runs and tasks runs are added by default. Argo CD, prunes these resources by default. These resource exclusions are added to the new Argo CD instances that are created from the {product-title}. If the instances are created from the CLI, the resources are not added. link:https://issues.redhat.com/browse/GITOPS-1876[GITOPS-1876]

* With this update, you can select the tracking method that by Argo CD uses by setting the `resourceTrackingMethod` parameter in the Operand's specification. link:https://issues.redhat.com/browse/GITOPS-1862[GITOPS-1862]

* With this update, you can add entries to the `argocd-cm` configMap using the `extraConfig` field of {gitops-title} Argo CD custom resource. The entries specified are reconciled to the live `config-cm` configMap without validations. link:https://issues.redhat.com/browse/GITOPS-1964[GITOPS-1964]

* With this update, on {product-title} 4.11, the {gitops-title} *Environments* page in the *Developer* perspective shows history of the successful deployments of the application environments, along with links to the revision for each deployment. link:https://issues.redhat.com/browse/GITOPS-1269[GITOPS-1269]

* With this update, you can manage resources with Argo CD that are also being used as template resources or "source" by an Operator. link:https://issues.redhat.com/browse/GITOPS-982[GITOPS-982]

* With this update, the Operator will now configure the Argo CD workloads with the correct permissions to satisfy the Pod Security Admission that has been enabled for Kubernetes 1.24. link:https://issues.redhat.com/browse/GITOPS-2026[GITOPS-2026]

* With this update, Config Management Plugins 2.0 is supported. You can use the Argo CD custom resource to specify sidebar containers for the repo server. link:https://issues.redhat.com/browse/GITOPS-766[GITOPS-776]

* With this update, all communication between the Argo CD components and the Redis cache are properly secured using modern TLS encryption. link:https://issues.redhat.com/browse/GITOPS-720[GITOPS-720]

* This release of {gitops-title} adds support for IBM Z and IBM Power on {product-title} 4.10. Currently, installations in restricted environments are not supported on IBM Z and IBM Power.

[id="fixed-issues-1-6-0_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, the `system:serviceaccount:argocd:gitops-argocd-application-controller` cannot create resource "prometheusrules" in API group `monitoring.coreos.com` in the namespace `webapps-dev`. This update fixes this issue and {gitops-title} is now able to manage all resources from the `monitoring.coreos.com` API group. link:https://issues.redhat.com/browse/GITOPS-1638[GITOPS-1638]

* Before this update, while reconciling cluster permissions, if a secret belonged to a cluster config instance it was deleted. This update fixes this issue. Now, the `namespaces` field from the secret is deleted instead of the secret. link:https://issues.redhat.com/browse/GITOPS-1777[GITOPS-1777]

* Before this update, if you installed the HA variant of Argo CD through the Operator, the Operator created the Redis `StatefulSet` object with `podAffinity` rules instead of `podAntiAffinity` rules. This update fixes this issue and now the Operator creates the Redis `StatefulSet` with `podAntiAffinity` rules. link:https://issues.redhat.com/browse/GITOPS-1645[GITOPS-1645]

* Before this update, Argo CD **ApplicationSet** had too many `ssh` Zombie processes. This update fixes this issue: it adds tini, a simple init daemon that spawns processes and reaps zombies, to the **ApplicationSet** controller. This ensures that a `SIGTERM` signal is properly passed to the running process, preventing it from being a zombie process. link:https://issues.redhat.com/browse/GITOPS-2108[GITOPS-2108]

[id="known-issues-1-6-0_{context}"]
== Known issues

*  {gitops-title} Operator can make use of RHSSO (KeyCloak) through OIDC in addition to Dex. However, with a recent security fix applied, the certificate of RHSSO cannot be validated in some scenarios. link:https://issues.redhat.com/browse/GITOPS-2214[GITOPS-2214]
+
As a workaround, disable TLS validation for the OIDC (Keycloak/RHSSO) endpoint in the ArgoCD specification.

[source,yaml]
----
spec:
  extraConfig:
    oidc.tls.insecure.skip.verify: "true"
...
----