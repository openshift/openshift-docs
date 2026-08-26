// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-getting-started.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-deploy-func-kn_{context}"]
= Deploying functions

You can deploy a function to your cluster as a Knative service by using the `kn func deploy` command. If the targeted function is already deployed, it is updated with a new container image that is pushed to a container image registry, and the Knative service is updated.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.
* You must have already created and initialized the function that you want to deploy.

.Procedure

* Deploy a function:
+
[source,terminal]
----
$ kn func deploy [-n <namespace> -p <path> -i <image>]
----
+
.Example output
[source,terminal]
----
Function deployed at: http://func.example.com
----
** If no `namespace` is specified, the function is deployed in the current namespace.
** The function is deployed from the current directory, unless a `path` is specified.
** The Knative service name is derived from the project name, and cannot be changed using this command.

[NOTE]
====
You can create a serverless function with a Git repository URL by using *Import from Git* or *Create Serverless Function* in the *+Add* view of the *Developer* perspective.
====
