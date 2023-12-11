// Module included in the following assemblies:
//
// * serverless/security/serverless-custom-domains.adoc
// * serverless/reference/kn-serving-ref.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-create-domain-mapping-kn_{context}"]
= Creating a custom domain mapping by using the Knative CLI

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have created a Knative service or route, and control a custom domain that you want to map to that CR.
+
[NOTE]
====
Your custom domain must point to the DNS of the {product-title} cluster.
====
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

.Procedure

* Map a domain to a CR in the current namespace:
+
[source,terminal]
----
$ kn domain create <domain_mapping_name> --ref <target_name>
----
+
.Example command
[source,terminal]
----
$ kn domain create example.com --ref example-service
----
+
The `--ref` flag specifies an Addressable target CR for domain mapping.
+
If a prefix is not provided when using the `--ref` flag, it is assumed that the target is a Knative service in the current namespace.

* Map a domain to a Knative service in a specified namespace:
+
[source,terminal]
----
$ kn domain create <domain_mapping_name> --ref <ksvc:service_name:service_namespace>
----
+
.Example command
[source,terminal]
----
$ kn domain create example.com --ref ksvc:example-service:example-namespace
----

* Map a domain to a Knative route:
+
[source,terminal]
----
$ kn domain create <domain_mapping_name> --ref <kroute:route_name>
----
+
.Example command
[source,terminal]
----
$ kn domain create example.com --ref kroute:example-route
----
