// Module included in the following assemblies:
//
// * * rosa_cli/rosa-checking-logs-cli.adoc

[id="rosa-logs-uninstall_{context}"]
= logs uninstall

Show the cluster uninstall logs by using the following command syntax:

.Syntax
[source,terminal]
----
$ rosa logs uninstall --cluster=<cluster_name> | <cluster_id> [arguments]
----

.Arguments
[cols="30,70"]
|===
|Option |Definition

|--cluster
|The name or ID (string) of the cluster to get logs for.

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

.Example
Show the last 100 uninstall logs for a cluster named `mycluster`:
[source,terminal]
----
$ rosa logs uninstall --cluster=mycluster --tail=100
----