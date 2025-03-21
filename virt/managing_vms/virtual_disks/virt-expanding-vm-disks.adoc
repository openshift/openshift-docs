:_mod-docs-content-type: ASSEMBLY
[id="virt-expanding-vm-disks"]
= Expanding virtual machine disks
include::_attributes/common-attributes.adoc[]
:context: virt-expanding-vm-disks

toc::[]

You can increase the size of a virtual machine (VM) disk by expanding the persistent volume claim (PVC) of the disk.

If your storage provider does not support volume expansion, you can expand the available virtual storage of a VM by adding blank data volumes.

You cannot reduce the size of a VM disk.

include::modules/virt-expanding-vm-disk-pvc.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources for volume expansion
* link:https://docs.microsoft.com/en-us/windows-server/storage/disk-management/extend-a-basic-volume[Extending a basic volume in Windows]
* link:https://access.redhat.com/solutions/29095[Extending an existing file system partition without destroying data in Red Hat Enterprise Linux]
* link:https://access.redhat.com/solutions/24770[Extending a logical volume and its file system online in Red Hat Enterprise Linux]

include::modules/virt-expanding-storage-with-data-volumes.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources for data volumes
* xref:../../../virt/storage/virt-using-preallocation-for-datavolumes.adoc#virt-using-preallocation-for-datavolumes[Configuring preallocation mode for data volumes]
* xref:../../../virt/storage/virt-managing-data-volume-annotations.adoc#virt-managing-data-volume-annotations[Managing data volume annotations]

