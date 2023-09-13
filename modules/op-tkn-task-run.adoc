// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-task-run_{context}"]
= Task run commands

== taskrun
Manage task runs.

.Example: Display help
[source,terminal]
----
$ tkn taskrun -h
----

== taskrun cancel
Cancel a task run.

.Example: Cancel the `mytaskrun` task run from a namespace
[source,terminal]
----
$ tkn taskrun cancel mytaskrun -n myspace
----

== taskrun delete
Delete a TaskRun.

.Example: Delete the `mytaskrun1` and `mytaskrun2` task runs from a namespace
[source,terminal]
----
$ tkn taskrun delete mytaskrun1 mytaskrun2 -n myspace
----

.Example: Delete all but the five most recently executed task runs from a namespace
[source,terminal]
----
$ tkn taskrun delete -n myspace --keep 5 <1>
----
<1> Replace `5` with the number of most recently executed task runs you want to retain.

== taskrun describe
Describe a task run.

.Example: Describe the `mytaskrun` task run in a namespace
[source,terminal]
----
$ tkn taskrun describe mytaskrun -n myspace
----

== taskrun list
List task runs.

.Example: List all the task runs in a namespace
[source,terminal]
----
$ tkn taskrun list -n myspace
----


== taskrun logs
Display task run logs.

.Example: Display live logs for the `mytaskrun` task run in a namespace

[source,terminal]
----
$ tkn taskrun logs -f mytaskrun -n myspace
----
