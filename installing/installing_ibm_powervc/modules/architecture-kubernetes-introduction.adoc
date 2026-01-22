// Module included in the following assemblies:
//
// * architecture/architecture.adoc

:_mod-docs-content-type: CONCEPT
[id="architecture-kubernetes-introduction_{context}"]
= About Kubernetes

Although container images and the containers that run from them are the
primary building blocks for modern application development, to run them at scale
requires a reliable and flexible distribution system. Kubernetes is the
defacto standard for orchestrating containers.

Kubernetes is an open source container orchestration engine for automating
deployment, scaling, and management of containerized applications. The general
concept of Kubernetes is fairly simple:

* Start with one or more worker nodes to run the container workloads.
* Manage the deployment of those workloads from one or more control plane nodes.
* Wrap containers in a deployment unit called a pod. Using pods provides extra
metadata with the container and offers the ability to group several containers
in a single deployment entity.
* Create special kinds of assets. For example, services are represented by a
set of pods and a policy that defines how they are accessed. This policy
allows containers to connect to the services that they need even if they do not
have the specific IP addresses for the services. Replication controllers are
another special asset that indicates how many pod replicas are required to run
at a time. You can use this capability to automatically scale your application
to adapt to its current demand.

In only a few years, Kubernetes has seen massive cloud and on-premise adoption.
The open source development model allows many people to extend Kubernetes
by implementing different technologies for components such as networking,
storage, and authentication.
