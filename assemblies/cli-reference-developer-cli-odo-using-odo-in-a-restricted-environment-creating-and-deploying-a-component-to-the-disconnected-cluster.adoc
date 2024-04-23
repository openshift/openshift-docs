:_mod-docs-content-type: ASSEMBLY
[id="creating-and-deploying-a-component-to-the-disconnected-cluster"]
= Creating and deploying a component to the disconnected cluster
include::_attributes/common-attributes.adoc[]
:context: creating-and-deploying-a-component-to-the-disconnected-cluster

toc::[]

After you push the `init` image to a cluster with a mirrored registry, you must mirror a supported builder image for your application with the `oc` tool, overwrite the mirror registry using the environment variable, and then create your component.

== Prerequisites

* Install `oc` on the client operating system.
* xref:../../../cli_reference/developer_cli_odo/installing-odo.adoc#installing-odo-on-linux_installing-odo[Install `{odo-title}`] on the client operating system.
* Access to an restricted cluster with a configured {product-registry} or a mirror registry.
* xref:../../../cli_reference/developer_cli_odo/using_odo_in_a_restricted_environment/pushing-the-odo-init-image-to-the-restricted-cluster-registry.adoc#pushing-the-odo-init-image-to-a-mirror-registry_pushing-the-odo-init-image-to-the-restricted-cluster-registry[Push the `odo` init image to your cluster registry].

include::modules/developer-cli-odo-mirroring-a-supported-builder-image.adoc[leveloffset=+1]
include::modules/developer-cli-odo-overwriting-a-mirror-registry.adoc[leveloffset=+1]
include::modules/developer-cli-odo-creating-and-deploying-a-nodejs-application-with-odo.adoc[leveloffset=+1]
