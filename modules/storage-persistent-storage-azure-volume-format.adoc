// Module included in the following assemblies:
//
// * storage/persistent_storage-azure.adoc

[id="volume-format-azure_{context}"]
= Volume format
Before {product-title} mounts the volume and passes it to a container, it checks
that it contains a file system as specified by the `fsType` parameter in the
persistent volume definition. If the device is not formatted with the file
system, all data from the device is erased and the device is automatically
formatted with the given file system.

This allows using unformatted Azure volumes as persistent volumes, because
{product-title} formats them before the first use.
