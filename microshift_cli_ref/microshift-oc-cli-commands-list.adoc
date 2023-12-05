:_mod-docs-content-type: ASSEMBLY
[id="microshift-oc-cli-commands"]
= OpenShift CLI command reference
include::_attributes/attributes-microshift.adoc[]
:context: microshift-oc-cli-commands

toc::[]

Descriptions and example commands for OpenShift CLI (`oc`) commands are included in this reference document. You must have `cluster-admin` or equivalent permissions to use these commands. To list administrator commands and information about them, use the following commands:

* Enter the `oc adm -h` command to list all administrator commands:
+
.Command syntax
+
[source,terminal]
----
$ oc adm -h
----

* Enter the `oc <command> --help` command to get additional details for a specific command:
+
.Command syntax
+
[source,terminal]
----
$ oc <command> --help
----

[IMPORTANT]
====
Using `oc <command> --help` lists details for any `oc` command. Not all `oc` commands apply to using {product-title}.
====

// The OCP files are auto-generated from the openshift/oc repository; use the MicroShift-specific flags to generate MicroShift command files from the same repo
include::modules/microshift-oc-by-example-content.adoc[leveloffset=+1]

include::modules/microshift-oc-adm-by-example-content.adoc[leveloffset=+1]
