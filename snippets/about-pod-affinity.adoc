// Snippets included in the following assemblies and modules:
//
// * /nodes/scheduling/nodes-scheduler-pod-affinity.adoc
// * /modules/logging-loki-reliability-hardening.adoc

:_mod-docs-content-type: SNIPPET

Affinity is a property of pods that controls the nodes on which they prefer to be scheduled. Anti-affinity is a property of pods
that prevents a pod from being scheduled on a node.

In {product-title}, _pod affinity_ and _pod anti-affinity_ allow you to constrain which nodes your pod is eligible to be scheduled on based on the key-value labels on other pods.
