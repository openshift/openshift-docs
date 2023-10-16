// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-node-names.adoc

[id="nodes-scheduler-node-name-configuring_{context}"]
= Configuring the Pod Node Constraints admission controller to use names

You can configure the Pod Node Constraints admission controller to ensure that pods are only placed onto nodes with a specific name.

.Prerequisites

Ensure you have the desired labels
and node selector set up in your environment.

For example, make sure that your pod configuration features the `nodeName`
value indicating the desired label:

[source,yaml]
----
apiVersion: v1
kind: Pod
spec:
  nodeName: <value>
----

.Procedure

To configure the Pod Node Constraints admission controller:

. Create a file containing the admission controller information:
+
[source,yaml]
----
podNodeSelectorPluginConfig:
 clusterDefaultNodeSelector: name-of-node-selector
 namespace1: name-of-node-selector
 namespace2: name-of-node-selector
----
+
For example:
+
[source,yaml]
----
podNodeConstraintsPluginConfig:
 clusterDefaultNodeSelector: ns1
 ns1: region=west,env=test,infra=fedora,os=fedora
----

. Create an *AdmissionConfiguration* object that references the file:
+
[source,yaml]
----
kind: AdmissionConfiguration
apiVersion: apiserver.k8s.io/v1alpha1
plugins:
- name: PodNodeConstraints
  path: podnodeconstraints.yaml
----

