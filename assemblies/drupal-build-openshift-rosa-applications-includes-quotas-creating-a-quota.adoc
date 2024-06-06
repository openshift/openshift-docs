// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

:_mod-docs-content-type: PROCEDURE
[id="quotas-creating-a-quota_{context}"]
= Creating a quota

You can create a quota to constrain resource usage in a given project.

.Procedure

. Define the quota in a file.

. Use the file to create the quota and apply it to a project:
+
[source,terminal]
----
$ oc create -f <file> [-n <project_name>]
----
+
For example:
+
[source,terminal]
----
$ oc create -f core-object-counts.yaml -n demoproject
----
