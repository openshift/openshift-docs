// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

:_mod-docs-content-type: PROCEDURE
[id="cli-logging-in-web_{context}"]
= Logging in to the OpenShift CLI using a web browser

You can log in to the OpenShift CLI (`oc`) with the help of a web browser to access and manage your cluster. This allows users to avoid inserting their access token into the command line.

[WARNING]
====
Logging in to the CLI through the web browser runs a server on localhost with HTTP, not HTTPS; use with caution on multi-user workstations.
====

.Prerequisites

* You must have access to an {product-title} cluster.
* You must have installed the OpenShift CLI (`oc`).
* You must have a browser installed.

.Procedure

. Enter the `oc login` command with the `--web` flag:
+
[source,terminal]
----
$ oc login <cluster_url> --web <1>
----
<1> Optionally, you can specify the server URL and callback port. For example, `oc login <cluster_url> --web --callback-port 8280 localhost:8443`.

. The web browser opens automatically. If it does not, click the link in the command output. If you do not specify the {product-title} server `oc` tries to open the web console of the cluster specified in the current `oc` configuration file. If no `oc` configuration exists, `oc` prompts interactively for the server URL.
+
.Example output

[source,terminal]
----
Opening login URL in the default browser: https://openshift.example.com
Opening in existing browser session.
----

. If more than one identity provider is available, select your choice from the options provided.

. Enter your username and password into the corresponding browser fields. After you are logged in, the browser displays the text `access token received successfully; please return to your terminal`.

. Check the CLI for a login confirmation.
+
.Example output

[source,terminal]
----
Login successful.

You don't have any projects. You can try to create a new project, by running

    oc new-project <projectname>

----

[NOTE]
====
The web console defaults to the profile used in the previous session. To switch between Administrator and Developer profiles, log out of the {product-title} web console and clear the cache.
====

You can now create a project or issue other commands for managing your cluster.