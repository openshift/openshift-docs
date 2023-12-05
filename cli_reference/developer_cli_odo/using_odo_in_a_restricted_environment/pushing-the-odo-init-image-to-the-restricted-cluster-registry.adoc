:_mod-docs-content-type: ASSEMBLY
[id="pushing-the-odo-init-image-to-the-restricted-cluster-registry"]
include::_attributes/common-attributes.adoc[]
= Pushing the {odo-title} init image to the restricted cluster registry
:context: pushing-the-odo-init-image-to-the-restricted-cluster-registry

toc::[]

Depending on the configuration of your cluster and your operating system you can either push the `odo` init image to a mirror registry or directly to an {product-registry}.

== Prerequisites

* Install `oc` on the client operating system.
* xref:../../../cli_reference/developer_cli_odo/installing-odo.adoc#installing-odo-on-linux_installing-odo[Install `{odo-title}`] on the client operating system.
* Access to a restricted cluster with a configured {product-registry} or a mirror registry.

include::modules/developer-cli-odo-pushing-the-odo-init-image-to-a-mirror-registry.adoc[leveloffset=+1]
include::modules/developer-cli-odo-pushing-the-odo-init-image-to-an-internal-registry-directly.adoc[leveloffset=+1]
