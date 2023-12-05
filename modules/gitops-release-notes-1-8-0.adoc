// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

:_mod-docs-content-type: REFERENCE
[id="gitops-release-notes-1-8-0_{context}"]
= Release notes for {gitops-title} 1.8.0

{gitops-title} 1.8.0 is now available on {product-title} 4.10, 4.11, 4.12, and 4.13.

[id="new-features-1-8-0_{context}"]
== New features

The current release adds the following improvements:

* With this update,  you can add support for the ApplicationSet Progressive Rollout Strategy feature. Using this feature, you can enhance the ArgoCD ApplicationSet resource to embed a rollout strategy for a progressive application resource update after you modify the ApplicationSet spec or Application templates. When you enable this feature, applications are updated in a declarative order instead of simultaneously. link:https://issues.redhat.com/browse/GITOPS-956[GITOPS-956]
+
[IMPORTANT]
====
ApplicationSet Progressive Rollout Strategy is a Technology Preview feature.
====
//https://github.com/argoproj/argo-cd/pull/12103

* With this update, the *Application environments* page in the *Developer* perspective of the {product-title} web console is decoupled from the {gitops-title} Application Manager command-line interface (CLI), `kam`. You do not have to use the `kam` CLI to generate Application Environment manifests for the environments to show up in the *Developer* perspective of the {product-title} web console. You can use your own manifests, but the environments must still be represented by namespaces. In addition, specific labels and annotations are still needed. link:https://issues.redhat.com/browse/GITOPS-1785[GITOPS-1785]

* With this update, the {gitops-title} Operator and the `kam` CLI are now available to use on ARM architecture on {product-title}. link:https://issues.redhat.com/browse/GITOPS-1688[GITOPS-1688]
+
[IMPORTANT]
====
`spec.sso.provider: keycloak` is not yet supported on ARM.
====

* With this update, you can enable workload monitoring for specific Argo CD instances by setting the `.spec.monitoring.enabled` flag value to `true`. As a result, the Operator creates a `PrometheusRule` object that contains alert rules for each Argo CD component. These alert rules trigger an alert when the replica count of the corresponding component has drifted from the desired state for a certain amount of time. The Operator will not overwrite the changes made to the `PrometheusRule` object by the users. link:https://issues.redhat.com/browse/GITOPS-2459[GITOPS-2459]

* With this update, you can pass command arguments to the repo server deployment using the Argo CD CR. link:https://issues.redhat.com/browse/GITOPS-2445[GITOPS-2445]
+
For example:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  repo:
    extraRepoCommandArgs:
      - --max.combined.directory.manifests.size
      - 10M
----

[id="fixed-issues-1-8-0_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, you could set the `ARGOCD_GIT_MODULES_ENABLED` environment variable only on the `openshift-gitops-repo-server` pod and not on the `ApplicationSet Controller` pod. As a result, when using the Git generator, Git submodules were cloned during the generation of child applications because the variable was missing from the `ApplicationSet Controller` environment. In addition, if the credentials required to clone these submodules were not configured in ArgoCD, the application generation failed. This update fixes the issue; you can now add any environment variables such as `ArgoCD_GIT_MODULES_ENABLED` to the `ApplicationSet Controller` pod using the Argo CD CR. The `ApplicationSet Controller` pod then successfully generates child applications from the cloned repository and no submodule is cloned in the process. link:https://issues.redhat.com/browse/GITOPS-2399[GITOPS-2399]
+
For example:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  applicationSet:
    env:
     - name: ARGOCD_GIT_MODULES_ENABLED
       value: "true"
----

* Before this update, while installing the {gitops-title} Operator v1.7.0, the default `argocd-cm.yml` config map file created for authenticating Dex contained the base64-encoded client secret in the format of a `key:value` pair. This update fixes this issue by not storing the client secret in the default `argocd-cm.yml` config map file. Instead, the client secret is inside an `argocd-secret` object now, and you can reference it inside the configuration map as a secret name. link:https://issues.redhat.com/browse/GITOPS-2570[GITOPS-2570]

[id="known-issues-1-8-0_{context}"]
== Known issues

* When you deploy applications using your manifests without using the `kam` CLI and view the applications in the *Application environments* page in the *Developer* perspective of the {product-title} web console, the Argo CD URL to the corresponding application does not load the page as expected from the Argo CD icon in the card. link:https://issues.redhat.com/browse/GITOPS-2736[GITOPS-2736]
