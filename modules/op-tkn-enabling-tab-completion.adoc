// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/installing-tkn.adoc

:_mod-docs-content-type: PROCEDURE
[id="op-tkn-enabling-tab-completion_{context}"]
= Enabling tab completion

After you install the `tkn` CLI, you can enable tab completion to automatically complete `tkn` commands or suggest options when you press Tab.

.Prerequisites

* You must have the `tkn` CLI tool installed.
* You must have `bash-completion` installed on your local system.

.Procedure

The following procedure enables tab completion for Bash.

. Save the Bash completion code to a file:
+
[source,terminal]
----
$ tkn completion bash > tkn_bash_completion
----

. Copy the file to `/etc/bash_completion.d/`:
+
[source,terminal]
----
$ sudo cp tkn_bash_completion /etc/bash_completion.d/
----
+
Alternatively, you can save the file to a local directory and source it from your `.bashrc` file instead.

Tab completion is enabled when you open a new terminal.
