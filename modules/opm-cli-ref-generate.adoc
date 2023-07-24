// Module included in the following assemblies:
//
// * cli_reference/opm/cli-opm-ref.adoc

[id="opm-cli-ref-generate_{Context}"]
= generate

Generate various artifacts for declarative config indexes.

.Command syntax
[source,terminal]
----
$ opm generate <subcommand> [<flags>]
----

.`generate` subcommands
[options="header",cols="1,3"]
|===
|Subcommand |Description

|`dockerfile`
|Generate a Dockerfile for a declarative config index.
|===

.`generate` flags
[options="header",cols="1,3"]
|===
|Flags |Description

|`-h`, `--help`
|Help for generate.

|===


[id="opm-cli-ref-generate-dockerfile_{context}"]
== dockerfile

Generate a Dockerfile for a declarative config index.

[IMPORTANT]
====
This command creates a Dockerfile in the same directory as the `<dcRootDir>` (named `<dcDirName>.Dockerfile`) that is used to build the index. If a Dockerfile with the same name already exists, this command fails.

When specifying extra labels, if duplicate keys exist, only the last value of each duplicate key gets added to the generated Dockerfile.
====

.Command syntax
[source,terminal]
----
$ opm generate dockerfile <dcRootDir> [<flags>]
----

.`generate dockerfile` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-i,` `--binary-image` (string)
|Image in which to build catalog. The default value is `quay.io/operator-framework/opm:latest`.

|`-l`, `--extra-labels` (string)
|Extra labels to include in the generated Dockerfile. Labels have the form `key=value`.

|`-h`, `--help`
|Help for Dockerfile.

|===

ifndef::openshift-origin[]
[NOTE]
====
To build with the official Red Hat image, use the `registry.redhat.io/openshift4/ose-operator-registry:v{product-version}` value with the `-i` flag.
====
endif::[]