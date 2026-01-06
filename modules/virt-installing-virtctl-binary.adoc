// Module included in the following assemblies:
//
// * virt/getting_started/virt-using-the-cli-tools.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-installing-virtctl-binary_{context}"]
= Installing the virtctl binary on {op-system-base} 9 or later, Linux, Windows, or macOS

You can download the `virtctl` binary by using the {product-title} web console and then install it on {op-system-base-full} 9 or later, Linux, Windows, or macOS.

.Procedure

. Navigate to the *Virtualization -> Overview* page in the web console.
. Click the *Download virtctl* link to download the `virtctl` binary for your operating system.

. Install `virtctl`:

* For {op-system-base} and other Linux operating systems:

.. Decompress the archive file:
+
[source,terminal]
----
$ tar -xvf <virtctl-version-distribution.arch>.tar.gz
----

.. Run the following command to make the `virtctl` binary executable:
+
[source,terminal]
----
$ chmod +x <path/virtctl-file-name>
----

.. Move the `virtctl` binary to a directory in your `PATH` environment variable.
+
You can check your path by running the following command:
+
[source,terminal]
----
$ echo $PATH
----

.. Set the `KUBECONFIG` environment variable:
+
[source,terminal]
----
$ export KUBECONFIG=/home/<user>/clusters/current/auth/kubeconfig
----

* For Windows:
+
.. Decompress the archive file.

.. Navigate the extracted folder hierarchy and double-click the `virtctl` executable file to install the client.

.. Move the `virtctl` binary to a directory in your `PATH` environment variable.
+
You can check your path by running the following command:
+
[source,terminal]
----
C:\> path
----

* For macOS:
+
.. Decompress the archive file.

.. Move the `virtctl` binary to a directory in your `PATH` environment variable.
+
You can check your path by running the following command:
+
[source,terminal]
----
echo $PATH
----
