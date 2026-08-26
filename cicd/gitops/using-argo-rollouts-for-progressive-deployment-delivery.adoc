:_mod-docs-content-type: ASSEMBLY
[id="using-argo-rollouts-for-progressive-deployment-delivery"]
= Using Argo Rollouts for progressive deployment delivery
include::_attributes/common-attributes.adoc[]
:context: using-argo-rollouts-for-progressive-deployment-delivery

toc::[]

:FeatureName: Argo Rollouts
include::snippets/technology-preview.adoc[leveloffset=+1]

Progressive delivery is the process of releasing product updates in a controlled and gradual manner.
Progressive delivery reduces the risk of a release by exposing the new version of a product update only to a subset of users initially. The process involves continuously observing and analyzing this new version to verify whether its behavior matches the requirements and expectations set. The verifications continue as the process gradually exposes the product update to a broader and wider audience.

{product-title} provides some progressive delivery capability by using routes to split traffic between different services, but this typically requires manual intervention and management.

With Argo Rollouts, you can use automation and metric analysis to support progressive deployment delivery and drive the automated rollout or rollback of a new version of an application.
Argo Rollouts provide advanced deployment capabilities and enable integration with ingress controllers and service meshes.
You can use Argo Rollouts to manage multiple replica sets that represent different versions of the deployed application. Depending on your deployment strategy, you can handle traffic to these versions during an update by optimizing their existing traffic shaping abilities and gradually shifting traffic to the new version. You can combine Argo Rollouts with a metric provider like Prometheus to do metric-based and policy-driven rollouts and rollbacks based on the parameters set.

[id="prerequisites_using-argo-rollouts-for-progressive-deployment-delivery"]
== Prerequisites
* You have access to the cluster with `cluster-admin` privileges.
* You have access to the {product-title} web console.
* {gitops-title} 1.9.0 or a newer version is installed in your cluster.

include::modules/gitops-benefits-of-argo-rollouts.adoc[leveloffset=+1]

include::modules/gitops-about-argo-rollout-manager-custom-resources-and-spec.adoc[leveloffset=+1]

include::modules/gitops-creating-rolloutmanager-custom-resource.adoc[leveloffset=+1]

include::modules/gitops-deleting-rolloutmanager-custom-resource.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_argo-rollouts-in-gitops"]
== Additional resources
* xref:../../cicd/gitops/installing-openshift-gitops.adoc#installing-gitops-operator-in-web-console_installing-openshift-gitops[Installing {gitops-title}]
* xref:../../cicd/gitops/uninstalling-openshift-gitops.adoc#go-uninstalling-gitops-operator_uninstalling-openshift-gitops[Uninstalling {gitops-title}]
* xref:../../applications/deployments/deployment-strategies.adoc#deployments-canary-deployments_deployment-strategies[Canary deployments]
* xref:../../applications/deployments/route-based-deployment-strategies.adoc#deployments-blue-green_route-based-deployment-strategies[Blue-green deployments]
* link:https://argo-rollouts-manager.readthedocs.io/en/latest/crd_reference/[`RolloutManager` Custom Resource specification]
* link:https://www.redhat.com/architect/blue-green-canary-argo-rollouts[Blue-green and canary deployments with Argo Rollouts]
* link:https://cloud.redhat.com/blog/trying-out-argo-rollouts-in-openshift-gitops-1.9/[Argo Rollouts tech preview limitations]
