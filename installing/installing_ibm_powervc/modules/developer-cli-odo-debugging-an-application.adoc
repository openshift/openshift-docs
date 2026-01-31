// Module included in the following assemblies:
//
// * cli_reference/creating_and_deploying_applications_with_odo/debugging-applications-in-odo.adoc

:_mod-docs-content-type: PROCEDURE
[id="debugging-an-application_{context}"]

= Debugging an application

You can debug your application in `odo` with the `odo debug` command.

.Procedure

. Download the sample application that contains the necessary `debugrun` step within its devfile:
+
[source,terminal]
----
$ odo create nodejs --starter
----
+
.Example output
[source,terminal]
----
Validation
 ✓  Checking devfile existence [11498ns]
 ✓  Checking devfile compatibility [15714ns]
 ✓  Creating a devfile component from registry: DefaultDevfileRegistry [17565ns]
 ✓  Validating devfile component [113876ns]

Starter Project
 ✓  Downloading starter project nodejs-starter from https://github.com/odo-devfiles/nodejs-ex.git [428ms]

Please use `odo push` command to create the component with source deployed
----

. Push the application with the `--debug` flag, which is required for all debugging deployments:
+
[source,terminal]
----
$ odo push --debug
----
+
.Example output
[source,terminal]
----
Validation
 ✓  Validating the devfile [29916ns]

Creating Kubernetes resources for component nodejs
 ✓  Waiting for component to start [38ms]

Applying URL changes
 ✓  URLs are synced with the cluster, no changes are required.

Syncing to component nodejs
 ✓  Checking file changes for pushing [1ms]
 ✓  Syncing files to the component [778ms]

Executing devfile commands for component nodejs
 ✓  Executing install command "npm install" [2s]
 ✓  Executing debug command "npm run debug" [1s]

Pushing devfile component nodejs
 ✓  Changes successfully pushed to component
----
+
[NOTE]
====
You can specify a custom debug command by using the `--debug-command="custom-step"` flag.
====

. Port forward to the local port to access the debugging interface:
+
[source,terminal]
----
$ odo debug port-forward
----
+
.Example output
[source,terminal]
----
Started port forwarding at ports - 5858:5858
----
+
[NOTE]
====
You can specify a port by using the `--local-port` flag.
====

. Check that the debug session is running in a separate terminal window:
+
[source,terminal]
----
$ odo debug info
----
+
.Example output
[source,terminal]
----
Debug is running for the component on the local port : 5858
----

. Attach the debugger that is bundled in your IDE of choice. Instructions vary depending on your IDE, for example: link:https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_remote-debugging[VSCode debugging interface].
