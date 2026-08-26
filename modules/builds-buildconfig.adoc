// Module included in the following assemblies:
// * builds/understanding-builds.adoc

:_mod-docs-content-type: REFERENCE
[id="builds-buildconfig_{context}"]
= BuildConfigs

A build configuration describes a single build definition and a set of triggers for when a new build is created. Build configurations are defined by a `BuildConfig`, which is a REST object that can be used in a POST to the API server to create a new instance.

A build configuration, or `BuildConfig`, is characterized by a build strategy
and one or more sources. The strategy determines the process, while the sources provide its input.

Depending on how you choose to create your application using {product-title}, a `BuildConfig` is typically generated automatically for you if you use the web console or CLI, and it can be edited at any time. Understanding the parts that make up a `BuildConfig` and their available options can help if you choose to manually change your configuration later.

The following example `BuildConfig` results in a new build every time a container image tag or the source code changes:

.`BuildConfig` object definition
[source,yaml]
----
kind: BuildConfig
apiVersion: build.openshift.io/v1
metadata:
  name: "ruby-sample-build" <1>
spec:
  runPolicy: "Serial" <2>
  triggers: <3>
    -
      type: "GitHub"
      github:
        secret: "secret101"
    - type: "Generic"
      generic:
        secret: "secret101"
    -
      type: "ImageChange"
  source: <4>
    git:
      uri: "https://github.com/openshift/ruby-hello-world"
  strategy: <5>
    sourceStrategy:
      from:
        kind: "ImageStreamTag"
        name: "ruby-20-centos7:latest"
  output: <6>
    to:
      kind: "ImageStreamTag"
      name: "origin-ruby-sample:latest"
  postCommit: <7>
      script: "bundle exec rake test"
----
<1> This specification creates a new `BuildConfig` named `ruby-sample-build`.
<2> The `runPolicy` field controls whether builds created from this build configuration can be run simultaneously. The default value is `Serial`, which means new builds run sequentially, not simultaneously.
<3> You can specify a list of triggers, which cause a new build to be created.
<4> The `source` section defines the source of the build. The source type determines the primary source of input, and can be either `Git`, to point to a code repository location,
ifndef::openshift-online[]
`Dockerfile`, to build from an inline Dockerfile,
endif::[]
or `Binary`, to accept binary payloads. It is possible to have multiple sources at once. For more information about each source type, see "Creating build inputs".
<5> The `strategy` section describes the build strategy used to execute the build. You can specify a `Source`
ifndef::openshift-online[]
, `Docker`, or `Custom`
endif::[]
strategy here. This example uses the `ruby-20-centos7` container image that Source-to-image (S2I) uses for the application build.
<6> After the container image is successfully built, it is pushed into the repository described in the `output` section.
<7> The `postCommit` section defines an optional build hook.
