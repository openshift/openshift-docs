// Module included in the following assemblies:
//
// * operators/admin/olm-status.adoc
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="olm-status-conditions_{context}"]
= Operator subscription condition types

Subscriptions can report the following condition types:

.Subscription condition types
[cols="1,2",options="header"]
|===
|Condition |Description

|`CatalogSourcesUnhealthy`
|Some or all of the catalog sources to be used in resolution are unhealthy.

|`InstallPlanMissing`
|An install plan for a subscription is missing.

|`InstallPlanPending`
|An install plan for a subscription is pending installation.

|`InstallPlanFailed`
|An install plan for a subscription has failed.

|`ResolutionFailed`
|The dependency resolution for a subscription has failed.

|===

[NOTE]
====
Default {product-title} cluster Operators are managed by the Cluster Version Operator (CVO) and they do not have a `Subscription` object. Application Operators are managed by Operator Lifecycle Manager (OLM) and they have a `Subscription` object.
====
