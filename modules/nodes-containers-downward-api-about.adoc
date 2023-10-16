// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-projected-volumes-about_{context}"]
= Expose pod information to Containers using the Downward API

The Downward API contains such information as the pod's name, project, and resource values. Containers can consume
information from the downward API using environment variables or a volume
plugin.

Fields within the pod are selected using the `FieldRef` API type. `FieldRef`
has two fields:

[options="header"]
|===
|Field |Description

|`fieldPath`
|The path of the field to select, relative to the pod.

|`apiVersion`
|The API version to interpret the `fieldPath` selector within.
|===

Currently, the valid selectors in the v1 API include:

[options="header"]
|===
|Selector |Description

|`metadata.name`
|The pod's name. This is supported in both environment variables and volumes.

|`metadata.namespace`
|The pod's namespace.This is supported in both environment variables and volumes.

|`metadata.labels`
|The pod's labels. This is only supported in volumes and not in environment variables.

|`metadata.annotations`
|The pod's annotations. This is only supported in volumes and not in environment variables.

|`status.podIP`
|The pod's IP. This is only supported in environment variables and not volumes.
|===

The `apiVersion` field, if not specified, defaults to the API version of the
enclosing pod template.
