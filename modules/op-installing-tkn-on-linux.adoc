// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/installing-tkn.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-tkn-on-linux"]

= Installing the {pipelines-title} CLI on Linux

[role="_abstract"]
For Linux distributions, you can download the CLI as a `tar.gz` archive.

.Procedure

. Download the relevant CLI tool.

* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/{pipelines-version-number}.0/tkn-linux-amd64.tar.gz[Linux (x86_64, amd64)]

* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/{pipelines-version-number}.0/tkn-linux-s390x.tar.gz[Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x)]

* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/{pipelines-version-number}.0/tkn-linux-ppc64le.tar.gz[Linux on {ibm-power-name} (ppc64le)]

* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/{pipelines-version-number}.0/tkn-linux-arm64.tar.gz[Linux on ARM (aarch64, arm64)]

// Binaries also need to be updated in the following modules:
// op-installing-pipelines-as-code-cli.adoc
// op-installing-tkn-on-windows.adoc
// op-installing-tkn-on-macos.adoc

. Unpack the archive:
+
[source,terminal]
----
$ tar xvzf <file>
----
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
$ echo $PATH
----
