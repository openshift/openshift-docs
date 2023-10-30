:_mod-docs-content-type: PROCEDURE
[id="odc-editing-application-configuration-using-developer-perspective_{context}"]
= Editing the application configuration using the Developer perspective

You can use the *Topology* view in the *Developer* perspective to edit the configuration of your application.

[NOTE]
====
Currently, only configurations of applications created by using the *From Git*, *Container Image*, *From Catalog*, or *From Dockerfile* options in the *Add* workflow of the *Developer* perspective can be edited. Configurations of applications created by using the CLI or the *YAML* option from the *Add* workflow cannot be edited.
====

.Prerequisites
Ensure that you have created an application using  the *From Git*, *Container Image*, *From Catalog*, or *From Dockerfile* options in the *Add* workflow.

.Procedure

. After you have created an application and it is displayed in the *Topology* view, right-click the application to see the edit options available.
+
.Edit application
image::odc_edit_app.png[]
+
. Click *Edit _application-name_* to see the *Add* workflow you used to create the application. The form is pre-populated with the values you had added while creating the application.
. Edit the necessary values for the application.
+
[NOTE]
====
You cannot edit the *Name* field in the *General* section, the CI/CD pipelines, or the *Create a route to the application* field in the *Advanced Options* section.
====
+
. Click *Save* to restart the build and deploy a new image.
+
.Edit and redeploy application
image::odc_edit_redeploy.png[]
