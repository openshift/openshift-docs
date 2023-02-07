// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="dns-operator_{context}"]
= DNS Operator

[discrete]
== Purpose

The DNS Operator deploys and manages CoreDNS to provide a name resolution service to pods that enables DNS-based Kubernetes Service discovery in {product-title}.

The Operator creates a working default deployment based on the cluster's configuration.

* The default cluster domain is `cluster.local`.
* Configuration of the CoreDNS Corefile or Kubernetes plugin is not yet supported.

The DNS Operator manages CoreDNS as a Kubernetes daemon set exposed as a service with a static IP. CoreDNS runs on all nodes in the cluster.

[discrete]
== Project

link:https://github.com/openshift/cluster-dns-operator[cluster-dns-operator]
