// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="lvms-configuring-lvms-on-sno_{context}"]
= {lvms}

You can dynamically provision local storage on {sno} clusters with {lvms-first}.

[NOTE]
====
The recommended storage solution for {sno} is the Local Storage Operator. Alternatively, you can use {lvms} but it requires additional CPU resources to be allocated.
====

The following YAML example configures the storage of the node to be available to {product-title} applications.

.Recommended `LVMCluster` configuration (`StorageLVMCluster.yaml`)
[source,yaml]
----
include::snippets/ztp_StorageLVMCluster.yaml[]
----

.`LVMCluster` CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|LVMCluster CR field
|Description

|`deviceSelector.paths`
|Configure the disks used for LVM storage. If no disks are specified, the {lvms} uses all the unused disks in the specified thin pool.
|====
