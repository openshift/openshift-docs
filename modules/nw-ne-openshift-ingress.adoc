// Module included in the following assemblies:
// * understanding-networking.adoc


[id="nw-ne-openshift-ingress_{context}"]
= {product-title} Ingress Operator
When you create your {product-title} cluster, pods and services running on the cluster are each allocated their own IP addresses. The IP addresses are accessible to other pods and services running nearby but are not accessible to outside clients. The Ingress Operator implements the `IngressController` API and is the component responsible for enabling external access to {product-title} cluster services.

ifndef::openshift-rosa,openshift-dedicated[]
The Ingress Operator makes it possible for external clients to access your service by deploying and managing one or more HAProxy-based
link:https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/[Ingress Controllers] to handle routing. You can use the Ingress Operator to route traffic by specifying {product-title} `Route` and Kubernetes `Ingress` resources. Configurations within the Ingress Controller, such as the ability to define `endpointPublishingStrategy` type and internal load balancing, provide ways to publish Ingress Controller endpoints.
endif::[]

ifdef::openshift-rosa,openshift-dedicated[]
The Ingress Operator makes it possible for external clients to access your service by deploying and managing one or more HAProxy-based link:https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/[Ingress Controllers] to handle routing. Red Hat Site Reliability Engineers (SRE) manage the Ingress Operator for {product-title} clusters. While you cannot alter the settings for the Ingress Operator, you may view the default Ingress Controller configurations, status, and logs as well as the Ingress Operator status.
endif::[]