////
This module included in the following assemblies:
-service_mesh/v2x/ossm-traffic-manage.adoc
////
:_mod-docs-content-type: CONCEPT
[id="ossm-understanding-networkpolicy_{context}"]
= Understanding network policies

{SMProductName} automatically creates and manages a number of `NetworkPolicies` resources in the {SMProductShortName} control plane and application namespaces. This is to ensure that applications and the control plane can communicate with each other.

For example, if you have configured your {product-title} cluster to use the SDN plugin, {SMProductName} creates a `NetworkPolicy` resource in each member project. This enables ingress to all pods in the mesh from the other mesh members and the control plane. This also restricts ingress to only member projects. If you require ingress from non-member projects, you need to create a `NetworkPolicy` to allow that traffic through. If you remove a namespace from {SMProductShortName}, this `NetworkPolicy` resource is deleted from the project.
