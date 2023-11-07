// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-creating-from-console_{context}"]
= Creating an application by using the web console 

You can use the web console to create an application from a template.

.Procedure

. Select *Developer* from the context selector at the top of the web console
navigation menu.

. While in the desired project, click *+Add*

. Click *All services* in the *Developer Catalog* tile.

. Click *Builder Images* under *Type* to see the available builder images.
+
[NOTE]
====
Only image stream tags that have the `builder` tag listed in their annotations
appear in this list, as demonstrated here:
====
+
[source,yaml]
----
kind: "ImageStream"
apiVersion: "v1"
metadata:
  name: "ruby"
  creationTimestamp: null
spec:
# ...
  tags:
    - name: "2.6"
      annotations:
        description: "Build and run Ruby 2.6 applications"
        iconClass: "icon-ruby"
        tags: "builder,ruby" <1>
        supports: "ruby:2.6,ruby"
        version: "2.6"
# ...
----
<1> Including `builder` here ensures this image stream tag appears in the
web console as a builder.

. Modify the settings in the new application screen to configure the objects
to support your application.
