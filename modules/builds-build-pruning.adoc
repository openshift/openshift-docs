// Module included in the following assemblies:
//
// * builds/advanced-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-build-pruning_{context}"]
= Pruning builds

By default, builds that have completed their lifecycle are persisted indefinitely. You can limit the number of previous builds that are retained.

.Procedure

. Limit the number of previous builds that are retained by supplying a positive integer value for `successfulBuildsHistoryLimit` or `failedBuildsHistoryLimit` in your `BuildConfig`, for example:
+
[source,yaml]
----
apiVersion: "v1"
kind: "BuildConfig"
metadata:
  name: "sample-build"
spec:
  successfulBuildsHistoryLimit: 2 <1>
  failedBuildsHistoryLimit: 2 <2>
----
<1> `successfulBuildsHistoryLimit` will retain up to two builds with a status of `completed`.
<2> `failedBuildsHistoryLimit` will retain up to two builds with a status of `failed`, `canceled`, or `error`.

. Trigger build pruning by one of the following actions:
+
* Updating a build configuration.
* Waiting for a build to complete its lifecycle.

Builds are sorted by their creation timestamp with the oldest builds being pruned first.

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
[NOTE]
====
Administrators can manually prune builds using the 'oc adm' object pruning command.
====
endif::[]
