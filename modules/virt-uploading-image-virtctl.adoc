// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-uploading-image-virtctl_{context}"]
= Creating a VM from an uploaded image by using the command line

You can upload an operating system image by using the `virtctl` command line tool. You can use an existing data volume or create a new data volume for the image.

.Prerequisites

* You must have an `ISO`, `IMG`, or `QCOW2` operating system image file.
* For best performance, compress the image file by using the link:https://libguestfs.org/virt-sparsify.1.html[virt-sparsify] tool or the `xz` or `gzip` utilities.
* You must have `virtctl` installed.
* The client machine must be configured to trust the {product-title} router's
certificate.

.Procedure

. Upload the image by running the `virtctl image-upload` command:
+
[source,terminal]
----
$ virtctl image-upload dv <datavolume_name> \ <1>
  --size=<datavolume_size> \ <2>
  --image-path=</path/to/image> \ <3>
----
<1> The name of the data volume.
<2> The size of the data volume. For example: `--size=500Mi`, `--size=1G`
<3> The file path of the image.
+
[NOTE]
====
* If you do not want to create a new data volume, omit the `--size` parameter and include the `--no-create` flag.
* When uploading a disk image to a PVC, the PVC size must be larger than the size of the uncompressed virtual disk.
* To allow insecure server connections when using HTTPS, use the `--insecure` parameter. When you use the `--insecure` flag, the authenticity of the upload endpoint is *not* verified.
====

. Optional. To verify that a data volume was created, view all data volumes by running the following command:
+
[source,terminal]
----
$ oc get dvs
----
