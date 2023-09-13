// Module included in the following assemblies:
//
// * updating/preparing_for_updates/updating-cluster-prepare.adoc

[id="update-preparing-list_{context}"]
= Removed Kubernetes APIs

{product-title} 4.14 uses Kubernetes 1.27, which removed the following deprecated APIs. You must migrate manifests and API clients to use the appropriate API version. For more information about migrating removed APIs, see the link:https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-27[Kubernetes documentation].

.APIs removed from Kubernetes 1.27
[cols="2,2,2",options="header",]
|===
|Resource |Removed API |Migrate to

|`CSIStorageCapacity`
|`storage.k8s.io/v1beta1`
|`storage.k8s.io/v1`

|===
// Removed the "Notable changes" column since they were all "No" and table so wide it was causing a scrollbar. Add it back in for the next time there are notable changes (1.29)
