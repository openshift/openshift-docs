// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_rh/virt-creating-vms-from-templates.adoc

[id="virt-vm-storage-volume-types_{context}"]
= Storage volume types

.Storage volume types
[cols="1a,3a"]
|===
|Type |Description

|ephemeral
|A local copy-on-write (COW) image that uses a network volume as a read-only backing store. The backing volume must be a *PersistentVolumeClaim*. The ephemeral image is created when the virtual machine starts and stores all writes locally. The ephemeral image is discarded when the virtual machine is stopped, restarted, or deleted. The backing volume (PVC) is not mutated in any way.

|persistentVolumeClaim
|Attaches an available PV to a virtual machine. Attaching a PV allows for the virtual machine data to persist between sessions.

Importing an existing virtual machine disk into a PVC by using CDI and attaching the PVC to a virtual machine instance is the recommended method for importing existing virtual machines into {product-title}. There are some requirements for the disk to be used within a PVC.

|dataVolume
|Data volumes build on the `persistentVolumeClaim` disk type by managing the process of preparing the virtual machine disk via an import, clone, or upload operation. VMs that use this volume type are guaranteed not to start until the volume is ready.

Specify `type: dataVolume` or `type: ""`. If you specify any other value for `type`, such as `persistentVolumeClaim`, a warning is displayed, and the virtual machine does not start.

|cloudInitNoCloud
|Attaches a disk that contains the referenced cloud-init NoCloud data source, providing user data and metadata to the virtual machine. A cloud-init installation is required inside the virtual machine disk.

|containerDisk
|References an image, such as a virtual machine disk, that is stored in the container image registry. The image is pulled from the registry and attached to the virtual machine as a disk when the virtual machine is launched.

A `containerDisk` volume is not limited to a single virtual machine and is useful for creating large numbers of virtual machine clones that do not require persistent storage.

Only RAW and QCOW2 formats are supported disk types for the container image registry. QCOW2 is recommended for reduced image size.

[NOTE]
====
A `containerDisk` volume is ephemeral. It is discarded when the virtual machine is stopped, restarted, or deleted. A `containerDisk` volume is useful for read-only file systems such as CD-ROMs or for disposable virtual machines.
====

|emptyDisk
|Creates an additional sparse QCOW2 disk that is tied to the life-cycle of the virtual machine interface. The data survives guest-initiated reboots in the virtual machine but is discarded when the virtual machine stops or is restarted from the web console. The empty disk is used to store application dependencies and data that otherwise exceeds the limited temporary file system of an ephemeral disk.

The disk *capacity* size must also be provided.

|===
