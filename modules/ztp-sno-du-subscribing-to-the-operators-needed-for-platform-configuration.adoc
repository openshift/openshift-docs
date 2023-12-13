// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-subscribing-to-the-operators-needed-for-platform-configuration_{context}"]
= Operator subscriptions

{sno-caps} clusters that run DU workloads require the following `Subscription` CRs. The subscription provides the location to download the following Operators:

* Local Storage Operator
* Logging Operator
* PTP Operator
* SR-IOV Network Operator
* SRIOV-FEC Operator

For each Operator subscription, specify the channel to get the Operator from. The recommended channel is `stable`.

You can specify `Manual` or `Automatic` updates.
In `Automatic` mode, the Operator automatically updates to the latest versions in the channel as they become available in the registry.
In `Manual` mode, new Operator versions are installed only when they are explicitly approved.

[TIP]
====
Use `Manual` mode for subscriptions. This allows you to control the timing of Operator updates to fit within scheduled maintenance windows.
====

.Recommended Local Storage Operator subscription (`StorageSubscription.yaml`)
[source,yaml]
----
include::snippets/ztp_StorageSubscription.yaml[]
----

.Recommended SR-IOV Operator subscription (`SriovSubscription.yaml`)
[source,yaml]
----
include::snippets/ztp_SriovSubscription.yaml[]
----

.Recommended PTP Operator subscription (`PtpSubscription.yaml`)
[source,yaml]
----
include::snippets/ztp_PtpSubscription.yaml[]
----

.Recommended Cluster Logging Operator subscription (`ClusterLogSubscription.yaml`)
[source,yaml]
----
include::snippets/ztp_ClusterLogSubscription.yaml[]
----
