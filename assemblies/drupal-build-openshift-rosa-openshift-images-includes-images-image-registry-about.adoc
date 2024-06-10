// Module included in the following assemblies:
// * openshift_images/images-understand.adoc

[id="images-image-registry-about_{context}"]
= Image registry

An image registry is a content server that can store and serve container images. For example:

[source,text]
----
registry.redhat.io
----

A registry contains a collection of one or more image repositories, which contain one or more tagged images. Red Hat provides a registry at `registry.redhat.io` for subscribers. {product-title} can also supply its own {product-registry} for managing custom container images.
