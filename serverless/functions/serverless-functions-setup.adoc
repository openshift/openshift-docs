:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-functions-setup"]
= Setting up {FunctionsProductName}
:context: serverless-functions-setup

toc::[]

To improve the process of deployment of your application code, you can use {ServerlessProductName} to deploy stateless, event-driven functions as a Knative service on {product-title}. If you want to develop functions, you must complete the set up steps.

[id="prerequisites_serverless-functions-setup"]
== Prerequisites

To enable the use of {FunctionsProductName} on your cluster, you must complete the following steps:

* The {ServerlessOperatorName} and Knative Serving are installed on your cluster.
+
[NOTE]
====
Functions are deployed as a Knative service. If you want to use event-driven architecture with your functions, you must also install Knative Eventing.
====

ifdef::openshift-enterprise[]
* You have the xref:../../cli_reference/openshift_cli/getting-started-cli.adoc#cli-getting-started[`oc` CLI] installed.
endif::[]
// need to wait til CLI docs are added to OSD and ROSA for this link to work
// TODO: remove these conditionals once this is available
ifdef::openshift-dedicated,openshift-rosa[]
* You have the `oc` CLI installed.
endif::[]

* You have the xref:../../serverless/install/installing-kn.adoc#installing-kn[Knative (`kn`) CLI] installed. Installing the Knative CLI enables the use of `kn func` commands which you can use to create and manage functions.

* You have installed Docker Container Engine or Podman version 3.4.7 or higher.

* You have access to an available image registry, such as the OpenShift Container Registry.

ifdef::openshift-enterprise[]
* If you are using link:https://quay.io/[Quay.io] as the image registry, you must ensure that either the repository is not private, or that you have followed the {product-title} documentation on xref:../../openshift_images/managing_images/using-image-pull-secrets.adoc#images-allow-pods-to-reference-images-from-secure-registries_using-image-pull-secrets[Allowing pods to reference images from other secured registries].
endif::[]
// need to wait til images docs are added to OSD and ROSA for this link to work
// TODO: remove these conditionals once this is available
ifdef::openshift-dedicated,openshift-rosa[]
* If you are using link:https://quay.io/[Quay.io] as the image registry, you must ensure that either the repository is not private, or that you have allowed pods on your cluster to reference images from other secured registries.
endif::[]

ifdef::openshift-enterprise[]
* If you are using the OpenShift Container Registry, a cluster administrator must xref:../../registry/securing-exposing-registry.adoc#securing-exposing-registry[expose the registry].
endif::[]
// need to wait til registry docs are added to OSD and ROSA for this link to work
// TODO: remove these conditionals once this is available
ifdef::openshift-dedicated,openshift-rosa[]
* If you are using the OpenShift Container Registry, a cluster or dedicated administrator must expose the registry.
endif::[]

include::modules/serverless-functions-podman.adoc[leveloffset=+1]
include::modules/serverless-functions-podman-macos.adoc[leveloffset=+1]

[id="next-steps_serverless-functions-setup"]
== Next steps

ifdef::openshift-enterprise[]
* For more information about Docker Container Engine or Podman, see xref:../../architecture/understanding-development.adoc#container-build-tool-options[Container build tool options].
endif::[]
// need to wait til build tool docs are added to OSD and ROSA for this link to work
// TODO: remove these conditionals once this is available

* See xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-functions-getting-started[Getting started with functions].
