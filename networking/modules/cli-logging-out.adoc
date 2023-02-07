// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

[id="cli-logging-out_{context}"]
= Logging out of the OpenShift CLI

You can log out the OpenShift CLI to end your current session.

* Use the `oc logout` command.
+
[source,terminal]
----
$ oc logout
----
+
.Example output
[source,terminal]
----
Logged "user1" out on "https://openshift.example.com"
----

This deletes the saved authentication token from the server and removes it from
your configuration file.
