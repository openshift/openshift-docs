// Module included in the following assemblies:
//
// * web_console/dynamic-plugin/dynamic-plugins-get-started.adoc

:_mod-docs-content-type: PROCEDURE
[id="dynamic-plugin-development_{context}"]
= Dynamic plugin development

You can run the plugin using a local development environment. The {product-title} web console runs in a container connected to the cluster you have logged into.

.Prerequisites
* You must have an OpenShift cluster running.
* You must have the OpenShift CLI (`oc`) installed.
* You must have link:https://yarnpkg.com/[`yarn`] installed.
* You must have link:https://www.docker.com/[Docker] v3.2.0 or newer or link:https://podman.io/[Podman] installed and running.

.Procedure

. In your terminal, run the following command to install the dependencies for your plugin using yarn.

+
[source,terminal]
----
$ yarn install
----

. After installing, run the following command to start yarn.

+
[source,terminal]
----
$ yarn run start
----

. In another terminal window, login to the {product-title} through the CLI.
+
[source,terminal]
----
$ oc login
----

. Run the {product-title} web console in a container connected to the cluster you have logged into by running the following command:
+
[source,terminal]
----
$ yarn run start-console
----

.Verification
* Visit link:http://localhost:9000/example[localhost:9000] to view the running plugin. Inspect the value of `window.SERVER_FLAGS.consolePlugins` to see the list of plugins which load at runtime.
