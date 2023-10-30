// Module included in the following assemblies:
//
// * builds/advanced-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-assigning-builds-to-nodes_{context}"]
= Assigning builds to specific nodes

Builds can be targeted to run on specific nodes by specifying labels in the `nodeSelector` field of a build configuration. The `nodeSelector` value is a set of key-value pairs that are matched to `Node` labels when scheduling the build pod.

The `nodeSelector` value can also be controlled by cluster-wide default and override values. Defaults will only be applied if the build configuration does not define any key-value pairs for the `nodeSelector` and also does not define an explicitly empty map value of `nodeSelector:{}`. Override values will replace values in the build configuration on a key by key basis.

//See Configuring Global Build Defaults and Overrides for more information.

[NOTE]
====
If the specified `NodeSelector` cannot be matched to a node with those labels, the build still stay in the `Pending` state indefinitely.
====

.Procedure

* Assign builds to run on specific nodes by assigning labels in the `nodeSelector` field of the `BuildConfig`, for example:
+
[source,yaml]
----
apiVersion: "v1"
kind: "BuildConfig"
metadata:
  name: "sample-build"
spec:
  nodeSelector:<1>
    key1: value1
    key2: value2
----
<1> Builds associated with this build configuration will run only on nodes with the `key1=value2` and `key2=value2` labels.
