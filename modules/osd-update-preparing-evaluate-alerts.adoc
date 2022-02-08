// Module included in the following assemblies:
//
// * upgrading/rosa-updating-cluster-prepare.adoc
// * upgrading/osd-updating-cluster-prepare.adoc

[id="update-preparing-evaluate-alerts_{context}"]
= Reviewing alerts to identify uses of removed APIs

The `APIRemovedInNextReleaseInUse` alert tells you that there are removed APIs in use on your cluster. If this alert is firing in your cluster, review the alert; take action to clear the alert by migrating manifests and API clients to use the new API version. You can use the `APIRequestCount` API to get more information about which APIs are in use and which workloads are using removed APIs.
