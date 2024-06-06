:_mod-docs-content-type: ASSEMBLY
[id="creating-images"]
= Creating images
include::_attributes/common-attributes.adoc[]
:context: create-images

toc::[]

Learn how to create your own container images, based on pre-built images that are ready to help you. The process includes learning best practices for writing images, defining metadata for images, testing images, and using a custom builder workflow to create images to use with {product-title}.
ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
After you create an image, you can push it to the {product-registry}.
endif::[]


// include::modules/builds-define-build-inputs.adoc[leveloffset=+1]

include::modules/images-create-guidelines.adoc[leveloffset=+1]
include::modules/images-create-guide-general.adoc[leveloffset=+2]
include::modules/images-create-guide-openshift.adoc[leveloffset=+2]
include::modules/images-create-metadata.adoc[leveloffset=+1]
include::modules/images-create-s2i.adoc[leveloffset=+1]
include::modules/images-create-s2i-build.adoc[leveloffset=+2]
include::modules/images-create-s2i-scripts.adoc[leveloffset=+2]

//Testing may have to move
include::modules/images-test-s2i.adoc[leveloffset=+1]


//Section - use openshift to build images - link to build strategies
