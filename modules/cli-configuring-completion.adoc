// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/configuring-cli.adoc

:_mod-docs-content-type: PROCEDURE
[id="cli-enabling-tab-completion_{context}"]
= Enabling tab completion for Bash

After you install the OpenShift CLI (`oc`), you can enable tab completion to automatically complete `oc` commands or suggest options when you press Tab. The following procedure enables tab completion for the Bash shell.

.Prerequisites

* You must have the OpenShift CLI (`oc`) installed.
* You must have the package `bash-completion` installed.

.Procedure

. Save the Bash completion code to a file:
+
[source,terminal]
----
$ oc completion bash > oc_bash_completion
----

. Copy the file to `/etc/bash_completion.d/`:
+
[source,terminal]
----
$ sudo cp oc_bash_completion /etc/bash_completion.d/
----
+
You can also save the file to a local directory and source it from your `.bashrc` file instead.

Tab completion is enabled when you open a new terminal.
