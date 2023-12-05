// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-manually-add-source-clone-secrets_{context}"]
= Manually adding a source clone secret

Source clone secrets can be added manually to a build configuration by adding a `sourceSecret` field to the `source` section inside the `BuildConfig` and setting it to the name of the secret that you created. In this example, it is the `basicsecret`.

[source,yaml]
----
apiVersion: "build.openshift.io/v1"
kind: "BuildConfig"
metadata:
  name: "sample-build"
spec:
  output:
    to:
      kind: "ImageStreamTag"
      name: "sample-image:latest"
  source:
    git:
      uri: "https://github.com/user/app.git"
    sourceSecret:
      name: "basicsecret"
  strategy:
    sourceStrategy:
      from:
        kind: "ImageStreamTag"
        name: "python-33-centos7:latest"
----

.Procedure

You can also use the `oc set build-secret` command to set the source clone secret on an existing build configuration.

* To set the source clone secret on an existing build configuration, enter the following command:
+
[source,terminal]
----
$ oc set build-secret --source bc/sample-build basicsecret
----
