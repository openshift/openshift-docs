// Module included in the following assemblies:
//
// * nodes/nodes-containers-volumes.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-containers-volumes-listing_{context}"]
= Listing volumes and volume mounts in a pod

You can list volumes and volume mounts in pods or pod templates:

.Procedure

To list volumes:

[source,terminal]
----
$ oc set volume <object_type>/<name> [options]
----

List volume supported options:
[cols="3a*",options="header"]
|===

|Option |Description |Default

|`--name`
|Name of the volume.
|

|`-c, --containers`
|Select containers by name. It can also take wildcard `'*'` that matches any
character.
|`'*'`
|===

For example:

* To list all volumes for pod *p1*:
+
[source,terminal]
----
$ oc set volume pod/p1
----

* To list volume *v1* defined on all deployment configs:
+
[source,terminal]
----
$ oc set volume dc --all --name=v1
----
