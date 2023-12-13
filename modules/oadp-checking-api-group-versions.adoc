// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/advanced-topics.adoc


:_mod-docs-content-type: PROCEDURE
[id="oadp-checking-api-group-versions_{context}"]
= Listing the Kubernetes API group versions on a cluster

A source cluster might offer multiple versions of an API, where one of these versions is the preferred API version. For example, a source cluster with an API named `Example` might be available in the `example.com/v1` and `example.com/v1beta2` API groups.

If you use Velero to back up and restore such a source cluster, Velero backs up only the version of that resource that uses the preferred version of its Kubernetes API.

To return to the above example, if `example.com/v1` is the preferred API, then Velero only backs up the version of a resource that uses `example.com/v1`. Moreover, the target cluster needs to have `example.com/v1` registered in its set of available API resources in order for Velero to restore the resource on the target cluster.

Therefore, you need to generate a list of the Kubernetes API group versions on your target cluster to be sure the preferred API version is registered in its set of available API resources.

.Procedure

* Enter the following command:

[source,terminal]
----
$ oc api-resources
----
