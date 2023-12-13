:_mod-docs-content-type: ASSEMBLY
[id="triggering-updates-on-imagestream-changes"]
= Triggering updates on image stream changes
include::_attributes/common-attributes.adoc[]
:context: triggering-updates-on-imagestream-changes

toc::[]


When an image stream tag is updated to point to a new image, {product-title} can automatically take action to roll the new image out to resources that were using the old image. You configure this behavior in different ways depending on the type of resource that references the image stream tag.

[id="openshift-resources"]
== {product-title} resources

{product-title} deployment configurations and build configurations can be automatically triggered by changes to image stream tags. The triggered action can be run using the new value of the image referenced by the updated image stream tag.

include::modules/images-triggering-updates-imagestream-changes-kubernetes-about.adoc[leveloffset=+1]

include::modules/images-triggering-updates-imagestream-changes-kubernetes-cli.adoc[leveloffset=+1]
