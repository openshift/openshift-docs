// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-getting-started.adoc
// * serverless/cli_tools/kn-func-ref.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-kn-func-invoke_{context}"]
= Invoking a deployed function with a test event

You can use the `kn func invoke` CLI command to send a test request to invoke a function either locally or on your {product-title} cluster. You can use this command to test that a function is working and able to receive events correctly. Invoking a function locally is useful for a quick test during function development. Invoking a function on the cluster is useful for testing that is closer to the production environment.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.
* You must have already deployed the function that you want to invoke.

.Procedure

* Invoke a function:
+
[source,terminal]
----
$ kn func invoke
----
** The `kn func invoke` command only works when there is either a local container image currently running, or when there is a function deployed in the cluster.
** The `kn func invoke` command executes on the local directory by default, and assumes that this directory is a function project.
