// Module included in the following assembly:
//
// * cicd/gitops/collecting-debugging-data-for-support.adoc

:_mod-docs-content-type: PROCEDURE
[id="collecting-debugging-data-for-gitops_{context}"]
= Collecting debugging data for {gitops-title}

Use the `oc adm must-gather` CLI command to collect the following details about the cluster that is associated with {gitops-title}:

* The subscription and namespace of the {gitops-title} Operator.
* The namespaces where ArgoCD objects are available and the objects in those namespaces, such as `ArgoCD`, `Applications`, `ApplicationSets`, `AppProjects`, and `configmaps`.
* A list of the namespaces that are managed by the {gitops-title} Operator, and resources from those namespaces.
* All {gitops-shortname}-related custom resource objects and definitions.
* Operator and Argo CD logs.
* Warning and error-level events.

.Prerequisites
* You have logged in to the {product-title} cluster as an administrator.
* You have installed the {product-title} CLI (`oc`).
* You have installed the {gitops-title} Operator.

.Procedure

. Navigate to the directory where you want to store the debugging information.
. Run the `oc adm must-gather` command with the {gitops-title} `must-gather` image:
+
[source,terminal]
----
$ oc adm must-gather --image=registry.redhat.io/openshift-gitops-1/gitops-must-gather-rhel8:v1.9.0
----
+
The `must-gather` tool creates a new directory that starts with `./must-gather.local` in the current directory. For example, `./must-gather.local.4157245944708210399`.

. Create a compressed file from the directory that was just created. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ tar -cvaf must-gather.tar.gz must-gather.local.4157245944708210399
----

. Attach the compressed file to your support case on the link:https://access.redhat.com/[Red Hat Customer Portal].