// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-uploading-local-disk-images-block.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-an-upload-dv_{context}"]
= Creating an upload data volume

You can manually create a data volume with an `upload` data source to upload local disk images.

.Procedure

. Create a data volume configuration that specifies `upload` in the `spec.source` stanza:
+
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: <datavolume> <1>
spec:
  source:
    upload: {}
  storage:
    resources:
      requests:
        storage: <2Gi> <2>
----
<1> Specify the name of the new data volume.
<2> Specify the amount of available space requested for the data volume. This value must be greater than or equal to the _virtual_ size of the disk that you upload.

. Create the data volume by running the following command:
+
[source,terminal]
----
$ oc create -f <datavolume>.yaml
----
