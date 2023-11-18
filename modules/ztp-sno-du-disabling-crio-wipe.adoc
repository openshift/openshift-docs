// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-sno-du-disabling-crio-wipe_{context}"]
= Disable automatic CRI-O cache wipe

After an uncontrolled host shutdown or cluster reboot, CRI-O automatically deletes the entire CRI-O cache, causing all images to be pulled from the registry when the node reboots.
This can result in unacceptably slow recovery times or recovery failures.
To prevent this from happening in {sno} clusters that you install with {ztp}, disable the CRI-O delete cache feature during cluster installation.

.Recommended `MachineConfig` CR to disable CRI-O cache wipe on control plane nodes (`99-crio-disable-wipe-master.yaml`)
[source,yaml]
----
include::snippets/ztp_99-crio-disable-wipe-master.yaml[]
----

.Recommended `MachineConfig` CR to disable CRI-O cache wipe on worker nodes (`99-crio-disable-wipe-worker.yaml`)
[source,yaml]
----
include::snippets/ztp_99-crio-disable-wipe-worker.yaml[]
----
