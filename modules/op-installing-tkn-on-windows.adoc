// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/installing-tkn.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-tkn-on-windows"]

= Installing the {pipelines-title} CLI on Windows

[role="_abstract"]
For Windows, you can download the CLI as a `zip` archive.

.Procedure

.  Download the link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/{pipelines-version-number}.0/tkn-windows-amd64.zip[CLI tool].

. Extract the archive with a ZIP program.
ifndef::openshift-rosa,openshift-dedicated[]
. Add the location of your `tkn`, `tkn-pac`, and `opc` files to your `PATH` environment variable.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
. Add the location of your `tkn` and `tkn-pac` files to your `PATH` environment variable.
endif::openshift-rosa,openshift-dedicated[]

. To check your `PATH`, run the following command:
+
[source,terminal]
----
C:\> path
----
