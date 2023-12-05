:_mod-docs-content-type: ASSEMBLY
[id="persistent-storage-using-flexvolume"]
= Persistent storage using FlexVolume
include::_attributes/common-attributes.adoc[]
:context: persistent-storage-flexvolume

toc::[]

[IMPORTANT]
====
FlexVolume is a deprecated feature. Deprecated functionality is still included in {product-title} and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.

Out-of-tree Container Storage Interface (CSI) driver is the recommended way to write volume drivers in {product-title}. Maintainers of FlexVolume drivers should implement a CSI driver and move users of FlexVolume to CSI. Users of FlexVolume should move their workloads to CSI driver.

For the most recent list of major functionality that has been deprecated or removed within {product-title}, refer to the _Deprecated and removed features_ section of the {product-title} release notes.
====

{product-title} supports FlexVolume, an out-of-tree plugin that uses an executable model to interface with drivers.

To use storage from a back-end that does not have a built-in plugin, you can extend {product-title} through FlexVolume drivers and provide persistent storage to applications.

Pods interact with FlexVolume drivers through the `flexvolume` in-tree plugin.

[role="_additional-resources"]
.Additional resources

* xref:../../storage/expanding-persistent-volumes.adoc#expanding-persistent-volumes[Expanding persistent volumes]

include::modules/persistent-storage-flexvolume-drivers.adoc[leveloffset=+1]

include::modules/persistent-storage-flexvolume-driver-example.adoc[leveloffset=+1]

include::modules/persistent-storage-flexvolume-installing.adoc[leveloffset=+1]

include::modules/persistent-storage-flexvolume-consuming.adoc[leveloffset=+1]
