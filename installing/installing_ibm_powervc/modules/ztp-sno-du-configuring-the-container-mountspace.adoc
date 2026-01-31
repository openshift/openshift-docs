// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-configuring-the-container-mountspace_{context}"]
= Reduced platform management footprint

To reduce the overall management footprint of the platform, a `MachineConfig` custom resource (CR) is required that places all Kubernetes-specific mount points in a new namespace separate from the host operating system.
The following base64-encoded example `MachineConfig` CR illustrates this configuration.

.Recommended container mount namespace configuration (`01-container-mount-ns-and-kubelet-conf-master.yaml`)
[source,yaml]
----
include::snippets/ztp_01-container-mount-ns-and-kubelet-conf-master.yaml[]
----
