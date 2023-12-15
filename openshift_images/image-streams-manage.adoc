:_mod-docs-content-type: ASSEMBLY
[id="managing-image-streams"]
= Managing image streams
include::_attributes/common-attributes.adoc[]
:context: image-streams-managing

toc::[]

Image streams provide a means of creating and updating container images in an on-going way. As improvements are made to an image, tags can be used to assign new version numbers and keep track of changes. This document describes how image streams are managed.

include::modules/images-imagestream-use.adoc[leveloffset=+1]
include::modules/images-imagestream-configure.adoc[leveloffset=+1]
include::modules/images-using-imagestream-images.adoc[leveloffset=+1]
include::modules/images-using-imagestream-tags.adoc[leveloffset=+1]
include::modules/images-using-imagestream-change-triggers.adoc[leveloffset=+1]
ifndef::openshift-rosa,openshift-dedicated[]
include::modules/images-imagestream-mapping.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]

== Working with image streams

The following sections describe how to use image streams and image stream tags.

include::snippets/default-projects.adoc[]

include::modules/images-getting-info-about-imagestreams.adoc[leveloffset=+2]
include::modules/images-imagestream-adding-tags.adoc[leveloffset=+2]
include::modules/images-imagestream-external-image-tags.adoc[leveloffset=+2]
include::modules/images-imagestream-update-tag.adoc[leveloffset=+2]
include::modules/images-imagestream-remove-tag.adoc[leveloffset=+2]

See xref:../openshift_images/configuring-samples-operator.adoc#images-samples-operator-deprecated-image-stream_configuring-samples-operator[Removing deprecated image stream tags from the Cluster Samples Operator] for more information on how the Cluster Samples Operator handles deprecated image stream tags.

include::modules/images-imagestream-import.adoc[leveloffset=+2]

[id="images-imagestream-import-images-image-streams"]
== Importing and working with images and image streams

The following sections describe how to import, and work with, image streams.

include::modules/images-imagestream-import-images-private-registry.adoc[leveloffset=+2]
include::modules/images-allow-pods-to-reference-images-from-secure-registries.adoc[leveloffset=+3]


include::modules/images-imagestream-import-import-mode.adoc[leveloffset=+2]
include::modules/images-imagestream-periodic-import-list.adoc[leveloffset=+3]
include::modules/images-imagestream-ssl-import-list.adoc[leveloffset=+3]
include::modules/images-imagestream-specify-architecture.adoc[leveloffset=+2]
include::modules/importmode-configuration-fields.adoc[leveloffset=+2]
