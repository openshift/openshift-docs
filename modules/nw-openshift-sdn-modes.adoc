// Module included in the following assemblies:
//
// * networking/openshift_sdn/about-openshift-sdn.adoc

[id="nw-openshift-sdn-modes_{context}"]
= OpenShift SDN network isolation modes

OpenShift SDN provides three SDN modes for configuring the pod network:

* _Network policy_ mode allows project administrators to configure their own
isolation policies using `NetworkPolicy` objects. Network policy is the default mode in {product-title} {product-version}.

* _Multitenant_ mode provides project-level isolation for pods and services. Pods from different projects cannot send packets to or receive packets from pods and services of a different project. You can disable isolation for a project, allowing it to send network traffic to all pods and services in the entire cluster and receive network traffic from those pods and services.

* _Subnet_ mode provides a flat pod network where every pod can communicate with every other pod and service. The network policy mode provides the same functionality as subnet mode.
