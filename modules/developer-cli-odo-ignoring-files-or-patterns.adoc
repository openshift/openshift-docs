// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/configuring-the-odo-cli.adoc  

[id="ignoring-files-or-patterns_{context}"]
= Ignoring files or patterns

You can configure a list of files or patterns to ignore by modifying the `.odoignore` file in the root directory of your application. This applies to both `odo push` and `odo watch`.

If the `.odoignore` file does _not_ exist, the `.gitignore` file is used instead for ignoring specific files and folders.

To ignore `.git` files, any files with the `.js` extension, and the folder `tests`, add the following to either the `.odoignore` or the `.gitignore` file:

----
.git
*.js
tests/
----

The `.odoignore` file allows any glob expressions.