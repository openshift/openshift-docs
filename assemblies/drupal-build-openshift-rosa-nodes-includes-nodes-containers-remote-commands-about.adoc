// Module included in the following assemblies:
//
// * nodes/nodes-containers-remote-commands.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-containers-remote-commands-about_{context}"]
= Executing remote commands in containers

Support for remote container command execution is built into the CLI.

.Procedure

To run a command in a container:

[source,terminal]
----
$ oc exec <pod> [-c <container>] -- <command> [<arg_1> ... <arg_n>]
----

For example:

[source,terminal]
----
$ oc exec mypod date
----

.Example output
[source,terminal]
----
Thu Apr  9 02:21:53 UTC 2015
----

[IMPORTANT]
====
link:https://access.redhat.com/errata/RHSA-2015:1650[For security purposes], the
`oc exec` command does not work when accessing privileged containers except when
the command is executed by a `cluster-admin` user.
====
