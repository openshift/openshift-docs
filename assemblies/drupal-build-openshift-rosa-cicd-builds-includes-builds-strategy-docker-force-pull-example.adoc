// Module included in the following assemblies:
// * builds/build-strategies.adoc

[id="builds-strategy-docker-force-pull-example_{context}"]
= Docker force pull flag example

Set the following to use the `forcePull` flag with Docker:

[source,yaml]
----
strategy:
  dockerStrategy:
    forcePull: true <1>
----
<1> This flag causes the local builder image to be ignored, and a fresh version to be pulled from the registry to which the imagestream points. Setting `forcePull` to `false` results in the default behavior of honoring the image stored locally.
