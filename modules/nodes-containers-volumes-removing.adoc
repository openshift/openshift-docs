// Module included in the following assemblies:
//
// * nodes/nodes-containers-volumes.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-containers-volumes-removing_{context}"]
= Removing volumes and volume mounts from a pod

You can remove a volume or volume mount from a pod.

.Procedure

To remove a volume from pod templates:

[source,terminal]
----
$ oc set volume <object_type>/<name> --remove [options]
----

.Supported options for removing volumes
[cols="3a*",options="header"]
|===

|Option |Description |Default

|`--name`
|Name of the volume.
|

|`-c, --containers`
|Select containers by name. It can also take wildcard `'*'` that matches any character.
|`'*'`

|`--confirm`
|Indicate that you want to remove multiple volumes at once.
|

|`-o, --output`
|Display the modified objects instead of updating them on the server. Supported values: `json`, `yaml`.
|

|`--output-version`
|Output the modified objects with the given version.
|`api-version`
|===

For example:

* To remove a volume *v1* from the `DeploymentConfig` object *d1*:
+
[source,terminal]
----
$ oc set volume dc/d1 --remove --name=v1
----

* To unmount volume *v1* from container *c1* for the `DeploymentConfig` object *d1* and remove the volume *v1* if it is not referenced by any containers on *d1*:
+
[source,terminal]
----
$ oc set volume dc/d1 --remove --name=v1 --containers=c1
----

* To remove all volumes for replication controller *r1*:
+
[source,terminal]
----
$ oc set volume rc/r1 --remove --confirm
----
