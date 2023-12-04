// Module included in the following assemblies:
//
// * virt/storage/virt-creating-data-volumes.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-data-volumes-using-storage-api_{context}"]
= Creating data volumes by using the storage API

When you create a data volume by using the storage API, the Containerized Data Interface (CDI) optimizes your persistent volume claim (PVC) allocation based on the type of storage supported by your selected storage class. You only have to specify the data volume name, namespace, and the amount of storage that you want to allocate.

For example:

* When using Ceph RBD, `accessModes` is automatically set to `ReadWriteMany`, which enables live migration. `volumeMode` is set to `Block` to maximize performance.
* When you are using `volumeMode: Filesystem`, more space will automatically be requested by CDI, if required to accommodate file system overhead.

In the following YAML, using the storage API requests a data volume with two gigabytes of usable space. The user does not need to know the `volumeMode` in order to correctly estimate the required persistent volume claim (PVC) size. CDI chooses the optimal combination of `accessModes` and `volumeMode` attributes automatically.  These optimal values are based on the type of storage or the defaults that you define in your storage profile. If you want to provide custom values, they override the system-calculated values.

.Procedure

. Create a YAML file for a `DataVolume` object as shown in the following example:
+
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: <datavolume> <1>
spec:
  source:
    pvc:
      name: "<my_vm_disk>" <2>
      namespace: "<source_namespace>" <3>
  storage:
    storageClassName: <storage_class> <4>
----
<1> Specify the name of the new data volume.
<2> Specify the namespace of the source PVC.
<3> Specify the name of the source PVC.
<4> Optional: If the storage class is not specified, the default storage class is used.

. Create the data volume by running the following command:
+
[source,terminal]
----
$ oc create -f <datavolume>.yaml
----