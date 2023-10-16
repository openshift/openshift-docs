// Module included in the following assemblies:
//
// * cli_reference/opm/cli-opm-ref.adoc

[id="opm-cli-ref-init_{context}"]
= init

Generate an `olm.package` declarative config blob.

.Command syntax
[source,terminal]
----
$ opm init <package_name> [<flags>]
----

.`init` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-c`, `--default-channel` (string)
|The channel that subscriptions will default to if unspecified.

|`-d`, `--description` (string)
|Path to the Operator's `README.md` or other documentation.

|`-i`, `--icon` (string)
|Path to package's icon.

|`-o`, `--output` (string)
|Output format: `json` (the default value) or `yaml`.

|===
