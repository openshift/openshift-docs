// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

:_mod-docs-content-type: PROCEDURE
[id="viewing-a-project-using-the-CLI_{context}"]
= Viewing a project using the CLI

When viewing projects, you are restricted to seeing only the projects you have
access to view based on the authorization policy.

.Procedure

. To view a list of projects, run:
+
[source,terminal]
----
$ oc get projects
----

. You can change from the current project to a different project for CLI
operations. The specified project is then used in all subsequent operations that
manipulate project-scoped content:
+
[source,terminal]
----
$ oc project <project_name>
----
