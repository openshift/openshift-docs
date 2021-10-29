// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-task-management_{context}"]
= Task management commands

== task
Manage tasks.

.Example: Display help
[source,terminal]
----
$ tkn task -h
----

== task delete
Delete a task.

.Example: Delete `mytask1` and `mytask2` tasks from a namespace
[source,terminal]
----
$ tkn task delete mytask1 mytask2 -n myspace
----

== task describe
Describe a task.

.Example: Describe the `mytask` task in a namespace
[source,terminal]
----
$ tkn task describe mytask -n myspace
----

== task list
List tasks.

.Example: List all the tasks in a namespace
[source,terminal]
----
$ tkn task list -n myspace
----

== task logs
Display task logs.

.Example: Display logs for the `mytaskrun` task run of the `mytask` task
[source,terminal]
----
$ tkn task logs mytask mytaskrun -n myspace
----

== task start
Start a task.

.Example: Start the `mytask` task in a namespace
[source,terminal]
----
$ tkn task start mytask -s <ServiceAccountName> -n myspace
----
