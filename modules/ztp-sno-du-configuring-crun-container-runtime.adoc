// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-configuring-crun-container-runtime_{context}"]
= Configuring crun as the default container runtime

The following `ContainerRuntimeConfig` custom resources (CRs) configure crun as the default OCI container runtime for control plane and worker nodes.
The crun container runtime is fast and lightweight and has a low memory footprint.

[IMPORTANT]
====
For optimal performance, enable crun for control plane and worker nodes in {sno}, {3no}, and standard clusters.
To avoid the cluster rebooting when the CR is applied, apply the change as a {ztp} additional Day 0 install-time manifest.
====

.Recommended `ContainerRuntimeConfig` CR for control plane nodes (`enable-crun-master.yaml`)
[source,yaml]
----
include::snippets/ztp_enable-crun-master.yaml[]
----

.Recommended `ContainerRuntimeConfig` CR for worker nodes (`enable-crun-worker.yaml`)
[source,yaml]
----
include::snippets/ztp_enable-crun-worker.yaml[]
----
