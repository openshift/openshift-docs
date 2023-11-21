// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/configuring-the-odo-cli.adoc

:_mod-docs-content-type: PROCEDURE
[id="using-command-completion_{context}"]
= Using command completion

[NOTE]
====
Currently command completion is only supported for bash, zsh, and fish shells.
====

{odo-title} provides a smart completion of command parameters based on user input. For this to work, {odo-title} needs to integrate with the executing shell.

.Procedure

* To install command completion automatically:
. Run:
+
[source,terminal]
----
$ odo --complete
----
+
.  Press `y` when prompted to install the completion hook.

* To install the completion hook manually, add `complete -o nospace -C <full_path_to_your_odo_binary> odo` to your shell configuration file. After any modification to your shell configuration file, restart your shell.

* To disable completion:
. Run:
+
[source,terminal]
----
$ odo --uncomplete
----
+
. Press `y` when prompted to uninstall the completion hook.

[NOTE]
====
Re-enable command completion if you either rename the {odo-title} executable or move it to a different directory.
====
