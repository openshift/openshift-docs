// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-ref.adoc
// * operators/operator_sdk/osdk-cli-ref.adoc

[id="osdk-cli-ref-bundle_{context}"]
= bundle

The `operator-sdk bundle` command manages Operator bundle metadata.

[id="osdk-cli-ref-bundle-validate_{context}"]
== validate

The `bundle validate` subcommand validates an Operator bundle.

.`bundle validate` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-h`, `--help`
|Help output for the `bundle validate` subcommand.

|`--index-builder` (string)
|Tool to pull and unpack bundle images. Only used when validating a bundle image. Available options are `docker`, which is the default, `podman`, or `none`.

|`--list-optional`
|List all optional validators available. When set, no validators are run.

|`--select-optional` (string)
|Label selector to select optional validators to run. When run with the `--list-optional` flag, lists available optional validators.

|===
