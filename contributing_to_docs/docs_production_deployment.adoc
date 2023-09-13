[id="contributing-to-docs-docs-production-deployment"]
= Production deployment of the OpenShift documentation
:icons:
:toc: macro
:toc-title:
:toclevels: 1
:linkattrs:
:description: How to deploy the entire set of documentation

toc::[]

== Source-to-image pipeline
OpenShift documentation is built and deployed on an https://cloud.redhat.com/products/dedicated/[OpenShift Dedicated cluster]
using a https://github.com/openshift/source-to-image[source-to-image] build pipeline.

The source-to-image builder image is built from a https://github.com/openshift-cs/docs-builder/[community project in GitHub]
and published to https://quay.io/repository/openshift-cs/docs-builder.

== Documentation deployment
Deploying the OpenShift documentation is simplified by using a
https://github.com/openshift-cs/docs-builder/blob/main/template.yaml[pre-built OpenShift template YAML].

You can use the following command to deploy the OpenShift Container Platform (commercial) documentation:

[source,terminal]
----
oc new-app https://raw.githubusercontent.com/openshift-cs/docs-builder/main/template.yaml \
    -p NAME=docs-openshift-com \
    -p PACKAGE=commercial \
    -p APPLICATION_DOMAIN=docs.openshift.com \
    -p BUILD_REPO=https://github.com/openshift/openshift-docs.git \
    -p BUILD_BRANCH=main
----

You can use the following command to deploy the OKD (community) documentation

[source,terminal]
----
oc new-app https://raw.githubusercontent.com/openshift-cs/docs-builder/main/template.yaml \
    -p NAME=docs-openshift-com \
    -p PACKAGE=community \
    -p APPLICATION_DOMAIN=docs.openshift.com \
    -p BUILD_REPO=https://github.com/openshift/openshift-docs.git \
    -p BUILD_BRANCH=main
----

== Deployment customization
It's possible to change the documentation source repository to another repository for development by changing the
`BUILD_REPO` parameter in the `oc new-app` command.

To change the builder image, provide the `BUILDER_IMAGE` parameter in the `oc new-app` command.
