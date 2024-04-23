:_mod-docs-content-type: ASSEMBLY
[id="kubernetes-overview"]
= Kubernetes overview
include::_attributes/common-attributes.adoc[]
:context: kubernetes-overview

toc::[]

Kubernetes is an open source container orchestration tool developed by Google. You can run and manage container-based workloads by using Kubernetes. The most common Kubernetes use case is to deploy an array of interconnected microservices, building an application in a cloud native way. You can create Kubernetes clusters that can span hosts across on-premise, public, private, or hybrid clouds.

Traditionally, applications were deployed on top of a single operating system. With virtualization, you can split the physical host into several virtual hosts. Working on virtual instances on shared resources is not optimal for efficiency and scalability. Because a virtual machine (VM) consumes as many resources as a physical machine, providing resources to a VM such as CPU, RAM, and storage can be expensive. Also, you might see your application degrading in performance due to virtual instance usage on shared resources.

.Evolution of container technologies for classical deployments
image::247-OpenShift-Kubernetes-Overview.png[]

To solve this problem, you can use containerization technologies that segregate applications in a containerized environment. Similar to a VM, a container has its own filesystem, vCPU, memory, process space, dependencies, and more. Containers are decoupled from the underlying infrastructure, and are portable across clouds and OS distributions. Containers are inherently much lighter than a fully-featured OS, and are lightweight isolated processes that run on the operating system kernel. VMs are slower to boot, and are an abstraction of physical hardware. VMs run on a single machine with the help of a hypervisor.

You can perform the following actions by using Kubernetes:

* Sharing resources
* Orchestrating containers across multiple hosts
* Installing new hardware configurations
* Running health checks and self-healing applications
* Scaling containerized applications

include::modules/kubernetes-components.adoc[leveloffset=+1]

include::modules/kubernetes-resources.adoc[leveloffset=+1]

.Architecture of Kubernetes
image::247_OpenShift_Kubernetes_Overview-2.png[]

A cluster is a single computational unit consisting of multiple nodes in a cloud environment. A Kubernetes cluster includes a control plane and worker nodes. You can run Kubernetes containers across various machines and environments. The control plane node controls and maintains the state of a cluster. You can run the Kubernetes application by using worker nodes. You can use the Kubernetes namespace to differentiate cluster resources in a cluster. Namespace scoping is applicable for resource objects, such as deployment, service, and pods. You cannot use namespace for cluster-wide resource objects such as storage class, nodes, and persistent volumes.

include::modules/kubernetes-conceptual-guidelines.adoc[leveloffset=+1]
