// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc
// * Unused. Can be removed by 4.9 if still unused. Request full peer review for the module if it’s used.

[id="images-s2i-java-pulling-images_{context}"]
= Pulling images for Java

The Red Hat Enterprise Linux (RHEL) 8 image is available through the Red Hat Registry.

.Procedure

. To pull the RHEL 8 image, enter the following command:
[source,terminal]
----
$ podman pull registry.redhat.io/redhat-openjdk-18/openjdk18-openshift
----

To use this image on {product-title}, you can either access it directly from the Red Hat Registry or push it into your {product-title} container image registry. Additionally, you can create an image stream that points to the image, either in your container image registry or at the external location.

////
Your {product-title} resources can then reference the link:https://github.com/jboss-openshift/application-templates/blob/master/jboss-image-streams.json[image stream definition].
////
