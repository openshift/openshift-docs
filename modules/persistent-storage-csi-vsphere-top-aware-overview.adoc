// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

:content-type: CONCEPT
[id="persistent-storage-csi-vsphere-top-aware-overview_{context}"]
= vSphere CSI topology overview

{product-title} provides the ability to deploy {product-title} for vSphere on different zones and regions, which allows you to deploy over multiple compute clusters and datacenters, thus helping to avoid a single point of failure. 

This is accomplished by defining zone and region categories in vCenter, and then assigning these categories to different failure domains, such as a compute cluster, by creating tags for these zone and region categories. After you have created the appropriate categories, and assigned tags to vCenter objects, you can create additional machinesets that create virtual machines (VMs) that are responsible for scheduling pods in those failure domains.

The following example defines two failure domains with one region and two zones:

.vSphere storage topology with one region and two zones
|===
|Compute cluster | Failure domain |Description

|Compute cluster: ocp1, 
Datacenter: Atlanta
|openshift-region: us-east-1 (tag), openshift-zone: us-east-1a (tag)
|This defines a failure domain in region us-east-1 with zone us-east-1a.

|Computer cluster: ocp2, 
Datacenter: Atlanta
|openshift-region: us-east-1 (tag), openshift-zone: us-east-1b (tag)
|This defines a different failure domain within the same region called us-east-1b.
|===