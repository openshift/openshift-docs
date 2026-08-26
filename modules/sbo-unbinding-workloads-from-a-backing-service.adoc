// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/binding-workloads-using-sbo.adoc

:_mod-docs-content-type: PROCEDURE
[id="sbo-unbinding-workloads-from-a-backing-service_{context}"]
= Unbinding workloads from a backing service

[role="_abstract"]
You can unbind a workload from a backing service by using the `oc` tool.

* To unbind a workload from a backing service, delete the `ServiceBinding` custom resource (CR) linked to it:
+
[source,terminal]
----
$ oc delete ServiceBinding <.metadata.name>
----
+
.Example
[source,terminal]
----
$ oc delete ServiceBinding spring-petclinic-pgcluster
----
where:
[horizontal]
`spring-petclinic-pgcluster`:: Specifies the name of the `ServiceBinding` CR.