// Module included in the following assemblies:
//
// * operators/understanding/crds/crd-managing-resources-from-crds.adoc
// * operators/understanding/crds/extending-api-with-crds.adoc

[id="crd-custom-resource-definitions_{context}"]
= Custom resource definitions

In the Kubernetes API, a _resource_ is an endpoint that stores a collection of API objects of a certain kind. For example, the built-in `Pods` resource contains a collection of `Pod` objects.

A _custom resource definition_ (CRD) object defines a new, unique object type, called a _kind_, in the cluster and lets the Kubernetes API server handle its entire lifecycle.

_Custom resource_ (CR) objects are created from CRDs that have been added to the cluster by a cluster administrator, allowing all cluster users to add the new resource type into projects.

ifeval::["{context}" == "crd-extending-api-with-crds"]
When a cluster administrator adds a new CRD to the cluster, the Kubernetes API server reacts by creating a new RESTful resource path that can be accessed by the entire cluster or a single project (namespace) and begins serving the specified CR.

Cluster administrators that want to grant access to the CRD to other users can use cluster role aggregation to grant access to users with the `admin`, `edit`, or `view` default cluster roles. Cluster role aggregation allows the insertion of custom policy rules into these cluster roles. This behavior integrates the new resource into the RBAC policy of the cluster as if it was a built-in resource.
endif::[]

Operators in particular make use of CRDs by packaging them with any required RBAC policy and other software-specific logic.
ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
Cluster administrators can also add CRDs manually to the cluster outside of the lifecycle of an Operator, making them available to all users.

[NOTE]
====
While only cluster administrators can create CRDs, developers can create the CR from an existing CRD if they have read and write permission to it.
====
endif::[]
