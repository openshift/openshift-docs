:_mod-docs-content-type: ASSEMBLY
[id="argocd"]
= Using ArgoCD with {product-title}
include::_attributes/common-attributes.adoc[]

:context: argocd

toc::[]

[id="argocd-what"]
== What does ArgoCD do?

ArgoCD is a declarative continuous delivery tool that leverages GitOps to maintain cluster resources. ArgoCD is implemented as a controller that continuously monitors application definitions and configurations defined in a Git repository and compares the specified state of those configurations with their live state on the cluster. Configurations that deviate from their specified state in the Git repository are classified as OutOfSync. ArgoCD reports these differences and allows administrators to automatically or manually resync configurations to the defined state.

ArgoCD enables you to deliver global custom resources, like the resources that are used to configure {product-title} clusters.

[id="argocd-support"]
== Statement of support

Red Hat does not provide support for this tool. To obtain support for ArgoCD, see link:https://argoproj.github.io/argo-cd/SUPPORT/[Support] in the ArgoCD documentation.

[id="argocd-documentation"]
== ArgoCD documentation

For more information about using ArgoCD, see the link:https://argoproj.github.io/argo-cd/[ArgoCD documentation].
