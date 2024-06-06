// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-clustertask-management-commands_{context}"]
= ClusterTask management commands

[IMPORTANT]
====
In {pipelines-title} 1.10, ClusterTask functionality of the `tkn` command line utility is deprecated and is planned to be removed in a future release.
====

== clustertask
Manage ClusterTasks.

.Example: Display help
[source,terminal]
----
$ tkn clustertask --help
----

== clustertask delete
Delete a ClusterTask resource in a cluster.

.Example: Delete `mytask1` and `mytask2` ClusterTasks
[source,terminal]
----
$ tkn clustertask delete mytask1 mytask2
----

== clustertask describe
Describe a ClusterTask.

.Example: Describe the `mytask` ClusterTask
[source,terminal]
----
$ tkn clustertask describe mytask1
----

== clustertask list
List ClusterTasks.

.Example: List ClusterTasks
[source,terminal]
----
$ tkn clustertask list
----
== clustertask start
Start ClusterTasks.

.Example: Start the `mytask` ClusterTask
[source,terminal]
----
$ tkn clustertask start mytask
----
