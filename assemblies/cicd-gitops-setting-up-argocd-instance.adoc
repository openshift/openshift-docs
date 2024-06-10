:_mod-docs-content-type: ASSEMBLY
[id="setting-up-argocd-instance"]
= Setting up an Argo CD instance
include::_attributes/common-attributes.adoc[]
:context: setting-up-argocd-instance

toc::[]

By default, the {gitops-title} installs an instance of Argo CD in the `openshift-gitops` namespace with additional permissions for managing certain cluster-scoped resources. To manage cluster configurations or deploy applications, you can install and deploy a new Argo CD instance. By default, any new instance has permissions to manage resources only in the namespace where it is deployed.

include::modules/gitops-argo-cd-installation.adoc[leveloffset=+1]

include::modules/gitops-enable-replicas-for-argo-cd-server.adoc[leveloffset=+1]

include::modules/gitops-deploy-resources-different-namespaces.adoc[leveloffset=+1]

include::modules/gitops-customize-argo-cd-consolelink.adoc[leveloffset=+1]
