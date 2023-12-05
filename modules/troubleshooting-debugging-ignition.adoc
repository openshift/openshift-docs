// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operating-system-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="debugging-ignition_{context}"]
= Debugging Ignition failures

If a machine cannot be provisioned, Ignition fails and {op-system} will boot into the emergency shell. Use the following procedure to get debugging information.

.Procedure

. Run the following command to show which service units failed:
+
[source,terminal]
----
$ systemctl --failed
----

. Optional: Run the following command on an individual service unit to find out more information:
+
[source,terminal]
----
$ journalctl -u <unit>.service
----
