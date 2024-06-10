:_mod-docs-content-type: ASSEMBLY
[id="overview-openshift-builds"]
= Overview of Builds
:context: overview-openshift-builds
include::_attributes/common-attributes.adoc[]

toc::[]


Builds is an extensible build framework based on the link:https://shipwright.io/[Shipwright project], which you can use to build container images on an {product-title} cluster. You can build container images from source code and Dockerfiles by using image build tools, such as Source-to-Image (S2I) and Buildah. You can create and apply build resources, view logs of build runs, and manage builds in your {product-title} namespaces.

Builds includes the following capabilities:

* Standard Kubernetes-native API for building container images from source code and Dockerfiles
* Support for Source-to-Image (S2I) and Buildah build strategies
* Extensibility with your own custom build strategies
* Execution of builds from source code in a local directory
* Shipwright CLI for creating and viewing logs, and managing builds on the cluster
* Integrated user experience with the *Developer* perspective of the {product-title} web console


Builds consists of the following custom resources (CRs):

* `Build`
* `BuildStrategy` and `ClusterBuildStrategy`
* `BuildRun`
