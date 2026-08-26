// Module included in the following assemblies:
//
// * serverless/cli_tools/installing-kn.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-cli-web-console_{context}"]
= Installing the Knative CLI using the {product-title} web console

Using the {product-title} web console provides a streamlined and intuitive user interface to install the Knative (`kn`) CLI. After the {ServerlessOperatorName} is installed, you will see a link to download the Knative (`kn`) CLI for Linux (amd64, s390x, ppc64le), macOS, or Windows from the *Command Line Tools* page in the {product-title} web console.

.Prerequisites

* You have logged in to the {product-title} web console.
* The {ServerlessOperatorName} and Knative Serving are installed on your {product-title} cluster.
+
[IMPORTANT]
====
If *libc* is not available, you might see the following error when you run CLI commands:

[source,terminal]
----
$ kn: No such file or directory
----
====

* If you want to use the verification steps for this procedure, you must install the OpenShift (`oc`) CLI.

.Procedure

. Download the Knative (`kn`) CLI from the *Command Line Tools* page. You can access the *Command Line Tools* page by clicking the image:../images/question-circle.png[title="Help"] icon in the top right corner of the web console and selecting *Command Line Tools* in the list.

. Unpack the archive:
+
[source,terminal]
----
$ tar -xf <file>
----

. Move the `kn` binary to a directory on your `PATH`.

. To check your `PATH`, run:
+
[source,terminal]
----
$ echo $PATH
----

.Verification

* Run the following commands to check that the correct Knative CLI resources and route have been created:
+
[source,terminal]
----
$ oc get ConsoleCLIDownload
----
+
.Example output
[source,terminal]
----
NAME                  DISPLAY NAME                                             AGE
kn                    kn - OpenShift Serverless Command Line Interface (CLI)   2022-09-20T08:41:18Z
oc-cli-downloads      oc - OpenShift Command Line Interface (CLI)              2022-09-20T08:00:20Z
----
+
[source,terminal]
----
$ oc get route -n openshift-serverless
----
+
.Example output
[source,terminal]
----
NAME   HOST/PORT                                  PATH   SERVICES                      PORT       TERMINATION     WILDCARD
kn     kn-openshift-serverless.apps.example.com          knative-openshift-metrics-3   http-cli   edge/Redirect   None
----
