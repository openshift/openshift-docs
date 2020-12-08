// Module included in the following assemblies:
//
// storage/persistent_storage/persistent-storage-azure-file.adoc
// * post_installation_configuration/storage-configuration.adoc

[id="azure-file-considerations_{context}"]
= Considerations when using Azure File

The following file system features are not supported by the default Azure File storage class:

* Symlinks
* Hard links
* Extended attributes
* Sparse files
* Named pipes

Additionally, the owner user identifier (UID) of the Azure File mounted directory is different from the process UID of the container. The `uid` mount option can be specified in the `StorageClass` object to define
a specific user identifier to use for the mounted directory.

The following `StorageClass` object demonstrates modifying the user and group identifier, along with enabling symlinks for the mounted directory.

[source,yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: azure-file
mountOptions:
  - uid=1500 <1>
  - gid=1500 <2>
  - mfsymlinks <3>
provisioner: kubernetes.io/azure-file
parameters:
  location: eastus
  skuName: Standard_LRS
reclaimPolicy: Delete
volumeBindingMode: Immediate
----
<1> Specifies the user identifier to use for the mounted directory.
<2> Specifies the group identifier to use for the mounted directory.
<3> Enables symlinks.
