// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-ref.adoc
// * operators/operator_sdk/osdk-cli-ref.adoc

[id="osdk-cli-ref-completion_{context}"]
= completion

The `operator-sdk completion` command generates shell completions to make issuing CLI commands quicker and easier.

.`completion` subcommands
[options="header",cols="1,3"]
|===
|Subcommand |Description

|`bash`
|Generate bash completions.

|`zsh`
|Generate zsh completions.
|===

.`completion` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-h, --help`
|Usage help output.
|===

For example:

[source,terminal]
----
$ operator-sdk completion bash
----

.Example output
[source,terminal]
----
# bash completion for operator-sdk                         -*- shell-script -*-
...
# ex: ts=4 sw=4 et filetype=sh
----
