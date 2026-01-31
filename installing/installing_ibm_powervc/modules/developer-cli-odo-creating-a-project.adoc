// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating_and_deploying_applications_with_odo/creating-a-single-component-application-with-odo.adoc
// * cli_reference/developer_cli_odo/creating_and_deploying_applications_with_odo/creating-a-multicomponent-application-with-odo.adoc
// * cli_reference/developer_cli_odo/creating_and_deploying_applications_with_odo/creating-an-application-with-a-database.adoc
// * cli_reference/developer_cli_odo/creating_and_deploying_applications_with_odo/working-with-projects

:_mod-docs-content-type: PROCEDURE
[id="creating-a-project_{context}"]
= Creating a project

Create a project to keep your source code, tests, and libraries organized in a separate single unit.

.Procedure

. Log in to an {product-title} cluster:
+
[source,terminal]
----
$ odo login -u developer -p developer
----

. Create a project:
+
[source,terminal]
----
$ odo project create myproject
----
+
.Example output
[source,terminal]
----
 ✓  Project 'myproject' is ready for use
 ✓  New project created and now using project : myproject
----
