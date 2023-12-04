// Module included in the following assembly:
//
// * ../scalability_and_performance/optimization/optimizing-storage.adoc

:_mod-docs-content-type: REFERENCE

[id="optimizing-storage-azure_{context}"]
= Optimizing storage performance for Microsoft Azure

{product-title} and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes.

For production Azure clusters and clusters with intensive workloads, the virtual machine operating system disk for control plane machines should be able to sustain a tested and recommended minimum throughput of 5000 IOPS / 200MBps.
This throughput can be provided by having a minimum of 1 TiB Premium SSD (P30).
In Azure and Azure Stack Hub, disk performance is directly dependent on SSD disk sizes. To achieve the throughput supported by a `Standard_D8s_v3` virtual machine, or other similar machine types, and the target of 5000 IOPS, at least a P30 disk is required.

Host caching must be set to `ReadOnly` for low latency and high IOPS and throughput when reading data. Reading data from the cache, which is present either in the VM memory or in the local SSD disk, is much faster than reading from the disk, which is in the blob storage.
