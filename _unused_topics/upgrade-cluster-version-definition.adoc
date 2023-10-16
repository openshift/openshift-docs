// Module included in the following assemblies:
//
// * none

[id="upgrade-cluster-version-definition_{context}"]
= ClusterVersion definition

You can review the `ClusterVersion` definition to see the update history
for your cluster. You can also apply overrides to this definition if your
cluster is not for production or during debugging.

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: ClusterVersion
metadata:
  creationTimestamp: 2019-03-22T14:26:41Z
  generation: 1
  name: version
  resourceVersion: "16740"
  selfLink: /apis/config.openshift.io/v1/clusterversions/version
  uid: 82f9f2c4-4cae-11e9-90b7-06dc0f62ad38
spec:
  channel: stable-4.3 <1>
  overrides: "" <2>
  clusterID: 0b1cf91f-c3fb-4f9e-aa02-e0d70c71f6e6
  status: <3>
    availableUpdates: null <4>
    conditions: <5>
    - lastTransitionTime: 2019-05-22T07:13:26Z
      status: "True"
      type: RetrievedUpdates
    - lastTransitionTime: 2019-05-22T07:13:26Z
      message: Done applying 4.0.0-0.alpha-2019-03-22-124110
      status: "True"
      type: Available
    - lastTransitionTime: 2019-05-22T07:12:26Z
      status: "False"
      type: Failing
    - lastTransitionTime: 2019-05-22T07:13:26Z
      message: Cluster version is 4.0.0-0.alpha-2019-03-22-124110
      status: "False"
      type: Progressing
----
<1> Specify the channel to use to apply non-standard updates to the
cluster. If you do not change the value, the CVO uses the default channel.
+
[IMPORTANT]
====
The default channel contains stable updates. Do not modify the
`ClusterVersionSpec.channel` value on production clusters. If you update your
cluster from a different channel without explicit direction from Red Hat
support, your cluster is no longer supported.
====
<2>  A list of overrides for components that the CVO manages. Mark
components as `unmanaged` to prevent the CVO from creating or updating the object.
+
[IMPORTANT]
====
Set the `ClusterVersionSpec.overrides` parameter value only during cluster
debugging. Setting this value can prevent successful upgrades and is not
supported for production clusters.
====
<3> The status of available updates and any in-progress updates. These values display
the version that the cluster is reconciling to, and the conditions
array reports whether the update succeeded, is in progress, or is failing.
All of the `ClusterVersionStatus` values are set by the cluster itself, and you
cannot modify them.
<4> The list of appropriate updates for the cluster. This list is empty if no
updates are recommended, the update service is unavailable, or you specified
an invalid channel.
<5> The condition of the CVO. This section contains both the reason that the
cluster entered its current condition and a message that provides more
information about the condition.

* `Available` means that the upgrade to the `desiredUpdate` value completed.
* `Progressing` means that an upgrade is in progress.
* `Failing` means that an update is blocked by a temporary or permanent error.
