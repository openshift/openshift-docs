// Module included in the following assemblies:
//
// * web_console/web_terminal/uninstalling-web-terminal.adoc

:_mod-docs-content-type: PROCEDURE
[id="removing-web-terminal-operator_{context}"]
= Removing the {web-terminal-op}

You can uninstall the web terminal by removing the {web-terminal-op} and custom resources used by the Operator.

.Prerequisites

* You have access to an {product-title} cluster with cluster administrator permissions.
* You have installed the `oc` CLI.

.Procedure

. In the *Administrator* perspective of the web console, navigate to *Operators -> Installed Operators*.
. Scroll the filter list or type a keyword into the *Filter by name* box to find the {web-terminal-op}.
. Click the Options menu {kebab} for the {web-terminal-op}, and then select *Uninstall Operator*.
. In the *Uninstall Operator* confirmation dialog box, click *Uninstall* to remove the Operator, Operator deployments, and pods from the cluster. The Operator stops running and no longer receives updates.
// Removed steps, as they are in the following module. 

// TODO: Add a verification section
