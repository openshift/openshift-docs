// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-bundle-validate.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-about-bundle-validate_{context}"]
= About the bundle validate command

While the Operator SDK `scorecard` command can run tests on your Operator based on a configuration file and test images, the `bundle validate` subcommand can validate local bundle directories and remote bundle images for content and structure.

.`bundle validate` command syntax
[source,terminal]
----
$ operator-sdk bundle validate <bundle_dir_or_image> <flags>
----

[NOTE]
====
The `bundle validate` command runs automatically when you build your bundle using the `make bundle` command.
====

Bundle images are pulled from a remote registry and built locally before they are validated. Local bundle directories must contain Operator metadata and manifests. The bundle metadata and manifests must have a structure similar to the following bundle layout:

.Example bundle layout
[source,terminal]
----
./bundle
  ├── manifests
  │   ├── cache.my.domain_memcacheds.yaml
  │   └── memcached-operator.clusterserviceversion.yaml
  └── metadata
      └── annotations.yaml
----

Bundle tests pass validation and finish with an exit code of `0` if no errors are detected.

.Example output
[source,terminal]
----
INFO[0000] All validation tests have completed successfully
----

Tests fail validation and finish with an exit code of `1` if errors are detected.

.Example output
[source,terminal]
----
ERRO[0000] Error: Value cache.example.com/v1alpha1, Kind=Memcached: CRD "cache.example.com/v1alpha1, Kind=Memcached" is present in bundle "" but not defined in CSV
----

Bundle tests that result in warnings can still pass validation with an exit code of `0` as long as no errors are detected. Tests only fail on errors.

.Example output
[source,terminal]
----
WARN[0000] Warning: Value : (memcached-operator.v0.0.1) annotations not found
INFO[0000] All validation tests have completed successfully
----

For further information about the `bundle validate` subcommand, run:

[source,terminal]
----
$ operator-sdk bundle validate -h
----
