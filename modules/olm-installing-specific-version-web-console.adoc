// Module included in the following assemblies:
//
// * operators/admin/olm-adding-operators-to-cluster.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-installing-specific-version-web-console_{context}"]
= Installing a specific version of an Operator in the web console

You can install a specific version of an Operator by using the OperatorHub in the web console. You are able to browse the various versions of an operator across any channels it might have, view the metadata for that channel and version, and select the exact version you want to install.

.Prerequisites

* You must have administrator privileges.

.Procedure

. From the web console, click *Operators* → *OperatorHub*.

. Select an Operator you want to install.

. From the selected Operator, you can select a *Channel* and *Version* from the lists.
+
[NOTE]
====
The version selection defaults to the latest version for the channel selected. If the latest version for the channel is selected, the Automatic approval strategy is enabled by default. Otherwise Manual approval is required when not installing the latest version for the selected channel.

Manual approval applies to all operators installed in a namespace.

Installing an Operator with manual approval causes all Operators installed within the namespace to function with the Manual approval strategy and all Operators are updated together. Install Operators into separate namespaces for updating independently.
====

. Click *Install*

.Verification

* When the operator is installed, the metadata indicates which channel and version are installed.
+
[NOTE]
====
The channel and version dropdown menus are still available for viewing other version metadata in this catalog context.
====