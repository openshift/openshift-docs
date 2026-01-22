// Module included in the following assemblies:
//
// * serverless/reference/kn-serving-ref.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-manage-domain-mapping-kn_{context}"]
= Managing custom domain mappings by using the Knative CLI

After you have created a `DomainMapping` custom resource (CR), you can list existing CRs, view information about an existing CR, update CRs, or delete CRs by using the Knative (`kn`) CLI.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have created at least one `DomainMapping` CR.
* You have installed the Knative (`kn`) CLI tool.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

.Procedure

* List existing `DomainMapping` CRs:
+
[source,terminal]
----
$ kn domain list -n <domain_mapping_namespace>
----

* View details of an existing `DomainMapping` CR:
+
[source,terminal]
----
$ kn domain describe <domain_mapping_name>
----

* Update a `DomainMapping` CR to point to a new target:
+
[source,terminal]
----
$ kn domain update --ref <target>
----

* Delete a `DomainMapping` CR:
+
[source,terminal]
----
$ kn domain delete <domain_mapping_name>
----
