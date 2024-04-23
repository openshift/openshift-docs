:_mod-docs-content-type: ASSEMBLY
[id="argo-cd-custom-resource-properties"]
= Argo CD Operator
include::_attributes/common-attributes.adoc[]
:context: argo-cd-custom-resource-properties

toc::[]

[role="_abstract"]
The `ArgoCD` custom resource is a Kubernetes Custom Resource (CRD) that describes the desired state for a given Argo CD cluster that allows you to configure the components which make up an Argo CD cluster.

include::modules/argo-cd-command-line.adoc[leveloffset=+1]
include::modules/gitops-argo-cd-properties.adoc[leveloffset=+1]
include::modules/gitops-repo-server-properties.adoc[leveloffset=+1]
include::modules/gitops-argo-cd-notification.adoc[leveloffset=+1]
