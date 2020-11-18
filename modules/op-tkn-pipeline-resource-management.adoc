// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-pipeline-resource-management_{context}"]
= Pipeline Resource management commands

== resource
Manage Pipeline Resources.

.Example: Display help
[source,terminal]
----
$ tkn resource -h
----

== resource create
Create a Pipeline Resource.

.Example: Create a Pipeline Resource in a namespace
[source,terminal]
----
$ tkn resource create -n myspace
----
This is an interactive command that asks for input on the name of the Resource, type of the Resource, and the values based on the type of the Resource.

== resource delete
Delete a Pipeline Resource.

.Example: Delete the `myresource` Pipeline Resource from a namespace
[source,terminal]
----
$ tkn resource delete myresource -n myspace
----

== resource describe
Describe a Pipeline Resource.

.Example: Describe the `myresource` Pipeline Resource
[source,terminal]
----
$ tkn resource describe myresource -n myspace
----
== resource list
List Pipeline Resources.

.Example: List all Pipeline Resources in a namespace
[source,terminal]
----
$ tkn resource list -n myspace
----
