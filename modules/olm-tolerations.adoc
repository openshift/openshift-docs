// Module included in the following assemblies:
//
// * operators/admin/olm-cs-podsched.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-tolerations_{context}"]
= Overriding tolerations for catalog source pods

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
    tolerations:
      - key: "<key_name>"
        operator: "<operator_type>"
        value: "<value>"
        effect: "<effect>"
----
