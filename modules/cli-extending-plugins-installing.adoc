// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/extending-cli-plugins.adoc

:_mod-docs-content-type: PROCEDURE
[id="cli-installing-plugins_{context}"]
= Installing and using CLI plugins

After you write a custom plugin for the
ifndef::openshift-rosa,openshift-dedicated[]
{product-title}
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
OpenShift
endif::openshift-rosa,openshift-dedicated[]
CLI, you must install
the plugin before use.

.Prerequisites

* You must have the `oc` CLI tool installed.
* You must have a CLI plugin file that begins with `oc-` or `kubectl-`.

.Procedure

. If necessary, update the plugin file to be executable.
+
[source,terminal]
----
$ chmod +x <plugin_file>
----
. Place the file anywhere in your `PATH`, such as `/usr/local/bin/`.
+
[source,terminal]
----
$ sudo mv <plugin_file> /usr/local/bin/.
----
. Run `oc plugin list` to make sure that the plugin is listed.
+
[source,terminal]
----
$ oc plugin list
----
+
.Example output
[source,terminal]
----
The following compatible plugins are available:

/usr/local/bin/<plugin_file>
----
+
If your plugin is not listed here, verify that the file begins with `oc-`
or `kubectl-`, is executable, and is on your `PATH`.
. Invoke the new command or option introduced by the plugin.
+
For example, if you built and installed the `kubectl-ns` plugin from the
 link:https://github.com/kubernetes/sample-cli-plugin[Sample plugin repository],
  you can use the following command to view the current namespace.
+
[source,terminal]
----
$ oc ns
----
+
Note that the command to invoke the plugin depends on the plugin file name.
For example, a plugin with the file name of `oc-foo-bar` is invoked by the `oc foo bar`
command.
