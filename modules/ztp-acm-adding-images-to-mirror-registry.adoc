// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

:_mod-docs-content-type: PROCEDURE
[id="ztp-acm-adding-images-to-mirror-registry_{context}"]
= Adding {op-system} ISO and RootFS images to the disconnected mirror host

Before you begin installing clusters in the disconnected environment with {rh-rhacm-first}, you must first host {op-system-first} images for it to use. Use a disconnected mirror to host the {op-system} images.

.Prerequisites

* Deploy and configure an HTTP server to host the {op-system} image resources on the network. You must be able to access the HTTP server from your computer, and from the machines that you create.

[IMPORTANT]
====
The {op-system} images might not change with every release of {product-title}. You must download images with the highest version that is less than or equal to the version that you install. Use the image versions that match your {product-title} version if they are available. You require ISO and RootFS images to install {op-system} on the hosts. {op-system} QCOW2 images are not supported for this installation type.
====

.Procedure

. Log in to the mirror host.
. Obtain the {op-system} ISO and RootFS images from link:https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/[mirror.openshift.com], for example:

.. Export the required image names and {product-title} version as environment variables:
+
[source,terminal]
----
$ export ISO_IMAGE_NAME=<iso_image_name> <1>
----
+
[source,terminal]
----
$ export ROOTFS_IMAGE_NAME=<rootfs_image_name> <2>
----
+
[source,terminal]
----
$ export OCP_VERSION=<ocp_version> <3>
----
<1> ISO image name, for example, `rhcos-{product-version}.1-x86_64-live.x86_64.iso`
<2> RootFS image name, for example, `rhcos-{product-version}.1-x86_64-live-rootfs.x86_64.img`
<3> {product-title} version, for example, `{product-version}.1`

.. Download the required images:
+
[source,terminal,subs="attributes+"]
----
$ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/{product-version}/${OCP_VERSION}/${ISO_IMAGE_NAME} -O /var/www/html/${ISO_IMAGE_NAME}
----
+
[source,terminal,subs="attributes+"]
----
$ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/{product-version}/${OCP_VERSION}/${ROOTFS_IMAGE_NAME} -O /var/www/html/${ROOTFS_IMAGE_NAME}
----

.Verification steps

* Verify that the images downloaded successfully and are being served on the disconnected mirror host, for example:
+
[source,terminal]
----
$ wget http://$(hostname)/${ISO_IMAGE_NAME}
----
+
.Example output
+
[source,terminal,subs="attributes+"]
----
Saving to: rhcos-{product-version}.1-x86_64-live.x86_64.iso
rhcos-{product-version}.1-x86_64-live.x86_64.iso-  11%[====>    ]  10.01M  4.71MB/s
----
