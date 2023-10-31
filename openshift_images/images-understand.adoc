:_mod-docs-content-type: ASSEMBLY
[id="understanding-images"]
= Understanding containers, images, and image streams
include::_attributes/common-attributes.adoc[]
:context: images-understand

toc::[]

Containers, images, and image streams are important concepts to understand when you set out to create and manage containerized software. An image holds a set of software that is ready to run, while a container is a running instance of a container image. An image stream provides a way of storing different versions of the same basic image. Those different versions are represented by different tags on the same image name.

include::modules/images-about.adoc[leveloffset=+1]
include::modules/containers-about.adoc[leveloffset=+1]
include::modules/images-image-registry-about.adoc[leveloffset=+1]
include::modules/images-container-repository-about.adoc[leveloffset=+1]
include::modules/images-tag.adoc[leveloffset=+1]
include::modules/images-id.adoc[leveloffset=+1]
include::modules/images-imagestream-use.adoc[leveloffset=+1]
include::modules/images-imagestream-tag.adoc[leveloffset=+1]
include::modules/images-imagestream-image.adoc[leveloffset=+1]
include::modules/images-imagestream-trigger.adoc[leveloffset=+1]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
[role="_additional-resources"]
== Additional resources

* For more information on using image streams, see xref:../openshift_images/image-streams-manage.adoc#managing-image-streams[Managing image streams].
endif::[]
