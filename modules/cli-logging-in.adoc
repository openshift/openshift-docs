// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

:_mod-docs-content-type: PROCEDURE
[id="cli-logging-in_{context}"]
= Logging in to the OpenShift CLI

You can log in to the OpenShift CLI (`oc`) to access and manage your cluster.

.Prerequisites

* You must have access to
ifndef::openshift-rosa[]
an {product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
a ROSA
endif::openshift-rosa[]
cluster.
* The {oc-first} is installed.

[NOTE]
====
To access a cluster that is accessible only over an HTTP proxy server, you can set the `HTTP_PROXY`, `HTTPS_PROXY` and `NO_PROXY` variables.
These environment variables are respected by the `oc` CLI so that all communication with the cluster goes through the HTTP proxy.

Authentication headers are sent only when using HTTPS transport.
====

.Procedure

. Enter the `oc login` command and pass in a user name:
+
[source,terminal]
----
$ oc login -u user1
----

. When prompted, enter the required information:
+
.Example output
[source,terminal]
----
Server [https://localhost:8443]: https://openshift.example.com:6443 <1>
The server uses a certificate signed by an unknown authority.
You can bypass the certificate check, but any data you send to the server could be intercepted by others.
Use insecure connections? (y/n): y <2>

Authentication required for https://openshift.example.com:6443 (openshift)
Username: user1
Password: <3>
Login successful.

You don't have any projects. You can try to create a new project, by running

    oc new-project <projectname>

Welcome! See 'oc help' to get started.
----
<1> Enter the
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
server URL.
<2> Enter whether to use insecure connections.
<3> Enter the user's password.

[NOTE]
====
If you are logged in to the web console, you can generate an `oc login` command that includes your token and server information. You can use the command to log in to the
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
OpenShift
endif::openshift-rosa[]
CLI without the interactive prompts. To generate the command, select *Copy login command* from the username drop-down menu at the top right of the web console.
====

You can now create a project or issue other commands for managing your cluster.
