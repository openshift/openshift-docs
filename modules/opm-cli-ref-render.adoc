// Module included in the following assemblies:
//
// * cli_reference/opm/cli-opm-ref.adoc

[id="opm-cli-ref-render_{context}"]
= render

Generate a declarative config blob from the provided index images, bundle images, and SQLite database files.

.Command syntax
[source,terminal]
----
$ opm render <index_image | bundle_image | sqlite_file> [<flags>]
----

.`render` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-o`, `--output` (string)
|Output format: `json` (the default value) or `yaml`.

|===
