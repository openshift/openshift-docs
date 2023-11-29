// Module included in the following assemblies:
//
// * rosa_cli/rosa-get-started-cli.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-updating-the-rosa-cli_{context}"]
= Updating the ROSA CLI

Update to the latest compatible version of the ROSA CLI (`rosa`).

.Procedure

. Confirm that a new version of the ROSA CLI (`rosa`) is available:
+
[source,terminal]
----
$ rosa version
----
+
.Example output
[source,terminal]
----
1.2.12
There is a newer release version '1.2.15', please consider updating: https://mirror.openshift.com/pub/openshift-v4/clients/rosa/latest/
----

. Download the latest compatible version of the ROSA CLI:
+
[source,terminal]
----
$ rosa download rosa
----
+
This command downloads an archive called `rosa-*.tar.gz` into the current directory. The exact name of the file depends on your operating system and system architecture.

. Extract the contents of the archive:
+
[source,terminal]
----
$ tar -xzf rosa-linux.tar.gz
----

. Install the new version of the ROSA CLI by moving the extracted file into your path. In the following example, the `/usr/local/bin` directory is included in the path of the user:
+
[source,terminal]
----
$ sudo mv rosa /usr/local/bin/rosa
----

.Verification
* Verify that the new version of ROSA is installed.
+
[source,terminal]
----
$ rosa version
----
+
.Example output
[source,terminal]
----
1.2.15
Your ROSA CLI is up to date.
----