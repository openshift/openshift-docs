// Module included in the following assemblies:
//
// * admin/olm-cs-podsched.adoc

:_mod-docs-content-type: PROCEDURE
[id="disabling-catalogsource-objects_{context}"]
= Disabling default CatalogSource objects at a local level

You can apply persistent changes to a `CatalogSource` object, such as catalog source pods, at a local level, by disabling a default `CatalogSource` object. Consider the default configuration in situations where the default `CatalogSource` object's configuration does not meet your organization's needs. By default, if you modify fields in the `spec.grpcPodConfig` section of the   `CatalogSource` object, the Marketplace Operator automatically reverts these changes.

The Marketplace Operator, `openshift-marketplace`, manages the default custom resources (CRs) of the `OperatorHub`. The `OperatorHub` manages `CatalogSource` objects.

To apply persistent changes to `CatalogSource` object, you must first disable a default `CatalogSource` object.

.Procedure

* To disable all the default `CatalogSource` objects at a local level, enter the following command:
+
[source,terminal]
----
$ oc patch operatorhub cluster -p '{"spec": {"disableAllDefaultSources": true}}' --type=merge
----
+
[NOTE]
====
You can also configure the default `OperatorHub` CR to either disable all `CatalogSource` objects or disable a specific object.
====
