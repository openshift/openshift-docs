// Module included in the following assemblies:
//
// *cli_reference/developer_cli_odo/creating_and_deploying_applications_with_odo/working-with-storage.adoc

:_mod-docs-content-type: PROCEDURE
[id="switching-between-ephemeral-and-persistent-storage_{context}"]
= Switching between ephemeral and persistent storage

You can switch between ephemeral and persistent storage in your project by using the `odo preference` command. `odo preference` modifies the global preference in your cluster.

When persistent storage is enabled, the cluster stores the information between the restarts.

When ephemeral storage is enabled, the cluster does not store the information between the restarts.

Ephemeral storage is enabled by default.

.Procedure

. See the preference currently set in your project:
+
[source,terminal]
----
$ odo preference view
----
+
.Example output
+
[source,terminal]
----
PARAMETER             CURRENT_VALUE
UpdateNotification
NamePrefix
Timeout
BuildTimeout
PushTimeout
Experimental
PushTarget
Ephemeral             true
----

. To unset the ephemeral storage and set the persistent storage:
+
[source,terminal]
----
$ odo preference set Ephemeral false
----

. To set the ephemeral storage again:
+
[source,terminal]
----
$ odo preference set Ephemeral true
----
+
The `odo preference` command changes the global settings of all your currently deployed components as well as ones you will deploy in future.

. Run `odo push` to make `odo` create a specified storage for your component:
+
[source,terminal]
----
$ odo push
----
