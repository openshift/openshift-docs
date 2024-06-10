// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

[id="cli-getting-help_{context}"]
= Getting help

You can get help with CLI commands and 
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
resources in the following ways:

* Use `oc help` to get a list and description of all available CLI commands:
+
.Example: Get general help for the CLI
[source,terminal]
----
$ oc help
----
+
.Example output
[source,terminal]
----
OpenShift Client

This client helps you develop, build, deploy, and run your applications on any OpenShift or Kubernetes compatible
platform. It also includes the administrative commands for managing a cluster under the 'adm' subcommand.

Usage:
  oc [flags]

Basic Commands:
  login           Log in to a server
  new-project     Request a new project
  new-app         Create a new application

...
----

* Use the `--help` flag to get help about a specific CLI command:
+
.Example: Get help for the `oc create` command
[source,terminal]
----
$ oc create --help
----
+
.Example output
[source,terminal]
----
Create a resource by filename or stdin

JSON and YAML formats are accepted.

Usage:
  oc create -f FILENAME [flags]

...
----

* Use the `oc explain` command to view the description and fields for a
particular resource:
+
.Example: View documentation for the `Pod` resource
[source,terminal]
----
$ oc explain pods
----
+
.Example output
[source,terminal]
----
KIND:     Pod
VERSION:  v1

DESCRIPTION:
     Pod is a collection of containers that can run on a host. This resource is
     created by clients and scheduled onto hosts.

FIELDS:
   apiVersion	<string>
     APIVersion defines the versioned schema of this representation of an
     object. Servers should convert recognized schemas to the latest internal
     value, and may reject unrecognized values. More info:
     https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

...
----
