// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc


[id="persistent-storage-csi-architecture_{context}"]
= CSI architecture

CSI drivers are typically shipped as container images. These containers
are not aware of {product-title} where they run. To use CSI-compatible
storage back end in {product-title}, the cluster administrator must deploy
several components that serve as a bridge between {product-title} and the
storage driver.

The following diagram provides a high-level overview about the components
running in pods in the {product-title} cluster.

image::csi-arch-rev1.png["Architecture of CSI components"]

It is possible to run multiple CSI drivers for different storage back ends.
Each driver needs its own external controllers deployment and daemon set
with the driver and CSI registrar.
