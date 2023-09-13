// Module included in the following assemblies:
//
// * networking/understanding-networking.adoc

[id="nw-ne-comparing-ingress-route_{context}"]
= Comparing routes and Ingress
The Kubernetes Ingress resource in {product-title} implements the Ingress Controller with a shared router service that runs as a pod inside the cluster. The most common way to manage Ingress traffic is with the Ingress Controller. You can scale and replicate this pod like any other regular pod. This router service is based on link:http://www.haproxy.org/[HAProxy], which is an open source load balancer solution.

The {product-title} route provides Ingress traffic to services in the cluster. Routes provide advanced features that might not be supported by standard Kubernetes Ingress Controllers, such as TLS re-encryption, TLS passthrough, and split traffic for blue-green deployments.

Ingress traffic accesses services in the cluster through a route. Routes and Ingress are the main resources for handling Ingress traffic. Ingress provides features similar to a route, such as accepting external requests and delegating them based on the route. However, with Ingress you can only allow certain types of connections: HTTP/2, HTTPS and server name identification (SNI), and TLS with certificate. In {product-title}, routes are generated to meet the conditions specified by the Ingress resource.
