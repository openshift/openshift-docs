// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-node-selector.adoc

[id="nodes-scheduler-node-selectors-configuring_{context}"]
= Configuring the Pod Node Constraints admission controller to use node selectors

You can configure the Pod Node Constraints admission controller to ensure that pods are only placed onto nodes with specific labels.

.Prerequisites

. Ensure you have the desired labels
ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
labels on your nodes. 
endif::openshift-enterprise,openshift-webscale,openshift-origin[]
and node selector set up in your environment.
+
For example, make sure that your pod configuration features the `nodeSelector`
value indicating the desired label:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
spec:
  nodeSelector:
    <key>: <value>
...
----

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
  nodeSelectorLabelBlacklist:
  kubernetes.io/hostname
  - <label>
----

[NOTE] 
====
If you are using node selectors and node affinity in the same pod configuration, note the following:

* If you configure both `nodeSelector` and `nodeAffinity`, both conditions must be satisfied for the pod to be scheduled onto a candidate node.

* If you specify multiple `nodeSelectorTerms` associated with `nodeAffinity` types, then the pod can be scheduled onto a node if one of the `nodeSelectorTerms` is satisfied.

* If you specify multiple `matchExpressions` associated with `nodeSelectorTerms`, then the pod can be scheduled onto a node only if all `matchExpressions` are satisfied.
====

