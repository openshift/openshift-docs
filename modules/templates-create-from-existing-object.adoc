// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-create-from-existing-object_{context}"]
= Creating a template from existing objects

Rather than writing an entire template from scratch, you can export existing objects from your project in YAML form, and then modify the YAML from there by adding parameters and other customizations as template form.

.Procedure

* Export objects in a project in YAML form:
+
[source,terminal]
----
$ oc get -o yaml all > <yaml_filename>
----
+
You can also substitute a particular resource type or multiple resources instead of `all`. Run `oc get -h` for more examples.
+
The object types included in `oc get -o yaml all` are:
+
** `BuildConfig`
** `Build`
** `DeploymentConfig`
** `ImageStream`
** `Pod`
** `ReplicationController`
** `Route`
** `Service`

[NOTE]
====
Using the `all` alias is not recommended because the contents might vary across different clusters and versions. Instead, specify all required resources.
====
