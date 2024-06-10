:_mod-docs-content-type: ASSEMBLY
[id="using-images-overview"]
= Using images overview
include::_attributes/common-attributes.adoc[]
:context: using-images-overview

toc::[]

Use the following topics to discover the different Source-to-Image (S2I), database, and other container images that are available for {product-title} users.

Red Hat official container images are provided in the Red Hat Registry at link:https://registry.redhat.io[registry.redhat.io]. {product-title}'s supported S2I, database, and Jenkins images are provided in the `openshift4` repository in the Red Hat Quay Registry. For example, `quay.io/openshift-release-dev/ocp-v4.0-<address>` is the name of the OpenShift Application Platform image.

The xPaaS middleware images are provided in their respective product repositories on the Red Hat Registry but suffixed with a `-openshift`. For example, `registry.redhat.io/jboss-eap-6/eap64-openshift` is the name of the JBoss EAP image.

All Red Hat supported images covered in this section are described in the link:https://catalog.redhat.com/software/containers/explore[Container images section of the Red Hat Ecosystem Catalog]. For every version of each image, you can find details on its contents and usage. Browse or search for the image that interests you.

[IMPORTANT]
====
The newer versions of container images are not compatible with earlier versions of {product-title}. Verify and use the correct version of container images, based on your version of {product-title}.
====
