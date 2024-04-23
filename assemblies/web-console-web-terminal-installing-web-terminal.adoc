:_mod-docs-content-type: ASSEMBLY
[id="installing-web-terminal"]
= Installing the web terminal
include::_attributes/common-attributes.adoc[]
:context: installing-web-terminal

toc::[]

You can install the web terminal by using the {web-terminal-op} listed in the {product-title} OperatorHub. When you install the {web-terminal-op}, the custom resource definitions (CRDs) that are required for the command line configuration, such as the `DevWorkspace` CRD, are automatically installed. The web console creates the required resources when you open the web terminal.

[discrete]
[id="prerequisites_installing-web-terminal"]
== Prerequisites

* You are logged into the {product-title} web console.
* You have cluster administrator permissions.

[discrete]
[id="installing-web-terminal-procedure"]
== Procedure

. In the *Administrator* perspective of the web console, navigate to *Operators -> OperatorHub*.
. Use the *Filter by keyword* box to search for the {web-terminal-op} in the catalog, and then click the *Web Terminal* tile.
. Read the brief description about the Operator on the *Web Terminal*  page, and then click *Install*.
. On the *Install Operator* page, retain the default values for all fields.

** The *fast* option in the *Update Channel* menu enables installation of the latest release of the {web-terminal-op}.
** The *All namespaces on the cluster* option in the *Installation Mode* menu  enables the Operator to watch and be available to all namespaces in the cluster.
** The *openshift-operators* option in the *Installed Namespace* menu installs the Operator in the default `openshift-operators` namespace.
** The *Automatic* option in the *Approval Strategy* menu ensures that the future upgrades to the Operator are handled automatically by the Operator Lifecycle Manager.

. Click *Install*.
. In the *Installed Operators* page, click the *View Operator* to verify that the Operator is listed on the *Installed Operators* page.
+
[NOTE]
====
The {web-terminal-op} installs the DevWorkspace Operator as a dependency.
====

. After the Operator is installed, refresh your page to see the command line terminal icon (image:odc-wto-icon.png[title="web terminal icon"]) in the masthead of the console.