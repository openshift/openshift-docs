// Module included in the following assemblies:
//
// * cli_reference/opm/cli-opm-install.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-installing-opm_{context}"]
= Installing the opm CLI

You can install the `opm` CLI tool on your Linux, macOS, or Windows workstation.

.Prerequisites

* For Linux, you must provide the following packages. RHEL 8 meets these requirements:
** `podman` version 1.9.3+ (version 2.0+ recommended)
** `glibc` version 2.28+

.Procedure

ifndef::openshift-rosa,openshift-dedicated[]
. Navigate to the link:https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/latest-{product-version}/[OpenShift mirror site] and download the latest version of the tarball that matches your operating system.
endif::openshift-rosa,openshift-dedicated[]

ifdef::openshift-rosa,openshift-dedicated[]
. Navigate to the link:https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/[OpenShift mirror site] and download the latest version of the tarball that matches your operating system.
endif::openshift-rosa,openshift-dedicated[]

. Unpack the archive.

** For Linux or macOS:
+
[source,terminal,subs="attributes+"]
----
$ tar xvf <file>
----

** For Windows, unzip the archive with a ZIP program.

. Place the file anywhere in your `PATH`.
+
--
* For Linux or macOS:

.. Check your `PATH`:
+
[source,terminal]
----
$ echo $PATH
----

.. Move the file. For example:
+
[source,terminal]
----
$ sudo mv ./opm /usr/local/bin/
----

* For Windows:

.. Check your `PATH`:
+
[source,terminal]
----
C:\> path
----

.. Move the file:
+
[source,terminal]
----
C:\> move opm.exe <directory>
----
--

.Verification

* After you install the `opm` CLI, verify that it is available:
+
[source,terminal]
----
$ opm version
----
