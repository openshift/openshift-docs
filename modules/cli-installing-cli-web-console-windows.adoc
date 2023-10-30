ifeval::["{context}" == "updating-restricted-network-cluster"]
:restricted:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="cli-installing-cli-web-console-macos-windows_{context}"]
= Installing the OpenShift CLI on Windows using the web console

You can install the OpenShift CLI (`oc`) binary on Windows by using the following procedure.

.Procedure
ifndef::openshift-rosa,openshift-dedicated[]
. From the web console, click *?*.
+
image::click-question-mark.png[]
. Click *Command Line Tools*.
+
image::CLI-list.png[]
. Select the `oc` binary for Windows platform, and then click *Download oc for Windows for x86_64*.
. Save the file.
. Unzip the archive with a ZIP program.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
. Download the latest version of the `oc` CLI for your operating system from the link:https://console.redhat.com/openshift/downloads[*Downloads*] page on {cluster-manager}.

. Extract the `oc` binary file from the downloaded archive.
endif::openshift-rosa,openshift-dedicated[]

. Move the `oc` binary to a directory that is on your `PATH`.
+
To check your `PATH`, open the command prompt and execute the following command:
+
[source,terminal]
----
C:\> path
----

After you install the OpenShift CLI, it is available using the `oc` command:

[source,terminal]
----
C:\> oc <command>
----

ifeval::["{context}" == "updating-restricted-network-cluster"]
:!restricted:
endif::[]
