:_mod-docs-content-type: ASSEMBLY
[id="persistent-storage-using-fibre"]
= Persistent storage using Fibre Channel
include::_attributes/common-attributes.adoc[]
:context: persistent-storage-fibre

toc::[]

{product-title} supports Fibre Channel, allowing you to provision your
{product-title} cluster with persistent storage using Fibre channel volumes.
Some familiarity with Kubernetes and Fibre Channel is assumed.

[IMPORTANT]
====
Persistent storage using Fibre Channel is not supported on ARM architecture based infrastructures.
====

The Kubernetes persistent volume framework allows administrators to provision a
cluster with persistent storage and gives users a way to request those
resources without having any knowledge of the underlying infrastructure.
Persistent volumes are not bound to a single project or namespace; they can be
shared across the {product-title} cluster.
Persistent volume claims are specific to a project or namespace and can be
requested by users.

[IMPORTANT]
====
High availability of storage in the infrastructure is left to the underlying
storage provider.
====

[role="_additional-resources"]
.Additional resources

* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_storage_devices/using-fibre-channel-devices_managing-storage-devices[Using Fibre Channel devices]

include::modules/persistent-storage-fibre-provisioning.adoc[leveloffset=+1]

include::modules/persistent-storage-fibre-disk-quotas.adoc[leveloffset=+2]

include::modules/persistent-storage-fibre-volume-security.adoc[leveloffset=+2]
