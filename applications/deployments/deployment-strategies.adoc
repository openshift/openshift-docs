:_mod-docs-content-type: ASSEMBLY
[id="deployment-strategies"]
= Using deployment strategies
include::_attributes/common-attributes.adoc[]
:context: deployment-strategies

toc::[]

_Deployment strategies_ are used to change or upgrade applications without downtime so that users barely notice a change.

Because users generally access applications through a route handled by a router, deployment strategies can focus on `DeploymentConfig` object features or routing features. Strategies that focus on `DeploymentConfig` object features impact all routes that use the application. Strategies that use router features target individual routes.

Most deployment strategies are supported through the `DeploymentConfig` object, and some additional strategies are supported through router features.

[id="choosing-deployment-strategies"]
== Choosing a deployment strategy

Consider the following when choosing a deployment strategy:

- Long-running connections must be handled gracefully.
- Database conversions can be complex and must be done and rolled back along with the application.
- If the application is a hybrid of microservices and traditional components, downtime might be required to complete the transition.
- You must have the infrastructure to do this.
- If you have a non-isolated test environment, you can break both new and old versions.

A deployment strategy uses readiness checks to determine if a new pod is ready for use. If a readiness check fails, the `DeploymentConfig` object retries to run the pod until it times out. The default timeout is `10m`, a value set in `TimeoutSeconds` in `dc.spec.strategy.*params`.

// Rolling strategies
include::modules/deployments-rolling-strategy.adoc[leveloffset=+1]
include::modules/deployments-canary-deployments.adoc[leveloffset=+2]
// Creating rolling deployments
include::modules/creating-rolling-deployments-CLI.adoc[leveloffset=+2]
// Editing a deployment
:context: rolling-strategy
include::modules/odc-editing-deployments.adoc[leveloffset=+2]
// Starting a deployment
include::modules/odc-starting-rolling-deployment.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* xref:../../applications/creating_applications/odc-creating-applications-using-developer-perspective.adoc#odc-creating-applications-using-developer-perspective[Creating and deploying applications on {product-title} using the *Developer* perspective]
* xref:../../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-viewing-application-composition-using-topology-view[Viewing the applications in your project, verifying their deployment status, and interacting with them in the *Topology* view]

// Recreate strategies
include::modules/deployments-recreate-strategy.adoc[leveloffset=+1]
// Editing a deployment
:context: recreate-strategy
include::modules/odc-editing-deployments.adoc[leveloffset=+2]
// Starting a deployment
include::modules/odc-starting-recreate-deployment.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* xref:../../applications/creating_applications/odc-creating-applications-using-developer-perspective.adoc#odc-creating-applications-using-developer-perspective[Creating and deploying applications on {product-title} using the *Developer* perspective]
* xref:../../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-viewing-application-composition-using-topology-view[Viewing the applications in your project, verifying their deployment status, and interacting with them in the *Topology* view]

// Custom strategies
include::modules/deployments-custom-strategy.adoc[leveloffset=+1]
// Editing a deployment
:context: custom-strategy
include::modules/odc-editing-deployments.adoc[leveloffset=+2]

include::modules/deployments-lifecycle-hooks.adoc[leveloffset=+1]
