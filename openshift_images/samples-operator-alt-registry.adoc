:_mod-docs-content-type: ASSEMBLY
[id="samples-operator-alt-registry"]
= Using the Cluster Samples Operator with an alternate registry
include::_attributes/common-attributes.adoc[]
:context: samples-operator-alt-registry

toc::[]

You can use the Cluster Samples Operator with an alternate registry by first creating a mirror registry.

[IMPORTANT]
====
You must have access to the internet to obtain the necessary container images. In this procedure, you place the mirror registry on a mirror host that has access to both your network and the internet.
====

include::modules/installation-about-mirror-registry.adoc[leveloffset=+1]

ifndef::openshift-rosa,openshift-dedicated[]
.Additional information

For information on viewing the CRI-O logs to view the image source, see xref:../installing/validating-an-installation.adoc#viewing-the-image-pull-source_validating-an-installation[Viewing the image pull source].
endif::openshift-rosa,openshift-dedicated[]

[id="samples-preparing-bastion"]
=== Preparing the mirror host

Before you create the mirror registry, you must prepare the mirror host.

include::modules/cli-installing-cli.adoc[leveloffset=+2]

//include::modules/installation-local-registry-pull-secret.adoc[leveloffset=+1]

include::modules/installation-adding-registry-pull-secret.adoc[leveloffset=+1]

include::modules/installation-mirror-repository.adoc[leveloffset=+1]

include::modules/installation-restricted-network-samples.adoc[leveloffset=+1]

include::modules/installation-images-samples-disconnected-mirroring-assist.adoc[leveloffset=+2]

See xref:../openshift_images/samples-operator-alt-registry.adoc#installation-restricted-network-samples_samples-operator-alt-registry[Using Cluster Samples Operator image streams with alternate or mirrored registries] for a detailed procedure.
