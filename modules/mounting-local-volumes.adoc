[id="mounting-local-volumes_{context}"]
= Mounting local volumes

This paragraph is the procedure module introduction: a short description of the procedure.

.Prerequisites

* All local volumes must be manually mounted before they can be consumed by {product-title} as PVs.

.Procedure

. Mount all volumes into the `*/mnt/local-storage/<storage-class-name>/<volume>*` path:
+
----
# device name   # mount point                  # FS    # options # extra
/dev/sdb1       /mnt/local-storage/ssd/disk1 ext4     defaults 1 2
/dev/sdb2       /mnt/local-storage/ssd/disk2 ext4     defaults 1 2
/dev/sdb3       /mnt/local-storage/ssd/disk3 ext4     defaults 1 2
/dev/sdc1       /mnt/local-storage/hdd/disk1 ext4     defaults 1 2
/dev/sdc2       /mnt/local-storage/hdd/disk2 ext4     defaults 1 2
----
+
Administrators must create local devices as needed using any method such as disk partition or LVM, create suitable file systems on these devices, and mount these devices using a script or /etc/fstab entries

. Make all volumes accessible to the processes running within the Docker containers:
+
----
$ chcon -R unconfined_u:object_r:svirt_sandbox_file_t:s0 /mnt/local-storage/
----
