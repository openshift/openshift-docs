// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-multi-arch-support.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-multi-arch-node-preference_{context}"]
= Using preferred node affinity rules to configure support for multi-architecture compute machines for Operator projects

If your Operator performs better on particular architectures, you can configure preferred node affinity rules to schedule pods to nodes to the specified architectures.

.Prerequisites

* An Operator project created or maintained with Operator SDK {osdk_ver} or later.
* A manifest list defining the platforms your Operator supports.
* Required node affinity rules are set for your Operator project.

.Procedure

. Search your Operator project for Kubernetes manifests that define pod spec and pod template spec objects.
+
.Example Kubernetes manifest
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: s1
spec:
  containers:
    - name: <container_name>
      image: docker.io/<org>/<image_name>
----

. Set your Operator's preferred node affinity rules in the Kubernetes manifests that define pod spec and pod template spec objects, similar to the following example:
+
.Example Kubernetes manifest
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: s1
spec:
  containers:
    - name: <container_name>
      image: docker.io/<org>/<image_name>
  affinity:
      nodeAffinity:
        preferredDuringSchedulingIgnoredDuringExecution: <1>
          - preference:
            matchExpressions: <2>
              - key: kubernetes.io/arch <3>
                operator: In <4>
                values:
                - amd64
                - arm64
            weight: 90 <5>
----
<1> Defines a preferred rule.
<2> If you specify multiple `matchExpressions` associated with `nodeSelectorTerms`, then the pod can be scheduled onto a node only if all `matchExpressions` are satisfied.
<3> Specifies the architectures defined in the manifest list.
<4> Specifies an `operator`. The Operator can be `In`, `NotIn`,  `Exists`, or `DoesNotExist`. For example, use the value of `In` to require the label to be in the node.
<5> Specifies a weight for the node, valid values are `1`-`100`. The node with highest weight is preferred.
