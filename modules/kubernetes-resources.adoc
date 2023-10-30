// Module included in the following assemblies:
//
// * getting_started/kubernetes-overview.adoc

:_mod-docs-content-type: CONCEPT
[id="kubernetes-resources_{context}"]
= Kubernetes resources

A custom resource is an extension of the Kubernetes API. You can customize Kubernetes clusters by using custom resources. Operators are software extensions which manage applications and their components with the help of custom resources. Kubernetes uses a declarative model when you want a fixed desired result while dealing with cluster resources. By using Operators, Kubernetes defines its states in a declarative way. You can modify the Kubernetes cluster resources by using imperative commands.
An Operator acts as a control loop which continuously compares the desired state of resources with the actual state of resources and puts actions in place to bring reality in line with the desired state.

.Kubernetes cluster overview
image::247_OpenShift_Kubernetes_Overview-1.png[]

.Kubernetes Resources
[cols="1,2",options="header"]
|===
|Resource |Purpose

|Service
|Kubernetes uses services to expose a running application on a set of pods.

|`ReplicaSets`
|Kubernetes uses the `ReplicaSets` to maintain the constant pod number.

|Deployment
|A resource object that maintains the life cycle of an application.
|===

Kubernetes is a core component of an {product-title}. You can use {product-title} for developing and running containerized applications. With its foundation in Kubernetes, the {product-title} incorporates the same technology that serves as the engine for massive telecommunications, streaming video, gaming, banking, and other applications. You can extend your containerized applications beyond a single cloud to on-premise and multi-cloud environments by using the {product-title}.
