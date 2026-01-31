// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/configuring-the-odo-cli.adoc

:_mod-docs-content-type: REFERENCE
[id="developer-cli-odo-set-config_{context}"]
= Setting a value

You can set a value for a preference key by using the following command:

[source,terminal]
----
$ odo preference set <key> <value>
----

[NOTE]
====
Preference keys are case-insensitive.
====

.Example command
[source,terminal]
----
$ odo preference set updatenotification false
----

.Example output
[source,terminal]
----
Global preference was successfully updated
----
