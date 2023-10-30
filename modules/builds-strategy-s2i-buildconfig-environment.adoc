// Module included in the following assemblies:
//* * builds/build-strategies.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-strategy-s2i-buildconfig-environment_{context}"]
= Using source-to-image build configuration environment

You can add environment variables to the `sourceStrategy` definition of the build configuration. The environment variables defined there are visible during the `assemble` script execution and will be defined in the output image, making them also available to the `run` script and application code.

.Procedure

* For example, to disable assets compilation for your Rails application:
+
[source,yaml]
----
sourceStrategy:
...
  env:
    - name: "DISABLE_ASSET_COMPILATION"
      value: "true"
----

[role="_additional-resources"]
.Additional resources

* The build environment section provides more advanced instructions.
* You can also manage environment variables defined in the build configuration with the `oc set env` command.
