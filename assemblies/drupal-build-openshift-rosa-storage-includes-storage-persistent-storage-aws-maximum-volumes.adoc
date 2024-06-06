// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc

[id="maximum-number-of-ebs-volumes-on-a-node_{context}"]
= Maximum number of EBS volumes on a node

By default, {product-title} supports a maximum of 39 EBS volumes attached to one
node. This limit is consistent with the
link:https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html#linux-specific-volume-limits[AWS volume limits]. The volume limit depends on the instance type.

[IMPORTANT]
====
As a cluster administrator, you must use either in-tree or Container Storage Interface (CSI) volumes and their respective storage classes, but never both volume types at the same time. The maximum attached EBS volume number is counted separately for in-tree and CSI volumes, which means you could have up to 39 EBS volumes of each type.
====
