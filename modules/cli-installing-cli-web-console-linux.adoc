ifeval::["{context}" == "updating-restricted-network-cluster"]
:restricted:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="cli-installing-cli-web-console-macos-linux_{context}"]
= Installing the OpenShift CLI on Linux using the web console

You can install the OpenShift CLI (`oc`) binary on Linux by using the following procedure.

.Procedure
ifndef::openshift-rosa,openshift-dedicated[]
. From the web console, click *?*.
+
image::click-question-mark.png[]
. Click *Command Line Tools*.
+
image::CLI-list.png[]
. Select appropriate `oc` binary for your Linux platform, and then click *Download oc for Linux*.

. Save the file.
. Unpack the archive.
endif::openshift-rosa,openshift-dedicated[]

ifdef::openshift-rosa,openshift-dedicated[]
. Download the latest version of the `oc` CLI for your operating system from the link:https://console.redhat.com/openshift/downloads[*Downloads*] page on {cluster-manager}.

. Extract the `oc` binary file from the downloaded archive.
endif::openshift-rosa,openshift-dedicated[]
+
[source,terminal]
----
$ tar xvf <file>
----
. Move the `oc` binary to a directory that is on your `PATH`.
+
To check your `PATH`, execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

After you install the OpenShift CLI, it is available using the `oc` command:

[source,terminal]
----
$ oc <command>
----

ifeval::["{context}" == "updating-restricted-network-cluster"]
:!restricted:
endif::[]
