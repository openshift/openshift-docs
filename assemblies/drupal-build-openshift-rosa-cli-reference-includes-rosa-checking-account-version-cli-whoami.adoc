// Module included in the following assemblies:
//
// * rosa_cli/rosa-checking-acct-version-cli.adoc

[id="rosa-whoami_{context}"]
= whoami

Display information about your AWS and Red Hat accounts by using the following command syntax:

.Syntax
[source,terminal]
----
$ rosa whoami [arguments]
----

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|--profile
|Specifies an AWS profile (string) from your credentials file.
|===

.Example
[source,terminal]
----
$ rosa whoami
----