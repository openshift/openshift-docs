// Module included in the following assemblies:
//
// * cli_reference/opm/cli-opm-ref.adoc

[id="opm-cli-ref-server_{context}"]
= serve

Serve declarative configs via a GRPC server.

[NOTE]
====
The declarative config directory is loaded by the `serve` command at startup. Changes made to the declarative config after this command starts are not reflected in the served content.
====

.Command syntax
[source,terminal]
----
$ opm serve <source_path> [<flags>]
----

.`serve` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`--cache-dir` (string)
|If this flag is set, it syncs and persists the server cache directory.

|`--cache-enforce-integrity`
|Exits with an error if the cache is not present or is invalidated. The default value is `true` when the `--cache-dir` flag is set and the `--cache-only` flag is `false`. Otherwise, the default is `false`.

|`--cache-only`
|Syncs the serve cache and exits without serving.

|`--debug`
|Enables debug logging.

|`h`, `--help`
|Help for serve.

|`-p`, `--port` (string)
|The port number for the service. The default value is `50051`.

|`--pprof-addr` (string)
|The address of the startup profiling endpoint. The format is `Addr:Port`.

|`-t`, `--termination-log` (string)
|The path to a container termination log file. The default value is `/dev/termination-log`.

|===
