// Be sure to set the :provider: value in each assembly
// on the line before the include statement for this module.
// For example:
// :provider: AWS
//
// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc
// * storage/persistent_storage-gce.adoc

[id="volume-format-{provider}_{context}"]
= Volume format
Before {product-title} mounts the volume and passes it to a container, it
checks that the volume contains a file system as specified by the `fsType`
parameter in the persistent volume definition. If the device is not
formatted with the file system, all data from the device is erased and the
device is automatically formatted with the given file system.

This verification enables you to use unformatted {provider} volumes as persistent volumes,
because {product-title} formats them before the first use.

// Undefined {provider} attribute, so that any mistakes are easily spotted
:!provider:
