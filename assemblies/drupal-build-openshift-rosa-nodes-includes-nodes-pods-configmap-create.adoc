// Module included in the following assemblies:
//
//* authentication/configmaps.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-configmap-create_{context}"]
= Creating a config map by using the CLI

You can use the following command to create a config map from directories, specific files, or literal values.

.Procedure

* Create a config map:
+
[source,terminal]
----
$ oc create configmap <configmap_name> [options]
----
