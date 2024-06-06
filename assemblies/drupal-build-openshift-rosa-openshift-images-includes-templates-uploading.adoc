// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-uploading_{context}"]
= Uploading a template

If you have a JSON or YAML file that defines a template, you can upload the template to projects using the CLI. This saves the template to the project for repeated use by any user with appropriate access to that project. Instructions about writing your own templates are provided later in this topic.

.Procedure

* Upload a template using one of the following methods:

** Upload a template to your current project's template library, pass the JSON or YAML file with the following command:
+
[source,terminal]
----
$ oc create -f <filename>
----

** Upload a template to a different project using the `-n` option with the name of the project:
+
[source,terminal]
----
$ oc create -f <filename> -n <project>
----

The template is now available for selection using the web console or the CLI.
