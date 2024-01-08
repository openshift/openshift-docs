// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-dependency-resolution.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-properties_{context}"]
ifeval::["{context}" == "olm-packaging-format"]
= Properties
endif::[]
ifeval::["{context}" != "olm-packaging-format"]
= Operator properties
endif::[]

All Operators in a catalog have the following properties:

`olm.package`:: Includes the name of the package and the version of the Operator

`olm.gvk`:: A single property for each provided API from the cluster service version (CSV)

Additional properties can also be directly declared by an Operator author by including a `properties.yaml` file in the `metadata/` directory of the Operator bundle.

.Example arbitrary property
[source,yaml]
----
properties:
- type: olm.kubeversion
  value:
    version: "1.16.0"
----

[id="olm-arbitrary-properties_{context}"]
== Arbitrary properties

Operator authors can declare arbitrary properties in a `properties.yaml` file in the `metadata/` directory of the Operator bundle. These properties are translated into a map data structure that is used as an input to the Operator Lifecycle Manager (OLM) resolver at runtime.

These properties are opaque to the resolver as it does not understand the properties, but it can evaluate the generic constraints against those properties to determine if the constraints can be satisfied given the properties list.

.Example arbitrary properties
[source,yaml]
----
properties:
  - property:
      type: color
      value: red
  - property:
      type: shape
      value: square
  - property:
      type: olm.gvk
      value:
        group: olm.coreos.io
        version: v1alpha1
        kind: myresource
----

This structure can be used to construct a Common Expression Language (CEL) expression for generic constraints.
