// Module included in the following assemblies:
// * builds/build-strategies.adoc

[id="builds-strategy-s2i-force-pull-example_{context}"]
= Source-to-Image (S2I) force pull flag example

Set the following to use the `forcePull` flag with S2I:

[source,yaml]
----
strategy:
  sourceStrategy:
    from:
      kind: "ImageStreamTag"
      name: "builder-image:latest" <1>
    forcePull: true <2>
----
<1> The builder image being used, where the local version on the node may not be up to date with the version in the registry to which the imagestream points.
<2> This flag causes the local builder image to be ignored and a fresh version to be pulled from the registry to which the imagestream points. Setting `forcePull` to `false` results in the default behavior of honoring the image stored locally.
