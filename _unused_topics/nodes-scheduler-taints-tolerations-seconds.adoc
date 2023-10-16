// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-taints-tolerations.adoc

[id="nodes-scheduler-taints-tolerations-seconds_{context}"]
= Setting a default value for toleration seconds

When using taints and tolerations, if taints are added to an existing node, non-matching pods on that node will be evicted. You can modify the time allowed before pods are evicted using the toleration seconds plug-in, which sets the eviction period at five minutes, by default.

.Procedure

To enable Default Toleration Seconds:

Create an *AdmissionConfiguration* object:
+
----
kind: AdmissionConfiguration
apiVersion: apiserver.k8s.io/v1alpha1
plugins:
- name: DefaultTolerationSeconds
...----
