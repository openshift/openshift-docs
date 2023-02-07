// Module included in the following assemblies:
//
// * storage/optimizing-storage.adoc

[id="data-storage-management_{context}"]
= Data storage management

The following table summarizes the main directories that {product-title} components write data to.

.Main directories for storing {product-title} data
[options="header,footer"]
|===
|Directory|Notes|Sizing|Expected growth

|*_/var/lib/etcd_*
|Used for etcd storage when storing the database.
|Less than 20 GB.

Database can grow up to 8 GB.
|Will grow slowly with the environment. Only storing metadata.

Additional 20-25 GB for every additional 8 GB of memory.

|*_/var/lib/containers_*
|This is the mount point for the CRI-O runtime. Storage used for active container runtimes, including pods, and storage of local images. Not used for registry storage.
|50 GB for a node with 16 GB memory. Note that this sizing should not be used to determine minimum cluster requirements.

Additional 20-25 GB for every additional 8 GB of memory.
|Growth is limited by capacity for running containers.

|*_/var/lib/kubelet_*
|Ephemeral volume storage for pods. This includes anything external that is mounted into a container at runtime. Includes environment variables, kube secrets, and data volumes not backed by persistent volumes.
|Varies
|Minimal if pods requiring storage are using persistent volumes. If using ephemeral storage, this can grow quickly.

|*_/var/log_*
|Log files for all components.
|10 to 30 GB.
|Log files can grow quickly; size can be managed by growing disks or by using log rotate.

|===
