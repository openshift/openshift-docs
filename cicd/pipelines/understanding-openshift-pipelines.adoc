:_mod-docs-content-type: ASSEMBLY
[id="understanding-openshift-pipelines"]
= Understanding {pipelines-shortname}
include::_attributes/common-attributes.adoc[]
:context: understanding-openshift-pipelines

toc::[]

:FeatureName: OpenShift Pipelines

{pipelines-title} is a cloud-native, continuous integration and continuous delivery (CI/CD) solution based on Kubernetes resources. It uses Tekton building blocks to automate deployments across multiple platforms by abstracting away the underlying implementation details. Tekton introduces a number of standard custom resource definitions (CRDs) for defining CI/CD pipelines that are portable across Kubernetes distributions.

[id="op-key-features"]
== Key features

* {pipelines-title} is a serverless CI/CD system that runs pipelines with all the required dependencies in isolated containers.
* {pipelines-title} are designed for decentralized teams that work on microservice-based architecture.
* {pipelines-title} use standard CI/CD pipeline definitions that are easy to extend and integrate with the existing Kubernetes tools, enabling you to scale on-demand.
* You can use {pipelines-title} to build images with Kubernetes tools such as Source-to-Image (S2I), Buildah, Buildpacks, and Kaniko that are portable across any Kubernetes platform.
* You can use the {product-title} web console *Developer* perspective to create Tekton resources, view logs of pipeline runs, and manage pipelines in your {product-title} namespaces.

[id="op-detailed-concepts"]
== {pipelines-shortname} Concepts
This guide provides a detailed view of the various pipeline concepts.

//About tasks
include::modules/op-about-tasks.adoc[leveloffset=+2]
//About when expression
include::modules/op-about-whenexpression.adoc[leveloffset=+2]
//About final tasks
include::modules/op-about-finally_tasks.adoc[leveloffset=+2]
//About task run
include::modules/op-about-taskrun.adoc[leveloffset=+2]
//About pipelines
include::modules/op-about-pipelines.adoc[leveloffset=+2]
//About pipeline run
include::modules/op-about-pipelinerun.adoc[leveloffset=+2]
//About workspace
include::modules/op-about-workspace.adoc[leveloffset=+2]
//About triggers
include::modules/op-about-triggers.adoc[leveloffset=+2]


[role="_additional-resources"]
== Additional resources

* For information on installing {pipelines-shortname}, see xref:../../cicd/pipelines/installing-pipelines.adoc#installing-pipelines[Installing {pipelines-shortname}].
* For more details on creating custom CI/CD solutions, see xref:../../cicd/pipelines/creating-applications-with-cicd-pipelines.adoc#creating-applications-with-cicd-pipelines[Creating CI/CD solutions for applications using {pipelines-shortname}].
* For more details on re-encrypt TLS termination, see link:https://docs.openshift.com/container-platform/3.11/architecture/networking/routes.html#re-encryption-termination[Re-encryption Termination].
* For more details on secured routes, see the xref:../../networking/routes/secured-routes.adoc#secured-routes[Secured routes] section.
