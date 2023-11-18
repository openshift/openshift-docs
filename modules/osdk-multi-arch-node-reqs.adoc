// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-multi-arch-support.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-multi-arch-node-reqs_{context}"]
= Using required node affinity rules to support multi-architecture compute machines for Operator projects

If you want your Operator to support multi-architecture compute machines, you must define your Operator's required node affinity rules.

.Prerequisites

* An Operator project created or maintained with Operator SDK {osdk_ver} or later.
* A manifest list defining the platforms your Operator supports.

.Procedure

. Search your Operator project for Kubernetes manifests that define pod spec and pod template spec objects.
+
[IMPORTANT]
====
Because object type names are not declared in YAML files, look for the mandatory `containers` field in your Kubernetes manifests. The `containers` field is required when specifying both pod spec and pod template spec objects.

You must set node affinity rules in all Kubernetes manifests that define a pod spec or pod template spec, including objects such as `Pod`, `Deployment`, `DaemonSet`, and `StatefulSet`.
====
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

. Set the required node affinity rules in the Kubernetes manifests that define pod spec and pod template spec objects, similar to the following example:
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
      requiredDuringSchedulingIgnoredDuringExecution: <1>
        nodeSelectorTerms: <2>
        - matchExpressions: <3>
          - key: kubernetes.io/arch <4>
            operator: In
            values:
            - amd64
            - arm64
            - ppc64le
            - s390x
          - key: kubernetes.io/os <5>
            operator: In
            values:
                - linux
----
<1> Defines a required rule.
<2> If you specify multiple `nodeSelectorTerms` associated with `nodeAffinity` types, then the pod can be scheduled onto a node if one of the `nodeSelectorTerms` is satisfied.
<3> If you specify multiple `matchExpressions` associated with `nodeSelectorTerms`, then the pod can be scheduled onto a node only if all `matchExpressions` are satisfied.
<4> Specifies the architectures defined in the manifest list.
<5> Specifies the operating systems defined in the manifest list.

. Go-based Operator projects that use dynamically created workloads might embed pod spec and pod template spec objects in the Operator's logic.
+
If your project embeds pod spec or pod template spec objects in the Operator's logic, edit your Operator's logic similar to the following example. The following example shows how to update a `PodSpec` object by using the Go API:
+
[source,go]
----
Template: corev1.PodTemplateSpec{
    ...
    Spec: corev1.PodSpec{
        Affinity: &corev1.Affinity{
            NodeAffinity: &corev1.NodeAffinity{
                RequiredDuringSchedulingIgnoredDuringExecution: &corev1.NodeSelector{
                    NodeSelectorTerms: []corev1.NodeSelectorTerm{
                        {
                            MatchExpressions: []corev1.NodeSelectorRequirement{
                                {
                                    Key:      "kubernetes.io/arch",
                                    Operator: "In",
                                    Values:   []string{"amd64","arm64","ppc64le","s390x"},
                                },
                                {
                                    Key:      "kubernetes.io/os",
                                    Operator: "In",
                                    Values:   []string{"linux"},
                                },
                            },
                        },
                    },
                },
            },
        },
        SecurityContext: &corev1.PodSecurityContext{
            ...
        },
        Containers: []corev1.Container{{
            ...
        }},
    },
----
+
where:

`RequiredDuringSchedulingIgnoredDuringExecution`:: Defines a required rule.
`NodeSelectorTerms`:: If you specify multiple `nodeSelectorTerms` associated with `nodeAffinity` types, then the pod can be scheduled onto a node if one of the `nodeSelectorTerms` is satisfied.
`MatchExpressions`:: If you specify multiple `matchExpressions` associated with `nodeSelectorTerms`, then the pod can be scheduled onto a node only if all `matchExpressions` are satisfied.
`kubernetes.io/arch`:: Specifies the architectures defined in the manifest list.
`kubernetes.io/os`:: Specifies the operating systems defined in the manifest list.

[WARNING]
====
If you do not set node affinity rules and a container is scheduled to a compute machine with an incompatible architecture, the pod fails and triggers one of the following events:

`CrashLoopBackOff`:: Occurs when an image manifest's entry point fails to run and an `exec format error` message is printed in the logs.
`ImagePullBackOff`:: Occurs when a manifest list does not include a manifest for the architecture where a pod is scheduled or the node affinity terms are set to the wrong values.
====
