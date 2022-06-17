// Module included in the following assemblies:
//
//*builds/understanding-image-builds


[id="builds-about_{context}"]
= Builds

A build is the process of transforming input parameters into a resulting object. Most often, the process is used to transform input parameters or source code into a runnable image. A `BuildConfig` object is the definition of the entire build process.

{product-title} uses Kubernetes by creating containers from build images and pushing them to a container image registry.

Build objects share common characteristics including inputs for a build, the requirement to complete a build process, logging the build process, publishing resources from successful builds, and publishing the final status of the build. Builds take advantage of resource restrictions, specifying limitations on resources such as CPU usage, memory usage, and build or pod execution time.

ifdef::openshift-origin,openshift-enterprise[]
The {product-title} build system provides extensible support for build strategies that are based on selectable types specified in the build API. There are three primary build strategies available:

* Docker build
* Source-to-image (S2I) build
* Custom build

By default, docker builds and S2I builds are supported.
endif::[]

The resulting object of a build depends on the builder used to create it. For docker and S2I builds, the resulting objects are runnable images. For custom builds, the resulting objects are whatever the builder image author has specified.

Additionally, the pipeline build strategy can be used to implement sophisticated
workflows:

* Continuous integration
* Continuous deployment
