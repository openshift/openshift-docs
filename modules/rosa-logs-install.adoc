// Module included in the following assemblies:
//
// * * rosa_cli/rosa-checking-logs-cli.adoc

[id="rosa-logs-install_{context}"]
= logs install

Show the cluster install logs by using the following command syntax:

.Syntax
[source,terminal]
----
$ rosa logs install --cluster=<cluster_name> | <cluster_id> [arguments]
----

.Arguments
[cols="30,70"]
|===
|Option |Definition

|--cluster
|Required: The name or ID (string) of the cluster to get logs for.

|--tail
|The number (integer) of lines to get from the end of the log. Default: `2000`

|--watch
|Watches for changes after getting the logs.
|===

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

.Examples
Show the last 100 install log lines for a cluster named `mycluster`:

[source,terminal]
----
$ rosa logs install mycluster --tail=100
----

Show the install logs for a cluster named `mycluster`:

[source,terminal]
----
$ rosa logs install --cluster=mycluster
----