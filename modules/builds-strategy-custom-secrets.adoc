// Module included in the following assemblies:
//
//* builds/build-strategies.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-strategy-custom-secrets_{context}"]
= Using secrets in custom builds

In addition to secrets for source and images that can be added to all build types, custom strategies allow adding an arbitrary list of secrets to the builder pod.

.Procedure

* To mount each secret at a specific location, edit the `secretSource` and `mountPath` fields of the `strategy` YAML file:
+
[source,yaml]
----
strategy:
  customStrategy:
    secrets:
      - secretSource: <1>
          name: "secret1"
        mountPath: "/tmp/secret1" <2>
      - secretSource:
          name: "secret2"
        mountPath: "/tmp/secret2"
----
<1> `secretSource` is a reference to a secret in the same namespace as the build.
<2> `mountPath` is the path inside the custom builder where the secret should be mounted.
