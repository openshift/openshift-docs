// Module included in the following assemblies:
//
// * security/container_security/security-network.adoc

[id="security-network-namespaces_{context}"]
= Using network namespaces

{product-title} uses software-defined networking (SDN) to provide a unified
cluster network that enables communication between containers across the
cluster.

Network policy mode, by default, makes all pods in a project accessible from
other pods and network endpoints.
To isolate one or more pods in a project, you can create `NetworkPolicy` objects
in that project to indicate the allowed incoming connections.
Using multitenant mode, you can provide project-level isolation for pods and services.
