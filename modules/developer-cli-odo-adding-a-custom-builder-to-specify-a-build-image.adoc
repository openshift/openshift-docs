// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating-a-single-component-application-with-odo.adoc

:_mod-docs-content-type: PROCEDURE
[id="adding-a-custom-builder-to-specify-a-build-image_{context}"]
= Adding a custom builder to specify a build image

With {product-title}, you can add a custom image to bridge the gap between the creation of custom images.

The following example demonstrates the successful import and use of the `redhat-openjdk-18` image:

.Prerequisites
* The OpenShift CLI (oc) is installed.

.Procedure

. Import the image into {product-title}:
+
[source,terminal]
----
$ oc import-image openjdk18 \
--from=registry.access.redhat.com/redhat-openjdk-18/openjdk18-openshift \
--confirm
----
. Tag the image to make it accessible to {odo-title}:
+
[source,terminal]
----
$ oc annotate istag/openjdk18:latest tags=builder
----
. Deploy the image with {odo-title}:
+
[source,terminal]
----
$ odo create openjdk18 --git \
https://github.com/openshift-evangelists/Wild-West-Backend
----
