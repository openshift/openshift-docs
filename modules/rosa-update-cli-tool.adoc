// Module included in the following assemblies:
//
// * rosa_release_notes/rosa-release-notes.adoc

:_mod-docs-content-type: PROCEDURE
[id="updating_rosa_cli{context}"]
== Updating the ROSA CLI tool

To use the latest version of the {product-title} (ROSA) CLI, `rosa`, download the ROSA CLI (`rosa`) from the Hybrid Cloud Console. If you already have this tool, the procedure is the same for updates.

.Procedure

. Download the file from the link:https://console.redhat.com/openshift/downloads[Hybrid Cloud Console].

. Unzip the downloaded file.

. Move the file to the `/usr/bin/rosa` directory by running the following command:
+
[source,terminal]
----
$ sudo mv rosa /usr/bin/rosa
----

. Confirm your version by running the following command:
+
[source,terminal]
----
$ rosa version
----
+
.Example output

[source,terminal]
----
<version>
Your ROSA CLI is up to date.
----

//Potential step 4: In the terminal, type `chmod a+x /usr/bin/rosa` to make the ROSA binary you downloaded executable.