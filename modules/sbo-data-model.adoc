// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/exposing-binding-data-from-a-service.adoc

:_mod-docs-content-type: CONCEPT
[id="sbo-data-model_{context}"]
= Data model

[role="_abstract"]
// The data model used in the annotations and OLM descriptors follow specific conventions.
// When the OLM descriptors are supported again, add this sentence.

The data model used in the annotations follows specific conventions.

Service binding annotations must use the following convention:

[source,yaml]
----
service.binding(/<NAME>)?:
    "<VALUE>|(path=<JSONPATH_TEMPLATE>(,objectType=<OBJECT_TYPE>)?(,elementType=<ELEMENT_TYPE>)?(,sourceKey=<SOURCE_KEY>)?(,sourceValue=<SOURCE_VALUE>)?)"
----
where:
[horizontal]
`<NAME>`:: Specifies the name under which the binding value is to be exposed. You can exclude it only when the `objectType` parameter is set to `Secret` or `ConfigMap`.
`<VALUE>`:: Specifies the constant value exposed when no `path` is set.

// Although, the data model is the same for custom resource definitions (CRD), custom resource (CR) annotations, and Operator Lifecycle Manager (OLM) descriptors, the syntax for each one differs.
// When the OLM descriptors are supported again, add this sentence.

The data model provides the details on the allowed values and semantic for the `path`, `elementType`, `objectType`, `sourceKey`, and `sourceValue` parameters.

.Parameters and their descriptions
[cols="3,6,4",options="header"]
|===
|Parameter
|Description
|Default value

|`path`
|JSONPath template that consists JSONPath expressions enclosed by curly braces {}.
|N/A

|`elementType`
a|Specifies whether the value of the element referenced in the `path` parameter complies with any one of the following types:

* `string`
* `sliceOfStrings`
* `sliceOfMaps`
|`string`

|`objectType`
|Specifies whether the value of the element indicated in the `path` parameter refers to a `ConfigMap`, `Secret`, or plain string in the current namespace.
|`Secret`, if `elementType` is non-string.


|`sourceKey`
a|Specifies the key in the `ConfigMap` or `Secret` resource to be added to the binding secret when collecting the binding data. +

Note:

* When used in conjunction with `elementType`=`sliceOfMaps`, the `sourceKey` parameter specifies the key in the slice of maps whose value is used as a key in the binding secret.
* Use this optional parameter to expose a specific entry in the referenced `Secret` or `ConfigMap` resource as binding data.
* When not specified, all keys and values from the `Secret` or `ConfigMap` resource are exposed and are added to the binding secret.
|N/A

|`sourceValue`
a|Specifies the key in the slice of maps. +

Note:

* The value of this key is used as the base to generate the value of the entry for the key-value pair to be added to the binding secret.
* In addition, the value of the `sourceKey` is used as the key of the entry for the key-value pair to be added to the binding secret.
* It is mandatory only if `elementType`=`sliceOfMaps`.
|N/A
|===

[NOTE]
====
The `sourceKey` and `sourceValue` parameters are applicable only if the element indicated in the `path` parameter refers to a `ConfigMap` or `Secret` resource.
====