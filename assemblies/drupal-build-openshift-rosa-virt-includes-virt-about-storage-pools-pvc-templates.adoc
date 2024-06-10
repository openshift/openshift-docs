// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-local-storage-with-hpp.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-storage-pools-pvc-templates_{context}"]
= About storage pools created with PVC templates

If you have a single, large persistent volume (PV), you can create a storage pool by defining a PVC template in the hostpath provisioner (HPP) custom resource (CR).

A storage pool created with a PVC template can contain multiple HPP volumes. Splitting a PV into smaller volumes provides greater flexibility for data allocation.

The PVC template is based on the `spec` stanza of the `PersistentVolumeClaim` object:

.Example `PersistentVolumeClaim` object
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: iso-pvc
spec:
  volumeMode: Block <1>
  storageClassName: my-storage-class
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
----
<1> This value is only required for block volume mode PVs.

You define a storage pool using a `pvcTemplate` specification in the HPP CR. The Operator creates a PVC from the `pvcTemplate` specification for each node containing the HPP CSI driver. The PVC created from the PVC template consumes the single large PV, allowing the HPP to create smaller dynamic volumes.

You can combine basic storage pools with storage pools created from PVC templates.
