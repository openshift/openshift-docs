// Module included in the following assemblies:
//
// * operators/admin/olm-cs-podsched.adoc

ifdef::openshift-origin[]
:global_ns: olm
endif::[]
ifndef::openshift-origin[]
:global_ns: openshift-marketplace
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="olm-priority-class-name_{context}"]
= Overriding the priority class name for catalog source pods

.Prerequisites

* A `CatalogSource` object of source type `grpc` with `spec.image` is defined.
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* Edit the `CatalogSource` object and add or modify the `spec.grpcPodConfig` section to include the following:
+
[source,yaml]
----
  grpcPodConfig:
    priorityClassName: <priority_class>
----
+
where `<priority_class>` is one of the following:
+
--
* One of the default priority classes provided by Kubernetes: `system-cluster-critical` or `system-node-critical`
* An empty set (`""`) to assign the default priority
* A pre-existing and custom defined priority class
--

[NOTE]
====
Previously, the only pod scheduling parameter that could be overriden was `priorityClassName`. This was done by adding the `operatorframework.io/priorityclass` annotation to the `CatalogSource` object. For example:

[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: example-catalog
  namespace: {global_ns}
  annotations:
    operatorframework.io/priorityclass: system-cluster-critical
----

If a `CatalogSource` object defines both the annotation and `spec.grpcPodConfig.priorityClassName`, the annotation takes precedence over the configuration parameter.
====
