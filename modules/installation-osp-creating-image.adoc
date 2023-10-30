//Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

:_mod-docs-content-type: PROCEDURE
[id="installation-osp-creating-image_{context}"]
= Creating the {op-system-first} image

The {product-title} installation program requires that a {op-system-first} image be present in the {rh-openstack-first} cluster. Retrieve the latest {op-system} image, then upload it using the {rh-openstack} CLI.

.Prerequisites

* The {rh-openstack} CLI is installed.

.Procedure

. Log in to the Red Hat Customer Portal's https://access.redhat.com/downloads/content/290[Product Downloads page].

. Under *Version*, select the most recent release of {product-title} {product-version} for {op-system-base-full} 8.
+
[IMPORTANT]
====
The {op-system} images might not change with every release of {product-title}.
You must download images with the highest version that is less than or equal to
the {product-title} version that you install. Use the image versions that match
your {product-title} version if they are available.
====

. Download the _{op-system-first} - OpenStack Image (QCOW)_.

. Decompress the image.
+
[NOTE]
====
You must decompress the {rh-openstack} image before the cluster can use it. The name of the downloaded file might not contain a compression extension, like `.gz` or `.tgz`. To find out if or how the file is compressed, in a command line, enter:

[source,terminal]
----
$ file <name_of_downloaded_file>
----

====

. From the image that you downloaded, create an image that is named `rhcos` in your cluster by using the {rh-openstack} CLI:
+
[source,terminal]
----
$ openstack image create --container-format=bare --disk-format=qcow2 --file rhcos-${RHCOS_VERSION}-openstack.qcow2 rhcos
----
+
[IMPORTANT]
Depending on your {rh-openstack} environment, you might be able to upload the image in either link:https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/15/html/instances_and_images_guide/index[`.raw` or `.qcow2` formats]. If you use Ceph, you must use the `.raw` format.
+
[WARNING]
If the installation program finds multiple images with the same name, it chooses one of them at random. To avoid this behavior, create unique names for resources in {rh-openstack}.

After you upload the image to {rh-openstack}, it is usable in the installation process.
