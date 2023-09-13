// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc


[id="using_fsGroup_{context}"]
= Using fsGroup to reduce pod timeouts

If a storage volume contains many files (~1,000,000 or greater), you may experience pod timeouts.

This can occur because, by default, {product-title} recursively changes ownership and permissions for the contents of each volume to match the `fsGroup` specified in a pod's `securityContext` when that volume is mounted. For large volumes, checking and changing ownership and permissions can be time consuming, slowing pod startup. You can use the `fsGroupChangePolicy` field inside a `securityContext` to control the way that {product-title} checks and manages ownership and permissions for a volume.

`fsGroupChangePolicy` defines behavior for changing ownership and permission of the volume before being exposed inside a pod. This field only applies to volume types that support `fsGroup`-controlled ownership and permissions. This field has two possible values:

* `OnRootMismatch`: Only change permissions and ownership if permission and ownership of root directory does not match with expected permissions of the volume. This can help shorten the time it takes to change ownership and permission of a volume to reduce pod timeouts.

* `Always`: Always change permission and ownership of the volume when a volume is mounted.

.`fsGroupChangePolicy` example
[source,yaml]
----
securityContext:
  runAsUser: 1000
  runAsGroup: 3000
  fsGroup: 2000
  fsGroupChangePolicy: "OnRootMismatch" <1>
  ...
----
<1> `OnRootMismatch` specifies skipping recursive permission change, thus helping to avoid pod timeout problems.

[NOTE]
====
The fsGroupChangePolicyfield has no effect on ephemeral volume types, such as secret, configMap, and emptydir.
====
