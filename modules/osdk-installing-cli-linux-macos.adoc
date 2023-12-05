// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-install.adoc
// * operators/operator_sdk/osdk-installing-cli.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-installing-cli-linux-macos_{context}"]
= Installing the Operator SDK CLI on Linux

You can install the OpenShift SDK CLI tool on Linux.

.Prerequisites

* link:https://golang.org/dl/[Go] v1.19+
ifdef::openshift-origin[]
* link:https://docs.docker.com/install/[`docker`] v17.03+, link:https://github.com/containers/libpod/blob/master/install.md[`podman`] v1.2.0+, or link:https://github.com/containers/buildah/blob/master/install.md[`buildah`] v1.7+
endif::[]
ifndef::openshift-origin[]
* `docker` v17.03+, `podman` v1.9.3+, or `buildah` v1.7+
endif::[]

.Procedure

. Navigate to the link:https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/operator-sdk/[OpenShift mirror site].

. From the latest {product-version} directory, download the latest version of the tarball for Linux.

. Unpack the archive:
+
[source,terminal,subs="attributes+"]
----
$ tar xvf operator-sdk-v{osdk_ver}-ocp-linux-x86_64.tar.gz
----

. Make the file executable:
+
[source,terminal]
----
$ chmod +x operator-sdk
----

. Move the extracted `operator-sdk` binary to a directory that is on your `PATH`.
+
[TIP]
====
To check your `PATH`:

[source,terminal]
----
$ echo $PATH
----
====
+
[source,terminal]
----
$ sudo mv ./operator-sdk /usr/local/bin/operator-sdk
----

.Verification

* After you install the Operator SDK CLI, verify that it is available:
+
[source,terminal]
----
$ operator-sdk version
----
+
.Example output
[source,terminal,subs="attributes+"]
----
operator-sdk version: "v{osdk_ver}-ocp", ...
----
