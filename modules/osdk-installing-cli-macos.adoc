// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-install.adoc
// * operators/operator_sdk/osdk-installing-cli.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-installing-cli-macos_{context}"]
= Installing the Operator SDK CLI on macOS

You can install the OpenShift SDK CLI tool on macOS.

.Prerequisites

* link:https://golang.org/dl/[Go] v1.19+
ifdef::openshift-origin[]
* link:https://docs.docker.com/install/[`docker`] v17.03+, link:https://github.com/containers/libpod/blob/master/install.md[`podman`] v1.2.0+, or link:https://github.com/containers/buildah/blob/master/install.md[`buildah`] v1.7+
endif::[]
ifndef::openshift-origin[]
* `docker` v17.03+, `podman` v1.9.3+, or `buildah` v1.7+
endif::[]

.Procedure
ifndef::openshift-rosa,openshift-dedicated[]
. For the `amd64` and `arm64` architectures, navigate to the link:https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/operator-sdk/[OpenShift mirror site for the `amd64` architecture] and link:https://mirror.openshift.com/pub/openshift-v4/arm64/clients/operator-sdk/[OpenShift mirror site for the `arm64` architecture] respectively.
endif::openshift-rosa,openshift-dedicated[]

ifdef::openshift-rosa,openshift-dedicated[]
. For the `amd64` architecture, navigate to the link:https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/operator-sdk/[OpenShift mirror site for the `amd64` architecture].
endif::openshift-rosa,openshift-dedicated[]


. From the latest {product-version} directory, download the latest version of the tarball for macOS.

. Unpack the Operator SDK archive for `amd64` architecture by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ tar xvf operator-sdk-v{osdk_ver}-ocp-darwin-x86_64.tar.gz
----
ifndef::openshift-rosa,openshift-dedicated[]
. Unpack the Operator SDK archive for `arm64` architecture by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ tar xvf operator-sdk-v{osdk_ver}-ocp-darwin-aarch64.tar.gz
----
endif::openshift-rosa,openshift-dedicated[]
. Make the file executable by running the following command:
+
[source,terminal]
----
$ chmod +x operator-sdk
----

. Move the extracted `operator-sdk` binary to a directory that is on your `PATH` by running the following command:
+
[TIP]
====
Check your `PATH` by running the following command:

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

* After you install the Operator SDK CLI, verify that it is available by running the following command::
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
