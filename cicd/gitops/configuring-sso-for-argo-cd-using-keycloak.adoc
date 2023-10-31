:_mod-docs-content-type: ASSEMBLY
[id="configuring-sso-for-argo-cd-using-keycloak"]
= Configuring SSO for Argo CD using Keycloak
include::_attributes/common-attributes.adoc[]
:context: configuring-sso-for-argo-cd-using-keycloak

toc::[]

After the {gitops-title} Operator is installed, Argo CD automatically creates a user with `admin` permissions. To manage multiple users, cluster administrators can use Argo CD to configure Single Sign-On (SSO).

.Prerequisites
* Red Hat SSO is installed on the cluster.
* {gitops-title} Operator is installed on the cluster.
* Argo CD is installed on the cluster.

include::modules/gitops-creating-a-new-client-using-keycloak.adoc[leveloffset=+1]

include::modules/gitops-logging-into-keycloak.adoc[leveloffset=+1]

include::modules/gitops-uninstall-keycloak.adoc[leveloffset=+1]

////
[role="_additional-resources"]
.Additional resources
* link:https://stedolan.github.io/jq/[`jq` command-line JSON processor documentation.]
* link:https://argoproj.github.io/argo-cd/operator-manual/rbac/[Argo CD upstream documentation, RBAC Configuration section].
////
