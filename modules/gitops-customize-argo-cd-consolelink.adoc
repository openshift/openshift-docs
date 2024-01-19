// Module included in the following assembly:
//
// * cicd/gitops/setting-up-argocd-instance.adoc

:_mod-docs-content-type: PROCEDURE
[id="gitops-customize-argo-cd-consolelink_{context}"]
= Customizing the Argo CD console link

In a multi-tenant cluster, users might have to deal with multiple instances of Argo CD. For example, after installing an Argo CD instance in your namespace, you might find a different Argo CD instance attached to the Argo CD console link, instead of your own Argo CD instance, in the Console Application Launcher.

You can customize the Argo CD console link by setting the `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` environment variable:

* When you set `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` to `true`, the Argo CD console link is permanently deleted.
* When you set `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` to `false` or use the default value, the Argo CD console link is temporarily deleted and visible again when the Argo CD route is reconciled.

.Prerequisites
* You have logged in to the {product-title} cluster as an administrator.
* You have installed the {gitops-title} Operator.

.Procedure

. In the *Administrator* perspective, navigate to *Administration* -> *CustomResourceDefinitions*.
. Find the *Subscription* CRD and click to open it.
. Select the *Instances* tab and click the *openshift-gitops-operator* subscription.
. Select the *YAML* tab and make your customization:
** To enable or disable the Argo CD console link, edit the value of `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` as needed:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-gitops-operator
spec:
  config:
    env:
    - name: DISABLE_DEFAULT_ARGOCD_CONSOLELINK
      value: 'true'
----
