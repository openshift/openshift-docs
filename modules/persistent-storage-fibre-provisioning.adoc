// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-fibre.adoc

[id="provisioning-fibre_{context}"]
= Provisioning
To provision Fibre Channel volumes using the `PersistentVolume` API
the following must be available:

* The `targetWWNs` (array of Fibre Channel target's World Wide
Names).
* A valid LUN number.
* The filesystem type.

A persistent volume and a LUN have a one-to-one mapping between them.

.Prerequisites

* Fibre Channel LUNs must exist in the underlying infrastructure.

.`PersistentVolume` object definition

[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0001
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  fc:
    wwids: [scsi-3600508b400105e210000900000490000] <1>
    targetWWNs: ['500a0981891b8dc5', '500a0981991b8dc5'] <2>
    lun: 2 <2>
    fsType: ext4
----
<1> World wide identifiers (WWIDs). Either FC `*wwids*` or a combination of FC `*targetWWNs*` and `*lun*` must be set, but not both simultaneously. The FC WWID identifier is recommended over the WWNs target because it is guaranteed to be unique for every storage device, and independent of the path that is used to access the device. The WWID identifier can be obtained by issuing a SCSI Inquiry to retrieve the Device Identification Vital Product Data (`*page 0x83*`) or Unit Serial Number (`*page 0x80*`). FC WWIDs are identified as `*/dev/disk/by-id/*` to reference the data on the disk, even if the path to the device changes and even when accessing the device from different systems.
<2> Fibre Channel WWNs are identified as
`/dev/disk/by-path/pci-<IDENTIFIER>-fc-0x<WWN>-lun-<LUN#>`,
but you do not need to provide any part of the path leading up to the `WWN`,
including the `0x`, and anything after, including the `-` (hyphen).

[IMPORTANT]
====
Changing the value of the `fstype` parameter after the volume has been
formatted and provisioned can result in data loss and pod failure.
====
