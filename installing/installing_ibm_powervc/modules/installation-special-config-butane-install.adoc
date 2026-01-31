// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc

:_mod-docs-content-type: PROCEDURE
[id="installation-special-config-butane-install_{context}"]
= Installing Butane

You can install the Butane tool (`butane`) to create {product-title} machine configs from a command-line interface. You can install `butane` on Linux, Windows, or macOS by downloading the corresponding binary file.

[TIP]
====
Butane releases are backwards-compatible with older releases and with the Fedora CoreOS Config Transpiler (FCCT).
====

.Procedure

. Navigate to the Butane image download page at https://mirror.openshift.com/pub/openshift-v4/clients/butane/.
. Get the `butane` binary:
.. For the newest version of Butane, save the latest `butane` image to your current directory:
+
[source,terminal]
----
$ curl https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane --output butane
----
+
.. Optional: For a specific type of architecture you are installing Butane on, such as aarch64 or ppc64le, indicate the appropriate URL. For example:
+
[source,terminal]
----
$ curl https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane-aarch64 --output butane
----
+
. Make the downloaded binary file executable:
+
[source,terminal]
----
$ chmod +x butane
----
+
. Move the `butane` binary file to a directory on your `PATH`.
+
To check your `PATH`, open a terminal and execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

.Verification steps

* You can now use the Butane tool by running the `butane` command:
+
[source,terminal]
----
$ butane <butane_file>
----
