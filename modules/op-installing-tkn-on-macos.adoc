// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/installing-tkn.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-tkn-on-macos"]

= Installing the {pipelines-title} CLI on macOS

[role="_abstract"]
For macOS, you can download the CLI as a `tar.gz` archive.

.Procedure

. Download the relevant CLI tool.

* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/{pipelines-version-number}.0/tkn-macos-amd64.tar.gz[macOS]

* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/{pipelines-version-number}.0/tkn-macos-arm64.tar.gz[macOS on ARM]

. Unpack and extract the archive.

ifndef::openshift-rosa,openshift-dedicated[]
. Add the location of your `tkn`, `tkn-pac`, and `opc` files to your `PATH` environment variable.
endif::openshift-rosa,openshift-dedicated[]

ifdef::openshift-rosa,openshift-dedicated[]
. Add the location of your `tkn` and `tkn-pac` and files to your `PATH` environment variable.
endif::openshift-rosa,openshift-dedicated[]

. To check your `PATH`, run the following command:
+
[source,terminal]
----
$ echo $PATH
----
