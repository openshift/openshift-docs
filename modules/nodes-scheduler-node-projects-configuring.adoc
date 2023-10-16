// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-node-projects.adoc

[id="nodes-scheduler-node-projects-configuring_{context}"]
= Configuring the Pod Node Selector admission controller to use projects

You can configure the Pod Node Selector admission controller to ensure that pods are only placed onto nodes in specific projects.
The Pod Node Selector admission controller uses a configuration file to set options for the behavior of the backend. 

.Procedure

. Create a file containing the admission controller information:
+
[source,yaml]
----
podNodeSelectorPluginConfig:
 clusterDefaultNodeSelector: <node-selector>
 namespace1: <node-selector>
 namespace2: <node-selector>
----
+
For example:
+
[source,yaml]
----
podNodeSelectorPluginConfig:
 clusterDefaultNodeSelector: region=west
 ns1: os=centos,region=west
----

. Create an *AdmissionConfiguration* object that references the file:
+
[source,yaml]
----
kind: AdmissionConfiguration
apiVersion: apiserver.k8s.io/v1alpha1
plugins:
- name: PodNodeSelector
  path: podnodeselector.yaml
----


