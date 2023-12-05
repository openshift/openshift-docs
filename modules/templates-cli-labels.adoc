// Module included in the following assemblies:
//
//  * openshift_images/using-templates.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-cli-labels_{context}"]
= Adding labels

Labels are used to manage and organize generated objects, such as pods. The labels specified in the template are applied to every object that is generated from the template.

.Procedure

* Add labels in the template from the command line:
+
[source,terminal]
----
$ oc process -f <filename> -l name=otherLabel
----
