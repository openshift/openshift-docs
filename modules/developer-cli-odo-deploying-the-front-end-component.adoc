// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating-a-multicomponent-application-with-odo.adoc
// * cli_reference/developer_cli_odo/creating_and_deploying_applications_with_odo/creating-an-application-with-a-database.adoc

ifeval::["{context}" == "creating-a-multicomponent-application-with-odo"]
:multi:
endif::[]
ifeval::["{context}" == "creating-an-application-with-a-database"]
:database:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="deploying-the-front-end-component_{context}"]

= Deploying the front-end component

To create and deploy a front-end component, download the Node.js application and push the source code to your cluster with `{odo-title}`.

.Procedure

. Download the example front-end application:
+
[source,terminal]
----
$ git clone https://github.com/openshift/nodejs-ex frontend
----

. Change the current directory to the front-end directory:
+
[source,terminal]
----
$ cd frontend
----

. List the contents of the directory to see that the front end is a Node.js application.
+
[source,terminal]
----
$ ls
----
+
.Example output
[source,terminal]
----
README.md       openshift       server.js       views
helm            package.json    tests
----
+
[NOTE]
====
The front-end component is written in an interpreted language (Node.js); it does not need to be built.
====

. Create a component configuration of Node.js component-type named `frontend`:
+
[source,terminal]
----
$ odo create --s2i nodejs frontend
----
+
.Example output
[source,terminal]
----
 ✓  Validating component [5ms]
Please use `odo push` command to create the component with source deployed
----

ifdef::database[]
. Create a URL to access the frontend interface.
+
[source,terminal]
----
$ odo url create myurl
----
+
.Example output
[source,terminal]
----
 ✓  URL myurl created for component: nodejs-nodejs-ex-pmdp
----

. Push the component to the {product-title} cluster.
+
[source,terminal]
----
$ odo push
----
+
.Example output
[source,terminal]
----
Validation
 ✓  Checking component [7ms]

 Configuration changes
 ✓  Initializing component
 ✓  Creating component [134ms]

 Applying URL changes
 ✓  URL myurl: http://myurl-app-myproject.192.168.42.79.nip.io created

 Pushing to component nodejs-nodejs-ex-mhbb of type local
 ✓  Checking files for pushing [657850ns]
 ✓  Waiting for component to start [6s]
 ✓  Syncing files to the component [408ms]
 ✓  Building component [7s]
 ✓  Changes successfully pushed to component
----
endif::database[]

ifdef::multi[]
. Push the component to a running container.
+
[source,terminal]
----
$ odo push
----
+
.Example output
[source,terminal]
----
Validation
 ✓  Checking component [8ms]

Configuration changes
 ✓  Initializing component
 ✓  Creating component [83ms]

Pushing to component frontend of type local
 ✓  Checking files for pushing [2ms]
 ✓  Waiting for component to start [45s]
 ✓  Syncing files to the component [3s]
 ✓  Building component [18s]
 ✓  Changes successfully pushed to component
----
endif::multi[]

ifeval::["{context}" == "creating-a-multicomponent-application-with-odo"]
:!multi:
endif::[]
ifeval::["{context}" == "creating-an-application-with-a-database"]
:!database:
endif::[]
