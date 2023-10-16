// Module included in the following assemblies:
//
// * security/container_security/security-storage.adoc

[id="security-network-storage-block_{context}"]
= Block storage

For block storage providers like AWS Elastic Block Store (EBS), GCE Persistent
Disks, and iSCSI, {product-title} uses SELinux capabilities to secure the root
of the mounted volume for non-privileged pods, making the mounted volume owned
by and only visible to the container with which it is associated.
