// Module included in the following assemblies:
//
// * serverless/cli_tools/installing-kn.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-installing-cli-macos_{context}"]
= Installing the Knative CLI for macOS

If you are using macOS, you can install the Knative (`kn`) CLI as a binary file. To do this, you must download and unpack a `tar.gz` archive and add the binary to a directory on your `PATH`.

// no prereqs?

.Procedure

. Download the link:https://mirror.openshift.com/pub/openshift-v4/clients/serverless/latest/kn-macos-amd64.tar.gz[Knative (`kn`) CLI `tar.gz` archive].
+
You can also download any version of `kn` by navigating to that version's corresponding directory in the link:https://mirror.openshift.com/pub/openshift-v4/clients/serverless/[Serverless client download mirror].

. Unpack and extract the archive.

. Move the `kn` binary to a directory on your `PATH`.

. To check your `PATH`, open a terminal window and run:
+
[source,terminal]
----
$ echo $PATH
----
