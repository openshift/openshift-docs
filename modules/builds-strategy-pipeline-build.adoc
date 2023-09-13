// Module included in the following assemblies:
//
//*builds/build-strategies.adoc
//*builds/understanding-image-builds

[id="builds-strategy-pipeline-build_{context}"]
= Pipeline build

[IMPORTANT]
====
The Pipeline build strategy is deprecated in {product-title} 4. Equivalent and improved functionality is present in the {product-title} Pipelines based on Tekton.

Jenkins images on {product-title} are fully supported and users should follow Jenkins user documentation for defining their `jenkinsfile` in a job or store it in a Source Control Management system.
====

The Pipeline build strategy allows developers to define a Jenkins pipeline for use by the Jenkins pipeline plugin. The build can be started, monitored, and managed by {product-title} in the same way as any other build type.

Pipeline workflows are defined in a `jenkinsfile`, either embedded directly in the build configuration, or supplied in a Git repository and referenced by the build configuration.

//The first time a project defines a build configuration using a Pipeline
//strategy, {product-title} instantiates a Jenkins server to execute the
//pipeline. Subsequent Pipeline build configurations in the project share this
//Jenkins server.

//[role="_additional-resources"]
//.Additional resources

//* Pipeline build configurations require a Jenkins server to manage the
//pipeline execution.
