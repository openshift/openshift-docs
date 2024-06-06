// Module included in the following assemblies:
//
// * virt/storage/virt-using-preallocation-for-datavolumes.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-preallocation_{context}"]
= About preallocation

The Containerized Data Importer (CDI) can use the QEMU preallocate mode for data volumes to improve write performance. You can use preallocation mode for importing and uploading operations and when creating blank data volumes.

If preallocation is enabled, CDI uses the better preallocation method depending on the underlying file system and device type:

`fallocate`::
If the file system supports it, CDI uses the operating system's `fallocate` call to preallocate space by using the `posix_fallocate` function, which allocates blocks and marks them as uninitialized.

`full`::
If `fallocate` mode cannot be used, `full` mode allocates space for the image by writing data to the underlying storage. Depending on the storage location, all the empty allocated space might be zeroed.
