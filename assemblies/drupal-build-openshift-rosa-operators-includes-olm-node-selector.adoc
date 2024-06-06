// Module included in the following assemblies:
//
// * operators/admin/olm-cs-podsched.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-node-selector_{context}"]
= Overriding the node selector for catalog source pods

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
    nodeSelector:
      custom_label: <label>
----
+
where `<label>` is the label for the node selector that you want catalog source pods to use for scheduling.
