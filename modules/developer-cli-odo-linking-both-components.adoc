// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating-a-multicomponent-application-with-odo.adoc
:_mod-docs-content-type: PROCEDURE
[id="linking-both-components_{context}"]

= Linking both components

Components running on the cluster need to be connected to interact. {product-title} provides linking mechanisms to publish communication bindings from a program to its clients.

.Procedure

. List all the components that are running on the cluster:
+
[source,terminal]
----
$ odo list
----
+
.Example output
[source,terminal]
----
OpenShift Components:
APP     NAME         PROJECT     TYPE          SOURCETYPE     STATE
app     backend      testpro     openjdk18     binary         Pushed
app     frontend     testpro     nodejs        local          Pushed
----


. Link the current front-end component to the back end:
+
[source,terminal]
----
$ odo link backend --port 8080
----
+
.Example output
[source,terminal]
----
 ✓  Component backend has been successfully linked from the component frontend

Following environment variables were added to frontend component:
- COMPONENT_BACKEND_HOST
- COMPONENT_BACKEND_PORT
----
+
The configuration information of the back-end component is added to the front-end component and the front-end component restarts.
