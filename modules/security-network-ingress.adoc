// Module included in the following assemblies:
//
// * security/container_security/security-network.adoc

[id="security-network-ingress_{context}"]
=  Securing ingress traffic

There are many security implications related to how you configure
access to your Kubernetes services from outside of your {product-title} cluster.
Besides exposing HTTP and HTTPS routes, ingress routing allows you to set up
NodePort or LoadBalancer ingress types. NodePort exposes an application's
service API object from each cluster worker. LoadBalancer lets you assign an
external load balancer to an associated service API object
in your {product-title} cluster.
