// Module included in the following assemblies:
//
// * networking/verifying-connectivity-endpoint.adoc

[id="nw-pod-network-connectivity-checks_{context}"]
= Connection health checks performed

To verify that cluster resources are reachable, a TCP connection is made to each of the following cluster API services:

* Kubernetes API server service
* Kubernetes API server endpoints
* OpenShift API server service
* OpenShift API server endpoints
* Load balancers

To verify that services and service endpoints are reachable on every node in the cluster, a TCP connection is made to each of the following targets:

* Health check target service
* Health check target endpoints
