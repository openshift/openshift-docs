// Module included in the following assemblies:
//
// * service_mesh/v2x/create-mesh.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-about-adding-projects-using-label-selectors_{context}"]
= About adding projects using label selectors

For cluster-wide deployments, you can use label selectors to add projects to the mesh. Label selectors specified in the `ServiceMeshMemberRoll` resource enable the {SMProductShortName} Operator to add or remove namespaces to or from the mesh based on namespace labels. Unlike other standard {product-title} resources that you can use to specify a single label selector, you can use the `ServiceMeshMemberRoll` resource to specify multiple label selectors.

image::ossm-adding-project-using-label-selector.png[Adding project using label selector image]

If the labels for a namespace match any of the selectors specified in the `ServiceMeshMemberRoll` resource, then the namespace is included in the mesh.

[NOTE]
====
In {product-title}, a project is essentially a Kubernetes namespace with additional annotations, such as the range of user IDs that can be used in the project. Typically, the {product-title} web console uses the term _project_, and the CLI uses the term _namespace_, but the terms are essentially synonymous.
====