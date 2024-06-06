:_mod-docs-content-type: ASSEMBLY
[id="health-information-for-resources-deployment"]
= Monitoring health information for application resources and deployments
:context: health-information-for-resources-deployment
include::_attributes/common-attributes.adoc[]

toc::[]

The {gitops-title} *Environments* page in the *Developer* perspective of the {product-title} web console shows a list of the successful deployments of the application environments, along with links to the revision for each deployment.

The *Application environments* page in the *Developer* perspective of the {product-title} web console displays the health status of the application resources, such as routes, synchronization status, deployment configuration, and deployment history.

The environments pages in the *Developer* perspective of the {product-title} web console are decoupled from the {gitops-title} Application Manager command-line interface (CLI), `kam`. You do not have to use `kam` to generate Application Environment manifests for the environments to show up in the *Developer* perspective of the {product-title} web console. You can use your own manifests, but the environments must still be represented by namespaces. In addition, specific labels and annotations are still needed.

include::modules/go-settings-for-environment-labels-and-annotations.adoc[leveloffset=+1]
include::modules/go-health-monitoring.adoc[leveloffset=+1]
