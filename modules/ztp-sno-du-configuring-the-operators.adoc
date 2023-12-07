// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-configuring-the-operators_{context}"]
= Operators

{sno-caps} clusters that run DU workloads require the following Operators to be installed:

* Local Storage Operator
* Logging Operator
* PTP Operator
* SR-IOV Network Operator

You also need to configure a custom `CatalogSource` CR, disable the default `OperatorHub` configuration, and configure an `ImageContentSourcePolicy` mirror registry that is accessible from the clusters that you install.

.Recommended Storage Operator namespace and Operator group configuration (`StorageNS.yaml`, `StorageOperGroup.yaml`)
[source,yaml]
----
---
include::snippets/ztp_StorageNS.yaml[]
---
include::snippets/ztp_StorageOperGroup.yaml[]
----

.Recommended Cluster Logging Operator namespace and Operator group configuration (`ClusterLogNS.yaml`, `ClusterLogOperGroup.yaml`)
[source,yaml]
----
include::snippets/ztp_ClusterLogNS.yaml[]
include::snippets/ztp_ClusterLogOperGroup.yaml[]
----

.Recommended PTP Operator namespace and Operator group configuration (`PtpSubscriptionNS.yaml`, `PtpSubscriptionOperGroup.yaml`)
[source,yaml]
----
include::snippets/ztp_PtpSubscriptionNS.yaml[]
---
include::snippets/ztp_PtpSubscriptionOperGroup.yaml[]
----

.Recommended SR-IOV Operator namespace and Operator group configuration (`SriovSubscriptionNS.yaml`, `SriovSubscriptionOperGroup.yaml`)
[source,yaml]
----
---
include::snippets/ztp_SriovSubscriptionNS.yaml[]
---
include::snippets/ztp_SriovSubscriptionOperGroup.yaml[]
----

.Recommended `CatalogSource` configuration (`DefaultCatsrc.yaml`)
[source,yaml]
----
include::snippets/ztp_DefaultCatsrc.yaml[]
----

.Recommended `ImageContentSourcePolicy` configuration (`DisconnectedICSP.yaml`)
[source,yaml]
----
include::snippets/ztp_DisconnectedICSP.yaml[]
----

.Recommended `OperatorHub` configuration (`OperatorHub.yaml`)
[source,yaml]
----
include::snippets/ztp_OperatorHub.yaml[]
----
