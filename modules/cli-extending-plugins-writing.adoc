// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/extending-cli-plugins.adoc

:_mod-docs-content-type: PROCEDURE
[id="cli-writing-plugins_{context}"]
= Writing CLI plugins

You can write a plugin for the
ifndef::openshift-rosa,openshift-dedicated[]
{product-title}
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
OpenShift
endif::openshift-rosa,openshift-dedicated[]
CLI in any programming language
or script that allows you to write command-line commands. Note that you can not
use a plugin to overwrite an existing `oc` command.

.Procedure

This procedure creates a simple Bash plugin that prints a message to the
terminal when the `oc foo` command is issued.

. Create a file called `oc-foo`.
+
When naming your plugin file, keep the following in mind:

* The file must begin with `oc-` or `kubectl-` to be recognized as a
plugin.
* The file name determines the command that invokes the plugin. For example, a
plugin with the file name `oc-foo-bar` can be invoked by a command of
`oc foo bar`. You can also use underscores if you want the command to contain
dashes. For example, a plugin with the file name `oc-foo_bar` can be invoked
by a command of `oc foo-bar`.

. Add the following contents to the file.
+
[source,bash]
----
#!/bin/bash

# optional argument handling
if [[ "$1" == "version" ]]
then
    echo "1.0.0"
    exit 0
fi

# optional argument handling
if [[ "$1" == "config" ]]
then
    echo $KUBECONFIG
    exit 0
fi

echo "I am a plugin named kubectl-foo"
----

After you install this plugin for the
ifndef::openshift-rosa,openshift-dedicated[]
{product-title}
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa[]
OpenShift
endif::openshift-rosa[]
CLI, it can be invoked
using the `oc foo` command.

[role="_additional-resources"]
.Additional resources

* Review the link:https://github.com/kubernetes/sample-cli-plugin[Sample plugin repository]
for an example of a plugin written in Go.
* Review the link:https://github.com/kubernetes/cli-runtime/[CLI runtime repository] for a set of utilities to assist in writing plugins in Go.
