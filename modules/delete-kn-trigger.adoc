// Module included in the following assemblies:
//
// * /serverless/eventing/triggers/delete-triggers-cli.adoc

:_mod-docs-content-type: PROCEDURE
[id="delete-kn-trigger_{context}"]
= Deleting a trigger by using the Knative CLI

You can use the `kn trigger delete` command to delete a trigger.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your {product-title} cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

.Procedure

* Delete a trigger:
+
[source,terminal]
----
$ kn trigger delete <trigger_name>
----

.Verification

. List existing triggers:
+
[source,terminal]
----
$ kn trigger list
----

. Verify that the trigger no longer exists:
+
.Example output
[source,terminal]
----
No triggers found.
----
