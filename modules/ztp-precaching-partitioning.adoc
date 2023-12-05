// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-precaching-tool.adoc

:_module-type: PROCEDURE
[id="ztp-partitioning_{context}"]
= Partitioning the disk

To run the full pre-caching process, you have to boot from a live ISO and use the {factory-prestaging-tool} from a container image to partition and pre-cache all the artifacts required.

A live ISO or {op-system} live ISO is required because the disk must not be in use when the operating system ({op-system}) is written to the device during the provisioning.
Single-disk servers can also be enabled with this procedure.

.Prerequisites

* You have a disk that is not partitioned.
* You have access to the `quay.io/openshift-kni/telco-ran-tools:latest` image.
* You have enough storage to install {product-title} and pre-cache the required images.

.Procedure

. Verify that the disk is cleared:
+
[source,terminal]
----
# lsblk
----

+
.Example output
[source,terminal]
----
NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0     7:0    0  93.8G  0 loop /run/ephemeral
loop1     7:1    0 897.3M  1 loop /sysroot
sr0      11:0    1   999M  0 rom  /run/media/iso
nvme0n1 259:1    0   1.5T  0 disk
----

. Erase any file system, RAID or partition table signatures from the device:
+
[source,terminal]
----
# wipefs -a /dev/nvme0n1
----

+
.Example output
[source,terminal]
----
/dev/nvme0n1: 8 bytes were erased at offset 0x00000200 (gpt): 45 46 49 20 50 41 52 54
/dev/nvme0n1: 8 bytes were erased at offset 0x1749a955e00 (gpt): 45 46 49 20 50 41 52 54
/dev/nvme0n1: 2 bytes were erased at offset 0x000001fe (PMBR): 55 aa
----

[IMPORTANT]
====
The tool fails if the disk is not empty because it uses partition number 1 of the device for pre-caching the artifacts.
====

[id="ztp-create-partition_{context}"]
== Creating the partition

Once the device is ready, you create a single partition and a GPT partition table.
The partition is automatically labelled as `data` and created at the end of the device.
Otherwise, the partition will be overridden by the `coreos-installer`.

[IMPORTANT]
====
The `coreos-installer` requires the partition to be created at the end of the device and to be labelled as `data`. Both requirements are necessary to save the partition when writing the {op-system} image to the disk.
====

.Prerequisites

* The container must run as `privileged` due to formatting host devices.
* You have to mount the `/dev` folder so that the process can be executed inside the container.

.Procedure

In the following example, the size of the partition is 250 GiB due to allow pre-caching the DU profile for Day 2 Operators.

. Run the container as `privileged` and partition the disk:
+
[source,terminal]
----
# podman run -v /dev:/dev --privileged \
--rm quay.io/openshift-kni/telco-ran-tools:latest -- \
factory-precaching-cli partition \ <1>
-d /dev/nvme0n1 \ <2>
-s 250 <3>
----
<1> Specifies the partitioning function of the {factory-prestaging-tool}.
<2> Defines the root directory on the disk.
<3> Defines the size of the disk in GB.

. Check the storage information:
+
[source,terminal]
----
# lsblk
----

+
.Example output
[source,terminal]
----
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0         7:0    0  93.8G  0 loop /run/ephemeral
loop1         7:1    0 897.3M  1 loop /sysroot
sr0          11:0    1   999M  0 rom  /run/media/iso
nvme0n1     259:1    0   1.5T  0 disk
└─nvme0n1p1 259:3    0   250G  0 part
----

.Verification

You must verify that the following requirements are met:

* The device has a GPT partition table
* The partition uses the latest sectors of the device.
* The partition is correctly labeled as `data`.

Query the disk status to verify that the disk is partitioned as expected:

[source,terminal]
----
# gdisk -l /dev/nvme0n1
----

.Example output
[source,terminal]
----
GPT fdisk (gdisk) version 1.0.3

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.
Disk /dev/nvme0n1: 3125627568 sectors, 1.5 TiB
Model: Dell Express Flash PM1725b 1.6TB SFF
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): CB5A9D44-9B3C-4174-A5C1-C64957910B61
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 3125627534
Partitions will be aligned on 2048-sector boundaries
Total free space is 2601338846 sectors (1.2 TiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1      2601338880      3125627534   250.0 GiB   8300  data
----

[id="ztp-mount-partition_{context}"]
== Mounting the partition

After verifying that the disk is partitioned correctly, you can mount the device into `/mnt`.

[IMPORTANT]
====
It is recommended to mount the device into `/mnt` because that mounting point is used during {ztp} preparation.
====

. Verify that the partition is formatted as `xfs`:
+
[source,terminal]
----
# lsblk -f /dev/nvme0n1
----

+
.Example output
[source,terminal]
----
NAME        FSTYPE LABEL UUID                                 MOUNTPOINT
nvme0n1
└─nvme0n1p1 xfs          1bee8ea4-d6cf-4339-b690-a76594794071
----

. Mount the partition:
+
[source,terminal]
----
# mount /dev/nvme0n1p1 /mnt/
----

.Verification

* Check that the partition is mounted:
+
[source,terminal]
----
# lsblk
----

+
.Example output
[source,terminal]
----
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0         7:0    0  93.8G  0 loop /run/ephemeral
loop1         7:1    0 897.3M  1 loop /sysroot
sr0          11:0    1   999M  0 rom  /run/media/iso
nvme0n1     259:1    0   1.5T  0 disk
└─nvme0n1p1 259:2    0   250G  0 part /var/mnt <1>
----
<1> The mount point is `/var/mnt` because the `/mnt` folder in {op-system} is a link to `/var/mnt`.
