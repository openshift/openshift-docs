// Module included in the following assemblies:
//
// * migrating_from_ocp_3_to_4/advanced-migration-options-3-4.adoc

[id="migration-mapping-destination-namespaces-in-the-migplan-cr_{context}"]
= Mapping namespaces

If you map namespaces in the `MigPlan` custom resource (CR), you must ensure that the namespaces are not duplicated on the source or the destination clusters because the UID and GID ranges of the namespaces are copied during migration.

.Two source namespaces mapped to the same destination namespace
[source,yaml]
----
spec:
  namespaces:
    - namespace_2
    - namespace_1:namespace_2
----

If you want the source namespace to be mapped to a namespace of the same name, you do not need to create a mapping. By default, a source namespace and a target namespace have the same name.

.Incorrect namespace mapping
[source,yaml]
----
spec:
  namespaces:
    - namespace_1:namespace_1
----

.Correct namespace reference
[source,yaml]
----
spec:
  namespaces:
    - namespace_1
----
