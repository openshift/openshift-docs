// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-using-build-fields-as-environment-variables_{context}"]
= Using build fields as environment variables

You can inject information about the build object by setting the `fieldPath` environment variable source to the `JsonPath` of the field from which you are interested in obtaining the value.

[NOTE]
====
Jenkins Pipeline strategy does not support `valueFrom` syntax for environment variables.
====

.Procedure

* Set the `fieldPath` environment variable source to the `JsonPath` of the field from which you are interested in obtaining the value:
+
[source,yaml]
----
env:
  - name: FIELDREF_ENV
    valueFrom:
      fieldRef:
        fieldPath: metadata.name
----
