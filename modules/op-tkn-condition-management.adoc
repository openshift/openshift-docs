// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/op-tkn-references.adoc

[id="op-tkn-condition-management_{context}"]
= Condition management commands

== condition
Manage Conditions.

.Example: Display help
[source,terminal]
----
$ tkn condition --help
----

== condition delete
Delete a Condition.

.Example: Delete the `mycondition1` Condition from a namespace
[source,terminal]
----
$ tkn condition delete mycondition1 -n myspace
----

== condition describe
Describe a Condition.

.Example: Describe the `mycondition1` Condition in a namespace
[source,terminal]
----
$ tkn condition describe mycondition1 -n myspace
----

== condition list
List Conditions.

.Example: List Conditions in a namespace
[source,terminal]
----
$ tkn condition list -n myspace
----
