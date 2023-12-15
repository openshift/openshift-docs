// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vol-detach-non-graceful-shutdown.adoc
//

:_mod-docs-content-type: CONCEPT
[id="persistent-storage-csi-vol-detach-non-graceful-overview_{context}"]
= Overview

A graceful node shutdown occurs when the kubelet's node shutdown manager detects the upcoming node shutdown action. Non-graceful shutdowns occur when the kubelet does not detect a node shutdown action, which can occur because of system or hardware failures. Also, the kubelet may not detect a node shutdown action when the shutdown command does not trigger the Inhibitor Locks mechanism used by the kubelet on Linux, or because of a user error, for example, if the shutdownGracePeriod and shutdownGracePeriodCriticalPods details are not configured correctly for that node.

With this feature, when a non-graceful node shutdown occurs, you can manually add an `out-of-service` taint on the node to allow volumes to automatically detach from the node.