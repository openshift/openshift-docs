// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-about-openapi-validation_{context}"]
= About OpenAPI validation

OpenAPIv3 schemas are added to CRD manifests in the `spec.validation` block when the manifests are generated. This validation block allows Kubernetes to validate the properties in a Memcached custom resource (CR) when it is created or updated.

Markers, or annotations, are available to configure validations for your API. These markers always have a `+kubebuilder:validation` prefix.

[role="_additional-resources"]
.Additional resources

* For more details on the usage of markers in API code, see the following Kubebuilder documentation:
** link:https://book.kubebuilder.io/reference/generating-crd.html[CRD generation]
** link:https://book.kubebuilder.io/reference/markers.html[Markers]
** link:https://book.kubebuilder.io/reference/markers/crd-validation.html[List of OpenAPIv3 validation markers]

* For more details about OpenAPIv3 validation schemas in CRDs, see the link:https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#specifying-a-structural-schema[Kubernetes documentation].
