// Module included in the following assemblies:
//
// * nodes/nodes-pods-configuring.adoc
// * nodes/nodes-cluster-pods-configuring

:_mod-docs-content-type: REFERENCE
[id="nodes-pods-configuring-reducing_{context}"]
= Reducing pod timeouts when using persistent volumes with high file counts

If a storage volume contains many files (~1,000,000 or greater), you might experience pod timeouts.

This can occur because, when volumes are mounted, {product-title} recursively changes the ownership and permissions of the contents of each volume in order to match the `fsGroup` specified in a pod's `securityContext`. For large volumes, checking and changing the ownership and permissions can be time consuming, resulting in a very slow pod startup.

You can reduce this delay by applying one of the following workarounds:

* Use a security context constraint (SCC) to skip the SELinux relabeling for a volume.

* Use the `fsGroupChangePolicy` field inside an SCC to control the way that {product-title} checks and manages ownership and permissions for a volume.

* Use the Cluster Resource Override Operator to automatically apply an SCC to skip the SELinux relabeling.

* Use a runtime class to skip the SELinux relabeling for a volume.

For information, see link:https://access.redhat.com/solutions/6221251[When using Persistent Volumes with high file counts in OpenShift, why do pods fail to start or take an excessive amount of time to achieve "Ready" state?].
