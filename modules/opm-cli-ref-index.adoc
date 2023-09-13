// Module included in the following assemblies:
//
// * cli_reference/opm/cli-opm-ref.adoc

[id="opm-cli-ref-index_{context}"]
= index

Generate Operator index for SQLite database format container images from pre-existing Operator bundles.

[IMPORTANT]
====
As of {product-title} 4.11, the default Red Hat-provided Operator catalog releases in the file-based catalog format. The default Red Hat-provided Operator catalogs for {product-title} 4.6 through 4.10 released in the deprecated SQLite database format.

The `opm` subcommands, flags, and functionality related to the SQLite database format are also deprecated and will be removed in a future release. The features are still supported and must be used for catalogs that use the deprecated SQLite database format.

Many of the `opm` subcommands and flags for working with the SQLite database format, such as `opm index prune`, do not work with the file-based catalog format. 

ifndef::openshift-rosa,openshift-dedicated[]
For more information about working with file-based catalogs, see "Additional resources".
endif::openshift-rosa,openshift-dedicated[]
====

.Command syntax
[source,terminal]
----
$ opm index <subcommand> [<flags>]
----

.`index` subcommands
[options="header",cols="1,3"]
|===
|Subcommand |Description

|`add`
|Add Operator bundles to an index.

|`prune`
|Prune an index of all but specified packages.

|`prune-stranded`
|Prune an index of stranded bundles, which are bundles that are not associated with a particular image.

|`rm`
|Delete an entire Operator from an index.

|===

[id="opm-cli-ref-index-add_{context}"]
== add

Add Operator bundles to an index.

.Command syntax
[source,terminal]
----
$ opm index add [<flags>]
----

.`index add` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-i`, `--binary-image`
|Container image for on-image `opm` command

|`-u`, `--build-tool` (string)
|Tool to build container images: `podman` (the default value) or `docker`. Overrides part of the `--container-tool` flag.

|`-b`, `--bundles` (strings)
|Comma-separated list of bundles to add.

|`-c`, `--container-tool` (string)
|Tool to interact with container images, such as for saving and building: `docker` or `podman`.

|`-f`, `--from-index` (string)
|Previous index to add to.

|`--generate`
|If enabled, only creates the Dockerfile and saves it to local disk.

|`--mode` (string)
|Graph update mode that defines how channel graphs are updated: `replaces` (the default value), `semver`, or `semver-skippatch`.

|`-d`, `--out-dockerfile` (string)
|Optional: If generating the Dockerfile, specify a file name.

|`--permissive`
|Allow registry load errors.

|`-p`, `--pull-tool` (string)
|Tool to pull container images: `none` (the default value), `docker`, or `podman`. Overrides part of the `--container-tool` flag.

|`-t`, `--tag` (string)
|Custom tag for container image being built.

|===

[id="opm-cli-ref-index-prune_{context}"]
== prune

Prune an index of all but specified packages.

.Command syntax
[source,terminal]
----
$ opm index prune [<flags>]
----

.`index prune` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-i`, `--binary-image`
|Container image for on-image `opm` command

|`-c`, `--container-tool` (string)
|Tool to interact with container images, such as for saving and building: `docker` or `podman`.

|`-f`, `--from-index` (string)
|Index to prune.

|`--generate`
|If enabled, only creates the Dockerfile and saves it to local disk.

|`-d`, `--out-dockerfile` (string)
|Optional: If generating the Dockerfile, specify a file name.

|`-p`, `--packages` (strings)
|Comma-separated list of packages to keep.

|`--permissive`
|Allow registry load errors.

|`-t`, `--tag` (string)
|Custom tag for container image being built.

|===

[id="opm-cli-ref-index-prune-stranded_{context}"]
== prune-stranded

Prune an index of stranded bundles, which are bundles that are not associated with a particular image.

.Command syntax
[source,terminal]
----
$ opm index prune-stranded [<flags>]
----

.`index prune-stranded` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-i`, `--binary-image`
|Container image for on-image `opm` command

|`-c`, `--container-tool` (string)
|Tool to interact with container images, such as for saving and building: `docker` or `podman`.

|`-f`, `--from-index` (string)
|Index to prune.

|`--generate`
|If enabled, only creates the Dockerfile and saves it to local disk.

|`-d`, `--out-dockerfile` (string)
|Optional: If generating the Dockerfile, specify a file name.

|`-p`, `--packages` (strings)
|Comma-separated list of packages to keep.

|`--permissive`
|Allow registry load errors.

|`-t`, `--tag` (string)
|Custom tag for container image being built.

|===

[id="opm-cli-ref-index-rm_{context}"]
== rm

Delete an entire Operator from an index.

.Command syntax
[source,terminal]
----
$ opm index rm [<flags>]
----

.`index rm` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-i`, `--binary-image`
|Container image for on-image `opm` command

|`-u`, `--build-tool` (string)
|Tool to build container images: `podman` (the default value) or `docker`. Overrides part of the `--container-tool` flag.

|`-c`, `--container-tool` (string)
|Tool to interact with container images, such as for saving and building: `docker` or `podman`.

|`-f`, `--from-index` (string)
|Previous index to delete from.

|`--generate`
|If enabled, only creates the Dockerfile and saves it to local disk.

|`-o`, `--operators` (strings)
|Comma-separated list of Operators to delete.

|`-d`, `--out-dockerfile` (string)
|Optional: If generating the Dockerfile, specify a file name.

|`-p`, `--packages` (strings)
|Comma-separated list of packages to keep.

|`--permissive`
|Allow registry load errors.

|`-p`, `--pull-tool` (string)
|Tool to pull container images: `none` (the default value), `docker`, or `podman`. Overrides part of the `--container-tool` flag.

|`-t`, `--tag` (string)
|Custom tag for container image being built.

|===
