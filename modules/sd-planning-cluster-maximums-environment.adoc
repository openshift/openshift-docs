// Module included in the following assemblies:
//
// * osd_planning/osd-limits-scalability.adoc
// * rosa_planning/rosa-limits-scalability.adoc

[id="planning-cluster-maximums-environment-sd_{context}"]
= OpenShift Container Platform testing environment and configuration

The following table lists the OpenShift Container Platform environment and configuration on which the cluster maximums are tested for the AWS cloud platform.

[options="header",cols="8*"]
|===
| Node |Type |vCPU |RAM(GiB) |Disk type|Disk size(GiB)/IOPS |Count |Region

|Control plane/etcd ^[1]^
|m5.4xlarge
|16
|64
|gp3
|350 / 1,000
|3
|us-west-2

|Infrastructure nodes ^[2]^
|r5.2xlarge
|8
|64
|gp3
|300 / 900
|3
|us-west-2

|Workload ^[3]^
|m5.2xlarge
|8
|32
|gp3
|350 / 900
|3
|us-west-2

|Compute nodes
|m5.2xlarge
|8
|32
|gp3
|350 / 900
|102
|us-west-2
|===
[.small]
--
1. io1 disks are used for control plane/etcd nodes in all versions prior to 4.10.
2. Infrastructure nodes are used to host monitoring components because Prometheus can claim a large amount of memory, depending on usage patterns.
3. Workload nodes are dedicated to run performance and scalability workload generators.
--

Larger cluster sizes and higher object counts might be reachable. However, the sizing of the infrastructure nodes limits the amount of memory that is available to Prometheus. When creating, modifying, or deleting objects, Prometheus stores the metrics in its memory for roughly 3 hours prior to persisting the metrics on disk. If the rate of creation, modification, or deletion of objects is too high, Prometheus can become overwhelmed and fail due to the lack of memory resources.
